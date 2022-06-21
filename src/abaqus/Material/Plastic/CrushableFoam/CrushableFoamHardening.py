from abaqusConstants import *


class CrushableFoamHardening:
    r"""The CrushableFoamHardening object specifies hardening for the crushable foam plasticity
    model.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].crushableFoam.crushableFoamHardening
        import odbMaterial
        session.odbs[name].materials[name].crushableFoam.crushableFoamHardening

    The table data for this object are:

    - The yield stress in uniaxial compression, :math:`\sigma_c`.
    - The absolute value of the corresponding Plastic strain.(The first tabular 
      value entered must always be zero.)
    - Temperature, if the data depend on temperature.
    - Value of the first field variable, if the data depend on field variables.
    - Value of the second field variable.
    - Etc.

    The corresponding analysis keywords are:

    - CRUSHABLE FOAM HARDENING
    """

    def __init__(
        self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0
    ):
        """This method creates a CrushableFoamHardening object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].crushableFoam.CrushableFoamHardening
                session.odbs[name].materials[name].crushableFoam.CrushableFoamHardening
        
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
        A CrushableFoamHardening object. 

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self, *args, **kwargs):
        """This method modifies the CrushableFoamHardening object.

        Raises
        ------
        RangeError
        """
        pass
