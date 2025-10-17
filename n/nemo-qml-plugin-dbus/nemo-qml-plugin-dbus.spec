%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define libname libnemodbus
%define abiversion 1

Name: nemo-qml-plugin-dbus
Version: 2.1.39
Release: alt1

Summary: Nemo mobile D-Bus QML plugin
License: BSD-3-Clause and LGPL-2.1-or-later
Group: Graphical desktop/Other
URL: https://github.com/sailfishos/nemo-qml-plugin-dbus
VCS: https://github.com/sailfishos/nemo-qml-plugin-dbus.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel

Requires: %libname%abiversion = %EVR

%description
The Nemo Mobile D-Bus QML Plugin allows you to access services
on the system and session bus, as well as provide your own
services.

%package -n %libname%abiversion
Summary: nemo-dbus library provides C++11 extensions to QtDBus
Group: System/Libraries

%description -n %libname%abiversion
The nemo-dbus library provides C++11 extensions to QtDBus to
make it easier to call and handle the replies from asynchronous
DBus methods.

%package -n %libname-devel
Summary: Development libraries and headers for %libname
Group: Development/C++
Requires: %libname%abiversion = %EVR

%description -n %libname-devel
%summary.

%prep
%setup

%build
%qmake_qt5 CONFIG+=nostrip src
%make_build

%install
%install_qt5

# org.nemomobile.dbus legacy import
mkdir -p %buildroot/%_qt5_qmldir/org/nemomobile/dbus/
ln -s `relative %_qt5_qmldir/Nemo/DBus/%libname.so \
        %_qt5_qmldir/org/nemomobile/dbus/%libname.so` \
        %buildroot/%_qt5_qmldir/org/nemomobile/dbus/%libname.so
sed 's/Nemo.DBus/org.nemomobile.dbus/' \
    < %buildroot/%_qt5_qmldir/Nemo/DBus/qmldir \
    > %buildroot/%_qt5_qmldir/org/nemomobile/dbus/qmldir

%files
%_qt5_qmldir/Nemo/DBus/%libname.so
%_qt5_qmldir/Nemo/DBus/qmldir
%_qt5_qmldir/Nemo/DBus/plugins.qmltypes
# org.nemomobile.dbus legacy import
%_qt5_qmldir/org/nemomobile/dbus/%libname.so
%_qt5_qmldir/org/nemomobile/dbus/qmldir

%files -n %libname%abiversion
%_libdir/%libname.so.%abiversion
%_libdir/%libname.so.%abiversion.*

%files -n %libname-devel
%_pkgconfigdir/nemodbus.pc
%_libdir/%libname.so
%_includedir/nemo-dbus/
%_qt5_libdatadir/%libname.so

%changelog
* Wed Oct 15 2025 Egor Shestakov <ved@altlinux.org> 2.1.39-alt1
- Initial build.
