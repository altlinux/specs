# TODO:
# * python3
# * extract python2 binding as subpackage

%set_verify_elf_method rpath=relaxed

%define origname dee

Name: lib%origname
Version: 1.2.7
Release: alt1

Summary: Library for creating Model-View-Controller programs across DBus
Group: System/Libraries
License: LGPLv3
URL: https://launchpad.net/dee

Source0: %origname-%version.tar.gz

Patch0: dee-1.2.7-alt-build.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: rpm-build-gir glib2-devel libgio-devel gtk-doc vala-tools
BuildRequires: gobject-introspection-devel libicu-devel

# CheckRequires
BuildRequires: dbus dbus-test-runner

%description
Libdee is a library that uses DBus to provide objects allowing you to create
Model-View-Controller type programs across DBus. It also consists of utility
objects which extend DBus allowing for peer-to-peer discoverability of known
objects without needing a central registrar.

%package devel
Summary: Development files for dee
Group: Development/C

Requires: %name = %version-%release

%description devel
This package contains the development files for the dee library.

%package -n dee-tools
Summary: Library for creating Model-View-Controller programs across DBus - Tools
Group: Development/Tools

Requires: %name = %version-%release

%description -n dee-tools
This package contains some tools from the dee library.

%package docs
Summary: Documentation for dee
Group: Documentation
BuildArch: noarch

%description docs
This package contains the documentation for the dee library.

%package vala
Summary: Vala language bindings for the dee library
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description vala
This package provides Vala language bindings for the dee library.

%package gir
Summary: GObject introspection data for the dee library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the dee library.

%package gir-devel
Summary: GObject introspection devel data for the dee library.
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the dee library.

%prep
%setup -q -n %origname-%version
%patch0 -p1

%build
%autoreconf
%configure \
  --disable-static \
  --enable-gtk-doc
%make_build V=1

%check
make check || exit 1

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS
%_libdir/libdee-1.0.so.*
%{python_sitelibdir}/gi/overrides/Dee.py*
#{python3_sitearch}/gi/overrides/Dee.py*
#{python3_sitearch}/gi/overrides/__pycache__/Dee.cpython-*.py*

%files devel
%dir %_includedir/dee-1.0/
%_includedir/dee-1.0/*.h
%_libdir/libdee-1.0.so
%_pkgconfigdir/dee-1.0.pc
%_pkgconfigdir/dee-icu-1.0.pc

%files -n dee-tools
%_bindir/dee-tool

%files docs
%_datadir/gtk-doc/html/dee-1.0

%files vala
%_datadir/vala/vapi/dee-1.0.deps
%_datadir/vala/vapi/dee-1.0.vapi

%files gir
%_typelibdir/Dee-1.0.typelib

%files gir-devel
%_girdir/Dee-1.0.gir

%changelog
* Sat Nov 23 2013 Igor Zubkov <icesik@altlinux.org> 1.2.7-alt1
- 1.2.7

* Mon Sep 23 2013 Igor Zubkov <icesik@altlinux.org> 1.0.14-alt2
- Relax rpath check

* Mon Sep 16 2013 Igor Zubkov <icesik@altlinux.org> 1.0.14-alt1
- build for Sisyphus

