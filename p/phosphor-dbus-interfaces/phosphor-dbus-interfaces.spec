%define _unpackaged_files_terminate_build 1
%define soversion 1

Name: phosphor-dbus-interfaces
Version: 1.0.0
Release: alt1

Summary: YAML descriptors of standard dbus interfaces

License: Apache-2.0
Group: System/Configuration/Other
Url: https://www.openbmc.org/
Vcs: https://github.com/openbmc/phosphor-dbus-interfaces.git

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++ cmake
BuildRequires: libsdbusplus-devel
BuildRequires: sdbusplus-tools

%description
YAML descriptors of standard D-Bus interfaces.
The format is described by the sdbusplus binding generation tool sdbus++.

%package -n lib%name%soversion
Summary: library of standard dbus interfaces
Group: System/Libraries

%description -n lib%name%soversion
%summary.

%package -n lib%name-devel
Summary: C++ headers for standard dbus interfaces
Group: Development/C++

%description -n lib%name-devel
%summary.

%package doc
Summary: documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
%summary.

%package data
Summary: YAML descriptors
Group: System/Configuration/Other
BuildArch: noarch

%description data
YAML descriptors of standard dbus interfaces.

%prep
%setup

%build
%meson --includedir=%_includedir/%name
%meson_build

%install
%meson_install

%files -n lib%name%soversion
%_libdir/libphosphor_dbus.so.%{soversion}*

%files -n lib%name-devel
%_libdir/libphosphor_dbus.so
%_includedir/%name
%_pkgconfigdir/%name.pc

%files doc
%_docdir/%name/

%files data
%_datadir/phosphor-dbus-yaml
%_datadir/redfish-registry

%changelog
* Thu Apr 24 2025 Anton Meleshnikov <alton@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
