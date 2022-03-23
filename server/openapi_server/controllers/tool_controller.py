import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.tool import Tool  # noqa: E501
from openapi_server.models.tool_dependencies import ToolDependencies  # noqa: E501
from openapi_server.models.tool_type import ToolType
from openapi_server.models.license import License


def get_tool():  # noqa: E501
    """Get tool information

    Get information about the tool # noqa: E501


    :rtype: Tool
    """
    tool = Tool(
        name="location-annotator-mvp",
        version="0.1",
        license=License.APACHE_2_0,
        repository="github:paulheider/location-annotator-mvp",
        description="Example implementation of the NLP Sandbox Location " +
                "Annotator API",
        author="NLP Sandbox Team",
        author_email="team@nlpsandbox.io",
        url="https://github.com/paulheider/location-annotator-mvp",
        type=ToolType.LOCATION_ANNOTATOR,
        api_version="1.2.0"
    )
    return tool, 200


def get_tool_dependencies():  # noqa: E501
    """Get tool dependencies

    Get the dependencies of this tool # noqa: E501


    :rtype: ToolDependencies
    """
    return ToolDependencies(tools=[]), 200
