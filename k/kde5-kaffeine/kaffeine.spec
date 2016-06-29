
%define rname kaffeine
Name: kde5-%rname
Version: 2.0.3
Release: alt2
%K5init

Group: Video
Summary: Multimedia Player
Url: http://kaffeine.sourceforge.net/
License: GPLv2

Provides: kaffeine = %version-%release
#Requires: qt5-sql-sqlite

Requires: vlc-mini
Requires: vlc-plugin-alsa
Requires: vlc-plugin-pulseaudio
Requires: vlc-plugin-ffmpeg
Requires: vlc-plugin-flac
Requires: vlc-plugin-mpeg2
Requires: vlc-plugin-ogg
Requires: vlc-plugin-dvdnav
Requires: vlc-plugin-dvdread
Requires: vlc-plugin-audiocd
Requires: vlc-plugin-v4l
Requires: vlc-plugin-xcb
Requires: vlc-plugin-ts
Requires: vlc-plugin-live555
Requires: vlc-plugin-smb
Requires: vlc-plugin-xml
Requires: vlc-plugin-dbus
Requires: vlc-plugin-taglib

Source0: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-x11extras-devel
BuildRequires: libXres-devel
BuildRequires: libv4l-devel libvlc-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel
BuildRequires: kf5-kdbusaddons-devel kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Kaffeine provides fast access to the most important media sources.
It also handles Video CDs, DVDs, and DVB cards.

%prep
%setup -q -n %rname-%version

%build
%K5build


%install
%K5install
%K5install_move data kaffeine profiles solid
%find_lang --with-kde %rname


%files -f %rname.lang
%doc Changelog NOTES
%_K5bin/kaffeine
%_K5bin/dtvdaemon
%_K5data/kaffeine/
%_K5icon/hicolor/*/*/*.*
#%_K5icon/oxygen/*/*/*.*
%_K5data/solid/actions/kaffeine_*.desktop
%_K5data/profiles/kaffeine.profile.xml
%_K5xdgapp/org.kde.kaffeine.desktop

%changelog
* Wed Jun 29 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt2
- fix provides, build requires

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt1
- initial build

