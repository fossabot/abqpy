from typing import Optional, Sequence

from abqpy.decorators import abaqus_class_doc, abaqus_method_doc

from .Leaf import Leaf
from ..Datum.Datum import Datum
from ..UtilityAndView.abaqusConstants import DEFAULT_MODEL, SymbolicConstant


@abaqus_class_doc
class LeafFromDatums(Leaf):
    """The LeafFromDatums object can be used whenever a Leaf object is expected as an argument.
    Leaf objects are used to specify the items in a display group. Leaf objects are
    constructed as temporary objects, which are then used as arguments to DisplayGroup
    commands.
    The LeafFromDatums object is derived from the Leaf object.

    .. note::
        This object can be accessed by::

            import displayGroupMdbToolset
    """

    #: A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF,
    #: DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES.
    leafType: Optional[SymbolicConstant] = None

    @abaqus_method_doc
    def __init__(self, datumSeq: Sequence[Datum]):
        """This method creates a Leaf object from a sequence of datum objects. Leaf objects specify
        the items in a display group.

        .. note::
            This function can be accessed by::

                LeafFromDatums

        Parameters
        ----------
        datumSeq
            A sequence of datum objects.

        Returns
        -------
        LeafFromDatums
            A LeafFromDatums object.
        """
        super().__init__(DEFAULT_MODEL)
