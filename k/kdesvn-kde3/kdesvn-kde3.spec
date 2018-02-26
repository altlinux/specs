%define _unpackaged_files_terminate_build 1
%define oname kdesvn
Name: kdesvn-kde3
Version: 1.0.6
Release: alt2

Summary: A subversion client for the KDE with KIO integration

License: GPL
Url: http://www.alwins-world.de/wiki/programs/kdesvn
# There should be a better place
Group: Development/Other
Packager: Boris Savelev <boris@altlinux.ru>
Source: %oname-%version.tar.bz2
Patch: kdesvn-1.0.0-asneeded.patch
Patch1: kde-svn-alt-compile-fix.patch
Patch2: kdesvn-1.0.6-buildTDE.patch

BuildPreReq: cmake libsqlite3-devel libexpat-devel
BuildPreReq: gcc-c++ kdelibs-devel libsubversion-devel xml-utils
Conflicts: kdesvn

%description
Kdesvn is a subversion client for KDE.
It may used as standalone application or plugin (KPart). Base functions are provided
via a KIO protocol, too.

%package kiosvn
Group: Development/Other
Summary: A kde-kio integration for subversion based on kdesvn
Requires: %name = %version-%release
Conflicts: kdesdk-kio-svn
Provides: kio-svn

%description kiosvn
KIO integration (KIO::svn) based on kdesvn alternative protocol name.

%package -n libsvnqt3
Group: System/Libraries
Summary: Wrapper lib for subversion QT integration

%description -n libsvnqt3
Shared lib which contains a QT C++ wrapper for subversion. It is core part
of kdesvn but is designed to not require KDE so plain QT programs may use
it.

%package -n libsvnqt3-devel
Group: Development/C++
Summary: Wrapper lib for subversion QT integration
Requires: libsvnqt3 = %version
Conflicts: libsvnqt-devel

%description -n libsvnqt3-devel
Development files for libsvnqt

%prep
%setup -n %oname-%version
%patch -p1
%patch2 -p1

# gentoo
# Force kdesvn to recognize kio_svn protocol name instead of kio_ksvn
# (this way we can reuse .protocol files from kdesdk-kioslaves, avoiding
# collision)
grep -rle "kio_ksvn" * | xargs sed -i -e "s:kio_ksvn:kio_svn:"


%build
export QTDIR=%_qt3dir
export KDEDIR=%_K3prefix
BD=%_builddir/%name-%version/BUILD
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

if ! [ -f $BD/CMakeCache.txt ]
then
%K3cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
fi
%K3make

%install
%K3install

%find_lang --with-kde %oname

%files -f %oname.lang
%_bindir/kdesvn
%_bindir/kdesvnaskpass
%_man1dir/kdesvn.1*
%_man1dir/kdesvnaskpass.1*
%_Kmenudir/kdesvn.desktop
%_Kapps/kconf_update/*
%_Kapps/kdesvn/
%_Kapps/kdesvnpart/
%_Kapps/konqueror/servicemenus/*.desktop
%_libkde/kded_kdesvnd.*
%_libkde/libkdesvnpart.*
%_Kcfg/kdesvn_part.kcfg
%_Kservices/kded/kdesvnd.desktop
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svgz

%files kiosvn
%_libkde/kio_svn.*
%_Kservices/*.protocol

%files -n libsvnqt3
%_libdir/libsvnqt.so.*

%files -n libsvnqt3-devel
%_libdir/libsvnqt.so
%_includedir/svnqt

%changelog
* Sun Mar 11 2012 Roman Savochenko <rom_as@altlinux.ru> 1.0.6-alt2
- Build for TDE 3.5.13 release

* Tue Aug 25 2009 Boris Savelev <boris@altlinux.org> 1.0.6-alt1
- new version

* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 1.0.5-alt3
- add libexpat-devel to buildreq

* Mon Apr 13 2009 Boris Savelev <boris@altlinux.org> 1.0.5-alt2
- fix build

* Fri Mar 13 2009 Boris Savelev <boris@altlinux.org> 1.0.5-alt1
- build for KDE3

* Sat Mar 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.14.3-alt2
- 0.14.3

* Thu Mar 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.14.2-alt2
- add update_desktopdb/clean_desktopdb calls (found by repocop)

* Tue Mar 18 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Sun Dec 02 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Thu Oct 25 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.14.0-alt1
- 0.14.0
- enable _unpackaged_files_terminate_build
- spec fixes

* Sat Sep 22 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Tue Jul 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Thu May 31 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Wed Mar 28 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.11.2-alt1
- 0.11.2

* Mon Mar 19 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.11.1-alt1
- 0.11.1
- fix x86_64 (#10957, peet@)
- fix buildreqs

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.11.0-alt3
- rewrite buildreqs

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.11.0-alt2.1
- BuildPreReq: s/libneon-devel/libneon0.25-devel/

* Tue Dec 12 2006 Andrey Rahmatullin <wrar@altlinux.ru> 0.11.0-alt2
- Sisyphus build
- spec cleanup
- reworked link fixes patch

* Fri Dec  8 2006 Alexey Morozov <morozov@altlinux.org> 0.11.0-alt1
- New version (0.11.0)
- Dropped kdesvn-0.8.5-alt-compile_final.patch (#0) since cmake
  build system doesn't support final compilation for libraries
  (although KDE3_ENABLE_FINAL option does exist)
- Added kdesvn-0.11.0-alt-build_fixes.patch (#0) to be able to compile
  it against ALT libapr

* Mon Sep 18 2006 Alexey Morozov <morozov@altlinux.org> 0.9.3-alt1
- new version (0.9.3)

* Thu Jun 29 2006 Alexey Morozov <morozov@altlinux.org> 0.8.5-alt1
- New version (0.8.5)
- added patch kdesvn-0.8.5-alt-compile_final.patch to be cleanly
  compile with 'final' enabled

* Mon May 15 2006 Alexey Morozov <morozov@altlinux.org> 0.8.3-alt2
- Added proper libsvnqt subpackage
- Added previously missing files kio_ksvn files
- Added xml-utils build requirement

* Fri May 12 2006 Alexey Morozov <morozov@altlinux.org> 0.8.3-alt1
- new version (0.8.3)

* Fri Apr 14 2006 Alexey Morozov <morozov@altlinux.org> 0.8.1-alt1
- New version (0.8.1)

* Tue Mar 28 2006 Alexey Morozov <morozov@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux (spec is based on Rajko Albrecht's
  <ral@alwins-world.de> original spec)

