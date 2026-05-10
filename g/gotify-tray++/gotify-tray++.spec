Name: gotify-tray++
Version: 0.1.3
Release: alt1

Summary: A tray notification application for receiving messages from a Gotify server.
Summary(ru_RU.UTF-8): Программа для отображения пуш-уведомленй Gotify в системном лотке.

Group: Networking/Other
License: GPL-3.0-or-later
Url: https://github.com/seird/gotify-tray-cpp
VCS: https://github.com/seird/gotify-tray-cpp.git


Packager: Alexei Mezin <alexvm@altlinux.ru>

Source: %name-%version.tar.gz
Source1: %name.png
Source2: %name.desktop


Patch0: fix_server_path.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-qt6

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
#BuildRequires:  pkgconfig(Qt6Linguist)
#BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Widgets)
#BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  cmake
#BuildRequires:  awk

Requires:       icon-theme-hicolor

%description
A tray notification application for receiving messages from a Gotify server.

%description -l ru_RU.UTF-8
 Программа для отображения пуш-уведомленй Gotify в системном лотке.

%prep
%setup
%patch0 -p1

%build
%cmake 
%cmake_build 

%install
%cmake_install
install -m 755 -d %buildroot/%_iconsdir/hicolor/256x256/apps
install -m 644 %SOURCE1 %buildroot/%_iconsdir/hicolor/256x256/apps
desktop-file-install \
    --dir=%buildroot/%_desktopdir %SOURCE2

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%files
#%doc README.md gumbo-LICENSE.txt simplecrypt-LICENSE.txt
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Sun May 10 2026 Alexei Mezin <alexvm@altlinux.org> 0.1.3-alt1
- Initial build

