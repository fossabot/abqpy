from .GeometricRestriction import GeometricRestriction
from ..Region.Region import Region
from ..UtilityAndView.abaqusConstants import *


class ShapePlanarSymmetry(GeometricRestriction):
    """The ShapePlanarSymmetry object defines a shape planar symmetry geometric restriction.
    The ShapePlanarSymmetry object is derived from the GeometricRestriction object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import optimization
            mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    """

    #: A String specifying the geometric restriction repository key.
    name: str

    #: A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the vector positioned at the **csys** origin
    #: that is normal to the symmetry plane. Instead of through a ConstrainedSketchVertex, each point may be
    #: specified through a tuple of coordinates.
    clientDirection: tuple

    #: A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
    #: When used with a TopologyTask, there is no default value. When used with a ShapeTask,
    #: the default value is MODEL.
    region: Region

    #: None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
    #: global coordinate system is used. When this member is queried, it returns an Int. The
    #: default value is None.
    csys: int = None

    #: A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
    #: restriction. The default value is TRUE.
    allowNonSymmetricMesh: Boolean = TRUE

    #: A SymbolicConstant specifying the rule for determining the master node. Possible values
    #: are MAXIMUM and MINIMUM. The default value is MAXIMUM.
    masterPointDetermination: SymbolicConstant = MAXIMUM

    #: A Boolean specifying whether to ignore the geometric restriction in the first design
    #: cycle. The default value is ON.
    presumeFeasibleRegionAtStart: Boolean = ON

    #: A Float specifying the geometric tolerance in the 1-direction. The default value is
    #: 0.01.
    tolerance1: float = 0

    #: A Float specifying the geometric tolerance in the 2-direction. The default value is
    #: 0.01.
    tolerance2: float = 0

    #: A Float specifying the geometric tolerance in the 3-direction. The default value is
    #: 0.01.
    tolerance3: float = 0

    def __init__(
        self,
        name: str,
        clientDirection: tuple,
        region: Region,
        allowNonSymmetricMesh: Boolean = TRUE,
        csys: int = None,
        masterPointDetermination: SymbolicConstant = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method creates a ShapePlanarSymmetry object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].optimizationTasks[name].ShapePlanarSymmetry

        Parameters
        ----------
        name
            A String specifying the geometric restriction repository key.
        clientDirection
            A :py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` object of length 2 specifying the vector positioned at the **csys** origin
            that is normal to the symmetry plane. Instead of through a ConstrainedSketchVertex, each point may be
            specified through a tuple of coordinates.
        region
            A :py:class:`~abaqus.Region.Region.Region` object specifying the region to which the geometric restriction is applied.
            When used with a TopologyTask, there is no default value. When used with a ShapeTask,
            the default value is MODEL.
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
            restriction. The default value is TRUE.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for determining the master node. Possible values
            are MAXIMUM and MINIMUM. The default value is MAXIMUM.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.

        Returns
        -------
        ShapePlanarSymmetry
            A :py:class:`~abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry` object.
        """
        super().__init__()

    def setValues(
        self,
        allowNonSymmetricMesh: Boolean = TRUE,
        csys: int = None,
        masterPointDetermination: SymbolicConstant = MAXIMUM,
        presumeFeasibleRegionAtStart: Boolean = ON,
        tolerance1: float = 0,
        tolerance2: float = 0,
        tolerance3: float = 0,
    ):
        """This method modifies the ShapePlanarSymmetry object.

        Parameters
        ----------
        allowNonSymmetricMesh
            A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
            restriction. The default value is TRUE.
        csys
            None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
            global coordinate system is used. When this member is queried, it returns an Int. The
            default value is None.
        masterPointDetermination
            A SymbolicConstant specifying the rule for determining the master node. Possible values
            are MAXIMUM and MINIMUM. The default value is MAXIMUM.
        presumeFeasibleRegionAtStart
            A Boolean specifying whether to ignore the geometric restriction in the first design
            cycle. The default value is ON.
        tolerance1
            A Float specifying the geometric tolerance in the 1-direction. The default value is
            0.01.
        tolerance2
            A Float specifying the geometric tolerance in the 2-direction. The default value is
            0.01.
        tolerance3
            A Float specifying the geometric tolerance in the 3-direction. The default value is
            0.01.
        """
        ...
