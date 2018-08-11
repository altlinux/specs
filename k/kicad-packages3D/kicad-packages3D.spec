# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: kicad-packages3D
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Version: 5.0.0
Release: alt1.rc3
Source: %name-%version.tar.gz
License: GPLv2+
Group: Engineering
Url: https://code.launchpad.net/kicad

Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++

Requires: kicad-packages3D-part1 = %EVR
Requires: kicad-packages3D-part2 = %EVR

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Kicad-library содержит в себе 3D-модели для kicad.

%package part1
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Group: Engineering

%description part1
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.
Part1

%description part1 -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Kicad-library содержит в себе 3D-модели для kicad.
Часть 1

%package part2
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Group: Engineering

%description part2
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.
Part2

%description part2 -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Kicad-library содержит в себе 3D-модели для kicad.
Часть 2

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files

%files part1
%dir %_datadir/kicad
%dir %_datadir/kicad/modules
%dir %_datadir/kicad/modules/packages3d/
%_datadir/kicad/modules/packages3d/Battery.3dshapes
%_datadir/kicad/modules/packages3d/Button_Switch_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Button_Switch_THT.3dshapes
%_datadir/kicad/modules/packages3d/Capacitor_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Capacitor_Tantalum_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Capacitor_THT.3dshapes
%_datadir/kicad/modules/packages3d/Connector.3dshapes
%_datadir/kicad/modules/packages3d/Connector_Coaxial.3dshapes
%_datadir/kicad/modules/packages3d/Connector_FFC-FPC.3dshapes
%_datadir/kicad/modules/packages3d/Connector_IDC.3dshapes
%_datadir/kicad/modules/packages3d/Connector_JST.3dshapes
%_datadir/kicad/modules/packages3d/Connector_Molex.3dshapes
%_datadir/kicad/modules/packages3d/Connector_Phoenix_GMSTB.3dshapes
%_datadir/kicad/modules/packages3d/Connector_Phoenix_MC.3dshapes
%_datadir/kicad/modules/packages3d/Connector_Phoenix_MC_HighVoltage.3dshapes
%_datadir/kicad/modules/packages3d/Connector_Phoenix_MSTB.3dshapes
%_datadir/kicad/modules/packages3d/Connector_Pin.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinHeader_1.00mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinHeader_1.27mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinHeader_2.00mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinHeader_2.54mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinSocket_1.00mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinSocket_1.27mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinSocket_2.00mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_PinSocket_2.54mm.3dshapes
%_datadir/kicad/modules/packages3d/Connector_USB.3dshapes

%files part2
%dir %_datadir/kicad
%dir %_datadir/kicad/modules
%dir %_datadir/kicad/modules/packages3d/
%_datadir/kicad/modules/packages3d/Converter_ACDC.3dshapes
%_datadir/kicad/modules/packages3d/Converter_DCDC.3dshapes
%_datadir/kicad/modules/packages3d/Crystal.3dshapes
%_datadir/kicad/modules/packages3d/Diode_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Diode_THT.3dshapes
%_datadir/kicad/modules/packages3d/Display.3dshapes
%_datadir/kicad/modules/packages3d/Display_7Segment.3dshapes
%_datadir/kicad/modules/packages3d/Fuse.3dshapes
%_datadir/kicad/modules/packages3d/Inductor_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Inductor_THT.3dshapes
%_datadir/kicad/modules/packages3d/LED_SMD.3dshapes
%_datadir/kicad/modules/packages3d/LED_THT.3dshapes
%_datadir/kicad/modules/packages3d/OptoDevice.3dshapes
%_datadir/kicad/modules/packages3d/Oscillator.3dshapes
%_datadir/kicad/modules/packages3d/Package_BGA.3dshapes
%_datadir/kicad/modules/packages3d/Package_DFN_QFN.3dshapes
%_datadir/kicad/modules/packages3d/Package_DIP.3dshapes
%_datadir/kicad/modules/packages3d/Package_DirectFET.3dshapes
%_datadir/kicad/modules/packages3d/Package_QFP.3dshapes
%_datadir/kicad/modules/packages3d/Package_SO.3dshapes
%_datadir/kicad/modules/packages3d/Package_SON.3dshapes
%_datadir/kicad/modules/packages3d/Package_TO_SOT_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Package_TO_SOT_THT.3dshapes
%_datadir/kicad/modules/packages3d/Relay_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Relay_THT.3dshapes
%_datadir/kicad/modules/packages3d/Resistor_SMD.3dshapes
%_datadir/kicad/modules/packages3d/Resistor_THT.3dshapes
%_datadir/kicad/modules/packages3d/RF_Module.3dshapes
%_datadir/kicad/modules/packages3d/Sensor_Audio.3dshapes
%_datadir/kicad/modules/packages3d/Sensor_Current.3dshapes
%_datadir/kicad/modules/packages3d/Sensors.3dshapes
%_datadir/kicad/modules/packages3d/TestPoint.3dshapes
%_datadir/kicad/modules/packages3d/Valve.3dshapes

%changelog
* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- Initial build for ALT Sisyphus
