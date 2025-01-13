from enum import Enum
from typing import Any, Optional

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber
from flet.core.types import ColorEnums, ColorValue


class SpinkitType(Enum):
    ROTATING_CIRCLE = "rotatingcircle"
    FOLDING_CUBE = "foldingcube"


class Spinkit(ConstrainedControl):
    """
    Spinkit Control.
    """

    def __init__(
        self,
        #
        # Control
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        #
        # ConstrainedControl
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        #
        # Spinkit specific
        #
        color: Optional[str] = None,
        size: OptionalNumber = None,
        spinkit_type: Optional[SpinkitType] = None,
    ):
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        self.color = color
        self.size = size
        self.spinkit_type = spinkit_type

    def _get_control_name(self):
        return "spinkit"

    # color
    @property
    def color(self) -> Optional[ColorValue]:
        return self.__color

    @color.setter
    def color(self, value: Optional[ColorValue]):
        self.__color = value
        self._set_enum_attr("color", value, ColorEnums)

    # size
    @property
    def size(self):
        return self._get_attr("size")

    @size.setter
    def size(self, value):
        self._set_attr("size", value)

    # spinkit_type
    @property
    def spinkit_type(self) -> Optional[SpinkitType]:
        return self.__spinkit_type

    @spinkit_type.setter
    def spinkit_type(self, value: Optional[SpinkitType]):
        self.__spinkit_type = value
        self._set_attr(
            "spinkittype", value.value if isinstance(value, SpinkitType) else value
        )
