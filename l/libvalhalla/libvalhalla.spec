# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 2
%define libname libvalhalla%{major}
%define develname libvalhalla-devel

Name: libvalhalla
Version: 2.0.0
Release: alt1_14
URL: http://libvalhalla.geexbox.org/
Source:	http://libvalhalla.geexbox.org/releases/%{name}-%{version}.tar.bz2
# commit 1093 from upstream (http://hg.geexbox.org/libvalhalla)
# commit 1091 from upstream (http://hg.geexbox.org/libvalhalla)
Patch1: libvalhalla-fix_curl_include.patch
# http://hg.geexbox.org/libvalhalla/rev/883c6adb0024
Patch2: libvalhalla-2.0.0-libavformat-deprecated.patch
# http://hg.geexbox.org/libvalhalla/rev/70494a8fd3f5
Patch3: libvalhalla-2.0.0-libavformat-defines.patch
# http://hg.geexbox.org/libvalhalla/rev/804a298afa60
Patch4: libvalhalla-2.0.0-libavformat-moredefines.patch
# http://hg.geexbox.org/libvalhalla/rev/6f9d0738d006
Patch5: libvalhalla-2.0.0-stream-title.patch
# http://hg.geexbox.org/libvalhalla/rev/d5dc3dc95d62
Patch6: libvalhalla-2.0.0-libavformat-avdict.patch
# http://hg.geexbox.org/libvalhalla/rev/817b714e074a
Patch7: libvalhalla-2.0.0-libavformat-legacy.patch
# http://hg.geexbox.org/libvalhalla/rev/1f3669193d09
Patch8: libvalhalla-2.0.0-libavformat-avdict-test.patch
# http://hg.geexbox.org/libvalhalla/rev/b2a802ea4523
Patch9: libvalhalla-2.0.0-rt.patch

# (cg) This was a test originally in Funda's patch, but it's not upstream :s
Patch10: libvalhalla-2.0.0-libavformat-check.patch
# (cg) Also not yet upstream... no idea if this is the right approach
Patch11: libvalhalla-2.0.0-libavformat-open-api.patch
Patch12: libvalhalla-2.0.0-ffmpeg-2.0.patch
Patch13: libvalhalla-2.0.0-ffmpeg-2.4.patch

License: LGPLv2+
Summary: A media scanner
Group: System/Libraries
BuildRequires: libsqlite3-devel
BuildRequires: libavcodec-devel libavdevice-devel libavfilter-devel libavformat-devel libavresample-devel libavutil-devel libpostproc-devel libswresample-devel libswscale-devel
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: libexif-devel
BuildRequires: gcrypt-utils libgcrypt-devel
Source44: import.info

%description
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package test
Summary: A media scanner
Group: System/Libraries

%description test
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package -n %{libname}
Summary: A media scanner
Group: System/Libraries

%description -n %{libname}
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

%package -n %{develname}
Summary: A media scanner
Group: System/Libraries
Provides: %{name}-devel = %{version}-%{release}
Requires: %libname = %version

%description -n %{develname}
libvalhalla is a library written in C. It is a media scanner, that stores
various information in an SQLite database and relies on FFmpeg (libavformat
and libavutil) and libcurl. It features many Internet grabbers that allows
automatic download of covers, lyrics, informations on media files, tags
retrival in video and music files and so on.

This package contains the headers required for compiling software that uses
the libvalhalla library.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build

export
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--disable-static \
	--enable-pic \
	--enable-shared || cat config.log
%make

%install
%makeinstall_std

%files test
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_14
- new version

