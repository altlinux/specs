Name: libflowcanvas
Version: 0.7.1
Release: alt1

Summary: A canvas widget for graph-like interfaces
License: %gpl2plus
Group: System/Libraries

Url: http://drobilla.net/software/flowcanvas/
Source: %name-%version.tar.bz2
Patch: graphviz23.patch
Packager: Timur Batyrshin <erthad@altlinux.org>

BuildPreReq: rpm-build-licenses
# Automatically added by buildreq on Thu Aug 07 2014
# optimized out: fontconfig fontconfig-devel glib2-devel libart_lgpl-devel libatk-devel libatkmm-devel libcairo-devel libcairomm-devel libcloog-isl4 libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgnomecanvas-devel libgtk+2-devel libgtkmm2-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel pkg-config python-base python-modules python-modules-compiler python-modules-ctypes python-modules-encodings python-modules-logging
BuildRequires: boost-devel-headers gcc-c++ libgnomecanvasmm-devel libgraphviz-devel

%description
FlowCanvas is an interactive Gtkmm/Gnomecanvasmm widget for "boxes and lines"
environments (ie modular synths or interactive finite state automata diagrams).

    Note: FlowCanvas is dead, long live Ganv!

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%prep
%setup
%patch -p1

%build
./waf configure --prefix %_prefix --libdir %_libdir
./waf build

%install
./waf install --destdir %buildroot

%files
%_libdir/*.so.*
%doc AUTHORS README 

%files devel
%_libdir/*.so
%_includedir/flowcanvas
%_pkgconfigdir/*.pc

%changelog
* Thu Aug 07 2014 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- NMU: 0.7.1 (NB: deprecated upstream)
- re-enabled graphviz-2.30+ support (thanks debian for libcgraph patch)
- dropped doc subpackage (argh, that waf is yet another NIH crap)
- dropped static subpackage (waf crap again, and was disabled anyways)
- buildreq

* Thu Apr 24 2014 Michael Shigorin <mike@altlinux.org> 0.5.1-alt3
- NMU: rebuilt without graphviz support (cgraph migration in 2.30)

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 0.5.1-alt2
- NMU: rebuilt with current graphviz

* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.5.1-alt1
- Initial build for sisyphus

