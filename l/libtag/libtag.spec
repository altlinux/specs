%define rname taglib

Name: libtag
Version: 1.7.2
Release: alt1

Summary: TagLib, is well, a library for reading and editing audio meta data
License: LGPL / MPL
Group: System/Libraries
Url: http://ktown.kde.org/~wheeler/taglib/
Packager: Sergey V Turchin <zerg@altlinux.org>

Provides: %rname = %version-%release

Source0: %rname-%version.tar.bz2
Source1: taglib-csa6.tar.bz2
Source2: version-script.libtag

Patch1: taglib-1.6-alt-rcc-fix.patch
Patch2: taglib-1.5-alt-gcc43.patch
Patch3: taglib-1.6-alt-versioning.patch
#(tpg) http://foetida.jaist.ac.jp:37565/~yaz/diary/2006/07/taglib-1.4_wchar.diff
Patch10:         taglib-1.4_wchar.diff

BuildRequires: gcc-c++ librcc-devel zlib-devel
BuildRequires: doxygen graphviz cmake kde-common-devel

%description
TagLib, is well, a library for reading and editing audio meta data,
commonly know as tags.
Some goals of TagLib:
	A clean, high level, C++ API to handling audio meta data.
	Support for at least ID3v1, ID3v2 and Ogg Vorbis comments.
	A generic, simple API for the most common tagging related functions.
	Binary compatibility between minor releases using the standard KDE/Qt
	techniques for C++ binary compatibility.
	Make the tagging framework extensible by library users; i.e. it will be
	possible for libarary users to implement additional ID3v2 frames,
	without modifying the TagLib source.
Because TagLib desires to be toolkit agnostic, in hope of being widely
adopted and the most flexible in licensing TagLib provides many of its
own toolkit classes; in fact the only external dependancy that TagLib has,
it a semi-sane STL implementation.

%package devel
Group: Development/C
Summary: Headers and static lib for taglib development
Requires: %name = %version-%release
Provides: %rname-devel = %version-%release

%description devel
Install this package if you want do compile applications using the libtag
library.


%prep
%setup -q -n %rname-%version -a1
install -m0644 %SOURCE2 ./
patch -p1 <taglib-csa/taglib-1.5-ds-rusxmms.patch
%patch1 -p1
%patch2 -p1
%patch3 -p1
#
%patch10 -p1


%build
%Kcmake \
    -DINCLUDE_INSTALL_DIR=%_includedir \
    -DWITH_ASF:BOOL=ON \
    -DWITH_MP4:BOOL=ON
%Kmake
%Kmake docs

%install
%Kinstall

%files
%doc AUTHORS NEWS
%_libdir/libtag.so.*
%_libdir/libtag_c.so.*

%files devel
%doc BUILD-*/doc/html AUTHORS NEWS
%_bindir/taglib-config
%_libdir/libtag.so
%_libdir/libtag_c.so
%_libdir/pkgconfig/taglib*.pc
%dir %_includedir/taglib/
%_includedir/taglib/*.h
%_includedir/taglib/*.tcc

%changelog
* Fri May 11 2012 Sergey V Turchin <zerg@altlinux.org> 1.7.2-alt1
- new version

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 1.7-alt0.M60P.1
- built for M60P

* Mon Dec 19 2011 Sergey V Turchin <zerg@altlinux.org> 1.7-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt5
- fix to build

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.6.3-alt3
- Rebuilt for soname set-versions.

* Tue Dec 14 2010 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt2
- rebuilt

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt0.M51.1
- built for M51

* Wed May 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1
- new version

* Thu Nov 12 2009 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt0.M51.1
- built for M51

* Wed Nov 11 2009 Sergey V Turchin <zerg@altlinux.org> 1.6.1-alt1
- new version

* Sat Sep 26 2009 Sergey V Turchin <zerg@altlinux.org> 1.6-alt3
- add versioning

* Fri Sep 25 2009 Sergey V Turchin <zerg@altlinux.org> 1.6-alt2
- built with ASF and MP4 support

* Fri Sep 25 2009 Sergey V Turchin <zerg@altlinux.org> 1.6-alt1
- new version
- update rusxmms patch

* Mon Jun 29 2009 Sergey V Turchin <zerg@altlinux.org> 1.5-alt4
- fix to build
- add patch to convert cjk chars into utf8

* Tue Dec 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt3
- NMU: fixed build with gcc 4.3

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 1.5-alt2
- reapply RCC patch; thanks shrek@alt
- fix build requires to generate docs

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.5-alt1
- new version

* Mon Sep 03 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4-alt5
- fix %%license

* Thu Jan 25 2007 Sergey V Turchin <zerg at altlinux dot org> 1.4-alt4
- add patch to ignore 0 lenght tag frames (#10705)
- fix build requires

* Wed Oct 25 2006 Igor Zubkov <icesik@altlinux.org> 1.4-alt3
- NMU
- move to Sisyphus

* Thu May 11 2006 Igor Zubkov <icesik@altlinux.ru> 1.4-alt2
- build with taglib-ds-rcc.patch (taglib-csa3.tar.bz2)

* Thu Aug 04 2005 Sergey V Turchin <zerg at altlinux dot org> 1.4-alt1
- new version
- add html docs

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 1.3.1-alt2
- rebuild with gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 1.3.1-alt1
- new version

* Thu Sep 30 2004 Sergey V Turchin <zerg at altlinux dot org> 1.3-alt1
- new version

* Thu Apr 08 2004 Sergey V Turchin <zerg at altlinux dot org> 1.1-alt1
- new version

* Tue Mar 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- build for ALT

* Thu Jan 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0-1mdk
- 1.0

* Mon Dec 22 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.96-2mdk
- Move taglib-config to libname-devel (Thanks Nicolas Chipaux to report me this bug)

* Tue Dec 02 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.96-1mdk
- 0.96

* Wed Nov 05 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.95-2mdk
- Fix description

* Tue Nov 04 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.95-1mdk
- Initial package

