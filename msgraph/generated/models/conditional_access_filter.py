from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_mode import FilterMode

@dataclass
class ConditionalAccessFilter(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The mode property
    mode: Optional[FilterMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Rule syntax is similar to that used for membership rules for groups in Azure Active Directory (Azure AD). For details, see rules with multiple expressions
    rule: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessFilter
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessFilter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .filter_mode import FilterMode

        from .filter_mode import FilterMode

        fields: Dict[str, Callable[[Any], None]] = {
            "mode": lambda n : setattr(self, 'mode', n.get_enum_value(FilterMode)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rule": lambda n : setattr(self, 'rule', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("mode", self.mode)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("rule", self.rule)
        writer.write_additional_data_value(self.additional_data)
    

