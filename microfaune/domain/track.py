PREDICTION_SAMPLE_WIDTH_IN_MS = 20

class Track:

    # "tracks": [
    #     {
    #         "id": 47,
    #         "name": "SWIFT_20000101_022052.wav",
    #         "file": "/media/SWIFT_20000101_022052.wav",
    #         "format": "wav",
    #         "project_id": 1,
    #         "duration": 60.0,
    #         "prediction": "",
    #         "annotation_set": [
    #             {
    #                 "id": 1,
    #                 "track_id": 47,
    #                 "value":"[
    #                   {\"id\":\"wavesurfer_4kgitqcktig\",\"start\":4.935061842665718,\"end\":10.509955195406347,\"annotation\":\"\"},
    #                   {\"id\":\"wavesurfer_afb13jpasm8\",\"start\":17.55982033205593,\"end\":22.95971703246838,\"annotation\":\"\"},
    #                   {\"id\":\"wavesurfer_jdu8bguik4\",\"start\":26.334652470226157,\"end\":30.184578821446145,\"annotation\":\"\"}
    #                 ]",
    #           "user_id": 1,
    #           "reviewed": false,
    #           "reviewed_by_id": null,
    #           "date_time": "2020-10-17T19:12:13.800Z",
    #           "username": "admin",
    #           "reviewer": null
    #           }
    #         ] --> Fin annotation_set
    #     }, --> Fin du TrackElmt
    # ] --> Fin du Tracks

    def map_annotation_set_to_prediction_ndxes(self, track_elmt:dict) -> [(int,int)] :
        # return [ self._map_annotation_set_elmt_to_prediction_ndxes(annotation_set_elmt.get("value"))
        #          for annotation_set_elmt in track_elmt.get("annotation_set") ]
        l = [(int,int)]
        l.append(self._map_annotation_set_elmt_to_prediction_ndxes(annotation_set_elmt.get("value"))
                 for annotation_set_elmt in track_elmt.get("annotation_set"))
        return l

    def _map_annotation_set_elmt_to_prediction_ndxes(self, value_list:[dict]) -> [(int,int)]:
        l = [(int,int)]
        l.append(self._convert_from_annonation_elmt_time_to_prediction_order(value.get("start"), value.get("end"))
                 for value in value_list)
        return l

    # return [ self._convert_from_annonation_elmt_time_to_prediction_order(value.get("start"), value.get("end"))
        #          for value in value_list ]

    def _convert_from_annonation_elmt_time_to_prediction_order(self, start_time_offset_in_sec:float, end_time_offset_in_sec:float) -> (int,int):
        (a,b) = ( (int) (start_time_offset_in_sec * 1000 // PREDICTION_SAMPLE_WIDTH_IN_MS) + 1,
                 (int) (end_time_offset_in_sec * 1000 // PREDICTION_SAMPLE_WIDTH_IN_MS) + 1)
        print(f'\nstart:{a} - end:{b}')
        return (a,b)