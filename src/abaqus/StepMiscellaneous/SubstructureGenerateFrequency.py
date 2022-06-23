class SubstructureGenerateFrequency:
    """A :py:class:`~abaqus.StepMiscellaneous.SubstructureGenerateFrequency.SubstructureGenerateFrequency` object is used to define the modes to be used in a modal
    dynamic analysis. These modes are selected from the specified frequency range including
    the frequency boundary.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name].frequencyRange[i]
    """

    #: A Float specifying the lower limit of the frequency range, in cycles/time.
    lower: float = None

    #: A Float specifying the upper limit of the frequency range, in cycles/time.
    upper: float = None
