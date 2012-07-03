%undefine __libtoolize
%define _optlevel s

Name: ksocrat
Version: 3.2.1
Release: alt15

Group: System/Internationalization
Summary: English/Russian and Russian/English dictionary for KDE
License: GPL && ARSENAL INC.
Url: http://ksocrat.linux.kiev.ua/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires: kdelibs >= {%get_version kdelibs}
Provides: ksocrat-data = %version-%release
Obsoletes: ksocrat-data < %version-%release

Source0: %name-%version.tar.bz2
Source1: ksocrat-enru-dic-1.0.1.tar.bz2
Source2: ksocrat-ruen-dic-1.0.1.tar.bz2
Source3: admin.tar.bz2

%set_gcc_version 4.5
BuildPreReq: iconv
BuildRequires: libX11-devel gcc4.5-c++
BuildRequires: glibc-devel kdelibs-devel libjpeg-devel
BuildRequires: libpng-devel libqt3-devel libstdc++4.5-devel zlib-devel
#BuildRequires: automake_1.4 autoconf_2.13
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
#BuildRequires: kdelibs > 1 kdelibs-devel > 1

%description
Simple frontend for Socrat English/Russian
and Russian/English dictionary.

%package data
Group: Text tools
Summary: En-Ru and Ru-En dictionaries for %name package
License: ARSENAL INC.

%description data
English/Russian and Russian/English dictionaries
for %name package

%prep
%setup -q -a3

tar xvfj %SOURCE1
tar xvfj %SOURCE2

pushd usr/share/apps/ksocrat
mv enru.dic enru.dic.koi8r
iconv -f KOI8-R -t UTF-8 -o enru.dic enru.dic.koi8r
popd

#subst "s/\(Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g" admin/acinclude.m4.in
#subst "s/\(Wl,--no-undefined\)/ -Wl,--allow-shlib-undefined \1/g" configure
#subst "s/\-lkdeui/-lkdeui -lpthread/g" configure
#subst "s/\.la/.so/g" configure
make -f admin/Makefile.common cvs

%build
export QTDIR=%_qt3dir
export KDEDIR=/usr

export LD_LIBRARY_PATH=$QTDIR/lib:$KDEDIR/lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:/usr/bin:$PATH

export CFLAGS="%optflags -I%_includedir/tqtinterface"
export CXXFLAGS="%optflags -I%_includedir/tqtinterface"

%configure \
	--disable-debug \
	--enable-final \
	--enable-shared \
	--disable-static \
	--disable-rpath \
%ifarch x86_64
	--enable-libsuffix=64 \
%endif
	--enable-new-ldflags \
	--without-arts

%make_build LIBDIR=%_libdir

%install
make DESTDIR=%buildroot LIBDIR=%_libdir install

mkdir -p %buildroot/%_Kmenudir/
mv %buildroot/%_datadir/applnk/Applications/*.desktop %buildroot/%_Kmenudir/

pushd usr/share/apps/ksocrat
		mv ruen.dic ruen.dic.koi8r
		iconv -f KOI8-R -t UTF-8 -o ruen.dic ruen.dic.koi8r
    install -m 0644 *.dic %buildroot/%_datadir/apps/ksocrat/
popd

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog* README TODO
#
%_bindir/*
%_iconsdir/*/*/apps/%name.*
%_Kmenudir/*.desktop
%_datadir/apps/%name
%doc usr/share/apps/ksocrat/Arsenal*
#
%dir %_datadir/apps/%name
%_datadir/apps/%name/*.dic

%changelog
* Thu Jun 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt15
- Fixed build

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt14
- Fixed build

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt13
- Rebuilt for debuginfo

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt12
- Built without arts

* Tue Jan 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt11
- Fixed:
  + build
  + desktop file

* Sat Dec 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt10
- Fixed russian->english translation (ALT #24600)

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt9
- Restored from archive
- Applied Debian's patch
- Broken russian->english translate (help needed)

* Tue Dec 25 2007 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt8
- fixed build with new autotools

* Mon Oct 22 2007 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt7
- remove %%_iconsdir/* directories ownership

* Tue Jul 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt6
- fix build on x86_64

* Mon Jul 03 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt5
- fix build requires

* Mon Jan 23 2006 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt4
- remove menufile

* Tue Jun 14 2005 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt3
- add missing dictionaries

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt2
- fix compile
- don't split data to separate package

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- new version

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2-alt2
- rebuild with KDE 3.2

* Mon May 05 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.2-alt1
- new version

* Thu Feb 06 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- 3.1.1
- add license to dictionaries

* Mon Jan 20 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 3.1-alt1
- 3.1
- Remove dictionaries

* Fri Nov 22 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 3.0-alt1
- 3.0
