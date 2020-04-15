Name: libflowcanvas
Version: 0.7.1
Release: alt3

Summary: A canvas widget for graph-like interfaces
License: %gpl2plus
Group: System/Libraries

Url: http://drobilla.net/software/flowcanvas/
Source: %name-%version.tar.bz2
Source1: waflib-1.6.2.tar
Source2: waf
Patch: graphviz23.patch
Packager: Timur Batyrshin <erthad@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: libgnomecanvasmm-devel
BuildRequires: libgraphviz-devel
BuildRequires: python-modules
BuildRequires: python-modules-logging

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
tar xf %SOURCE1
rm -f waf
cp %SOURCE2 waf
%patch -p1

%build
export CXXFLAGS=-std=gnu++11
%__python waf configure --prefix %_prefix --libdir %_libdir
%__python waf build

%install
%__python waf install --destdir %buildroot

%files
%_libdir/*.so.*
%doc AUTHORS README 

%files devel
%_libdir/*.so
%_includedir/flowcanvas
%_pkgconfigdir/*.pc

%changelog
* Wed Apr 15 2020 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt3
- Fix build by extract waflib and use custom waf for build.

* Wed Oct 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt2
- Fix build with gcc5

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.1-alt1.1
- Rebuilt for gcc5 C++11 ABI.

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

