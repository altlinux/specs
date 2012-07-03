Name: libdbus-tqt
Version: 3.5.13
Release: alt1
Summary: TQT/KDE bindings for D-Bus
URL: http://dbus.freedesktop.org/
License: GPL or Academic Free License
Group: System/Libraries

Source0: dbus-tqt-%version.tar

# Automatically added by buildreq on Mon Dec 18 2006
BuildRequires: gcc-c++ libXext-devel libXt-devel libdbus-devel libjpeg-devel libpng-devel libtqt-devel cmake kde-common-devel

%description
TQT/KDE bindings for D-Bus.

%package devel
Summary: Developer package for TQT/KDE bindings for D-Bus
Requires: %name = %version-%release
Requires: libdbus-devel >= 0.94
Requires: libtqt-devel
Group: Development/C++

%description devel
Developer package for TQT/KDE bindings for D-Bus.

%prep
%setup -q -n dbus-tqt-%version

%build
%Kbuild -DPKGCONFIG_INSTALL_DIR=%_pkgconfigdir

%install
%Kinstall

%files
%_libdir/*.so.*

%files devel
%_includedir/dbus-1.0/dbus/*.h
%_pkgconfigdir/dbus-tqt.pc
%_libdir/*.so

%changelog
* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- Initial build for TDE 3.5.13
