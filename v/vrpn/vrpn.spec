%define _unpackaged_files_terminate_build 1

%global _cmake__builddir %_target_cpu-alt-linux

Name:    vrpn
Version: 07.36
Release: alt1

Summary: Virtual Reality Peripheral Network
License: BSL-1.0 and GPL-2.0-or-later
Group:   Networking/Other
URL:     https://github.com/vrpn/vrpn/wiki
VCS:     https://github.com/vrpn/vrpn

Source: %name-%version.tar
Source1: %name-postsubmodules-%version.tar
Patch0: fat-lto-objects.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libusb-devel libhidapi-devel jsoncpp-devel
BuildRequires: libgpm-devel libmodbus-devel libwiiuse-devel
BuildRequires: libfreeglut-devel libGL-devel libGLU-devel
BuildRequires: qt5-base-devel perl-Parse-RecDescent
BuildRequires: python3-dev swig

%description
The Virtual-Reality Peripheral Network (VRPN) is a set of classes within a
library and a set of servers that are designed to implement a
network-transparent interface between application programs and the set of
physical devices (tracker, etc.) used in a virtual-reality (VR) system.
The idea is to have a PC or other host at each VR station that controls
the peripherals (tracker, button device, haptic device, analog inputs,
sound, etc). VRPN provides connections between the application and all of
the devices using the appropriate class-of-service for each type of device
sharing this link. The application remains unaware of the network
topology. Note that it is possible to use VRPN with devices that are
directly connected to the machine that the application is running on,
either using separate control programs or running all as a single program.

%package server
Summary: VRPN server
Group: Networking/Other
Requires: %name = %EVR

%description server
The VRPN server and sample configuration.

%package devel
Summary: Development files for VRPN
Group: Development/C
Requires: %name = %EVR

%description devel
Headers and static libraries for building VRPN applications.

%package tests
Summary: Test programs for VRPN
Group: Other
Requires: %name = %EVR

%description tests
Test and example programs for VRPN.

%package -n python3-module-vrpn
Summary: Python 3 bindings for VRPN
Group: Development/Python3
Requires: %name = %EVR
Requires: python3

%description -n python3-module-vrpn
Python 3 bindings for the Virtual Reality Peripheral Network library.

%prep
%setup -a1
%patch0 -p1

%build
%cmake \
    -DVRPN_GPL_SERVER=ON \
    -DVRPN_USE_MODBUS=ON \
    -DVRPN_USE_MOTIONNODE=ON \
    -DMODBUS_INCLUDE_DIR=%_includedir/modbus \
    -DMODBUS_LIBRARY=%_libdir/libmodbus.so \
    -DVRPN_USE_LOCAL_HIDAPI=OFF \
    -DVRPN_USE_LOCAL_JSONCPP=OFF \
    -DVRPN_BUILD_HID_GUI=ON

%cmake_build

%install
%cmake_install
# libvrpn_timecode_generator.a is empty when VRPN_INCLUDE_TIMECODE_SERVER is off.
rm -f %buildroot%_libdir/libvrpn_timecode_generator.a

# VRPN installs the Python module into /usr/lib/pythondist-packages, but ALT uses site-packages.
if [ -d %buildroot/usr/lib/pythondist-packages ]; then
	mkdir -p %buildroot/%python3_sitelibdir
	mv %buildroot/usr/lib/pythondist-packages/* %buildroot/%python3_sitelibdir/
	rmdir %buildroot/usr/lib/pythondist-packages 2>/dev/null || true
fi

# hid_gui target has no install rule upstream.
install -Dm755 %_cmake__builddir/hid_gui/vrpn_hid_gui %buildroot%_bindir/vrpn_hid_gui

# VRPN installs gpsnmealib headers flat in include/, but vrpn_Tracker_GPS.h
# and the headers themselves reference them as gpsnmealib/*. Reorganize.
mkdir -p %buildroot%_includedir/gpsnmealib
for hdr in nmeaParser.h latLonCoord.h utmCoord.h; do
    if [ -e %buildroot%_includedir/$hdr ]; then
        mv %buildroot%_includedir/$hdr %buildroot%_includedir/gpsnmealib/
    fi
done
install -m644 gpsnmealib/typedCoord.h %buildroot%_includedir/gpsnmealib/

# Move test/example binaries out of %%_bindir to %%_libexecdir/%%name per ALT guidelines.
mkdir -p %buildroot%_libexecdir/%name
for app in \
    add_vrpn_cookie bdbox_client checklogfile clock_drift_estimator \
    ff_client forcedevice_test_client forwarderClient logfilesenders \
    logfiletypes phan_client printcereal printvals sound_client \
    sphere_client testSharedObject test_Zaber test_imager test_mutex \
    text tracker_to_poser vrpn_LamportClock vrpn_ping testimager_client \
    vrpn_orientation client_and_server forward last_of_sequence \
    sample_analog sample_server testSharedObjectServer test_analogfly \
    test_auxiliary_logger test_freespace test_logging test_loopback \
    test_mutexServer test_peerMutex test_radamec_spi test_rumble \
    test_vrpn testimager_server textServer time_test; do
    if [ -e %buildroot%_bindir/$app ]; then
        mv %buildroot%_bindir/$app %buildroot%_libexecdir/%name/
    fi
done

%files
%doc README README.Compiling README.Legal
%_bindir/vrpn_HID_device_watcher
%_bindir/vrpn_average_analogs
%_bindir/vrpn_hid_gui
%_bindir/vrpn_log_devices
%_bindir/vrpn_print_devices
%_bindir/vrpn_print_messages
%_bindir/vrpn_print_performance
%_bindir/run_auxiliary_logger
%_bindir/vrpn_streamPrint

%files server
%config(noreplace) %_sysconfdir/vrpn.cfg
%_datadir/%name-%version
%_bindir/vrpn_server

%files devel
%_includedir/vrpn_*.h
%_includedir/quat.h
%_includedir/gpsnmealib/
%_libdir/libvrpn.a
%_libdir/libvrpnserver.a
%_libdir/libvrpn_atmel.a
%_libdir/libquat.a
%_libdir/libgpsnmea.a

%files tests
%_libexecdir/%name/

%files -n python3-module-vrpn
%python3_sitelibdir/vrpn*.so

%changelog
* Thu Jul 16 2026 Sergey Palcheh <minergenon@altlinux.org> 07.36-alt1
- Initial build for Sisyphus
