id: data-cleansing
namespace: yesakris.team

inputs:
  - id: file_input
    type: FILE

tasks:
  - id: cleaning
    type: io.kestra.plugin.scripts.python.Script
    inputFiles:
      input_csv: "{{ inputs.file_input }}"
    
    beforeCommands:
      - pip install pandas

    script: |
      import pandas as pd
      
      cr = pd.read_csv('{{ inputs.file_input }}', na_values=['null'], low_memory=False)
      
      jenis = ['itemId', 'category', 'name', 'rating']
      cr = cr[jenis]

      cr['itemId'] = cr['itemId'].fillna(0).astype(int)
      cr['category'] = cr['category'].fillna('Unknown').str.strip()
      cr['name'] = cr['name'].fillna('Anonymous').str.strip()
      cr['rating'] = pd.to_numeric(cr['rating'], errors='coerce')
      

      cr = cr.dropna()
      
      cr.to_csv('hasil_clean.csv', index=False)

    outputFiles:
      - 'hasil_clean.csv'
