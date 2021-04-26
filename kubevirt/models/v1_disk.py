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


class V1Disk(object):
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
        'block_size': 'V1BlockSize',
        'boot_order': 'int',
        'cache': 'str',
        'cdrom': 'V1CDRomTarget',
        'dedicated_io_thread': 'bool',
        'disk': 'V1DiskTarget',
        'floppy': 'V1FloppyTarget',
        'io': 'str',
        'lun': 'V1LunTarget',
        'name': 'str',
        'serial': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'block_size': 'blockSize',
        'boot_order': 'bootOrder',
        'cache': 'cache',
        'cdrom': 'cdrom',
        'dedicated_io_thread': 'dedicatedIOThread',
        'disk': 'disk',
        'floppy': 'floppy',
        'io': 'io',
        'lun': 'lun',
        'name': 'name',
        'serial': 'serial',
        'tag': 'tag'
    }

    def __init__(self, block_size=None, boot_order=None, cache=None, cdrom=None, dedicated_io_thread=None, disk=None, floppy=None, io=None, lun=None, name=None, serial=None, tag=None):
        """
        V1Disk - a model defined in Swagger
        """

        self._block_size = None
        self._boot_order = None
        self._cache = None
        self._cdrom = None
        self._dedicated_io_thread = None
        self._disk = None
        self._floppy = None
        self._io = None
        self._lun = None
        self._name = None
        self._serial = None
        self._tag = None

        if block_size is not None:
          self.block_size = block_size
        if boot_order is not None:
          self.boot_order = boot_order
        if cache is not None:
          self.cache = cache
        if cdrom is not None:
          self.cdrom = cdrom
        if dedicated_io_thread is not None:
          self.dedicated_io_thread = dedicated_io_thread
        if disk is not None:
          self.disk = disk
        if floppy is not None:
          self.floppy = floppy
        if io is not None:
          self.io = io
        if lun is not None:
          self.lun = lun
        self.name = name
        if serial is not None:
          self.serial = serial
        if tag is not None:
          self.tag = tag

    @property
    def block_size(self):
        """
        Gets the block_size of this V1Disk.
        If specified, the virtual disk will be presented with the given block sizes.

        :return: The block_size of this V1Disk.
        :rtype: V1BlockSize
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """
        Sets the block_size of this V1Disk.
        If specified, the virtual disk will be presented with the given block sizes.

        :param block_size: The block_size of this V1Disk.
        :type: V1BlockSize
        """

        self._block_size = block_size

    @property
    def boot_order(self):
        """
        Gets the boot_order of this V1Disk.
        BootOrder is an integer value > 0, used to determine ordering of boot devices. Lower values take precedence. Each disk or interface that has a boot order must have a unique value. Disks without a boot order are not tried if a disk with a boot order exists.

        :return: The boot_order of this V1Disk.
        :rtype: int
        """
        return self._boot_order

    @boot_order.setter
    def boot_order(self, boot_order):
        """
        Sets the boot_order of this V1Disk.
        BootOrder is an integer value > 0, used to determine ordering of boot devices. Lower values take precedence. Each disk or interface that has a boot order must have a unique value. Disks without a boot order are not tried if a disk with a boot order exists.

        :param boot_order: The boot_order of this V1Disk.
        :type: int
        """

        self._boot_order = boot_order

    @property
    def cache(self):
        """
        Gets the cache of this V1Disk.
        Cache specifies which kvm disk cache mode should be used. Supported values are: CacheNone, CacheWriteThrough.

        :return: The cache of this V1Disk.
        :rtype: str
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """
        Sets the cache of this V1Disk.
        Cache specifies which kvm disk cache mode should be used. Supported values are: CacheNone, CacheWriteThrough.

        :param cache: The cache of this V1Disk.
        :type: str
        """

        self._cache = cache

    @property
    def cdrom(self):
        """
        Gets the cdrom of this V1Disk.
        Attach a volume as a cdrom to the vmi.

        :return: The cdrom of this V1Disk.
        :rtype: V1CDRomTarget
        """
        return self._cdrom

    @cdrom.setter
    def cdrom(self, cdrom):
        """
        Sets the cdrom of this V1Disk.
        Attach a volume as a cdrom to the vmi.

        :param cdrom: The cdrom of this V1Disk.
        :type: V1CDRomTarget
        """

        self._cdrom = cdrom

    @property
    def dedicated_io_thread(self):
        """
        Gets the dedicated_io_thread of this V1Disk.
        dedicatedIOThread indicates this disk should have an exclusive IO Thread. Enabling this implies useIOThreads = true. Defaults to false.

        :return: The dedicated_io_thread of this V1Disk.
        :rtype: bool
        """
        return self._dedicated_io_thread

    @dedicated_io_thread.setter
    def dedicated_io_thread(self, dedicated_io_thread):
        """
        Sets the dedicated_io_thread of this V1Disk.
        dedicatedIOThread indicates this disk should have an exclusive IO Thread. Enabling this implies useIOThreads = true. Defaults to false.

        :param dedicated_io_thread: The dedicated_io_thread of this V1Disk.
        :type: bool
        """

        self._dedicated_io_thread = dedicated_io_thread

    @property
    def disk(self):
        """
        Gets the disk of this V1Disk.
        Attach a volume as a disk to the vmi.

        :return: The disk of this V1Disk.
        :rtype: V1DiskTarget
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """
        Sets the disk of this V1Disk.
        Attach a volume as a disk to the vmi.

        :param disk: The disk of this V1Disk.
        :type: V1DiskTarget
        """

        self._disk = disk

    @property
    def floppy(self):
        """
        Gets the floppy of this V1Disk.
        Attach a volume as a floppy to the vmi.

        :return: The floppy of this V1Disk.
        :rtype: V1FloppyTarget
        """
        return self._floppy

    @floppy.setter
    def floppy(self, floppy):
        """
        Sets the floppy of this V1Disk.
        Attach a volume as a floppy to the vmi.

        :param floppy: The floppy of this V1Disk.
        :type: V1FloppyTarget
        """

        self._floppy = floppy

    @property
    def io(self):
        """
        Gets the io of this V1Disk.
        IO specifies which QEMU disk IO mode should be used. Supported values are: native, default, threads.

        :return: The io of this V1Disk.
        :rtype: str
        """
        return self._io

    @io.setter
    def io(self, io):
        """
        Sets the io of this V1Disk.
        IO specifies which QEMU disk IO mode should be used. Supported values are: native, default, threads.

        :param io: The io of this V1Disk.
        :type: str
        """

        self._io = io

    @property
    def lun(self):
        """
        Gets the lun of this V1Disk.
        Attach a volume as a LUN to the vmi.

        :return: The lun of this V1Disk.
        :rtype: V1LunTarget
        """
        return self._lun

    @lun.setter
    def lun(self, lun):
        """
        Sets the lun of this V1Disk.
        Attach a volume as a LUN to the vmi.

        :param lun: The lun of this V1Disk.
        :type: V1LunTarget
        """

        self._lun = lun

    @property
    def name(self):
        """
        Gets the name of this V1Disk.
        Name is the device name

        :return: The name of this V1Disk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Disk.
        Name is the device name

        :param name: The name of this V1Disk.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def serial(self):
        """
        Gets the serial of this V1Disk.
        Serial provides the ability to specify a serial number for the disk device.

        :return: The serial of this V1Disk.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this V1Disk.
        Serial provides the ability to specify a serial number for the disk device.

        :param serial: The serial of this V1Disk.
        :type: str
        """

        self._serial = serial

    @property
    def tag(self):
        """
        Gets the tag of this V1Disk.
        If specified, disk address and its tag will be provided to the guest via config drive metadata

        :return: The tag of this V1Disk.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this V1Disk.
        If specified, disk address and its tag will be provided to the guest via config drive metadata

        :param tag: The tag of this V1Disk.
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, V1Disk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
