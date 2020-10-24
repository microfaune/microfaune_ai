from functools import reduce
import operator

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
        prediction_ndxes_of_annotation_set_elmt = []
        prediction_ndxes_of_annotation_set_elmt +=  map(lambda annotation_set_elmt :
            self._map_annotation_set_elmt_to_prediction_ndxes(annotation_set_elmt.get("value"), track_elmt.get("duration"), len(track_elmt.get("prediction")) ) ,
                                                              track_elmt.get("annotation_set"))
        prediction_ndxes_of_annotation_set_elmt = reduce(operator.concat, prediction_ndxes_of_annotation_set_elmt, [])
        return prediction_ndxes_of_annotation_set_elmt

    def _map_annotation_set_elmt_to_prediction_ndxes(self, value_list:[dict], track_duration:float, track_predictions_count:int ) -> [(int,int)]:
        prediction_ndxes_of_value_elmt = []
        prediction_ndxes_of_value_elmt += map(lambda value : self._convert_from_annonation_elmt_time_to_prediction_order(value, track_duration, track_predictions_count),
                                              value_list)
        return prediction_ndxes_of_value_elmt

    # duration(60 sec) --represente-par--> track.prediction.length (2814)
    # start            ------------------>  ?
    def _convert_from_annonation_elmt_time_to_prediction_order(self, value:dict, track_duration:float, track_predictions_count:int ) -> (int,int):
        # return ( (int) (value.get("start") * 1000 // PREDICTION_SAMPLE_WIDTH_IN_MS) + 1,
        #          (int) (value.get("end") * 1000 // PREDICTION_SAMPLE_WIDTH_IN_MS) + 1 )
        return (  int(value.get("start") * track_predictions_count // track_duration) + 1,
                  int(value.get("end") * track_predictions_count // track_duration) + 1 )