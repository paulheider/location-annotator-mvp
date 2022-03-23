import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_location_annotation_request import TextLocationAnnotationRequest  # noqa: E501
from openapi_server.models.text_location_annotation_response import TextLocationAnnotationResponse  # noqa: E501
from openapi_server import util


def create_text_location_annotations(text_location_annotation_request=None):  # noqa: E501
    """Annotate locations in a clinical note

    Return the location annotations found in a clinical note # noqa: E501

    :param text_location_annotation_request: 
    :type text_location_annotation_request: dict | bytes

    :rtype: TextLocationAnnotationResponse
    """
    if connexion.request.is_json:
        text_location_annotation_request = TextLocationAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
