%def_enable snapshot
%define _name cloudproviders
%define ver_major 0.3

%def_enable gtk_doc
%def_enable check
%def_enable installed_tests

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: Library for integration of cloud storage providers
Group: System/Libraries
License: LGPLv3+
Url: https://gitlab.gnome.org/External/%name

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.52

BuildRequires(pre): meson
BuildRequires: libgio-devel >= %glib_ver gobject-introspection-devel vala-tools
%{?_enable_gtk_doc:BuildRequires: gtk-doc}

%description
%name is a DBus API that allows cloud storage sync clients to
expose their services. Clients such as file managers and desktop
environments can then provide integrated access to the cloud providers
services.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
%name is a library for desktop integration of cloud storage providers.

This package provides libraries and header files for developing
applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for %_name library

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %_name library

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%name is a library for desktop integration of cloud storage providers.

This package contains development documentation for %name.

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %_name library.


%prep
%setup

%build
%meson %{?_enable_gtk_doc:-Denable-gtk-doc=true} \
	%{?_enable_installed_tests:-Dinstalled-tests=true}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/%name.so.*
%doc CHANGELOG README.md

%files devel
%_includedir/%_name/
%_pkgconfigdir/%_name.pc
%_libdir/%name.so
%_vapidir/%_name.*

%files gir
%_typelibdir/CloudProviders-%version.typelib

%files gir-devel
%_girdir/CloudProviders-%version.gir

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%if_enabled installed_tests
%files tests
%_bindir/testcloudprovidersclient
%_bindir/testcloudprovidersserver
%dir %_datadir/cloud-providers
%_datadir/cloud-providers/org.freedesktop.CloudProviders.ServerExample.ini
%_datadir/dbus-1/services/org.freedesktop.CloudProviders.ServerExample.service
%endif

%changelog
* Sat Jan 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0
- new -gir, -gir-devel, -tests subpackages

* Tue Jun 26 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt2
- updated to 0.2.5-13-gd188a03

* Wed Dec 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- first build for Sisyphus


