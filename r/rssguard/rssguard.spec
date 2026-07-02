
Name: rssguard
Version: 5.2.1
Release: alt1

Summary: RSS Guard is a simple RSS/ATOM feed reader
Summary(ru_RU.UTF-8): RSS Guard - программа для чтения RSS/ATOM

Group: Networking/News
License: GPL-3.0-or-later
Url: https://github.com/martinrotter/rssguard
VCS: https://github.com/martinrotter/rssguard


# probably should manually remove mips64el??? (no GO support)
ExclusiveArch: %qt6_qtwebengine_arches

Packager: Alexei Mezin <alexvm@altlinux.ru>

Source: %name-%version.tar.gz
Source1: 3rd-party.tar.gz
Source2: go-vendor.tar.gz

BuildRequires(pre): rpm-macros-cmake rpm-macros-qt6 rpm-macros-golang rpm-macros-qt6-webengine

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  golang
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
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  cmake
BuildRequires:  awk


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

Также RSS Guard поддерживает протокол Gemini.

%prep
%setup
# Add additional vendored sources
tar zxf %SOURCE1 -C src/librssguard
# Preserve libraries licenses
cp src/librssguard/3rd-party/gumbo/doc/COPYING gumbo-LICENSE.txt
awk '/\/\*/{flag=1; next} /\*\//{flag=0; exit} flag' src/librssguard/3rd-party/sc/simplecrypt.h > simplecrypt-LICENSE.txt


# add Go vendored sources
tar zxf %SOURCE2 -C resources/scripts/standalone/article-extractor


%build
%cmake -DBUILD_WITH_QT6=1 -DNO_UPDATE_CHECK=1
%cmake_build 

%install
%cmake_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.rssguard.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.rssguard.metainfo.xml

%files
%doc README.md gumbo-LICENSE.txt simplecrypt-LICENSE.txt
%_bindir/%name
%_libdir/lib%name.so
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.xml
# plugins ???
%_libdir/%name/*

%changelog
* Fri Jul 03 2026 Alexei Mezin <alexvm@altlinux.org> 5.2.1-alt1
- New version

* Mon May 11 2026 Alexei Mezin <alexvm@altlinux.org> 5.1.2-alt1
- New version

* Sat May 09 2026 Alexei Mezin <alexvm@altlinux.org> 5.1.1-alt1
- New version
  * Reintroduce QtWebEngine support

* Sat Mar 14 2026 Alexei Mezin <alexvm@altlinux.org> 5.0.4-alt1
- New version

* Sat Feb 28 2026 Alexei Mezin <alexvm@altlinux.org> 5.0.0-alt1
- New vesrion: major version upgrade!
  * No more QtWebEngine dependency!

* Sat Sep 13 2025 Alexei Mezin <alexvm@altlinux.org> 4.8.6-alt1
- New version

* Tue Jun 10 2025 Alexei Mezin <alexvm@altlinux.org> 4.8.5-alt1
- New version

* Sun Apr 06 2025 Alexei Mezin <alexvm@altlinux.org> 4.8.3-alt1
- New version

* Mon Jan 13 2025 Ivan A. Melnikov <iv@altlinux.org> 4.8.1-alt2.1
- NMU: Use rpm-macros-qt6-webengine to detect Qt6WebEngineCore
  presence (adds loongarch64 support)

* Sun Jan 12 2025 Alexei Mezin <alexvm@altlinux.org> 4.8.1-alt2
- Disable build on architectures without QtWebEngineCore

* Sun Jan 12 2025 Alexei Mezin <alexvm@altlinux.org> 4.8.1-alt1
- Initial build



