Name: spek
Version: 0.8.3
Release: alt3
Summary: Acoustic Spectrum Analyser
Group: Sound
License: GPLv3
Url: http://spek.cc/
Source: %name-%version.tar.gz
Patch1: spek-0.8.2-stdlib.patch
Patch2: spek-0.8.3-ffmpeg.patch

# Automatically added by buildreq on Thu Aug 09 2018
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libavcodec-devel libavutil-devel libgdk-pixbuf libopencore-amrnb0 libopencore-amrwb0 libp11-kit libstdc++-devel libwayland-client libwayland-server libx265-160 perl perl-Encode perl-XML-Parser perl-parent pkg-config python-base sh3 xz
BuildRequires: gcc-c++ intltool libavformat-devel libwxGTK-devel

%description
Spek helps to analyse your audio files by showing their spectrogram.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc README*
%_bindir/*
%_man1dir/*
%_desktopdir/*
%_iconsdir/*/*/*/*

%changelog
* Thu Aug 09 2018 Fr. Br. George <george@altlinux.ru> 0.8.3-alt3
- fixed build with new ffmpeg

* Tue Jun 13 2017 Anton Farygin <rider@altlinux.ru> 0.8.3-alt2
- fixed build with new ffmpeg

* Tue Apr 21 2015 Fr. Br. George <george@altlinux.ru> 0.8.3-alt1
- Autobuild version bump to 0.8.3
- Fix build

* Thu Sep 18 2014 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Initial build

