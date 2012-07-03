Name: gmerlin-avdecoder
Summary: A multimedia decoding library
Version: 1.1.0
Release: alt1
Url: http://gmerlin.sourceforge.net/
License: LGPLv2+
Group: Video

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar.gz
Patch:  %name-1.0.3-autotools.patch
Patch1: %name-%version-ffmpeg.patch

# Automatically added by buildreq on Mon Mar 28 2011
BuildRequires: doxygen libXext-devel
BuildRequires: libavformat-devel libcdio-devel libdca-devel libdvdread-devel
BuildRequires: libflac-devel libgmerlin-devel libmad-devel libmjpegtools-devel
BuildRequires: libmpcdec-devel libmpeg2-devel libopenjpeg-devel
BuildRequires: libpng-devel libpostproc-devel libschroedinger-devel libsmbclient-devel libspeex-devel libswscale-devel libtheora-devel libtiff-devel libvorbis-devel xorg-cf-files

%description
This is gmerlin_avdecoder, a multimedia decoding library.
It it primarly a support library for gmerlin, but it can also be
used as a standalone library for getting sophisticated media file
decoding support for your application.

%package -n lib%name
Group: System/Libraries
Summary: Libraries for %name
Requires: %name = %version

%description -n lib%name
This package contains shared libraries for %name.

%package -n lib%name-devel
Group: Development/Other
Summary: Development files for %name
Requires: lib%name = %version
Provides: %name-devel = %version

%description -n lib%name-devel
This package contains development files for %name.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
AUTOPOINT=true %autoreconf
%configure
%make_build

rm -f %buildroot%_libdir/*.la

%install
%makeinstall
%find_lang %name

rm -f %buildroot%_libdir/gmerlin/plugins/*.la

%files -f %name.lang
%_bindir/*
%_libdir/gmerlin/plugins/*.so
%doc AUTHORS COPYING NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/gmerlin/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%doc %_docdir/%name

%changelog
* Thu Sep 22 2011 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.0-alt1
- New version
- add patch likes 
http://lists.alioth.debian.org/pipermail/pkg-multimedia-maintainers/2011-August/021391.html


* Mon Mar 28 2011 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.3-alt2
- fix BuildRequires

* Sun Apr 25 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.3-alt1
- Build for ALT Linux

* Sun Feb 28 2010 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2010.1
+ Revision: 512584
- New version 1.0.3


