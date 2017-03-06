%define sover 13
%define libarchive libarchive%sover

Name: libarchive
Version: 3.3.1
Release: alt1%ubt

Group: System/Libraries
Summary: A library for handling streaming archive formats
License: BSD
Url: http://www.libarchive.org/
#Url: https://github.com/libarchive/libarchive

Source0: libarchive-%version.tar.gz
# SuSE
# ALT
Patch100: alt-disable-lzma-mt.patch

# Automatically added by buildreq on Mon Mar 11 2013 (-bi)
# optimized out: elfutils pkg-config python-base ruby ruby-stdlibs
#BuildRequires: bzlib-devel glibc-devel-static libacl-devel libattr-devel libe2fs-devel liblzma-devel liblzo2-devel libssl-devel libxml2-devel rpm-build-ruby zlib-devel
BuildRequires(pre): rpm-build-ubt
BuildRequires: bzlib-devel glibc-devel libacl-devel libattr-devel libe2fs-devel liblzma-devel liblzo2-devel libssl-devel libxml2-devel zlib-devel
BuildRequires: libnettle-devel

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package -n %libarchive
Summary: Full-featured tar replacement built on libarchive
Group: System/Libraries
%description -n %libarchive
The bsdtar program is a full-featured tar replacement built on libarchive.

%package -n bsdtar
Summary: Full-featured tar replacement built on libarchive
Group: Archiving/Backup
Requires: %libarchive = %EVR
%description -n bsdtar
The bsdtar program is a full-featured tar replacement built on libarchive.

%package -n bsdcpio
Summary: Full-featured cpio replacement built on libarchive
Group: Archiving/Backup
Requires: %libarchive = %EVR
%description -n bsdcpio
The bsdcpio program is a full-featured cpio replacement built on libarchive.

%package -n bsdcat
Summary: Full-featured cat replacement built on libarchive
Group: Archiving/Backup
Requires: %libarchive = %EVR
%description -n bsdcat
The bsdcpio program is a full-featured cat replacement built on libarchive.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %libarchive = %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -q
%patch100 -p1
%autoreconf


%build
%configure \
    --disable-rpath \
    --disable-static \
    --enable-shared \
    --enable-bsdtar=shared \
    --enable-bsdcpio=shared \
    --with-lzma \
    --without-lzmadec
%make_build


%install
%make DESTDIR=%buildroot  install


%files -n %libarchive
%doc README* NEWS
%_libdir/*.so.%sover
%_libdir/*.so.%sover.*

%files -n bsdtar
%_bindir/bsdtar
%_man1dir/bsdtar*

%files -n bsdcpio
%_bindir/bsdcpio
%_man1dir/bsdcpio*

%files -n bsdcat
%_bindir/bsdcat
%_man1dir/bsdcat*

%files devel
%doc
%_includedir/*
%_man3dir/*
%_man5dir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 06 2017 Sergey V Turchin <zerg@altlinux.org> 3.3.1-alt1%ubt
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 3.2.1-alt1
- new version

* Wed Dec 16 2015 Sergey V Turchin <zerg@altlinux.org> 3.1.2-alt3
- rebuild with new libnettle

* Wed Aug 05 2015 Sergey V Turchin <zerg@altlinux.org> 3.1.2-alt2
- merge SuSE and FC patches
- security fixes: CVE-2013-0211

* Mon Mar 11 2013 Sergey V Turchin <zerg@altlinux.org> 3.1.2-alt1
- new version

* Wed Feb 29 2012 Sergey V Turchin <zerg@altlinux.org> 2.8.5-alt1.M60P.1
- built for M60P

* Wed Feb 29 2012 Sergey V Turchin <zerg@altlinux.org> 2.8.5-alt2
- remove versioning
- add patches from SuSE

* Mon Nov 14 2011 Sergey V Turchin <zerg@altlinux.org> 2.8.5-alt1
- new version

* Wed Dec 08 2010 Sergey V Turchin <zerg@altlinux.org> 2.8.4-alt3
- rebuilt

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 2.8.4-alt2
- rebuilt with new ssl

* Mon Jul 12 2010 Sergey V Turchin <zerg@altlinux.org> 2.8.4-alt1
- new version

* Thu Sep 24 2009 Sergey V Turchin <zerg@altlinux.org> 2.7.1-alt2
- build with liblzma instead of liblzmadec

* Mon Aug 24 2009 Sergey V Turchin <zerg@altlinux.org> 2.7.1-alt1
- new version

* Thu Jun 25 2009 Sergey V Turchin <zerg@altlinux.org> 2.7.0-alt1
- new version
- package bsdcpio

* Thu Apr 09 2009 Sergey V Turchin <zerg@altlinux.org> 2.6.2-alt1
- new version
- package bsdtar

* Thu Apr 09 2009 Sergey V Turchin <zerg@altlinux.org> 2.6.0-alt1
- new version
- remove deprecated macroses from specfile

* Mon Sep 15 2008 Sergey V Turchin <zerg at altlinux dot org> 2.5.5-alt1
- new version
- add versioning

* Mon Mar 24 2008 Sergey V Turchin <zerg at altlinux dot org> 2.4.14-alt1
- initial specfile
