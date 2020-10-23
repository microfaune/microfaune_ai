
import json

def read_json_file(json_file_path:str) -> dict:
    """ Read json file with labels.

                Parameters
                ----------
                json_file_path : str
                    Path of json file.

                Returns:
                -------
                data_dict : list
                    List of labels, each label is a dictionary item with entries 'id', 'start', 'end', 'annotation'
    """
    with open(json_file_path) as json_data:
        data_dict = json.load(json_data)
    return data_dict

# def read_json_file(json_file_path:str, attr_to_extract:[str]) -> dict:
#     """ Read json file with labels.
#
#                 Parameters
#                 ----------
#                 json_file_path : str
#                     Path of json file.
#
#                 Returns:
#                 -------
#                 data_dict : list
#                     List of labels, each label is a dictionary item with entries 'id', 'start', 'end', 'annotation'
#     """
#     l = [str]
#     with open(json_file_path) as json_data:
#         attr_to_extract.apply(lambda x: json.loads(str(x)))
#         data_dict = json.load(json_data)
#     return data_dict

# valsToKeep = ["correct", "duration", "misses", "session_duration"]
# typesToKeep = ["int", "number", "boolean"]
#
# specs = pd.read_csv('../input/data-science-bowl-2019/specs.csv')
# specs.args = specs.args.apply(lambda x: json.loads(str(x)))
# eventIdsToDrop = []
# for _, spec in specs.iterrows():
#     j = pd.io.json.json_normalize(spec.args)
#     vals = j.loc[(j.name.isin(valsToKeep)) &amp; (j.type.isin(typesToKeep))].name.values
#     if len(vals) == 0:
#         eventIdsToDrop += [spec.event_id]
# set(eventIdsToDrop)