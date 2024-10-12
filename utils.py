def download_config():
    i = 0
    try :
      file = open("pipeline/config.yaml","r")
      file.close()
    except FileNotFoundError:
      i = 1
    if i == 1:
      !git clone https://github.com/Hiisox/pipeline.git