from typing import Optional

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Leaf import Leaf
from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant


@abaqus_class_doc
class LeafFromOdbElementLayups(Leaf):
    """The LeafFromOdbElementLayups object can be used whenever a Leaf object is expected as an
    argument. Leaf objects are used to specify the items in a display group. Leaf objects
    are constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromOdbElementLayups object is derived from the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupOdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, elementLayups: tuple):
        """This method creates a Leaf object from a sequence of Strings specifying layup names.
        Leaf objects specify the items in a display group.

        .. note::
            This function can be accessed by::

                LeafFromOdbElementLayups

        Parameters
        ----------
        elementLayups
            A sequence of Strings specifying element layups.

        Returns
        -------
        LeafFromOdbElementLayups
            A LeafFromOdbElementLayups object.
        """
        super().__init__(DEFAULT_MODEL)
