%def_disable snapshot

%define _name dleyna
%define api_ver 1.0
%define gupnp_api_ver 1.2

Name: %_name-core
Version: 0.7.0
Release: alt1

Summary: Utilities for higher level %_name libraries
Group: System/Libraries
License: LGPLv2.1
Url: https://github.com/phako/%name

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/phako/dleyna-core.git
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgio-devel libgupnp%gupnp_api_ver-devel >= 1.2.1

%description
dleyna-core is a library of utility functions that are used by the higher
level dLeyna libraries that communicate with DLNA devices, e.g.,
dleyna-server. In brief, it provides APIs for logging, error, settings
and task management and an IPC abstraction API.

%package -n lib%name
Summary: Development files for %name
Group: System/Libraries

%description -n lib%name
dleyna-core is a library of utility functions that are used by the higher
level dLeyna libraries that communicate with DLNA devices, e.g.,
dleyna-server. In brief, it provides APIs for logging, error, settings
and task management and an IPC abstraction API.

This package provides shared %_name library.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name library.

%prep
%setup

%build

%meson
%meson_build

%install
%meson_install

%files -n lib%name
%_libdir/lib%_name-core-%api_ver.so.*
%doc AUTHORS ChangeLog README*

%files -n lib%name-devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-core-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc


%changelog
* Mon Sep 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0 (new upstream, ported to Meson build system)

* Mon Dec 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt2
- updated to v0.6.0-2-g1c6853f (ported to gupnp-1.2)

* Wed Oct 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

