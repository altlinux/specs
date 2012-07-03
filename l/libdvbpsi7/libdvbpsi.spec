Name: libdvbpsi7
Version: 0.2.2
Release: alt1

Summary: A library for decoding and generating MPEG 2 and DVB PSI sections
License: LGPL
Group: System/Libraries
Url: http://www.videolan.org/

Source: %name-%version.tar

BuildRequires: doxygen graphviz fonts-type1-urw

%description
%name is a simple library designed for MPEG 2 TS and DVB PSI tables
decoding and generating. The important features are:
 * PAT decoder and genarator.
 * PMT decoder and generator.

%package -n libdvbpsi-devel
Summary: Development files for libdvbpsi
Group: Development/C
Requires: %name = %version-%release

%description -n libdvbpsi-devel
The libdvbpsi-devel package includes the header files and libraries
necessary for developing programs which will manipulate MPEG 2 and DVB PSI
information using the libdvbpsi

%prep
%setup

%build
%autoreconf
%configure --disable-static --enable-release
%make_build all doc

%install
%makeinstall

%files
%doc AUTHORS NEWS README
%_libdir/*.so.*

%files -n libdvbpsi-devel
%doc ChangeLog doc/doxygen/html
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Nov 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.2-alt1
- 0.2.2 released

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt2
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.6-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdvbpsi5
  * postun_ldconfig for libdvbpsi5
  * postclean-05-filetriggers for spec file

* Mon Oct 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.1.6-alt1
- 0.1.6 release.
- Package renamed to libdvbpsi5 due to soname change.

* Fri Jun 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1.5-alt1
- 0.1.5 release.

* Thu Nov 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.3-alt1
- new version.
- don't package .la files.

* Tue Mar 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt1
- Adopted for Sisyphus.

* Fri Oct 11 2002 Samuel Hocevar <sam@zoy.org>
- 0.1.2 release.

* Sat May 18 2002 Arnaud de Bossoreille de Ribou <bozo@via.ecp.fr>
- 0.1.1 release.

* Mon Apr 8 2002 Arnaud de Bossoreille de Ribou <bozo@via.ecp.fr>
- split into two separate packages.

* Thu Apr 4 2002 Jean-Paul Saman <saman@natlab.research.philips.com>
- first version of package for redhat systems.
