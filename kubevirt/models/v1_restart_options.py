# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1RestartOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        'grace_period_seconds': 'int',
        'kind': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'grace_period_seconds': 'gracePeriodSeconds',
        'kind': 'kind'
    }

    def __init__(self, api_version=None, grace_period_seconds=None, kind=None):
        """
        V1RestartOptions - a model defined in Swagger
        """

        self._api_version = None
        self._grace_period_seconds = None
        self._kind = None

        if api_version is not None:
          self.api_version = api_version
        if grace_period_seconds is not None:
          self.grace_period_seconds = grace_period_seconds
        if kind is not None:
          self.kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1RestartOptions.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1RestartOptions.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1RestartOptions.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1RestartOptions.
        :type: str
        """

        self._api_version = api_version

    @property
    def grace_period_seconds(self):
        """
        Gets the grace_period_seconds of this V1RestartOptions.
        The duration in seconds before the object should be force-restared. Value must be non-negative integer. The value zero indicates, restart immediately. If this value is nil, the default grace period for deletion of the corresponding VMI for the specified type will be used to determine on how much time to give the VMI to restart. Defaults to a per object value if not specified. zero means restart immediately. Allowed Values: nil and 0 +optional

        :return: The grace_period_seconds of this V1RestartOptions.
        :rtype: int
        """
        return self._grace_period_seconds

    @grace_period_seconds.setter
    def grace_period_seconds(self, grace_period_seconds):
        """
        Sets the grace_period_seconds of this V1RestartOptions.
        The duration in seconds before the object should be force-restared. Value must be non-negative integer. The value zero indicates, restart immediately. If this value is nil, the default grace period for deletion of the corresponding VMI for the specified type will be used to determine on how much time to give the VMI to restart. Defaults to a per object value if not specified. zero means restart immediately. Allowed Values: nil and 0 +optional

        :param grace_period_seconds: The grace_period_seconds of this V1RestartOptions.
        :type: int
        """

        self._grace_period_seconds = grace_period_seconds

    @property
    def kind(self):
        """
        Gets the kind of this V1RestartOptions.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1RestartOptions.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1RestartOptions.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1RestartOptions.
        :type: str
        """

        self._kind = kind

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1RestartOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
