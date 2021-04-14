%define repo qtdbusextended

Name: libdbusextended-qt5
Summary: Extended DBus for Qt
Version: 0.0.3
Release: alt1
License: LGPL-2.1+
Group: System/Libraries
Url: https://github.com/nemomobile/qtdbusextended
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%description
%summary.

%package -n dbusextended-qt5-devel
Summary: Development package for %name
Group: Development/Other

%description -n dbusextended-qt5-devel
Header files and libraries for %name.

%prep
%setup -n %repo-%version

%build
%qmake_qt5 CONFIG+=nostrip
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc COPYING README.md
%_libdir/lib*.so.1*

%files -n dbusextended-qt5-devel
%dir %_qt5_headerdir/DBusExtended/
%_qt5_headerdir/DBusExtended/DBusExtended
%_qt5_headerdir/DBusExtended/DBusExtendedAbstractInterface
%_qt5_headerdir/DBusExtended/dbusextended.h
%_qt5_headerdir/DBusExtended/dbusextendedabstractinterface.h
%_qt5_archdatadir/mkspecs/features/*.prf
%_pkgconfigdir/*.pc
%_libdir/lib*.so

%changelog
* Wed Apr 14 2021 Leontiy Volodin <lvol@altlinux.org> 0.0.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
