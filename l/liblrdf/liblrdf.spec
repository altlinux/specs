%def_disable static

Name: liblrdf
Version: 0.4.0
Release: alt3.1

Summary: Library for handling RDF descriptions of audio plugins
License: GPLv2+
Group: System/Libraries
Url: http://lrdf.sourceforge.net
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Source: http://prdownloads.sf.net/lrdf/%name-%version.tar.gz

%define raptor_ver 1.2.0

BuildPreReq: ladspa_sdk >= 1.12-alt2
BuildPreReq: libraptor-devel >= %raptor_ver

# Automatically added by buildreq on Sun Apr 04 2004
BuildRequires: gcc-c++ glib2-devel ladspa_sdk libcurl-devel libraptor-devel libssl-devel libstdc++-devel libxml2-devel pkgconfig zlib-devel

%description
liblrdf is a library for handling RDF (http://www.w3.org/RDF/)
descriptions of LADSPA (and potentially other format) plugins.

It allows grouping of plugins into trees for user slection and finer
description of plugins and ports than the .so format allows (for example
to indicatate textual equivalents of integer port values). It also
provides named and described defaults and presets, metadata and general
semnatic goodness.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libraptor-devel >= %raptor_ver

%description devel
This package contains the headers that programmers will need to develop
applications which will use libraries from %name.

%prep
%setup -q

%build
%autoreconf
%configure \
    %{subst_enable static}

%make_build

%install
%makeinstall

%files
%_libdir/*.so.*
%_ladspa_datadir/rdf/ladspa.rdfs

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3.1
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3
- Rebuilt for soname set-versions

* Sun Dec 14 2008 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt2
- fixed Url and license tags
- removed obsolete %%post{,un}_ldconfig

* Mon Dec 04 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version

* Thu Oct 21 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.7-alt1.1.1
- Rebuilt with libcurl.so.3.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.7-alt1.1
- Rebuilt with openssl-0.9.7d.

* Sun Apr 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.7-alt1
- 0.3.7

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.5-alt1
- new version.

* Tue Jan 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.4-alt1
- new version.

* Sat Nov 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.2-alt1
- new version.
- do not package .la files.

* Wed Apr 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Thu Mar 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Tue Feb 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt1
- Adopted for Sisyphus.

* Tue Feb 18 2003 Austin Acton <aacton@yorku.ca> 0.2.3-1mdk
- initial package
