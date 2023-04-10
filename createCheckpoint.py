from ruamel.yaml import YAML
import great_expectations as gx
from pprint import pprint

yaml = YAML()
context = gx.get_context()

my_checkpoint_name = "getting_started_checkpoint_py" # This was populated from your CLI command.

yaml_config = f"""
name: {my_checkpoint_name}
config_version: 1.0
class_name: SimpleCheckpoint
run_name_template: "%Y%m%d-%H%M%S-my-run-name-template"
validations:
  - batch_request:
      datasource_name: getting_started_datasource_py
      data_connector_name: default_inferred_data_connector_name
      data_asset_name: yellow_tripdata_sample_2019-01.csv
      data_connector_query:
        index: -1
    expectation_suite_name: getting_started_expectation_suite_taxi_py.demo
"""
print(yaml_config)

# Run this cell to print out the names of your Datasources, Data Connectors and Data Assets
pprint(context.get_available_data_asset_names())

context.list_expectation_suite_names()

my_checkpoint = context.test_yaml_config(yaml_config=yaml_config)

print(my_checkpoint.get_config(mode="yaml"))

context.add_checkpoint(**yaml.load(yaml_config))

context.run_checkpoint(checkpoint_name=my_checkpoint_name)
context.open_data_docs()