#
# This is not a mistake. Indi libraries have symbols that are defined in other
# indi libraries. At the stage of linking the target application, everything
# will be resolved.
#
%set_verify_elf_method none

%ifarch %ix86
%def_without check
%else
%def_with check
%endif

%def_without static
%def_with use_system_jsonlib
%def_with use_system_httplib
%def_with use_system_hidapi
%def_with qt

#
# Upstream provides static libraries for some of its components, despite
# the fact that static library building is disabled in CMake.
# See https://www.altlinux.org/LTO
#
%define optflags_lto %nil

%global descr INDI is a distributed control protocol designed to operate\
astronomical instrumentation. INDI is small, flexible, easy to parse,\
and scalable. It supports common DCS functions such as remote control,\
data acquisition, monitoring, and a lot more.

%global soversion 2

Name: indi
Version: 2.2.1.1
Release: alt1

Summary: Instrument Neutral Distributed Interface
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later and BSD-3-Clause AND ISC AND MIT AND CFITSIO
Group: System/Libraries
Url: https://indilib.org
Vcs: https://github.com/indilib/indi.git

Source: %name-%version.tar
Patch0: fix-indi2-ALT-SharedLibsPolicy-CMakeLists.txt.patch
Patch1: fix-indi2-ALT-vtable_undefined_symbol-CMakeLists.txt.patch

BuildRequires(Pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: libbrotli-devel
BuildRequires: libcfitsio-devel
BuildRequires: libcurl-devel
BuildRequires: libev-devel
BuildRequires: libfftw3-devel
BuildRequires: libjpeg-devel
BuildRequires: libgsl-devel
BuildRequires: libnova-devel
BuildRequires: libusb-devel
BuildRequires: rtl-sdr-devel
BuildRequires: zlib-devel

%if_with use_system_jsonlib
BuildRequires: nlohmann-json-devel
%endif

%if_with use_system_httplib
BuildRequires: libcpp-httplib-devel
BuildRequires: libssl-devel
%endif

%if_with use_system_hidapi
BuildRequires: libhidapi-devel
%endif

%if_with qt
BuildRequires: qt6-base-devel
%endif

%if_with check
BuildRequires: ctest
BuildRequires: libgmock-devel
%endif

Provides: indilib
Obsoletes: indilib <= 1.9.0-alt3

%description
%descr

%package -n lib%name-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Obsoletes: indilib-common <= 1.9.0-alt3

%description -n lib%name-common
%descr
%summary.

%package -n lib%name%soversion
Group: System/Libraries
Summary: %summary
Requires: lib%name-common
Provides: libindi
Obsoletes: libindi <= 1.9.0-alt3

%description -n lib%name%soversion
%descr
%summary.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files for the %name
Requires: lib%name%soversion
Provides: indi-devel
Provides: indilib-devel

%description -n lib%name-devel
%descr
%summary.

%package -n lib%name-devel-static
Group: Development/C++
Summary: Static libraries from %name
Requires: lib%name-devel
Conflicts: libindi-devel < 1.8.9-alt1

%description -n lib%name-devel-static
%descr
%summary.

%prep
%setup
%autopatch

%build
%add_optflags %optflags_shared
%cmake -G Ninja \
	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,--no-allow-shlib-undefined" \
	-DUDEVRULES_INSTALL_DIR=%_udevrulesdir \
	-DINDI_BUILD_STATIC=%{with static} \
	-DINDI_SYSTEM_JSONLIB=%{with use_system_jsonlib} \
	-DINDI_SYSTEM_HTTPLIB=%{with use_system_httplib} \
	-DINDI_SYSTEM_HIDAPILIB=%{with use_system_hidapi} \
	-DINDI_BUILD_QT_CLIENT=%{with qt} \
	-DINDI_BUILD_UNITTESTS=%{with check} \
	-DINDI_BUILD_INTEGTESTS=%{with check} \
%nil
%cmake_build

%install
%cmake_install

%check
pushd %_cmake__builddir
# This is not an error. The test fails due to hasher limitations.
ctest -E IndiserverSingleDriver.DontLeakFds
popd

%files
%_bindir/%{name}_Excalibur
%_bindir/%{name}_aaf2_focus
%_bindir/%{name}_aagsolo_weather
%_bindir/%{name}_activefocuser_focus
%_bindir/%{name}_alluna_tcs2
%_bindir/%{name}_alpaca_ccd
%_bindir/%{name}_alpaca_dome
%_bindir/%{name}_alpaca_filterwheel
%_bindir/%{name}_alpaca_focuser
%_bindir/%{name}_alpaca_server
%_bindir/%{name}_alpaca_telescope
%_bindir/%{name}_alto
%_bindir/%{name}_arduinost4
%_bindir/%{name}_astrolink4
%_bindir/%{name}_astrolink4mini2
%_bindir/%{name}_astromech_lpm
%_bindir/%{name}_astromechfoc
%_bindir/%{name}_astrometry
%_bindir/%{name}_astrotrac_telescope
%_bindir/%{name}_avalon_upas
%_bindir/%{name}_baader_dome
%_bindir/%{name}_camelot_rotator
%_bindir/%{name}_celestron_dewpower
%_bindir/%{name}_celestron_gps
%_bindir/%{name}_celestron_sct_focus
%_bindir/%{name}_cheapodc
%_bindir/%{name}_crux_mount
%_bindir/%{name}_ddw_dome
%_bindir/%{name}_deepskydad_af1_focus
%_bindir/%{name}_deepskydad_af2_focus
%_bindir/%{name}_deepskydad_af3_focus
%_bindir/%{name}_deepskydad_fp
%_bindir/%{name}_deepskydad_fr1
%_bindir/%{name}_dmfc_focus
%_bindir/%{name}_domepro2_dome
%_bindir/%{name}_dragon_light
%_bindir/%{name}_dragonlair_dome
%_bindir/%{name}_dreamfocuser_focus
%_bindir/%{name}_dsc_telescope
%_bindir/%{name}_efa_focus
%_bindir/%{name}_eq500x_telescope
%_bindir/%{name}_esatto_focus
%_bindir/%{name}_esattoarco_focus
%_bindir/%{name}_eval
%_bindir/%{name}_falcon_rotator
%_bindir/%{name}_falconv2_rotator
%_bindir/%{name}_fcusb_focus
%_bindir/%{name}_flipflat
%_bindir/%{name}_gemini_flatpanel
%_bindir/%{name}_gemini_focus
%_bindir/%{name}_getprop
%_bindir/%{name}_getdevice
%_bindir/%{name}_giotto
%_bindir/%{name}_gpusb
%_bindir/%{name}_hakos_roof
%_bindir/%{name}_hitecastrodc_focus
%_bindir/%{name}_hitech_weather
%_bindir/%{name}_iafscaa_focus
%_bindir/%{name}_ieaf_focus
%_bindir/%{name}_ieq_telescope
%_bindir/%{name}_ieqlegacy_telescope
%_bindir/%{name}_imager_agent
%_bindir/%{name}_integra_focus
%_bindir/%{name}_ioptronHC8406
%_bindir/%{name}_ioptron_wheel
%_bindir/%{name}_ioptronv3_telescope
%_bindir/%{name}_ipx800v4
%_bindir/%{name}_joystick
%_bindir/%{name}_lacerta_mfoc_fmc_focus
%_bindir/%{name}_lacerta_mfoc_focus
%_bindir/%{name}_lakeside_focus
%_bindir/%{name}_lx200_10micron
%_bindir/%{name}_lx200_16
%_bindir/%{name}_lx200_esp32go
%_bindir/%{name}_lx200_OnStep
%_bindir/%{name}_lx200_OpenAstroTech
%_bindir/%{name}_lx200_TeenAstro
%_bindir/%{name}_lx200_pegasus_nyx101
%_bindir/%{name}_lx200am5
%_bindir/%{name}_lx200ap_legacy
%_bindir/%{name}_lx200ap_v2
%_bindir/%{name}_lx200autostar
%_bindir/%{name}_lx200basic
%_bindir/%{name}_lx200classic
%_bindir/%{name}_lx200fs2
%_bindir/%{name}_lx200gemini
%_bindir/%{name}_lx200generic
%_bindir/%{name}_lx200gotonova
%_bindir/%{name}_lx200gps
%_bindir/%{name}_lx200pulsar2
%_bindir/%{name}_lx200ss2000pc
%_bindir/%{name}_lx200zeq25
%_bindir/%{name}_lynx_focus
%_bindir/%{name}_manual_wheel
%_bindir/%{name}_mbox_weather
%_bindir/%{name}_meta_weather
%_bindir/%{name}_mlastro_rpa
%_bindir/%{name}_microtouch_focus
%_bindir/%{name}_moonlite_focus
%_bindir/%{name}_moonlitedro_focus
%_bindir/%{name}_myDewControllerPro
%_bindir/%{name}_mydcp4esp32
%_bindir/%{name}_myfocuserpro2_focus
%_bindir/%{name}_nexdome_beaver
%_bindir/%{name}_nfocus
%_bindir/%{name}_nframe_rotator
%_bindir/%{name}_nightcrawler_focus
%_bindir/%{name}_nstep_focus
%_bindir/%{name}_onfocus_focus
%_bindir/%{name}_openweathermap_weather
%_bindir/%{name}_optec_wheel
%_bindir/%{name}_paramount_telescope
%_bindir/%{name}_pegasus_focuscube
%_bindir/%{name}_pegasus_focuscube3
%_bindir/%{name}_pegasus_flatmaster
%_bindir/%{name}_pegasus_ppb
%_bindir/%{name}_pegasus_ppba
%_bindir/%{name}_pegasus_prodigyMF
%_bindir/%{name}_pegasus_scopsoag
%_bindir/%{name}_pegasus_spb
%_bindir/%{name}_pegasus_upb
%_bindir/%{name}_pegasus_upb3
%_bindir/%{name}_pegasusindigo_wheel
%_bindir/%{name}_perfectstar_focus
%_bindir/%{name}_pinefeat_cef_focus
%_bindir/%{name}_planewave_deltat
%_bindir/%{name}_planewave_telescope
%_bindir/%{name}_pmc8_telescope
%_bindir/%{name}_pyxis_rotator
%_bindir/%{name}_qhycfw1_wheel
%_bindir/%{name}_qhycfw2_wheel
%_bindir/%{name}_qhycfw3_wheel
%_bindir/%{name}_quantum_wheel
%_bindir/%{name}_rainbow_telescope
%_bindir/%{name}_rainbowrsf_focus
%_bindir/%{name}_rbfocus_focus
%_bindir/%{name}_rigel_dome
%_bindir/%{name}_robo_focus
%_bindir/%{name}_rolloff_dome
%_bindir/%{name}_rtlsdr
%_bindir/%{name}_safetymonitor
%_bindir/%{name}_scopedome_dome
%_bindir/%{name}_script_dome
%_bindir/%{name}_script_telescope
%_bindir/%{name}_seestar_ccd
%_bindir/%{name}_sestosenso2_focus
%_bindir/%{name}_sestosenso3_focus
%_bindir/%{name}_sestosenso_focus
%_bindir/%{name}_setprop
%_bindir/%{name}_siefs_focus
%_bindir/%{name}_simulator_ccd
%_bindir/%{name}_simulator_dome
%_bindir/%{name}_simulator_dustcover
%_bindir/%{name}_simulator_focus
%_bindir/%{name}_simulator_gps
%_bindir/%{name}_simulator_guide
%_bindir/%{name}_simulator_io
%_bindir/%{name}_simulator_lightpanel
%_bindir/%{name}_simulator_receiver
%_bindir/%{name}_simulator_rotator
%_bindir/%{name}_simulator_pac
%_bindir/%{name}_simulator_sqm
%_bindir/%{name}_simulator_telescope
%_bindir/%{name}_simulator_weather
%_bindir/%{name}_simulator_wheel
%_bindir/%{name}_skycommander_telescope
%_bindir/%{name}_skysafari
%_bindir/%{name}_skywatcherAltAzMount
%_bindir/%{name}_smartfocus_focus
%_bindir/%{name}_snapcap
%_bindir/%{name}_spectracyber
%_bindir/%{name}_sqm_weather
%_bindir/%{name}_startech_hub
%_bindir/%{name}_star2000
%_bindir/%{name}_steeldrive2_focus
%_bindir/%{name}_steeldrive_focus
%_bindir/%{name}_svbony_powerbox
%_bindir/%{name}_synscan_telescope
%_bindir/%{name}_synscanlegacy_telescope
%_bindir/%{name}_tcfs3_focus
%_bindir/%{name}_tcfs_focus
%_bindir/%{name}_teenastro_focus
%_bindir/%{name}_temma_telescope
%_bindir/%{name}_terrans_powerboxgo_v2
%_bindir/%{name}_terrans_powerboxpro_v2
%_bindir/%{name}_trutech_wheel
%_bindir/%{name}_universalror_dome
%_bindir/%{name}_ups_safety
%_bindir/%{name}_uranus_weather
%_bindir/%{name}_usbdewpoint
%_bindir/%{name}_usbfocusv3_focus
%_bindir/%{name}_v4l2_ccd
%_bindir/%{name}_vantage_weather
%_bindir/%{name}_wake_on_lan
%_bindir/%{name}_wanderer_cover
%_bindir/%{name}_wanderer_dew_terminator
%_bindir/%{name}_wanderer_eclipse
%_bindir/%{name}_wanderer_lite_rotator
%_bindir/%{name}_wanderer_rotator_lite_v2
%_bindir/%{name}_wanderer_rotator_mini
%_bindir/%{name}_wanderer_snowflake_wheel
%_bindir/%{name}_wandererbox_plus_v3
%_bindir/%{name}_wandererbox_pro_v3
%_bindir/%{name}_wanderercover_v4_ec
%_bindir/%{name}_wanderercover_v4_pro_ec
%_bindir/%{name}_watchdog
%_bindir/%{name}_watcher_weather
%_bindir/%{name}_wavesharemodbus_relay
%_bindir/%{name}_weather_safety_alpaca
%_bindir/%{name}_weather_safety_proxy
%_bindir/%{name}_weatherflow_weather
%_bindir/%{name}_xagyl_wheel
%_bindir/%{name}server
%_bindir/shelyak_usis
%_udevrulesdir/80-dbk21-camera.rules
%_udevrulesdir/99-indi_auxiliary.rules

%files -n lib%name-common
%doc ChangeLog README
%_datadir/%name

%files -n lib%name%soversion
%_libdir/%name%soversion
%_libdir/lib%{name}AlignmentDriver.so.%{soversion}*
%_libdir/lib%{name}client.so.%{soversion}*
%_libdir/lib%{name}driver.so.%{soversion}*
%_libdir/lib%{name}lx200.so.%{soversion}*
%if_with qt
%_libdir/lib%{name}clientqt.so.%{soversion}*
%endif

%files -n lib%name-devel
%_includedir/lib%name
%_libdir/lib%{name}AlignmentDriver.so
%_libdir/lib%{name}client.so
%_libdir/lib%{name}driver.so
%_libdir/lib%{name}lx200.so
%if_with qt
%_libdir/lib%{name}clientqt.so
%endif
%_pkgconfigdir/lib%{name}.pc

%files -n lib%name-devel-static
%_libdir/lib%{name}AlignmentClient.a

%changelog
* Tue May 05 2026 Ulysses Apokin <ulysses@altlinux.org> 2.2.1.1-alt1
- New version.

* Wed Apr 01 2026 Ulysses Apokin <ulysses@altlinux.org> 2.1.9-alt3
- Used the default linker instead of the bfd linker on all arches.

* Sat Mar 07 2026 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.1.9-alt2
- e2k build fix

* Wed Feb 18 2026 Ulysses Apokin <ulysses@altlinux.org> 2.1.9-alt1
- Initial build for Sisyphus instead of obsolete indilib.
