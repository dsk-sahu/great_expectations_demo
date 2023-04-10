
#Create a new pandas Datasource
import great_expectations as gx
from great_expectations.cli.datasource import sanitize_yaml_and_save_datasource, check_if_datasource_name_exists
context = gx.get_context()

#Customize Your Datasource Configuration . Change name
datasource_name = "getting_started_datasource_py"

#For files based Datasources
example_yaml = f"""
name: {datasource_name}
class_name: Datasource
execution_engine:
  class_name: PandasExecutionEngine
data_connectors:
  default_inferred_data_connector_name:
    class_name: InferredAssetFilesystemDataConnector
    base_directory: ../data
    default_regex:
      group_names:
        - data_asset_name
      pattern: (.*)
  default_runtime_data_connector_name:
    class_name: RuntimeDataConnector
    assets:
      my_runtime_asset_name:
        batch_identifiers:
          - runtime_batch_identifier_name
"""
print(example_yaml)

#Test Your Datasource Configuration
context.test_yaml_config(yaml_config=example_yaml)

#Save Your Datasource Configuration
sanitize_yaml_and_save_datasource(context, example_yaml, overwrite_existing=False)
context.list_datasources()