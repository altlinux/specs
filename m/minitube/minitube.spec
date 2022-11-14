# SPEC file for Minitube
#

Name:     minitube
Version:  3.9.3
Release:  alt1.1

Summary: a YouTube desktop application

Group:    Video
License:  %gpl3plus
URL:      https://flavio.tordini.org/minitube
# URL: https://github.com/flaviotordini/minitube

Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Source1: submodules-%version.tar
Patch0:  %name-%version-%release.patch
# https://github.com/flaviotordini/minitube/issues/217
Patch1:  %name-fix-mpv-api-change.patch

BuildRequires(pre): rpm-build-licenses desktop-file-utils
BuildRequires(pre): rpm-macros-qt5

# Automatically added by buildreq on Fri Jul 09 2021
# optimized out: fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libcairo-gobject libcdio-paranoia libdc1394-22 libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-sql libqt5-widgets libqt5-x11extras librabbitmq-c libraw1394-11 libspirv-tools0 libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server libx265-199 libxcb-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel ruby ruby-stdlibs sh4
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel libmpv-devel qt5-phonon-devel qt5-script-devel qt5-svg-devel qt5-tools-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel
%ifnarch %e2k ppc64le
BuildRequires: qt5-webengine-devel
%endif

#BuildRequires: kf5-kwallet-devel libkwalletbackend5

%description
Minitube is a YouTube desktop application.

Minitube focuses on a pleasing overall experience, not on having
tons of features. Here's what Minitube can do:

- Channel subscriptions without using a YouTube account
- Compact mode: a small, always-on-top window
- Take video snapshots at full resolution
- Editable playlist: drag'n'drop and remove videos
- Stop after this video: "Last one, kids!"
- Sort videos by relevance, date, view count and rating
- Filter videos by publication date, video duration and quality
- Search by keyword, channel name or paste a YouTube link.
  Suggestions while typing.
- Remembers recent keywords and channels.
- YouTube categories: "Most Popular", "Music", "Games", etc.
- Related videos
- Fullscreen mode: mouse cursor, toolbar and playlist autohide
- Copy YouTube link to clipboard
- Share on Facebook, Twitter or via email
- Translated to more than 30 languages including German, French,
  Italian, Russian, Danish, Dutch, Spanish, Portuguese, Hebrew
  and Chinese.


%prep
%setup
%patch0 -p1

tar -x  -f %SOURCE1
%patch1 -p1

mv -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/COPYING) COPYING

%build
%qmake_qt5  PREFIX=%prefix
%make

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md TODO AUTHORS CHANGES
%doc --no-dereference COPYING

%_bindir/%name

%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.metainfo.xml
%_datadir/%name

%changelog
* Mon Nov 14 2022 L.A. Kostis <lakostis@altlinux.ru> 3.9.3-alt1.1
- NMU:
  + apply fix for libmpv2 compatibility.
  + BR: exclude qt5-webengine-devel for ppc64 too.

* Thu Feb 03 2022 Nikolay A. Fetisov <naf@altlinux.org> 3.9.3-alt1
- New version

* Fri Nov 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.9.2-alt1
- New version

* Tue Nov 16 2021 Michael Shigorin <mike@altlinux.org> 3.9-alt1.1
- E2K: avoid webengine for now (unavailable)

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.9-alt1
- Initial build for ALT Linux Sisyphus

