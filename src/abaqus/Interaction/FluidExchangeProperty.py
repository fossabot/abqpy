from abaqusConstants import *
from .ContactProperty import ContactProperty


class FluidExchangeProperty(ContactProperty):
    """The FluidExchangeProperty object is an interaction property that defines the fluid
    exchange property for a flow between two fluid cavities or between a fluid cavity and
    its environment.
    The FluidExchangeProperty object is derived from the InteractionProperty object.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactionProperties[name]

    The corresponding analysis keywords are:

    - FLUID EXCHANGE PROPERTY
    """

    def __init__(
        self,
        name: str,
        dataTable: tuple,
        definition: SymbolicConstant = BULK_VISCOSITY,
        pressureDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        fieldDependencies: int = 0,
    ):
        """This method creates a FluidExchangeProperty object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].FluidExchangeProperty

        Parameters
        ----------
        name
            A String specifying the interaction property repository key.
        dataTable
            A sequence of sequences of Floats specifying the viscous and hydrodynamic resistance
            coefficients when **definition** = BULK_VISCOSITY. Each sequence contains the following
            data:
            
            - The viscous resistance coefficient.
            - The hydrodynamic resistance coefficient.
            - The average absolute pressure, if the data depend on pressure.
            - The average temperature, if the data depend on temperature.
            - The value of the first field variable, if the data depend on field variables.
            - The value of the second field variable.
            - Etc.
            
            Alternatively, the sequence data may specify the mass flow rate. This is applicable only
            when **definition** = MASS_FLUX. In this form, only one sequence is specified and that
            sequence contains the following data:
            
            - The mass flow rate per unit area.
              Alternatively, the sequence data may specify the mass rate leakage. This is applicable
              only when **definition** = MASS_RATE_LEAK. Each sequence contains the following data:
              
              - The absolute value of the mass flow rate per unit area. (The first tabular value
                entered must always be zero.)
              - The absolute value of the pressure difference. (The first tabular value entered must
                always be zero.)
              - The average absolute pressure, if the data depend on pressure.
              - The average temperature, if the data depend on temperature.
              - The value of the first field variable, if the data depend on field variables.
              - The value of the second field variable.
              - Etc.
            
            Alternatively, the sequence data may specify the volume flow rate. This is applicable
            only when **definition** = VOL_FLUX. In this form, only one sequence is specified and that
            sequence contains the following data:
            
            - The volumetric flow rate per unit area.
              Alternatively, the sequence data may specify the volume rate leakage. This is applicable
              only when **definition** = VOL_RATE_LEAK. Each sequence contains the following data:
              
              - The absolute value of the volumetric flow rate per unit area. (The first tabular value
                entered must always be zero.)
              - The absolute value of the pressure difference. (The first tabular value entered must
                always be zero.)
              - The average absolute pressure, if the data depend on pressure.
              - The average temperature, if the data depend on temperature.
              - The value of the first field variable, if the data depend on field variables.
              - The value of the second field variable.
              - Etc.
        definition
            A SymbolicConstant specifying the type of fluid exchange property to be defined.
            Possible values are BULK_VISCOSITY, MASS_FLUX, MASS_RATE_LEAK, VOL_FLUX, and
            VOL_RATE_LEAK. The default value is BULK_VISCOSITY.
        pressureDependency
            A Boolean specifying whether the data will have pressure dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data will have temperature dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        fieldDependencies
            An Int specifying the number of field variable dependencies in the data. This argument
            is applicable only when **definition** = BULK_VISCOSITY, or when
            **definition** = MASS_RATE_LEAK, or when **definition** = VOL_RATE_LEAK. The default value is 0.

        Returns
        -------
        A FluidExchangeProperty object.
        """
        super().__init__(name)
        pass

    def setValues(
        self,
        definition: SymbolicConstant = BULK_VISCOSITY,
        pressureDependency: Boolean = OFF,
        temperatureDependency: Boolean = OFF,
        fieldDependencies: int = 0,
    ):
        """This method modifies the FluidExchangeProperty object.

        Parameters
        ----------
        definition
            A SymbolicConstant specifying the type of fluid exchange property to be defined.
            Possible values are BULK_VISCOSITY, MASS_FLUX, MASS_RATE_LEAK, VOL_FLUX, and
            VOL_RATE_LEAK. The default value is BULK_VISCOSITY.
        pressureDependency
            A Boolean specifying whether the data will have pressure dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        temperatureDependency
            A Boolean specifying whether the data will have temperature dependency. This argument is
            applicable only when **definition** = BULK_VISCOSITY, or when **definition** = MASS_RATE_LEAK,
            or when **definition** = VOL_RATE_LEAK. The default value is OFF.
        fieldDependencies
            An Int specifying the number of field variable dependencies in the data. This argument
            is applicable only when **definition** = BULK_VISCOSITY, or when
            **definition** = MASS_RATE_LEAK, or when **definition** = VOL_RATE_LEAK. The default value is 0.
        """
        pass
