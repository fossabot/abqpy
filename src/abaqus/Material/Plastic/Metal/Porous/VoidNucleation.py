from abaqusConstants import *


class VoidNucleation:
    r"""The VoidNucleation object defines the nucleation of voids in a porous material.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].porousMetalPlasticity.voidNucleation
        import odbMaterial
        session.odbs[name].materials[name].porousMetalPlasticity.voidNucleation

    The table data for this object are:

    - :math:`\varepsilon_{N}`, the mean value of the nucleation-strain normal distribution.
    - :math:`s_{N}`, the standard deviation of the nucleation-strain normal distribution.
    - :math:`f_{N}`, the volume fraction of nucleating voids.
    - Temperature, if the data depend on temperature.
    - Value of the first field variable, if the data depend on field variables.
    - Value of the second field variable.
    - Etc.

    The corresponding analysis keywords are:

    - VOID NUCLEATION
    """

    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a VoidNucleation object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].porousMetalPlasticity.VoidNucleation
                session.odbs[name].materials[name].porousMetalPlasticity.VoidNucleation
        
        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
        A VoidNucleation object. 

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the VoidNucleation object.

        Raises
        ------
        RangeError
        """
        pass
