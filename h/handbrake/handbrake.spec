%define _unpackaged_files_terminate_build 1
%define optflags_lto %nil
%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

Name: handbrake
Version: 1.9.0
Release: alt1
Summary: Multithreaded Video Transcoder
Url: http://handbrake.fr/
Group: Video
License: GPL-2.0-or-later

Source: %name-%version.tar
Source7: libvpl-2.13.0.tar.gz
Source8: ffmpeg-7.1.tar.bz2
Source34: x265_4.1.tar.gz

Patch0: alt-use_system_libraries.patch
Patch1: alt-fix_locale_path.patch
Patch2: alt-ffmpeg-disable-strip.patch
Patch3: alt-disable-asm-altivec-x265.patch
Patch4: alt-explicit_cast_neon_func_parameters.patch


BuildRequires: tar gcc-c++ git binutils coreutils m4 patch tar python3 gcc-common make 
BuildRequires: automake-common libtool-common   autoconf-common
BuildRequires: meson nasm ninja-build conan cmake rpm-macros-cmake rpm-macros-make
BuildRequires: libnuma-devel liblame-devel  libopus-devel libspeex-devel
BuildRequires: libxml2-devel libgio-devel libgtk+3-devel gstreamer1.0-devel
BuildRequires: libnuma-devel   liblzma-devel
# System libraries to use instead of contribs
BuildRequires: libdvdnav-devel libtheora-devel libx265-devel
BuildRequires: libharfbuzz-devel libjansson-devel libavutil-devel
BuildRequires: bzlib-devel libfreetype-devel liblame-devel libfribidi-devel
BuildRequires: libvpx-devel libvorbis-devel libbluray-devel libsvt-av1-devel
BuildRequires: nv-codec-headers libx264-devel libass-devel libturbojpeg-devel
BuildRequires: libavcodec-devel libavformat-devel libswscale-devel libswresample-devel
BuildRequires: libavfilter-devel libpostproc-devel fontconfig-devel libdav1d-devel
BuildRequires: libzimg-devel libdvdread-devel  libdovi-devel libgtk4-devel

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
mkdir -p %_builddir/%name-%version/download
cp  %SOURCE7 %SOURCE8 %SOURCE34 \
%_builddir/%name-%version/download

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
sed -i 's|loc_dir_replace_this_with_value|%_datadir/locale/|g' \
%_builddir/%name-%version/gtk/src/meson.build

%_bindir/python3 %_builddir/%name-%version/make/configure.py \
	--disable-df-fetch  --disable-df-verify --verbose  \
	--debug max \
	--optimize speed \
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
%make_build --trace
#%%make --trace

%install
%__make --directory=build install
%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"
%__rm "%buildroot%_datadir/icons"/*/*.cache
%find_lang --output=%name.lang %name

%files cli
%_bindir/HandBrakeCLI

%files gtk -f %name.lang
%_bindir/ghb
%_bindir/HandBrakeGUI
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%_datadir/icons/hicolor/scalable/apps/fr.handbrake.ghb.svg
%_datadir/applications/mimeinfo.cache
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sat Dec 28 2024 Oleg Proskurin <proskur@altlinux.org> 1.9.0-alt1
- New version (Closes: #52164, #52141, #38550)

* Wed Dec 27 2023 Oleg Proskurin <proskur@altlinux.org> 1.7.2-alt1
- Initial build
