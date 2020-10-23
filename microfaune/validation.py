import os

from detection import RNNDetector
from domain.track import Track
from utils import file_utils


class RNNValidator:

    def __init__(self, detector:RNNDetector):
        self.detector = detector

    def load_annotation_file(self, json_file_path :str) -> dict :
        return file_utils.read_json_file(json_file_path)

    def map_annotation_elmt_to_prediction_ndx(self, all_annotations:dict) -> [int] :
        prediction_ndxes = [(int,int)]
        track = Track()
        self.compute_prediction_metrics(
            # all_annotations.get("tracks")
                map(lambda annotation_set: track.map_annotation_set_elmt_to_prediction_ndxes(annotation_set), all_annotations.get("tracks"))
        )
        return 0

    def compute_prediction_metrics(self, positive_prediction_ndxes = [(int,int)]) -> (float, float, float):
        for biNdx in positive_prediction_ndxes :
            print(f"start:%d - end:%d", biNdx[0], biNdx[1] )
        return (1,2,3)

if __name__ == '__main__' :
    detector = RNNDetector()
    validator = RNNValidator(detector)
    all_annotations = validator.load_annotation_file( os.path.abspath(os.path.join(os.path.dirname(__file__), "media-annotation/SWIFT_20000101_022052.json")) )
    validator.map_annotation_elmt_to_prediction_ndx(all_annotations)
    # global_score, local_score = detector.predict_on_wav(os.path.abspath(os.path.join(os.path.dirname(__file__), "media/SWIFT_20190723_050006.wav"))) # NB: Check that loaded wav file actually exists on your disk
    # print(f"Golbal score: {global_score}  -  Localscore: {local_score}")