def wing_weight_TBW(
        wing_af_thickness=0.119,
        wing_ar=19.7,
        wing_area=1477.,
        wing_sweep_delta=0.0,
        wing_taper=0.35,
        strut_eta=0.5766,
        mtow=150000.,
        engine_weight=6335.
):
    """
    Estimate wing structural weight of the TBW vehicle configuration for
    integration with vehicle sizing tools like FLOPS or LEAPS
    :param wing_af_thickness: Thickness of airfoils on the wing. Assumed
        constant airfoil shape along the span of the wing
        Bounds = [0.095, 0.144]
    :type wing_af_thickness: float
    :param wing_ar: Aspect ratio of the wing using b^2/S where b is the span
        in ft and S is the Wimpress area in sq. ft
        Bounds = [15.2 23.0]
    :type wing_ar: float
    :param wing_area: Planform area of the wing measured using the Wimpress
        method (sq. ft.)
        Bounds = [1000 16000]
    :type wing_area: float
    :param wing_sweep_delta: The change of half-chord sweep of the main wing, measured from the baseline (11.3 degrees)
        Bounds = [-10.0 15.0]
    :type wing_sweep_delta: float
    :param wing_taper: Taper ratio of the wing defined as c_t/c_r where c_t
        is the non-projected tip chord and c_r is the non-projected root
        chord (for the OpenVSP file, this is measured from the centerline,
        i.e. y = 0 rather than the intersection of the wing with the
        fuselage/fairing)
        Bounds = [0.25, 0.45]
    :type wing_taper: float
    :param strut_eta: Attatchment of the strut to the main wing, measured in fractions of half-span
        Bounds = [0.4, 0.8]
    :type strut_eta: float
    :param mtow: Maximum takeoff weight of the vehicle in lbs
        Bounds = [130e3, 170e3]
    :type mtow: float
    :param engine_weight: Weight of the inboard engine in lbs
        Bounds = [5070, 7602]
    :type engine_weight: float
    :return: Total wing structural weight
    :rtype: float
    """
    estimate = (
                   -4257.26345359943) + -11878.2969879508 * wing_af_thickness + 220.047706073815 * wing_ar \
                           + 2.64728559072833 * wing_area + 75.4053233846004 * wing_sweep_delta + 1452.77234682876 \
                           * wing_taper + -2840.11373863797 * strut_eta + 0.0231475966595803 * mtow \
                           + -0.0281462321260778 * engine_weight + (
                           wing_af_thickness - 0.12009881577931) * (
                           (wing_af_thickness - 0.12009881577931) * -93927.1316771324) + (
                           wing_af_thickness - 0.12009881577931) * (
                           (wing_ar - 19.0573830880172) * -712.841100798117) + (
                           wing_af_thickness - 0.12009881577931) * (
                           (wing_area - 1291.76098653448) * 5.70416745646755) + (
                           wing_af_thickness - 0.12009881577931) * (
                           (wing_sweep_delta - 1.05176726295862) * -60.619851207008) + (
                           wing_af_thickness - 0.12009881577931) * (
                           (wing_taper - 0.351275896575862) * -360.920445388845) + (
                           wing_af_thickness - 0.12009881577931) * (
                           (strut_eta - 0.601967383174137) * 36661.7051591474) + (
                           wing_af_thickness - 0.12009881577931) * ((mtow - 149907.522727931) * -0.0718072798081834) + (
                           wing_af_thickness - 0.12009881577931) * (
                           (engine_weight - 6347.67961655518) * 0.831622167897022) + (wing_ar - 19.0573830880172) * (
                           (wing_ar - 19.0573830880172) * 0.538820920056799) + (wing_ar - 19.0573830880172) * (
                           (wing_area - 1291.76098653448) * 0.0506411839572489) + (wing_ar - 19.0573830880172) * (
                           (wing_sweep_delta - 1.05176726295862) * 1.37984895550461) + (wing_ar - 19.0573830880172) * (
                           (wing_taper - 0.351275896575862) * 69.5083489834382) + (wing_ar - 19.0573830880172) * (
                           (strut_eta - 0.601967383174137) * -188.579489755346) + (wing_ar - 19.0573830880172) * (
                           (mtow - 149907.522727931) * 0.00152905050270633) + (wing_ar - 19.0573830880172) * (
                           (engine_weight - 6347.67961655518) * -0.00655434625154175) + (
                           wing_area - 1291.76098653448) * ((wing_area - 1291.76098653448) * -0.00013541546356773) + (
                           wing_area - 1291.76098653448) * (
                           (wing_sweep_delta - 1.05176726295862) * 0.0383395672631393) + (
                           wing_area - 1291.76098653448) * ((wing_taper - 0.351275896575862) * -0.617691059452396) + (
                           wing_area - 1291.76098653448) * ((strut_eta - 0.601967383174137) * 1.44078662538476) + (
                           wing_area - 1291.76098653448) * ((mtow - 149907.522727931) * 0.0000227994507106466) + (
                           wing_area - 1291.76098653448) * (
                           (engine_weight - 6347.67961655518) * 0.00009694916258896) + (
                           wing_sweep_delta - 1.05176726295862) * (
                           (wing_sweep_delta - 1.05176726295862) * 4.833051284172) + (
                           wing_sweep_delta - 1.05176726295862) * (
                           (wing_taper - 0.351275896575862) * 19.2005241223105) + (
                           wing_sweep_delta - 1.05176726295862) * (
                           (strut_eta - 0.601967383174137) * -161.825393761682) + (
                           wing_sweep_delta - 1.05176726295862) * ((mtow - 149907.522727931) * 0.000825530517339874) + (
                           wing_sweep_delta - 1.05176726295862) * (
                           (engine_weight - 6347.67961655518) * 0.000685309015180898) + (
                           wing_taper - 0.351275896575862) * ((wing_taper - 0.351275896575862) * -391.683666763851) + (
                           wing_taper - 0.351275896575862) * ((strut_eta - 0.601967383174137) * -7245.88839254213) + (
                           wing_taper - 0.351275896575862) * ((mtow - 149907.522727931) * -0.000820981801417466) + (
                           wing_taper - 0.351275896575862) * (
                           (engine_weight - 6347.67961655518) * 0.0408977843116594) + (
                           strut_eta - 0.601967383174137) * ((strut_eta - 0.601967383174137) * 43571.624852289) + (
                           strut_eta - 0.601967383174137) * ((mtow - 149907.522727931) * -0.0132795899631609) + (
                           strut_eta - 0.601967383174137) * ((engine_weight - 6347.67961655518) * 0.242705684135127) + (
                           mtow - 149907.522727931) * ((mtow - 149907.522727931) * -0.0000000043932470908) + (
                           mtow - 149907.522727931) * ((engine_weight - 6347.67961655518) * -0.0000013189201742769) + (
                           engine_weight - 6347.67961655518) * (
                           (engine_weight - 6347.67961655518) * -0.0000599254543483901)
    return estimate


if __name__ == "__main__":

    # Input parameters

    INPUT_wing_af_thickness = 0.119
    INPUT_wing_ar = 19.7
    INPUT_wing_area = 1477.
    INPUT_wing_sweep_delta = 0.0
    INPUT_wing_taper = 0.35
    INPUT_strut_eta = 0.5766
    INPUT_mtow = 150000.
    INPUT_fuel_weight_ratio = 0.35
    INPUT_engine_weight = 6335.

    weight_estimate = wing_weight_TBW(
        wing_af_thickness=INPUT_wing_af_thickness,
        wing_ar=INPUT_wing_ar,
        wing_area=INPUT_wing_area,
        wing_sweep_delta=INPUT_wing_sweep_delta,
        wing_taper=INPUT_wing_taper,
        strut_eta=INPUT_strut_eta,
        mtow=INPUT_mtow,
        engine_weight= INPUT_engine_weight
    )
    print(weight_estimate)

    pred_jmp = 4757.88328411493

    print(
        'Error is between python and jmp surrogates for baseline is: \n' + str(
            (weight_estimate-pred_jmp)/pred_jmp))