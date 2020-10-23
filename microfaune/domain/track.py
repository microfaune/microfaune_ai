PREDICTION_SAMPLE_WIDTH_IN_MS = 20

class Track:
    # trackEmlt : dict
    #
    # def __init__(self, trackEmlt : dict):
    #     self.trackEmlt = trackEmlt


    def map_annotation_set_elmt_to_prediction_ndxes(self, annotation_set:dict) -> [(int,int)] :
        # annotation_set_elmt est une sequence de duration càd de 60 sec.
        positive_prediction_ndxes = [(int,int)] # (start_poisition_index, end_position_index)
        positive_prediction_ndxes.append(
            # annotation_set.get("annotation_set")
                map(lambda elmt: self.convert_from_annonation_elmt_time_to_prediction_order(elmt.get("start")), annotation_set.get("annotation_set"))
        )
        return positive_prediction_ndxes

    def convert_from_annonation_elmt_time_to_prediction_order(self, start_time_offset_in_sec:float, end_time_offset_in_sec:float) -> (int,int):
        return ( (int) (start_time_offset_in_sec * 1000 // PREDICTION_SAMPLE_WIDTH_IN_MS) + 1,
                 (int) (end_time_offset_in_sec * 1000 // PREDICTION_SAMPLE_WIDTH_IN_MS) + 1)