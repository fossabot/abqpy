from abaqusConstants import *


class BrittleFailure:
    """The BrittleFailure object specifies the brittle failure of the material.

    .. note:: 
        This object can be accessed by:

        .. code-block:: python

            import material
            mdb.models[name].materials[name].brittleCracking.brittleFailure
            import odbMaterial
            session.odbs[name].materials[name].brittleCracking.brittleFailure

        The table data for this object are:

        - If parent :py:class:`~abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking` member **type** = STRAIN the table data specify the following:
        
            - Direct cracking failure strain.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.
        - If parent :py:class:`~abaqus.Material.Plastic.Concrete.BrittleCracking.BrittleCracking` member **type** = DISPLACEMENT or **type** = GFI the table data specify the following:
        
            - Direct cracking failure displacement.
            - Temperature, if the data depend on temperature.
            - Value of the first field variable, if the data depend on field variables.
            - Value of the second field variable.
            - Etc.

        The corresponding analysis keywords are:

        - BRITTLE FAILURE
    """

    def __init__(
        self,
        table: tuple,
        temperatureDependency: Boolean = OFF,
        dependencies: int = 0,
        failureCriteria: SymbolicConstant = UNIDIRECTIONAL,
    ):
        """This method creates a BrittleFailure object.

        .. note:: 
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].materials[name].brittleCracking.BrittleFailure
                session.odbs[name].materials[name].brittleCracking.BrittleFailure

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below.
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF.
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0.
        failureCriteria
            A SymbolicConstant specifying the failure criteria. Possible values are UNIDIRECTIONAL,
            BIDIRECTIONAL, and TRIDIRECTIONAL. The default value is UNIDIRECTIONAL.

        Returns
        -------
        BrittleFailure
            A :py:class:`~abaqus.Material.Plastic.Concrete.BrittleFailure.BrittleFailure` object.

        Raises
        ------
        RangeError
        """
        ...

    def setValues(self, *args, **kwargs):
        """This method modifies the BrittleFailure object.

        Raises
        ------
        RangeError
        """
        ...
