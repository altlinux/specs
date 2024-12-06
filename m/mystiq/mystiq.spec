Name: mystiq
Version: 24.12.01
Release: alt1

Summary: Audio/Video converter
License: GPLv3
Group: Video

Url: https://mystiqapp.com/
Vcs: https://github.com/biglinux/MystiQ/
Source: MystiQ-%version.tar.gz

BuildRequires: qt6-charts-devel qt6-declarative-devel qt6-multimedia-devel qt6-svg-devel qt6-tools-devel
BuildRequires: extra-cmake-modules
BuildRequires: libnotify-devel

Requires: /usr/bin/ffmpeg /usr/bin/ffprobe /usr/bin/sox
Requires: icon-theme-hicolor

%description
MystiQ is a GUI for FFmpeg, a powerful media converter.
FFmpeg can read audio and video files in various
formats and convert them into other formats.
MystiQ features an intuitive graphical
interface and a rich set of presets to help you
convert media files within a few clicks.
Advanced users can also adjust conversion parameters in detail.

%prep
%setup -n MystiQ-%version
chmod -x mystiq.desktop icons/mystiq.svg

%build
lrelease-qt6 *.pro
qmake-qt6 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" PREFIX=%prefix DEFINES+=NO_NEW_VERSION_CHECK
%ifarch %e2k
# unsupported as of lcc 1.25.15
sed -i 's,-fno-fat-lto-objects,,' Makefile
%endif
%make_build USE_LIBNOTIFY=1

%install
sed -i 's/strip$/echo/' Makefile
make INSTALL_ROOT=%buildroot install

%files
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/%name
%_datadir/metainfo/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/*.desktop
%_man1dir/*

%changelog
* Fri Dec 06 2024 Andrew A. Vasilyev <andy@altlinux.org> 24.12.01-alt1
- 24.12.01
- build with Qt6

* Wed Jul 31 2024 Andrew A. Vasilyev <andy@altlinux.org> 24.06.15-alt1
- 24.06.15

* Wed Mar 13 2024 Andrew A. Vasilyev <andy@altlinux.org> 23.05.15-alt1
- 23.05.15 (ALT #49494)

* Fri May 14 2021 Michael Shigorin <mike@altlinux.org> 20.03.23-alt2
- E2K: avoid lcc-unsupported option

* Fri May 01 2020 Motsyo Gennadi <drool@altlinux.ru> 20.03.23-alt1
- initial build
