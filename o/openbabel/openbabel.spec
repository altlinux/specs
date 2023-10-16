%define ver_major 3.1
%define ver_base %ver_major.0

Name: openbabel
Version: %ver_major.1
Release: alt4

%define tag_ver %(echo %version|tr . -)

Summary: Chemistry software file format converter
License: GPL-2.0
Group: Sciences/Chemistry
Url: http://openbabel.sourceforge.net
Vcs: https://github.com/openbabel/openbabel.git

Packager: Michael Shigorin <mike@altlinux.org>

Source: %name-%version.tar
#Source: https://github.com/openbabel/openbabel/releases/download/openbabel-%tag_ver/openbabel-%version-source.tar.bz2
Source1: %name.watch
Patch: %name-%version-%release.patch

BuildRequires: rpm-macros-cmake rpm-build-python3
BuildRequires: cmake eigen3 gcc-c++ rapidjson
BuildRequires: boost-devel boost-filesystem-devel
BuildRequires: libcairo-devel libwxGTK3.2-devel
BuildRequires: zlib-devel libxml2-devel xml-utils
BuildRequires: python3-devel python3-module-setuptools swig

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

%package -n python3-module-%name
Summary: Python 3 bindings for Open Babel
Group: Development/Python3
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

%description -n python3-module-%name
Python bindings for Open Babel.

%prep
%setup -n %name-%version
%patch -p1
# fix python install path
sed -i 's/dist\(-packages\)/site\1/' scripts/CMakeLists.txt

%build
%ifarch %e2k
# see also mcst#3675; there *is* -fPIC there
%add_optflags -Wl,--no-warn-shared-textrel
%endif
%cmake \
    -DWITH_MAEPARSER:BOOL=OFF \
    -DWITH_COORDGEN:BOOL=OFF \
    -DBUILD_GUI:BOOL=ON \
    -DRUN_SWIG=ON \
    -DPYTHON_BINDINGS:BOOL=ON \
    -DPYTHON_EXECUTABLE=%__python3
%nil
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS README* THANKS 
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
%_libdir/cmake/openbabel3

%files -n python3-module-%name
%python3_sitelibdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Oct 16 2023 Anton Midyukov <antohami@altlinux.org> 3.1.1-alt4
- NMU: rebuild with wxGTK3.2

* Wed May 03 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt3
- NMU: fixed FTBFS.

* Wed Dec 08 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt2
- updated to openbabel-3-1-1-73-gf3ed2a9a5

* Tue Dec 07 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- 3.1.1 from upstream git

* Sat Sep 12 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt7
- build python 3 subpackage instead of python 2 one

* Sun Sep 22 2019 Michael Shigorin <mike@altlinux.org> 2.4.1-alt6
- E2K: link-time workaround for mcst#3675
- minor spec cleanup

* Sun Sep 22 2019 Michael Shigorin <mike@altlinux.org> 2.4.1-alt5
- built against eigen3

* Tue Apr 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.1-alt4
- Fixed build on aarch64 and ppc64le (-Wnarrowing).

* Wed May 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt3
- NMU: fixed build with new toolchain.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt2
- Fixed build with new toolchain

* Sun Oct 16 2016 Michael Shigorin <mike@altlinux.org> 2.4.1-alt1
- new version (watch file uupdate)

* Mon Feb 01 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.2-alt2
- fix to build with gcc5

* Sun Apr 13 2014 Michael Shigorin <mike@altlinux.org> 2.3.2-alt1
- added watch file
- new version (watch file uupdate)
- enabled wxGTK GUI

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
