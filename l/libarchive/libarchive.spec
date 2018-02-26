Name: libarchive
Version: 2.8.5
Release: alt2

Group: System/Libraries
Summary: A library for handling streaming archive formats
License: BSD
Url: http://code.google.com/p/libarchive/
#Url: http://people.freebsd.org/~kientzle/libarchive/

Source0: libarchive-%version.tar.gz
Source1: libarchive.map
Source2: libarchive.lds
# ALT
Patch1: libarchive-2.8.5-alt-versioning.patch
# MDK
Patch101: libarchive-2.6.1-headers.patch
# SuSE
Patch201: libarchive-2.5.5_handle_ENOSYS_from_lutimes.patch
Patch202: libarchive-ignore-sigpipe-in-test-suite.patch
Patch203: libarchive-test-fuzz.patch


BuildRequires: bzlib-devel glibc-devel libacl-devel libattr-devel libe2fs-devel libssl-devel zlib-devel
BuildRequires: liblzma-devel

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package -n bsdtar
Summary: Full-featured tar replacement built on libarchive
Group: Archiving/Backup
Requires: %name = %version-%release
%description -n bsdtar
The bsdtar program is a full-featured tar replacement built on libarchive.

%package -n bsdcpio
Summary: Full-featured tar replacement built on libarchive
Group: Archiving/Backup
Requires: %name = %version-%release
%description -n bsdcpio
The bsdcpio program is a full-featured tar replacement built on libarchive.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup -q
install -m 0644 %SOURCE1 libarchive.map
install -m 0644 %SOURCE2 libarchive.lds
%patch1 -p1
%patch101 -p0
%patch201 -p0
%patch202 -p1
%patch203 -p1
autoreconf -fisv


%build
%configure \
    --disable-static \
    --enable-shared \
    --enable-bsdtar=shared \
    --enable-bsdcpio=shared \
    --with-lzma \
    --without-lzmadec
%make_build


%install
%make DESTDIR=%buildroot  install


%files
%doc README NEWS
%_libdir/*.so.*

%files -n bsdtar
%_bindir/bsdtar
%_man1dir/bsdtar*

%files -n bsdcpio
%_bindir/bsdcpio
%_man1dir/bsdcpio*

%files devel
%doc
%_includedir/*
%_man3dir/*
%_man5dir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
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
