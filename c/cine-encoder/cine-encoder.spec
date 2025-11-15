%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: cine-encoder
Version: 3.5.5
Release: alt1

Summary: Application for transcoding multimedia files
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/CineEncoder/cine-encoder

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: libmediainfo-devel

Requires: ffmpeg
Requires: mkvtoolnix

%description
Cine Encoder is an application that uses the FFmpeg, MKVToolNix and MediaInfo
utilities to convert media files while preserving HDR metadata.
Supported hardware encoding NVENC and Intel QSV (for Windows and experimental
for Linux). The following encoding modes are implemented: H265, H264, VP9,
MPEG-2, XDCAM, XAVC, DNxHR, ProRes.

%prep
%setup
sed -i '/^Version=/d' share/cine-encoder.desktop

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm644 share/cine-encoder.desktop -t %buildroot%_datadir/applications/
install -Dm644 share/cine-encoder.png -t %buildroot%_iconsdir/hicolor/64x64/apps/
install -Dm644 share/cine-encoder.wav -t %buildroot%_datadir/sounds/

%files
%doc AUTHORS LICENSE README.md images share/ABOUT
%_bindir/cine_encoder
%_desktopdir/cine-encoder.desktop
%_iconsdir/hicolor/64x64/apps/cine-encoder.png
%_datadir/sounds/cine-encoder.wav

%changelog
* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 3.5.5-alt1
- Initial build for Sisyphus
