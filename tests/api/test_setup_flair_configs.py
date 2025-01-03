import os.path

import yaml

from src.api.setup_flair_configs import setup_config_flair_detect


def test_setup_config_flair_detect(tests_output_folder):
    # init
    input_image_path = "/input/prediction/tile_RGBN.tif"
    model_weights_path = "tile_model.tif"
    output_image_name = "tile_model.tif"
    output_folder = tests_output_folder

    # act
    runtime_config_path = setup_config_flair_detect(
        input_image_path=input_image_path,
        model_weights_path=model_weights_path,
        output_image_name=output_image_name,
        output_folder=output_folder,
        batch_size=8,
    )

    # assert
    assert os.path.exists(runtime_config_path)
    with open(runtime_config_path) as f:
        updated_config = yaml.safe_load(f)

    assert updated_config["output_path"] == output_folder
    assert updated_config["output_name"] == output_image_name
    assert updated_config["input_img_path"] == input_image_path
    assert updated_config["channels"] == [1, 2, 3, 4]
    assert updated_config["model_weights"] == model_weights_path
    assert updated_config["img_pixels_detection"] == 1024
    assert updated_config["margin"] == 256
    assert updated_config["num_worker"] == 0
    assert updated_config["batch_size"] == 8
