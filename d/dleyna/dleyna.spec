%define _libexecdir %_prefix/libexec

%define _name dLeyna
%define api_ver 1.0
%define rdn_name com.intel.dleyna

%def_enable man
%def_disable docs

Name: dleyna
Version: 0.8.3
Release: alt1

Summary: Services and D-Bus APIs for UPnP access
Group: System/Servers
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/World/dLeyna

Vcs: https://gitlab.gnome.org/World/dLeyna.git
Source: https://gitlab.gnome.org/World/dLeyna/-/archive/v%version/%_name-v%version.tar.bz2

%define gupnp_api_ver 1.6

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gssdp-%gupnp_api_ver)
BuildRequires: pkgconfig(gupnp-%gupnp_api_ver)
BuildRequires: pkgconfig(gupnp-av-1.0)
BuildRequires: pkgconfig(gupnp-dlna-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libxml-2.0)
%{?_enable_man:BuildRequires: /usr/bin/rst2man}

%description
dLeyna is a set of services and D-Bus APIs that aim to simplify access to UPnP
and DLNA media devices in a network.

%package -n lib%name-core
Summary: dLeyna Core Library
Group: System/Libraries

%description -n lib%name-core
dleyna-core is a library of utility functions that are used by the higher
level dLeyna libraries that communicate with DLNA devices, e.g.,
dleyna-server. In brief, it provides APIs for logging, error, settings
and task management and an IPC abstraction API.

%package connector-dbus
Summary: D-Bus connector for dLeyna services
Group: System/Servers
Requires: lib%name-core = %EVR

%description connector-dbus
D-Bus connector for dLeyna services.

%package renderer
Summary: Service for interacting with Digital Media Renderers
Group: System/Servers
Requires: lib%name-core = %EVR

%description renderer
This package contains shared dleyna-renderer library and D-Bus service to
discover and manipulate DLNA Digital Media Renderers.

%package server
Summary: Service for interacting with Digital Media Servers
Group: System/Servers
Requires: lib%name-core = %EVR

%description server
This package contains shared dleyna-server library and D-Bus service to
discover and manipulate DLNA Digital Media Servers.

%package devel
Summary: Development files for the dLeyna components
Group: Development/C
Requires: lib%name-core = %EVR
Requires: %name-renderer = %EVR
Requires: %name-server = %EVR

%description devel
dLeyna is a set of services and D-Bus APIs that aim to simplify access to UPnP
and DLNA media devices in a network. This package contains files used for
development with dLeyna.

%prep
%setup -n %_name-v%version

%build
%meson \
    %{?_disable_docs:-Ddocs=false}
%nil
%meson_build

%install
%meson_install

%files -n lib%name-core
%dir %_libdir/%name
%_libdir/lib%name-core-%api_ver.so.*
%doc AUTHORS ChangeLog.core NEWS README.md

%files connector-dbus
%dir %_libdir/%name-%api_ver
%dir %_libdir/%name-%api_ver/connectors
%_libdir/%name-%api_ver/connectors/lib%name-connector-dbus.so
%doc ChangeLog.connector-dbus

%files renderer
%config(noreplace) %_sysconfdir/%name-renderer-service.conf
%_libexecdir/%name-renderer-service
%_libdir/%name/lib%name-renderer-%api_ver.so.*
%_datadir/dbus-1/services/%rdn_name-renderer.service
%{?_enable_man:%_man1dir/%name-renderer-service.1*
%_man5dir/%name-renderer-service.conf.5*}
%doc ChangeLog.renderer

%files server
%config(noreplace) %_sysconfdir/%name-server-service.conf
%_libexecdir/%name-server-service
%dir %_libdir/%name-server
%_libdir/%name-server/lib%name-server-%api_ver.so.*
%_datadir/dbus-1/services/%rdn_name-server.service
%{?_enable_man:%_man1dir/%name-server-service.1*
%_man5dir/%name-server-service.conf.5*}
%doc ChangeLog.server

%files devel
%_includedir/%name-%api_ver/
%_libdir/lib%name-core-%api_ver.so
%_pkgconfigdir/%name-core-%api_ver.pc
# renderer devel
%_libdir/%name/lib%name-renderer-%api_ver.so
%_pkgconfigdir/%name-renderer-service-%api_ver.pc
# server devel
%_libdir/%name-server/lib%name-server-%api_ver.so
%_pkgconfigdir/%name-server-service-%api_ver.pc

%exclude %python3_sitelibdir_noarch

%changelog
* Mon Oct 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- first build for Sisyphus



