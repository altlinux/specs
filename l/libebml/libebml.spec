Name: libebml
Version: 1.3.5
Release: alt1

Summary: Extensible Binary Meta Language access library
License: GPL/QPL
Group: System/Libraries
Url: http://www.matroska.org

Source: %name-%version-%release.tar

BuildRequires: gcc-c++

%description
A library for reading and writing files with the Extensible Binary
Meta Language, a binary pendant to XML.

%package devel
Summary: Development files for libebml
Group: Development/C++
Requires: %name = %version-%release

%description devel
Files needed to build programs using libebml

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
%_includedir/ebml
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Sun Apr 01 2018 Anton Farygin <rider@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Fri Sep 02 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.4-alt1
- 1.3.4 released

* Wed Jul 15 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt2
- rebuilt with gcc5

* Fri Jan 16 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Sun Sep 14 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Mon Dec 10 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt0.1
- 1.3.0 prerelease

* Thu Oct 13 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt1
- 1.2.2 released

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.1
- Rebuilt for soname set-versions

* Wed Aug 18 2010 Afanasov Dmitry <ender@altlinux.org> 1.0.0-alt1
- 1.0.0 release.

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libebml
  * postun_ldconfig for libebml

* Sun Apr 06 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.7.8-alt1
- 0.7.8 release.

* Sun May 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.7.7-alt1
- 0.7.7 release.

* Wed Nov 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.7.6-alt1
- 0.7.6 release.
- Fixed some errors in specfile.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.0-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Apr 27 2004 Alexey Morozov <morozov@altlinux.org> 0.7.0-alt1
- Initial build.
- Package autotoolized
