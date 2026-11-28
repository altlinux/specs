Name: mrpdi
Version: 2.8.0
Release: alt1

Summary: User space drivers for interactive whiteboards

License: GPL-3.0-or-later
Group: System/Configuration/Hardware
URL: https://github.com/edupals/mrpdi
# Source-url: https://github.com/edupals/mrpdi/tree/master
Source: %name-%version.tar
Source1: %name.service
Source2: %name.conf
Source3: README.ALT
Source4: %name-gui-launch.sh
Patch0: %name-build.patch
Patch1: %name-polkit.patch
Patch2: %name-callbacks.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake gcc-c++
BuildRequires: pkgconfig(gtkmm-3.0) pkgconfig(giomm-2.4)
BuildRequires: pkgconfig(glibmm-2.4) pkgconfig(libconfig++)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1) pkgconfig(hidapi-libusb)
BuildRequires: pkgconfig(libusb-1.0) pkgconfig(x11) pkgconfig(xrandr)

%description
MrPDI provides user space drivers for interactive whiteboards, including
eBeam, SMART Board 6xx, Team Board and IQBoard. It includes command line
and graphical tools for device discovery and calibration.

%package -n libmrpdi2
Summary: Runtime library for MrPDI whiteboard drivers
Group: System/Libraries

%description -n libmrpdi2
Runtime library used by the MrPDI command line and graphical tools and
their interactive whiteboard driver plugins.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp %SOURCE3 .

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWITH_PROMETHEAN=OFF
%cmake_build

%install
%cmake_install
install -D -m 0755 %SOURCE4 %buildroot%_bindir/%name-gui-launch
install -D -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -D -m 0644 %SOURCE2 %buildroot%_prefix/lib/modules-load.d/%name.conf
# The unversioned library is private to this application; there is no SDK.
rm %buildroot%_libdir/libmrpdi.so

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.ALT
%_bindir/mrpdi-*
%_libdir/mrpdi/
%dir %_sysconfdir/mrpdi
%_unitdir/%name.service
%_prefix/lib/modules-load.d/%name.conf
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/polkit-1/actions/lliurex.mrpdi.gui.policy

%files -n libmrpdi2
%_libdir/libmrpdi.so.2
%_libdir/libmrpdi.so.2.8.0

%changelog
* Fri Nov 27 2026 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- initial build for ALT Sisyphus

