%def_enable snapshot

%define _name dleyna
%define api_ver 1.0

Name: %_name-core
Version: 0.5.0
Release: alt1

Summary: Utilities for higher level %_name libraries
Group: System/Libraries
License: LGPLv2.1
Url: https://01.org/%_name/

%if_disabled snapshot
Source: https://01.org/%_name/sites/default/files/downloads/%name-%version.tar.gz
%else
#VCS: https://github.com/01org/dleyna-core.git
Source: %name-%version.tar
%endif

BuildRequires: libgio-devel libgupnp-devel

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
%autoreconf
%configure  --disable-static
%make_build

%install
%makeinstall_std

%files -n lib%name
%_libdir/lib%_name-core-%api_ver.so.*
%doc AUTHORS ChangeLog README

%files -n lib%name-devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-core-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc


%changelog
* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

