from abaqusConstants import *
from .InteractionState import InteractionState


class FluidCavityState(InteractionState):
    """The FluidCavityState object stores the propagating data for an FluidCavity object. One
    instance of this object is created internally by the FluidCavity object for each step.
    The instance is also deleted internally by the FluidCavity object.
    The FluidCavityState object has no constructor or methods.
    The FluidCavityState object is derived from the InteractionState object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].steps[name].interactionStates[name]
    """

    #: A SymbolicConstant specifying the propagation state of the InteractionState object.
    #: Possible values are:
    #: 
    #: - NOT_YET_ACTIVE
    #: - CREATED
    #: - PROPAGATED
    #: - MODIFIED
    #: - DEACTIVATED
    #: - NO_LONGER_ACTIVE
    #: - TYPE_NOT_APPLICABLE
    #: - INSTANCE_NOT_APPLICABLE
    #: - BUILT_INTO_BASE_STATE
    status: SymbolicConstant = None
