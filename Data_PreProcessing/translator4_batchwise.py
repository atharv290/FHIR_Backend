#AIzaSyBzV7gTQlfWRsACS83ktwW23X0f_7LVr00
import pandas as pd
import google.generativeai as genai
from deep_translator import GoogleTranslator
import os
import time
import traceback  # 👈 for full error details

# 🔑 Configure Gemini
genai.configure(api_key="Your-API-Key")
model = genai.GenerativeModel("gemini-2.5-flash")

# File paths
input_file = r"C:\Users\ATHARVA M JOSHI\Desktop\sih-term-service\backend\NATIONAL SIDDHA MORBIDITY CODES.xls"
output_file = "namaste_with_gemini.csv"

# Load dataset (resume if file already exists)
if os.path.exists(output_file):
    df = pd.read_csv(output_file, encoding="utf-8-sig")
else:
    df = pd.read_excel(input_file)
    if "English_Term" not in df.columns:
        df["English_Term"] = ""

batch_size = 10

# Helper: build prompt for a batch
def build_prompt(batch):
    prompt = (
        "You are a medical terminology expert.\n\n"  
        "Translate the following Tamil Siddha medical terms into the most accurate single English medical term.\n"
        "Use the short and long definitions as context.\n"
        "Return only the English term, numbered exactly as the input.\n\n"
    )
    for i, row in batch.iterrows():
        tamil_term = str(row.get("Tamil_term", ""))
        short_def = str(row.get("Short_definition", ""))
        long_def = str(row.get("Long_definition", ""))
        prompt += f"{i+1}. {tamil_term} | Short: {short_def} | Long: {long_def}\n"

    prompt += "\nReturn format:\n1. English term\n2. English term..."
    return prompt

# Safe save function to handle PermissionError
def safe_save(df, path):
    for _ in range(5):  # retry up to 5 times
        try:
            temp_file = path + ".tmp"
            df.to_csv(temp_file, index=False, encoding="utf-8-sig")
            os.replace(temp_file, path)  # replace safely
            return
        except PermissionError as e:
            print(f"⚠️ File is locked ({e}), retrying in 3 sec...")
            time.sleep(3)
        except Exception:
            print("❌ Unexpected error while saving file:")
            traceback.print_exc()
            break

# Process in batches
for start in range(0, len(df), batch_size):
    end = min(start + batch_size, len(df))
    batch = df.iloc[start:end]    

    # Skip batch if already translated
    if all(batch["English_Term"].notna() & (batch["English_Term"].str.strip() != "")):
        print(f"⏩ Skipping batch {start}-{end-1}, already done")
        continue

    untranslated_batch = batch[batch["English_Term"].isna() | (batch["English_Term"].str.strip() == "")]
    if untranslated_batch.empty:
        continue

    prompt = build_prompt(untranslated_batch)

    try:
        response = model.generate_content(prompt)
        lines = response.text.strip().split("\n")

        for line in lines:
            if "." in line:
                idx_str, term = line.split(".", 1)
                idx = int(idx_str.strip()) - 1
                df.at[start + idx, "English_Term"] = term.strip()

        print(f"✅ Batch {start}-{end-1} translated")

    except Exception as e:
        print(f"⚠️ Gemini failed for batch {start}-{end-1}")
        traceback.print_exc()  # 👈 show full error trace

        # Fallback: Google Translate
        for i, row in untranslated_batch.iterrows():
            try:
                translated = GoogleTranslator(source="ta", target="en").translate(str(row["Tamil_term"]))
                df.at[i, "English_Term"] = translated
                print(f"   → Row {i} translated with Google: {translated}")
            except Exception as sub_e:
                print(f"   ❌ Google Translate failed for row {i}: {sub_e}")
                df.at[i, "English_Term"] = ""

    # Save progress safely
    safe_save(df, output_file)

print("🎉 Remaining rows processed. File updated:", output_file)
