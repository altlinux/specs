%define rname taglib
%define _K6link %_K6lib

%define sover 2
%define libtag libtag%sover
%define libtag_c libtag_c%sover

Name: taglib
Version: 2.0.2
Release: alt2

Group: System/Libraries
Summary: TagLib, is well, a library for reading and editing audio meta data
License: (LGPL-2.1-only OR MPL-1.1) AND BSD-2-Clause AND LGPL-2.1-only
Url: http://taglib.github.io/

Provides: %rname = %version-%release

Source0: %rname-%version.tar

# SuSE
Patch2: taglib-1.8-ds-rusxmms-r2.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: gcc-c++ zlib-devel libutfcpp-devel
#BuildRequires: librcc-devel
BuildRequires: doxygen graphviz cmake

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
#Provides: libtag-devel = %version-%release
Conflicts: libtag-devel
%description devel
Install this package if you want do compile applications using the libtag
library.

%package -n %libtag
Summary: Library for reading and editing audio meta data
Group: System/Libraries
%description -n %libtag
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags

%package -n %libtag_c
Summary: Library for reading and editing audio meta data
Group: System/Libraries
%description -n %libtag_c
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags

%prep
%setup -n %rname-%version
#%patch2 -p1

%build
%K6cmake \
    -DINCLUDE_INSTALL_DIR=%_includedir \
    -DWITH_ASF:BOOL=ON \
    -DWITH_MP4:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    #
%K6make
%K6make docs

%install
%K6install

#install alternative
sed -i -E 's|^Requires:[[:space:]]+%rname$|Requires: %rname-2|' %buildroot/%_libdir/pkgconfig/%{rname}_c.pc
mv %buildroot/%_libdir/pkgconfig/%rname{,-2}.pc
mv %buildroot/%_libdir/pkgconfig/%{rname}_c{,-2}.pc
install -d %buildroot/%_sysconfdir/alternatives/packages.d/
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name-devel <<__EOF__
%_libdir/pkgconfig/%rname.pc %_libdir/pkgconfig/%rname-2.pc %version
%_libdir/pkgconfig/%rname.pc %_libdir/pkgconfig/%{rname}_c-2.pc %version
__EOF__

%files -n %libtag
%doc AUTHORS CHANGELOG.md
%_libdir/libtag.so.%sover
%_libdir/libtag.so.*

%files -n %libtag_c
%doc AUTHORS CHANGELOG.md
%_libdir/libtag_c.so.%sover
%_libdir/libtag_c.so.*

%files devel
%doc BUILD*/doc/html AUTHORS CHANGELOG.md README.md
%config %_sysconfdir/alternatives/packages.d/%name-devel
%_bindir/taglib-config
%_libdir/libtag.so
%_libdir/libtag_c.so
%_libdir/pkgconfig/taglib*.pc
%dir %_includedir/taglib/
%_includedir/taglib/*.h
%_includedir/taglib/*.tcc
%_libdir/cmake/taglib/

%changelog
* Tue Mar 18 2025 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt2
- switch pc-files via alternatives

* Mon Mar 17 2025 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version (closes: 53481)

* Fri Jan 31 2025 Sergey V Turchin <zerg@altlinux.org> 1.13.1-alt1
- new version

* Mon May 17 2021 Sergey V Turchin <zerg@altlinux.org> 1.12-alt1
- new version

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 1.11.1-alt0.M80P.1
- build for M80P

* Wed Nov 23 2016 Sergey V Turchin <zerg@altlinux.org> 1.11.1-alt1
- new version

* Thu Nov 12 2015 Sergey V Turchin <zerg@altlinux.org> 1.10-alt1
- new version

* Wed May 20 2015 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt2
- rebuild with gcc5

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 1.9.1-alt1
- new version

* Tue Mar 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.8-alt1.M60P.1
- built for M60P (ALT#28700)

* Tue Mar 19 2013 Sergey V Turchin <zerg@altlinux.org> 1.8-alt2
- sync patches with SuSE (return rusxmms patch)

* Mon Jan 14 2013 Sergey V Turchin <zerg@altlinux.org> 1.8-alt0.M60P.1
- build for M60P

* Tue Oct 16 2012 Sergey V Turchin <zerg@altlinux.org> 1.8-alt1
- new version
- built without tag encoding detection patch

* Wed May 16 2012 Sergey V Turchin <zerg@altlinux.org> 1.7.2-alt0.M60P.1
- build for M60P

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

