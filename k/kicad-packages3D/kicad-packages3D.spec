# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: kicad-packages3D
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Version: 6.0.0
Release: alt1
Source: %name-%version.tar.gz
License: GPLv2+
Group: Engineering
Url: https://code.launchpad.net/kicad

Packager: Anton Midyukov <antohami@altlinux.org>
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake gcc-c++

Requires: kicad-packages3D-part1 = %EVR
Requires: kicad-packages3D-part2 = %EVR
Requires: kicad-packages3D-part3 = %EVR
Requires: kicad-packages3D-part4 = %EVR

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит в себе 3D-модели для kicad.

%package part1
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Group: Engineering

Requires: kicad-common

%description part1
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.
Part1

%description part1 -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит в себе 3D-модели для kicad.
Часть 1

%package part2
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Group: Engineering

Requires: kicad-common

%description part2
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.
Part2

%description part2 -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит в себе 3D-модели для kicad.
Часть 2

%package part3
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Group: Engineering

Requires: kicad-common

%description part3
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.
Part3

%description part3 -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит в себе 3D-модели для kicad.
Часть 3

%package part4
Summary: 3D models for kicad (creation of electronic schematic diagrams)
Summary(ru_RU.UTF-8): 3D модели для kicad (разработка печатных плат)
Group: Engineering

Requires: kicad-common

%description part4
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

%name is a set of 3D models needed by kicad.
Part4

%description part4 -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

%name содержит в себе 3D-модели для kicad.
Часть 4

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files

%files part1
%_datadir/kicad/3dmodels/Battery.3dshapes
%_datadir/kicad/3dmodels/Button_Switch_SMD.3dshapes
%_datadir/kicad/3dmodels/Button_Switch_THT.3dshapes
%_datadir/kicad/3dmodels/Buzzer_Beeper.3dshapes
%_datadir/kicad/3dmodels/Capacitor_SMD.3dshapes
%_datadir/kicad/3dmodels/Capacitor_Tantalum_SMD.3dshapes
%_datadir/kicad/3dmodels/Capacitor_THT.3dshapes
%_datadir/kicad/3dmodels/Connector.3dshapes
%_datadir/kicad/3dmodels/Connector_AMASS.3dshapes
%_datadir/kicad/3dmodels/Connector_BarrelJack.3dshapes
%_datadir/kicad/3dmodels/Connector_Card.3dshapes
%_datadir/kicad/3dmodels/Connector_Coaxial.3dshapes
%_datadir/kicad/3dmodels/Connector_Dsub.3dshapes
%_datadir/kicad/3dmodels/Connector_FFC-FPC.3dshapes
%_datadir/kicad/3dmodels/Connector_IDC.3dshapes
%_datadir/kicad/3dmodels/Connector_JST.3dshapes
%_datadir/kicad/3dmodels/Connector_Molex.3dshapes
%_datadir/kicad/3dmodels/Connector_Phoenix_GMSTB.3dshapes
%_datadir/kicad/3dmodels/Connector_Phoenix_MC.3dshapes
%_datadir/kicad/3dmodels/Connector_Phoenix_MC_HighVoltage.3dshapes
%_datadir/kicad/3dmodels/Connector_Phoenix_MSTB.3dshapes
%_datadir/kicad/3dmodels/Connector_Pin.3dshapes

%files part2
%_datadir/kicad/3dmodels/Connector_PinHeader_1.00mm.3dshapes
%_datadir/kicad/3dmodels/Connector_PinHeader_1.27mm.3dshapes
%_datadir/kicad/3dmodels/Connector_PinHeader_2.00mm.3dshapes
%_datadir/kicad/3dmodels/Connector_PinHeader_2.54mm.3dshapes

%files part3
%_datadir/kicad/3dmodels/Connector_PinSocket_1.00mm.3dshapes
%_datadir/kicad/3dmodels/Connector_PinSocket_1.27mm.3dshapes
%_datadir/kicad/3dmodels/Connector_PinSocket_2.00mm.3dshapes
%_datadir/kicad/3dmodels/Connector_PinSocket_2.54mm.3dshapes

%files part4
%_datadir/kicad/3dmodels/Connector_RJ.3dshapes
%_datadir/kicad/3dmodels/Connector_Samtec.3dshapes
%_datadir/kicad/3dmodels/Connector_SATA_SAS.3dshapes
%_datadir/kicad/3dmodels/Connector_Stocko.3dshapes
%_datadir/kicad/3dmodels/Connector_USB.3dshapes
%_datadir/kicad/3dmodels/Converter_ACDC.3dshapes
%_datadir/kicad/3dmodels/Converter_DCDC.3dshapes
%_datadir/kicad/3dmodels/Crystal.3dshapes
%_datadir/kicad/3dmodels/Diode_SMD.3dshapes
%_datadir/kicad/3dmodels/Diode_THT.3dshapes
%_datadir/kicad/3dmodels/Display.3dshapes
%_datadir/kicad/3dmodels/Display_7Segment.3dshapes
%_datadir/kicad/3dmodels/Ferrite_THT.3dshapes
%_datadir/kicad/3dmodels/Filter.3dshapes
%_datadir/kicad/3dmodels/Fuse.3dshapes
%_datadir/kicad/3dmodels/Heatsink.3dshapes
%_datadir/kicad/3dmodels/Inductor_SMD.3dshapes
%_datadir/kicad/3dmodels/Inductor_THT.3dshapes
%_datadir/kicad/3dmodels/LED_SMD.3dshapes
%_datadir/kicad/3dmodels/LED_THT.3dshapes
%_datadir/kicad/3dmodels/Module.3dshapes
%_datadir/kicad/3dmodels/MountingEquipment.3dshapes
%_datadir/kicad/3dmodels/Mounting_Wuerth.3dshapes
%_datadir/kicad/3dmodels/OptoDevice.3dshapes
%_datadir/kicad/3dmodels/Oscillator.3dshapes
%_datadir/kicad/3dmodels/Package_BGA.3dshapes
%_datadir/kicad/3dmodels/Package_DFN_QFN.3dshapes
%_datadir/kicad/3dmodels/Package_DIP.3dshapes
%_datadir/kicad/3dmodels/Package_DirectFET.3dshapes
%_datadir/kicad/3dmodels/Package_LGA.3dshapes
%_datadir/kicad/3dmodels/Package_QFP.3dshapes
%_datadir/kicad/3dmodels/Package_SIP.3dshapes
%_datadir/kicad/3dmodels/Package_SO.3dshapes
%_datadir/kicad/3dmodels/Package_SON.3dshapes
%_datadir/kicad/3dmodels/Package_TO_SOT_SMD.3dshapes
%_datadir/kicad/3dmodels/Package_TO_SOT_THT.3dshapes
%_datadir/kicad/3dmodels/Potentiometer_SMD.3dshapes
%_datadir/kicad/3dmodels/Potentiometer_THT.3dshapes
%_datadir/kicad/3dmodels/Relay_SMD.3dshapes
%_datadir/kicad/3dmodels/Relay_THT.3dshapes
%_datadir/kicad/3dmodels/Resistor_SMD.3dshapes
%_datadir/kicad/3dmodels/Resistor_THT.3dshapes
%_datadir/kicad/3dmodels/RF_Antenna.3dshapes
%_datadir/kicad/3dmodels/RF_Converter.3dshapes
%_datadir/kicad/3dmodels/RF_Module.3dshapes
%_datadir/kicad/3dmodels/Sensor.3dshapes
%_datadir/kicad/3dmodels/Sensor_Audio.3dshapes
%_datadir/kicad/3dmodels/Sensor_Current.3dshapes
%_datadir/kicad/3dmodels/Sensor_Distance.3dshapes
%_datadir/kicad/3dmodels/Sensor_Pressure.3dshapes
%_datadir/kicad/3dmodels/TerminalBlock_Altech.3dshapes
%_datadir/kicad/3dmodels/TerminalBlock_Phoenix.3dshapes
%_datadir/kicad/3dmodels/TestPoint.3dshapes
%_datadir/kicad/3dmodels/Transformer_SMD.3dshapes
%_datadir/kicad/3dmodels/Transformer_THT.3dshapes
%_datadir/kicad/3dmodels/Valve.3dshapes
%_datadir/kicad/3dmodels/Varistor.3dshapes

%changelog
* Thu Jan 06 2022 Anton Midyukov <antohami@altlinux.org> 6.0.0-alt1
- new version 6.0.0

* Sun Oct 11 2020 Anton Midyukov <antohami@altlinux.org> 5.1.6-alt1
- new version 5.1.6

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.4-alt1
- new version 5.1.4

* Fri Apr 26 2019 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt1
- New version 5.1.2

* Sat Mar 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.0-alt1
- New version 5.1.0

* Sat Jan 05 2019 Anton Midyukov <antohami@altlinux.org> 5.0.2-alt1
- New version 5.0.2

* Thu Nov 22 2018 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- New version 5.0.1

* Wed Jul 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- Initial build for ALT Sisyphus
