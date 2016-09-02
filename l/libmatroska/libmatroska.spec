Name: libmatroska
Version: 1.4.5
Release: alt1

Summary: an extensible open standard Audio/Video container format
License: LGPL
Group: System/Libraries
Url: http://www.matroska.org

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libebml-devel >= 1.3.4

%description
Matroska is aiming to become the standard of Multimedia Container
Formats one day. It is based on EBML (Extensible Binary Meta
Language), a kind of binary version of XML. This way the significant
advantages in terms of future format extensability are gained without
breaking file support in old parsers.

%package devel
Summary: Development files for libmatroska
Group: Development/C++
Requires: libmatroska = %version

%package doc
Summary: Matroska Project Documentation (doxygenized HTML)
Group: Development/C++
Requires: libmatroska-devel = %version

%description devel
Matroska is aiming to become the standard of Multimedia Container
Formats one day. It is based on EBML (Extensible Binary Meta
Language), a kind of binary version of XML. This way the significant
advantages in terms of future format extensability are gained without
breaking file support in old parsers.

This package contains files needed to build programs using libebml

%description doc
Matroska is aiming to become the standard of Multimedia Container
Formats one day. It is based on EBML (Extensible Binary Meta
Language), a kind of binary version of XML. This way the significant
advantages in terms of future format extensability are gained without
breaking file support in old parsers.

This package contains Matroska Development Documenation (doxygenized
HTML)

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/matroska
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Fri Sep 02 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.5-alt1
- 1.4.5 released

* Wed Jul 15 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt2
- rebuilt with gcc5

* Fri Jan 16 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- 1.4.2 released

* Sun Sep 14 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1 released

* Mon Dec 10 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt0.1
- 1.4.0 prereleased

* Thu Oct 13 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.2
- Rebuilt for debuginfo

* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.1
- Rebuilt for soname set-versions

* Wed Aug 18 2010 Afanasov Dmitry <ender@altlinux.org> 1.0.0-alt1
- 1.0.0 release.

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmatroska
  * postun_ldconfig for libmatroska

* Wed Feb 28 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1-alt1
- 0.8.1 release.
- Some spec cleanup.

* Wed Nov 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.0-alt1
- 0.8.0 release.
- Fixed some errors in spec.

* Wed Jan 19 2005 Anton Farygin <rider@altlinux.ru> 0.7.4-alt1
- NMU: new version
- NMU: make check disabled (gcc 3.4 build fix)

* Tue Apr 30 2004 Alexey Morozov <morozov@altlinux.org> 0.7.0-alt1
- Initial build.
- Package autotoolized
- Enabled usage of Matroska future API (needed for MPlayer)
