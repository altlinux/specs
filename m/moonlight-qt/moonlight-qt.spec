%define _unpackaged_files_terminate_build 1

Name:    moonlight-qt
Version: 6.1.0
Release: alt1
Summary: GameStream client for PCs (Windows, Mac, Linux, and Steam Link)
License: GPL-3.0
Group:   Other
Url:     https://moonlight-stream.org/
Vcs:     https://github.com/moonlight-stream/moonlight-qt.git

Source0: %name-%version.tar

Source1: %name-%version-moonlight-common-c.tar
Source2: %name-%version-h264bitstream.tar
Source3: %name-%version-qmdnsengine.tar
Source4: %name-%version-libsoundio.tar
Source5: %name-%version-SDL_GameControllerDB.tar
Source6: %name-%version-moonlight-common-c-enet.tar

BuildRequires(pre): rpm-macros-qt6
BuildRequires: qt6-tools
BuildRequires: qt6-base-devel qt6-declarative-devel qt6-svg-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: libopus-devel
BuildRequires: ffmpeg
BuildRequires: libEGL-devel
BuildRequires: libva-devel
BuildRequires: libvdpau-devel
BuildRequires: libswscale-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libavcodec-devel
BuildRequires: libssl-devel

Requires: libqt6-quickcontrols2basic 
Requires: libqt6-quickcontrols2basicstyleimpl 
Requires: libqt6-quickcontrols2material 
Requires: libqt6-quickcontrols2materialstyleimpl 
Requires: libqt6-quicklayouts

%description
%summary.

%prep
%setup -a1 -a2 -a3 -a4 -a5 -a6

%build
%qmake_qt6 moonlight-qt.pro PREFIX=%prefix
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc *.md
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*

%changelog
* Wed Feb 19 2025 Maxim Slipenko <maks1ms@altlinux.org> 6.1.0-alt1
- Initial build

