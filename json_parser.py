# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = trip_advisor_page_from_dict(json.loads(json_string))

from enum import Enum
from typing import Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class TypeEnum(Enum):
    LIST_ITEM = "ListItem"


class ItemListElement:
    type: TypeEnum
    position: int
    name: str
    url: str

    def __init__(self, type: TypeEnum, position: int, name: str, url: str) -> None:
        self.type = type
        self.position = position
        self.name = name
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'ItemListElement':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("@type"))
        position = from_int(obj.get("position"))
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        return ItemListElement(type, position, name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@type"] = to_enum(TypeEnum, self.type)
        result["position"] = from_int(self.position)
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        return result


class TripAdvisorPage:
    context: str
    type: str
    name: str
    description: str
    item_list_order: str
    item_list_element: List[ItemListElement]

    def __init__(self, context: str, type: str, name: str, description: str, item_list_order: str, item_list_element: List[ItemListElement]) -> None:
        self.context = context
        self.type = type
        self.name = name
        self.description = description
        self.item_list_order = item_list_order
        self.item_list_element = item_list_element

    @staticmethod
    def from_dict(obj: Any) -> 'TripAdvisorPage':
        assert isinstance(obj, dict)
        context = from_str(obj.get("@context"))
        type = from_str(obj.get("@type"))
        name = from_str(obj.get("name"))
        description = from_str(obj.get("description"))
        item_list_order = from_str(obj.get("ItemListOrder"))
        item_list_element = from_list(ItemListElement.from_dict, obj.get("itemListElement"))
        return TripAdvisorPage(context, type, name, description, item_list_order, item_list_element)

    def to_dict(self) -> dict:
        result: dict = {}
        result["@context"] = from_str(self.context)
        result["@type"] = from_str(self.type)
        result["name"] = from_str(self.name)
        result["description"] = from_str(self.description)
        result["ItemListOrder"] = from_str(self.item_list_order)
        result["itemListElement"] = from_list(lambda x: to_class(ItemListElement, x), self.item_list_element)
        return result


def trip_advisor_page_from_dict(s: Any) -> TripAdvisorPage:
    return TripAdvisorPage.from_dict(s)


def trip_advisor_page_to_dict(x: TripAdvisorPage) -> Any:
    return to_class(TripAdvisorPage, x)


