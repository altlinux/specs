%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name dleyna
%define api_ver 1.0

Name: %_name-connector-dbus
Version: 0.4.1
Release: alt1

Summary: D-Bus connector for dLeyna services
Group: System/Servers
License: LGPLv2.1
Url: https://github.com/phako/dleyna-connector-dbus

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/phako/dleyna-connector-dbus.git
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel libdbus-devel libdleyna-core-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains pc-file for developing applications that
use %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%dir %_libdir/%_name-%api_ver/connectors
%_libdir/%_name-%api_ver/connectors/lib%name.so
%doc AUTHORS ChangeLog README*

#%files devel
#%_pkgconfigdir/%name-%api_ver.pc

%changelog
* Mon Sep 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1 (new upstream, ported to Meson build system)

* Wed Oct 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

