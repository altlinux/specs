Name: phosphor-objmgr
Version: 1.0.0
Release: alt1.git11c0cc3

Summary: Phosphor Object Manager
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-objmgr
Vcs: https://github.com/openbmc/phosphor-objmgr.git

Source: %name-%version.tar
Patch0: fix-phosphor-objmgr-1.0.0-git11c0cc3-ALT-meson.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: boost-asio-devel
BuildRequires: boost-devel-headers
BuildRequires: cli11-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libdbus-devel
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: libsystemd-devel
BuildRequires: libtinyxml2-devel
BuildRequires: meson
BuildRequires: sdbusplus-tools

%description
%summary.

%package -n lib%name
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name
%summary.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
%summary.

%package -n %name-tools
Summary: Tools for %name
Group: Other
Requires: lib%name = %EVR

%description -n %name-tools
%summary.

%prep
%setup
%autopatch

%build
%meson -Dtests=disabled \
	-Dwerror=false
%meson_build

%install
%meson_install

%files -n lib%name
%_libdir/libmapper.so.*
%dir %_libexecdir/%name
%_libexecdir/%name/mapperx

%files -n lib%name-devel
%_libdir/libmapper.so
%_pkgconfigdir/libmapper.pc
%_includedir/*

%files -n %name-tools
%_bindir/*
%_unitdir/*
%_datadir/dbus-1/*/*

%changelog
* Thu Aug 14 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt1.git11c0cc3
- Initial build for Sisyphus.
