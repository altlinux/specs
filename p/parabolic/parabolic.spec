%define _unpackaged_files_terminate_build 1
%define app_id org.nickvision.tubeconverter

Name: parabolic
Version: 2025.11.1
Release: alt1

Summary: Download web video and audio
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

URL: https://nickvision.org/parabolic
VCS: https://github.com/NickvisionApps/Parabolic
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-cmake
BuildRequires: rpm-build-python3
BuildRequires: yelp
BuildRequires: gcc-c++
BuildRequires: libmaddy-devel
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libbrotlidec)
BuildRequires: pkgconfig(sqlcipher)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(mit-krb5-gssapi)
BuildRequires: pkgconfig(libnick)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(blkid)
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(libxml++-5.0)
BuildRequires: pkgconfig(libselinux)
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(libthai)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(libnghttp2)
BuildRequires: pkgconfig(datrie-0.2)
BuildRequires: pkgconfig(datrie-0.2)
BuildRequires: pkgconfig(libngtcp2)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(libnghttp3)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libdeflate)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(appstream)

Requires: aria2
Requires: ffmpeg
Requires: yt-dlp

ExclusiveArch: x86_64

%description
- A basic yt-dlp frontend
- Supports downloading videos in multiple formats (mp4, webm, mp3, opus, flac, and wav)
- Run multiple downloads at a time
- Supports downloading metadata and video subtitles

%prep
%setup
%patch -p 1

# Add shebang to .py files
find . -type f -name "*.py" -exec sed -i "1s|^|#!%__python3\n|" {} +

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DUI_PLATFORM=gnome \
  -Wno-dev
%cmake_build

%install
%cmake_install
%find_lang %name

%files -f %name.lang
%_bindir/%app_id
%_libdir/%app_id/*
%_datadir/applications/%app_id.desktop
%_datadir/dbus-1/services/%app_id.service
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml

%changelog
* Wed Dec 10 2025 David Sultaniiazov <x1z53@altlinux.org> 2025.11.1-alt1
- Initial build.
