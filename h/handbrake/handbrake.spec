%define optflags_lto %nil
Name: handbrake
Version: 1.7.2
Release: alt1
Summary: Multithreaded Video Transcoder
Url: http://handbrake.fr/
Group: Video
License: GPL-2.0-or-later
Source: %name-%version.tar

Patch0: deb-0001-Remove-embedded-downloaded-copies-of-various-librari.patch
Patch1: deb-0003-Remove-ambient-viewing-support.patch
Patch2: deb-0004-Do-not-use-contribs.patch

BuildRequires: tar gcc-c++ git binutils coreutils m4 patch tar python3 gcc-common make 
BuildRequires: automake-common libtool-common libtheora-devel libturbojpeg-devel autoconf-common 
BuildRequires: meson nasm ninja-build conan cmake rpm-macros-cmake rpm-macros-make python3
BuildRequires: liblame-devel libopus-devel libspeex-devel libvpx-devel libxml2-devel libx264-devel 
BuildRequires: libass-devel libfribidi-devel libgio-devel libgtk+3-devel gstreamer1.0-devel 
BuildRequires: libnuma-devel libjansson-devel libvorbis-devel bzlib-devel liblzma-devel 
BuildRequires: libx265-devel libavutil-devel libavcodec-devel libavformat-devel libswscale-devel
BuildRequires: libswresample-devel libavfilter-devel libbluray-devel libdvdnav-devel libsvt-av1-devel
BuildRequires: nv-codec-headers libpostproc-devel

%description
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

%package cli
Summary: Multithreaded Video Transcoder
Group: Video

%description cli
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.

This package contains a command-line interface for Handbrake.

%package gtk
Summary: Multithreaded Video Transcoder
Group: Video
Requires: %name-cli = %version-%release

%description gtk
HandBrake is an open-source, GPL-licensed, multiplatform, multithreaded video
transcoder.
This package contains a GTK+ graphical user interface for Handbrake.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%_bindir/python3 %_builddir/%name-%version/make/configure.py \
	--disable-df-fetch  --disable-df-verify --verbose  \
	--df-verbose  --src . --build build \
	--prefix "%buildroot%prefix" \
	--release  \
	--disable-fdk-aac \
	--enable-x265 \
	--lto=off \
%ifarch aarch64 x86_64 %ix86
	--enable-nvenc \
%else
	--disable-nvenc \
%endif

cd build
%make_build


%install
%__make --directory=build install
%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"
%__rm "%buildroot%_datadir/icons"/*/*.cache
%find_lang ghb

%files cli
%_bindir/HandBrakeCLI

%files gtk -f ghb.lang
%_bindir/ghb
%_bindir/HandBrakeGUI
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%_datadir/icons/hicolor/scalable/apps/fr.handbrake.ghb.svg
%_datadir/applications/mimeinfo.cache

%changelog
* Wed Dec 27 2023 Oleg Proskurin <proskur@altlinux.org> 1.7.2-alt1
- Initial build