Name: phosphor-objmgr
Version: 1.0.0
Release: alt3.git3fb58d2.1

Summary: Phosphor Object Manager
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-objmgr
Vcs: https://github.com/openbmc/phosphor-objmgr.git

Source: %name-%version.tar

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

%build
%meson -Dwerror=false
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
* Thu Jun 25 2026 Author: Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt3.git3fb58d2.1
- New snapshot.
- Enable tests.

* Tue Aug 26 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt2.gitea0e5d2
- Downgraded to commit from revision list.

* Thu Aug 14 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt1.git11c0cc3
- Initial build for Sisyphus.
