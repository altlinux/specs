%def_enable snapshot
%define _name cloudproviders
%define ver_major 0.2

%def_enable gtk_doc

Name: lib%_name
Version: %ver_major.5
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

BuildRequires: meson libgio-devel >= %glib_ver
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

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%name is a library for desktop integration of cloud storage providers.

This package contains development documentation for %name.


%prep
%setup

%build
%meson %{?_enable_gtk_doc:-Denable-gtk-doc=true}
%meson_build

%install
%meson_install

%files
%_libdir/%name.so.*
%doc CHANGELOG README.md

%files devel
%_includedir/%_name/
%_pkgconfigdir/%_name.pc
%_libdir/%name.so

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%changelog
* Wed Dec 27 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.5-alt1
- first build for Sisyphus


