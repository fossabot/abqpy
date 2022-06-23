from .PredefinedField import PredefinedField
from ..Region.Region import Region


class FluidCavityPressure(PredefinedField):
    """The FluidCavityPressure object stores the data for initial fluid cavity pressures. The
    base class*region* argument can not be specifed with this object.
    The FluidCavityPressure object is derived from the PredefinedField object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].predefinedFields[name]

    The corresponding analysis keywords are:

    - INITIAL CONDITIONS
    """

    #: A :py:class:`~abaqus.Region.Region.Region` object on which the **fluidCavity** interaction is specified.
    region: Region = Region()

    #: A String specifying the repository key.
    name: str

    #: A String specifying the name of a Fluid Cavity Interaction.
    fluidCavity: str

    #: A Float specifying the initial fluid pressure.
    fluidPressure: float

    def __init__(self, name: str, fluidCavity: str, fluidPressure: float):
        """This method creates a FluidCavityPressure object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].FluidCavityPressure

        Parameters
        ----------
        name
            A String specifying the repository key.
        fluidCavity
            A String specifying the name of a Fluid Cavity Interaction.
        fluidPressure
            A Float specifying the initial fluid pressure.

        Returns
        -------
        FluidCavityPressure
            A :py:class:`~abaqus.PredefinedField.FluidCavityPressure.FluidCavityPressure` object.
        """
        super().__init__()
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the FluidCavityPressure object."""
        pass
