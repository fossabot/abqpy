from .Profile import Profile


class CircularProfile(Profile):
    """The CircularProfile object defines the properties of a solid circular profile.
    The CircularProfile object is derived from the Profile object.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import section
            mdb.models[name].profiles[name]
            import odbSection
            session.odbs[name].profiles[name]

        The corresponding analysis keywords are:

        - BEAM SECTION
    """

    #: A String specifying the repository key.
    name: str

    #: A positive Float specifying the **r** dimension (outer radius) of the circular profile.
    #: For more information, see [Beam cross-section
    #: library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).
    r: float

    def __init__(self, name: str, r: float):
        """This method creates a CircularProfile object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].CircularProfile
                session.odbs[name].CircularProfile

        Parameters
        ----------
        name
            A String specifying the repository key.
        r
            A positive Float specifying the **r** dimension (outer radius) of the circular profile.
            For more information, see [Beam cross-section
            library](https://help.3ds.com/2021/English/DSSIMULIA_Established/SIMACAEELMRefMap/simaelm-c-beamcrosssectlib.htm?ContextScope=all).

        Returns
        -------
        CircularProfile
            A :py:class:`~abaqus.BeamSectionProfile.CircularProfile.CircularProfile` object.

        Raises
        ------
        RangeError

        """
        super().__init__()
        ...

    def setValues(self, *args, **kwargs):
        """This method modifies the CircularProfile object.

        Raises
        ------
        RangeError

        """
        ...
