Name: libpantheon
Version: 0.2
Release: alt1.r23

Summary: Library for the Pantheon Desktop Environment
Group: System/Libraries
License: GPLv3+
Url: http://launchpad.net/libpantheon

Source0: %name.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake rpm-build-gir gobject-introspection-devel
BuildRequires: libgtk+3-devel libgio-devel gcc-c++ libpixman-devel
BuildRequires: vala libexpat-devel libXdmcp-devel libgtk+3-gir-devel
BuildRequires: libXdamage-devel

%description
Library for the Pantheon Desktop Environment.

%package devel
Summary: Headers for Pantheon library
Group: Development/GNOME and GTK+

Requires: %name = %version-%release

%description devel
Development headers for the Pantheon Desktop Environment library.

%package vala
Summary: Vala language bindings for pantheon library
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for pantheon library.

%package gir
Summary: GObject introspection data for pantheon library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for pantheon library.

%package gir-devel
Summary: GObject introspection devel data for pantheon library.
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for pantheon library.

%prep
%setup -q -n %name

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%ifarch x86_64
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif

%files
%_libdir/libpantheon.so.*

%files devel
%_libdir/libpantheon.so
%_includedir/pantheon/pantheon.h
%_pkgconfigdir/pantheon.pc

%files gir
%_typelibdir/Pantheon-0.1.typelib

%files gir-devel
%_girdir/Pantheon-0.1.gir

%files vala
%_datadir/vala/vapi/pantheon.deps
%_datadir/vala/vapi/pantheon.vapi

%changelog
* Thu Nov 14 2013 Igor Zubkov <icesik@altlinux.org> 0.2-alt1.r23
- r23

