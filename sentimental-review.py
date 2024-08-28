id: sentimental-data
namespace: yesakris.team

inputs:
  - id: file
    type: FILE

tasks:
  - id: sentimental
    type: io.kestra.plugin.scripts.python.Script
    inputFiles: 
      input_csv: "{{ inputs.file }}"
    beforeCommands: 
      - pip install pandas
    script: |
      import pandas as pd

      cr = pd.read_csv('{{ inputs.file }}')
  
      def klasifikasi(category):
        if category == beli-harddisk-eksternal:
          return 'Tersedia'
        else:
          return 'Tidak Tersedia'

      cr['klasifikasi'] = cr['category'].apply(klasifikasi)
      cr.to_csv('analisis_sentimen.csv', index=False)

    outputFiles:
      - 'hasil-sentimental.csv'
