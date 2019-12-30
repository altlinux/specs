%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name dleyna
%define api_ver 1.0
%define gupnp_api_ver 1.2

Name: %_name-renderer
Version: 0.6.0
Release: alt3

Summary: Service for interacting with Digital Media Renderers
Group: System/Servers
License: LGPL-2.1
Url: https://01.org/%_name/

%if_disabled snapshot
Source: https://01.org/%_name/sites/default/files/downloads/%name-%version.tar.gz
%else
#VCS: https://github.com/01org/dleyna-renderer.git
Source: %name-%version.tar
%endif
# https://github.com/intel/dleyna-renderer/pull/167
Patch: %name-0.6.0-up-gupnp-1.2.patch

BuildRequires: libgio-devel libgssdp%gupnp_api_ver-devel libgupnp%gupnp_api_ver-devel
BuildRequires: libgupnp-av-devel libgupnp-dlna-devel libsoup-devel
BuildRequires: libdleyna-core-devel

%description
This package contains shared %name libraries and D-Bus service to
discover and manipulate DLNA Digital Media Renderers.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name-service.

%prep
%setup
%patch -p1 -b .gupnp-1.2

%build
%autoreconf
%configure  --disable-static
%make_build

%install
%makeinstall_std

%files
%_libexecdir/%name-service
%dir %_libdir/%name/
%_libdir/%name/lib%name-%api_ver.so.*
%_datadir/dbus-1/services/com.intel.%name.service
%_sysconfdir/%name-service.conf
%doc AUTHORS ChangeLog README

%files devel
%_includedir/%_name-%api_ver/lib%_name/renderer
%_libdir/%name/lib%name-%api_ver.so
%_pkgconfigdir/%name-service-%api_ver.pc

%exclude %_libdir/%name/*.la


%changelog
* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt3
- ported to gupnp-1.2 (
  see https://github.com/intel/dleyna-renderer/pull/167)

* Mon Dec 30 2019 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt2
- updated BR

* Wed Oct 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

