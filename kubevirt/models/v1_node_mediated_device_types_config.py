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


class V1NodeMediatedDeviceTypesConfig(object):
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
        'mediated_devices_types': 'list[str]',
        'node_selector': 'dict(str, str)'
    }

    attribute_map = {
        'mediated_devices_types': 'mediatedDevicesTypes',
        'node_selector': 'nodeSelector'
    }

    def __init__(self, mediated_devices_types=None, node_selector=None):
        """
        V1NodeMediatedDeviceTypesConfig - a model defined in Swagger
        """

        self._mediated_devices_types = None
        self._node_selector = None

        self.mediated_devices_types = mediated_devices_types
        self.node_selector = node_selector

    @property
    def mediated_devices_types(self):
        """
        Gets the mediated_devices_types of this V1NodeMediatedDeviceTypesConfig.

        :return: The mediated_devices_types of this V1NodeMediatedDeviceTypesConfig.
        :rtype: list[str]
        """
        return self._mediated_devices_types

    @mediated_devices_types.setter
    def mediated_devices_types(self, mediated_devices_types):
        """
        Sets the mediated_devices_types of this V1NodeMediatedDeviceTypesConfig.

        :param mediated_devices_types: The mediated_devices_types of this V1NodeMediatedDeviceTypesConfig.
        :type: list[str]
        """
        if mediated_devices_types is None:
            raise ValueError("Invalid value for `mediated_devices_types`, must not be `None`")

        self._mediated_devices_types = mediated_devices_types

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1NodeMediatedDeviceTypesConfig.
        NodeSelector is a selector which must be true for the vmi to fit on a node. Selector which must match a node's labels for the vmi to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

        :return: The node_selector of this V1NodeMediatedDeviceTypesConfig.
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1NodeMediatedDeviceTypesConfig.
        NodeSelector is a selector which must be true for the vmi to fit on a node. Selector which must match a node's labels for the vmi to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

        :param node_selector: The node_selector of this V1NodeMediatedDeviceTypesConfig.
        :type: dict(str, str)
        """
        if node_selector is None:
            raise ValueError("Invalid value for `node_selector`, must not be `None`")

        self._node_selector = node_selector

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
        if not isinstance(other, V1NodeMediatedDeviceTypesConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other