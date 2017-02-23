%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name dleyna
%define api_ver 1.0

Name: %_name-renderer
Version: 0.5.0
Release: alt1

Summary: Service for interacting with Digital Media Renderers
Group: System/Servers
License: LGPLv2.1
Url: https://01.org/%_name/

%if_disabled snapshot
Source: https://01.org/%_name/sites/default/files/downloads/%name-%version.tar.gz
%else
#VCS: https://github.com/01org/dleyna-renderer.git
Source: %name-%version.tar
%endif

BuildRequires: libgio-devel libgssdp-devel libgupnp-devel
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
* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

