%def_disable static

Name: libflowcanvas
Version: 0.5.1
Release: alt2

Summary: A canvas widget for graph-like interfaces
License: %gpl2plus
Group: System/Libraries
Url: http://drobilla.net/software/flowcanvas/
Packager: Timur Batyrshin <erthad@altlinux.org>

Source0: %name-%version.tar.bz2
Patch0: changeset_r2170.diff

BuildPreReq: rpm-build-licenses
# Automatically added by buildreq on Mon Aug 03 2009
BuildRequires: boost-devel doxygen gcc-c++ libgnomecanvasmm-devel libgraphviz-devel

%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes and lines"
environments (ie modular synths or interactive finite state automata diagrams).

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%package doc
Summary: Documentation for %name
Group: Development/Documentation

%description doc
Documentation for %name

%prep
%setup
%patch0 -p3

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall

%files
%_libdir/*.so.*
%doc AUTHORS README 

%files devel
%_libdir/*.so
%_includedir/flowcanvas
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%files doc
%doc doc/html/*

%changelog
* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.5.1-alt2
- NMU: rebuilt with current graphviz

* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.5.1-alt1
- Initial build for sisyphus

