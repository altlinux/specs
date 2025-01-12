# Qt6WebEngineCore is only available on those architectures
ExclusiveArch: x86_64 aarch64

Name: rssguard
Version: 4.8.1
Release: alt2

Summary: RSS Guard is a simple RSS/ATOM feed reader
Summary(ru_RU.UTF-8): RSS Guard - программа для чтения RSS/ATOM 

Group: Networking/News
License: GPL-3.0-or-later
Url: https://github.com/martinrotter/rssguard
VCS: https://github.com/martinrotter/rssguard

Packager: Alexei Mezin <alexvm@altlinux.ru>

Source: %name-%version.tar.gz

BuildPreReq: rpm-macros-cmake rpm-macros-qt6

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  cmake


Requires:       icon-theme-hicolor

%description
RSS Guard is a simple RSS/ATOM feed reader for Windows, Linux, BSD, OS/2 or macOS which can work with RSS/ATOM/JSON/iCalendar/Sitemap feeds as well as many online feed services:

* Feedly
* Gmail
* Google Reader API (Bazqux, FreshRSS, Inoreader, Miniflux, Reedah, The Old Reader and more)
* Nextcloud News
* Tiny Tiny RSS
* RSS Guard is also podcast player as it can play everything via its built-in mpv-based (or ffmpeg-based) media player.

Also, RSS Guard has built-in support for Gemini protocol and hypertext format, so it can very well act as reliable cross-platform Gemini client!


%description -l ru_RU.UTF-8
RSS Guard это программа для чтения новостных лент в формате RSS/ATOM/JSON/iCalendar/Sitemap и онлайн-сервисов:

* Feedly
* Gmail
* Google Reader API (Bazqux, FreshRSS, Inoreader, Miniflux, Reedah, The Old Reader и других)
* Nextcloud News
* Tiny Tiny RSS

RSS Guard умеет проигрывать подкасты встроенным mpv- или ffmpeg-плеером.

Так же RSS Guard поддерживает протокол Gemini.

%prep
%setup

%build
%cmake -DBUILD_WITH_QT6=1 -DNO_UPDATE_CHECK=1
%cmake_build 

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.rssguard.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.rssguard.metainfo.xml

%files
%doc README.md
%_bindir/%name
%_libdir/lib%name.so
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml
# plugins ???
%_libdir/%name/*

%changelog
* Sun Jan 12 2025 Alexei Mezin <alexvm@altlinux.org> 4.8.1-alt2
- Disable build on architectures without QtWebEngineCore

* Sun Jan 12 2025 Alexei Mezin <alexvm@altlinux.org> 4.8.1-alt1
- Initial build



