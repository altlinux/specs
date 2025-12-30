%define _unpackaged_files_terminate_build 1
%define optflags_lto %nil
%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

Name: handbrake
Version: 1.10.2
Release: alt1
Summary: Multithreaded Video Transcoder
Url: http://handbrake.fr/
VCS: https://github.com/HandBrake/HandBrake.git
Group: Video
License: GPL-2.0-or-later

Source: %name-%version.tar

# too old in Sisyphus (2.3.0-alt1).
Source3: SVT-AV1-v3.1.2.tar.gz
# too old in Sisyphus (2.3.1-alt1).
Source8: dovi_tool-libdovi-3.3.2.tar.gz
# hardly patched by the upstream.
Source17: x265-snapshot-20250729-13276.tar.gz
# too old in Sisyphus (2.3.1-alt1).
Source18: dovi_tool-libdovi-3.3.2_vendor.tar.gz
# too old in Sisyphus (5.4.5-alt1).
Source23: xz-5.8.1.tar.bz2
# hardly patched by the upstream.
Source24: ffmpeg-7.1.1.tar.bz2
# patched by the apstream.
Source31: zimg-snapshot-20250624.tar.gz

Patch0: alt-use_system_libraries_for_1.10.2.patch
Patch1: alt-fix_locale_path.patch
Patch2: alt-ffmpeg-disable-strip.patch
Patch3: alt-disable-asm-altivec-x265.patch
Patch5: alt-update_russian_translations.patch
Patch6: alt-return_russian_locale.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-make 
BuildRequires: tar gcc-c++ git binutils coreutils
BuildRequires: m4 patch tar python3 gcc-common make
BuildRequires: automake-common libtool-common   autoconf-common
BuildRequires: meson nasm ninja-build conan cmake 
BuildRequires: libnuma-devel liblame-devel  libopus-devel libspeex-devel
BuildRequires: libxml2-devel libgio-devel libgtk+3-devel gstreamer1.0-devel
BuildRequires: libnuma-devel   liblzma-devel

# System libraries to use instead of contribs.
BuildRequires: libdvdnav-devel libharfbuzz-devel libjansson-devel
BuildRequires: bzlib-devel libfreetype-devel liblame-devel libfribidi-devel
BuildRequires: libvpx-devel libvorbis-devel libbluray-devel
BuildRequires: nv-codec-headers  libass-devel libturbojpeg-devel
BuildRequires: fontconfig-devel libdav1d-devel libtheora-devel
BuildRequires: libdvdread-devel libgtk4-devel libx264-devel

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


cp %SOURCE3 %SOURCE8 %SOURCE17 \
%SOURCE18 %SOURCE23 \
%SOURCE24 %SOURCE31 \
%_builddir/%name-%version/download

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1

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
    --enable-nvenc 
%else
    --disable-nvenc 
%endif

cd build
%make_build --trace

%install
%__make --directory=build install
%__ln_s ghb "%buildroot%_bindir/HandBrakeGUI"
%__rm "%buildroot%_datadir/icons"/*/*.cache
%__rm %buildroot%_datadir/applications/mimeinfo.cache



%find_lang ghb

%files cli
%_bindir/HandBrakeCLI

%files gtk -f ghb.lang
%_bindir/ghb
%_bindir/HandBrakeGUI
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/scalable/apps/fr.handbrake.ghb.svg

%changelog
* Mon Dec 29 2025 Oleg Proskurin <proskur@altlinux.org> 1.10.2-alt1
- New version

* Wed May 07 2025 Oleg Proskurin <proskur@altlinux.org> 1.9.0-alt2
- Fix the build and update the russian translations (Closes #53272)

* Sat Dec 28 2024 Oleg Proskurin <proskur@altlinux.org> 1.9.0-alt1
- New version (Closes: #52164, #52141, #38550)

* Wed Dec 27 2023 Oleg Proskurin <proskur@altlinux.org> 1.7.2-alt1
- Initial build
