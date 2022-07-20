from configparser import ConfigParser

if __name__ == "__main__":
    # Este arquivo cria uma configuracao de arquivos.
    # Aqui são definidos os diretorios de organização do projeto.

    config = ConfigParser()

    # prepare_dataset.py configuration
    config['prepare_dataset'] = {
        'LIDC_DICOM_PATH': './LIDC-IDRI',
        'MASK_PATH':'./data/Mask',
        'IMAGE_PATH':'./data/Image',
        'CLEAN_PATH_IMAGE':'./data/Clean/Image',
        'CLEAN_PATH_MASK':'./data/Clean/Mask',
        'META_PATH': './data/Meta/',
        'Mask_Threshold':8
    }


    # Configuração da biblioteca pylidc
    config['pylidc'] = {
        'confidence_level': 0.5,
        'padding_size': 512
    }

    # Cria a configuração no arquivo lung.conf
    with open('./lung.conf', 'w') as f:
          config.write(f)
