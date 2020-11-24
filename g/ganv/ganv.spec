%def_without gir

Name: ganv
Version: 1.6.0
Release: alt3
Summary: Interactive Gtk widget for interactive "boxes and lines" or graph-like environments
License: GPL-3.0
Group: Graphics
Url: http://drobilla.net/software/ganv/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-gir
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libgtk+2-devel doxygen graphviz libgtkmm2-devel
BuildRequires: libgraphviz-devel gtk-doc
%if_with gir
BuildRequires: gobject-introspection-devel libgtk+2-gir-devel
%endif

%description
Ganv is an interactive Gtk widget for interactive "boxes and lines" or
graph-like environments (e.g. modular synths or finite state machine
diagrams).

%package -n lib%name
Summary: Interactive Gtk widget for interactive "boxes and lines" or graph-like environments
Group: System/Libraries

%description -n lib%name
Ganv is an interactive Gtk widget for interactive "boxes and lines" or
graph-like environments (e.g. modular synths or finite state machine
diagrams).

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Ganv is an interactive Gtk widget for interactive "boxes and lines" or
graph-like environments (e.g. modular synths or finite state machine
diagrams).

This package contains development files of lib%name.

%package -n lib%name-devel-docs
Summary: Documentation for lib%name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
Ganv is an interactive Gtk widget for interactive "boxes and lines" or
graph-like environments (e.g. modular synths or finite state machine
diagrams).

This package contains development documentation for lib%name.

%package -n lib%name-gir
Summary: GObject introspection data for the lib%name
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
Ganv is an interactive Gtk widget for interactive "boxes and lines" or
graph-like environments (e.g. modular synths or finite state machine
diagrams).

This package contains GObject introspection data for lib%name.

%package -n lib%name-gir-devel
Summary: GObject introspection data for the lib%name
Group: System/Libraries
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
Ganv is an interactive Gtk widget for interactive "boxes and lines" or
graph-like environments (e.g. modular synths or finite state machine
diagrams).

This package contains GObject introspection devel data for lib%name.

%package tests
Summary: Tests for lib%name
Group: Graphics
Requires: lib%name = %EVR

%description tests
Ganv is an interactive Gtk widget for interactive "boxes and lines" or
graph-like environments (e.g. modular synths or finite state machine
diagrams).

This package contains tests for lib%name.

%prep
%setup
# Set correct python2 executable in shebang
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)

%build
./waf configure \
	--debug \
	--docs \
	--light-theme \
	--no-nls \
	--gir \
	--prefix=%prefix \
	--configdir=%_sysconfdir \
	--libdir=%_libdir
./waf build -j %__nprocs
./gtkdoc.sh

%install
./waf install \
	--destdir=%buildroot

%files -n lib%name
%doc AUTHORS NEWS README.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_with gir
%files -n lib%name-gir
%_typelibdir/Ganv-1.0.typelib

%files -n lib%name-gir-devel
%_typelibdir/Ganv-1.0.gir
%endif

%files tests
%_bindir/*

%files -n lib%name-devel-docs
%doc docs/*

%changelog
* Tue Nov 24 2020 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt3
- Completely remove introspection build.

* Mon Nov 23 2020 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt2
- Build without introspection.

* Sun May 31 2020 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- New version.
- Use python3 in waf build scripts.
- Build with GObject introspection support.

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus

