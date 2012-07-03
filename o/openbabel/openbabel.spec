Name: openbabel
Version: 2.3.1
Release: alt1.1.1

Summary: Chemistry software file format converter
License: GPL
Group: Sciences/Chemistry

Url: http://openbabel.sourceforge.net
Source: http://dl.sf.net/%name/%name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu Dec 15 2011
# optimized out: cmake-modules libstdc++-devel pkg-config python-base
BuildRequires: cmake gcc-c++ libxml2-devel zlib-devel
BuildPreReq: python-devel eigen2

Summary(ru_RU.UTF-8): Конвертор биохимических форматов данных
Summary(uk_UA.UTF-8): Конвертор біохімічних форматів даних

%description
Open Babel is a project designed to pick up where Babel left off,
as a cross-platform program and library designed to interconvert
between many file formats used in molecular modeling and computational
chemistry.

%description -l ru_RU.UTF-8
Open Babel - продолжение проекта Babel как кросплатформенного
инструмента для конвертирования многочисленных форматов данных,
используемых в молекулярном моделировании и вычислительной химии.

%description -l uk_UA.UTF-8
Open Babel - продовження проекту Babel як кросплатформенного
інструменту для конвертування численних форматів даних, що
використовуються у молекулярному моделюванні та обчислювальній хімії.

%package -n lib%name
Summary: Shared libraries for programs which will use Open Babel
Group: System/Libraries

%package -n lib%name-devel
Summary: Development tools for programs which will use the lib%name library
Group: Development/C++
Requires: lib%name = %version-%release

%package -n python-module-%name
Summary: Python bindings for Open Babel
Group: Development/Python
Requires: lib%name = %version-%release

%if_enabled static
%package -n lib%name-devel-static
Summary: Static development files for lib%name
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static development files for lib%name
%endif

%description -n lib%name
Shared libraries for programs which will use Open Babel

%description -n lib%name-devel
The lib%name-devel package includes the header files and static libraries
necessary for developing programs using the lib%name library.

If you are going to develop programs which will use this library
you should install lib%name-devel.  You'll also need to have the
lib%name package installed.

%description -n python-module-%name
Python bindings for Open Babel.

%prep
%setup

echo PYTHON_BINDINGS:BOOL=ON >CMakeCache.txt

%build
%add_optflags -I%_includedir/eigen2
%cmake_insource
%make_build VERBOSE=1
gzip -9nf ChangeLog

%install
%makeinstall_std

%if_enabled static
%else
rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_libdir/%name/{%version/,}*.{a,la}
%endif

%files
%doc AUTHORS ChangeLog* README THANKS 
%doc doc/FAQ* doc/README* doc/dioxin.*
%_bindir/*
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/%name/
%dir %_libdir/%name/%version/
%_libdir/%name/%version/*.so

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/openbabel2

%files -n python-module-%name
%python_sitelibdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

# TODO:
# - build GUI (wxWidgets)

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1.1
- Added python interface

* Thu Dec 15 2011 Michael Shigorin <mike@altlinux.org> 2.3.1-alt1
- 2.3.1

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Mar 20 2011 Michael Shigorin <mike@altlinux.org> 2.2.3-alt3
- re-added lost BR, thx at@

* Sat Dec 04 2010 Michael Shigorin <mike@altlinux.org> 2.2.3-alt2
- rebuilt for set versions

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 2.2.3-alt1
- 2.2.3
- gzip ChangeLog (repocop)

* Fri Jul 10 2009 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1
- 2.2.2

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 2.2.1-alt1
- 2.2.1
  + fiddled a bit to build
- buildreq
- minor spec cleanup

* Wed Oct 15 2008 Sergey V Turchin <zerg at altlinux dot org> 2.2.0-alt1
- new version

* Thu Nov 09 2006 Michael Shigorin <mike@altlinux.org> 2.0.2-alt1
- 2.0.2
- patches removed (applied upstream)

* Sun Mar 26 2006 Michael Shigorin <mike@altlinux.org> 2.0.0-alt2
- fixed build with --as-needed
- added gcc41 patch by vlaaad/users.sf.net (from SF tracker)
- don't remove *.a when static library build is requested

* Tue Dec 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- add Packager tag
- add /usr/lib/openbabel to pack
- cleanup spec, repack source to tar.bz2

* Thu Dec 15 2005 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt0.1
- NMU: new version
- add URL to Source, update Buildrequires

* Sun Nov 27 2005 Michael Shigorin <mike@altlinux.org> 2.0.0-alt0
- 2.0.0 (initial build)
- warning, API's incompatible -- see the site or migration docs

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.100.2-alt1.1
- Rebuilt with libstdc++.so.6.

* Wed Mar 03 2004 Michael Shigorin <mike@altlinux.ru> 1.100.2-alt1
- 1.100.2

* Wed Dec 17 2003 Michael Shigorin <mike@altlinux.ru> 1.100.1-alt2
- removed *.la
- don't package static library by default

* Mon Sep 22 2003 Michael Shigorin <mike@altlinux.ru> 1.100.1-alt1
- 1.100.1
- #2994 fixed; thanks to Alex Ott (ott@) for a pointer
- spec cleanup (underlibification fixup)

* Mon Jun 30 2003 Michael Shigorin <mike@altlinux.ru> 1.100.0-alt1
- built for ALT Linux
- based on Mandrake Cooker spec by:
  * Lenny Cartier <lenny@mandrakesoft.com>
  * Austin Acton <aacton@yorku.ca>
- spec cleanup
