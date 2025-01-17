from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_identity import EmailIdentity
    from .initiator import Initiator
    from .provisioned_identity import ProvisionedIdentity
    from .provisioning_service_principal import ProvisioningServicePrincipal
    from .provisioning_system import ProvisioningSystem
    from .service_principal_identity import ServicePrincipalIdentity
    from .share_point_identity import SharePointIdentity
    from .teamwork_application_identity import TeamworkApplicationIdentity
    from .teamwork_conversation_identity import TeamworkConversationIdentity
    from .teamwork_tag_identity import TeamworkTagIdentity
    from .teamwork_user_identity import TeamworkUserIdentity
    from .user_identity import UserIdentity

@dataclass
class Identity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The display name of the identity. Note that this might not always be available or up to date. For example, if a user changes their display name, the API might show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.
    display_name: Optional[str] = None
    # Unique identifier for the identity.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailIdentity".casefold():
            from .email_identity import EmailIdentity

            return EmailIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.initiator".casefold():
            from .initiator import Initiator

            return Initiator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisionedIdentity".casefold():
            from .provisioned_identity import ProvisionedIdentity

            return ProvisionedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningServicePrincipal".casefold():
            from .provisioning_service_principal import ProvisioningServicePrincipal

            return ProvisioningServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningSystem".casefold():
            from .provisioning_system import ProvisioningSystem

            return ProvisioningSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalIdentity".casefold():
            from .service_principal_identity import ServicePrincipalIdentity

            return ServicePrincipalIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointIdentity".casefold():
            from .share_point_identity import SharePointIdentity

            return SharePointIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkApplicationIdentity".casefold():
            from .teamwork_application_identity import TeamworkApplicationIdentity

            return TeamworkApplicationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkConversationIdentity".casefold():
            from .teamwork_conversation_identity import TeamworkConversationIdentity

            return TeamworkConversationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTagIdentity".casefold():
            from .teamwork_tag_identity import TeamworkTagIdentity

            return TeamworkTagIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkUserIdentity".casefold():
            from .teamwork_user_identity import TeamworkUserIdentity

            return TeamworkUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userIdentity".casefold():
            from .user_identity import UserIdentity

            return UserIdentity()
        return Identity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .email_identity import EmailIdentity
        from .initiator import Initiator
        from .provisioned_identity import ProvisionedIdentity
        from .provisioning_service_principal import ProvisioningServicePrincipal
        from .provisioning_system import ProvisioningSystem
        from .service_principal_identity import ServicePrincipalIdentity
        from .share_point_identity import SharePointIdentity
        from .teamwork_application_identity import TeamworkApplicationIdentity
        from .teamwork_conversation_identity import TeamworkConversationIdentity
        from .teamwork_tag_identity import TeamworkTagIdentity
        from .teamwork_user_identity import TeamworkUserIdentity
        from .user_identity import UserIdentity

        from .email_identity import EmailIdentity
        from .initiator import Initiator
        from .provisioned_identity import ProvisionedIdentity
        from .provisioning_service_principal import ProvisioningServicePrincipal
        from .provisioning_system import ProvisioningSystem
        from .service_principal_identity import ServicePrincipalIdentity
        from .share_point_identity import SharePointIdentity
        from .teamwork_application_identity import TeamworkApplicationIdentity
        from .teamwork_conversation_identity import TeamworkConversationIdentity
        from .teamwork_tag_identity import TeamworkTagIdentity
        from .teamwork_user_identity import TeamworkUserIdentity
        from .user_identity import UserIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

