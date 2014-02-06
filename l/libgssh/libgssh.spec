%define ver_major 2014
%define api_ver 1
%def_disable introspection
%def_disable gtk_doc

Name: libgssh
Version: %ver_major.1
Release: alt0.1

Summary: GIO wrapper library for libssh
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/LibGSystem

Source: ftp://ftp.gnome.org/%name/%ver_major/%name-%version.tar

BuildRequires: libgio-devel >= 2.34 libgsystem-devel libssh-devel >= 0.6
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgsystem-gir-devel}
BuildRequires: intltool xsltproc gtk-doc

%description
LibGSsh wraps and extends libssh, providing an asynchronous
GIO-like API.

%package devel
Summary: Development files for LibGSsh
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using LibGSsh.

%package gir
Summary: GObject introspection data for the LibGSsh library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the LibGSsh library

%package gir-devel
Summary: GObject introspection devel data for the LibGSsh library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the LibGSsh library

%package devel-doc
Summary: Development documentation for LibGSsh
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for LibGSsh library.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/%name-%api_ver.so.*
#%doc README

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/GSsh-%api_ver.typelib

%files gir-devel
%_girdir/GSsh-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 2014.1-alt0.1
- first build for Sisyphus

