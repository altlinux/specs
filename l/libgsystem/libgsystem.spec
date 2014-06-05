%define ver_major 2014
%define api_ver 1.0
%def_enable introspection
%def_disable gtk_doc

Name: libgsystem
Version: %ver_major.2
Release: alt1

Summary: GIO-based library with Unix/Linux specific API
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/Projects/LibGSystem

Source: ftp://ftp.gnome.org/%name/%ver_major/%name-%version.tar

BuildRequires: libgio-devel >= 2.34 libattr-devel
BuildRequires: libsystemd-journal-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
BuildRequires: intltool xsltproc gtk-doc

%description
LibGSystem is a GIO-based library targeted primarily for use by
operating system components. It has a few goals:

Provide macros for the GCC attribute(cleanup) that work with GLib data
types. Using these can dramatically simplify local memory management
inside functions.

Prototype and test APIs that will eventually be in GLib. Currently these
include "GSSubprocess" for launching child processes, and some GFile
helpers.

Provide Linux-specific APIs in a nicer GLib fashion, such as O_NOATIME.

%package devel
Summary: Development files for LibGSystem
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using LibGSystem.

%package gir
Summary: GObject introspection data for the LibGSystem library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the LibGSystem library

%package gir-devel
Summary: GObject introspection devel data for the LibGSystem library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the LibGSystem library

%package devel-doc
Summary: Development documentation for LibGSystem
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for LibGSystem library.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc README

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%if_enabled introspection
%files gir
%_typelibdir/GSystem-%api_ver.typelib

%files gir-devel
%_girdir/GSystem-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Thu Jun 05 2014 Yuri N. Sedunov <aris@altlinux.org> 2014.2-alt1
- 2014.2

* Thu Feb 06 2014 Yuri N. Sedunov <aris@altlinux.org> 2014.1-alt0.1
- first build for Sisyphus

