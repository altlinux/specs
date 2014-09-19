Name: ganv
Version: 1.4.2
Release: alt1
Summary: Interactive Gtk widget for interactive "boxes and lines" or graph-like environments
License: GPLv3
Group: Graphics
Url: http://drobilla.net/software/ganv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-c++ libgtk+2-devel doxygen graphviz libgtkmm2-devel
BuildPreReq: libgraphviz-devel gtk-doc

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

%build
./waf configure \
	--debug \
	--docs \
	--lv2-user \
	--lv2-system \
	--test \
	--prefix=%prefix \
	--configdir=%_sysconfdir \
	--libdir=%_libdir
./waf build -j %__nprocs

./gtkdoc.sh

%install
./waf install \
	--destdir=%buildroot

%files -n lib%name
%doc AUTHORS NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files tests
%_bindir/*

%files -n lib%name-devel-docs
%doc docs/*

%changelog
* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Initial build for Sisyphus

