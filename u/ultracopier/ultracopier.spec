Name:    ultracopier
Version: 3.0
Release: alt1

Summary: Ultracopier acts as a replacement for files copy dialogs
License: GPL-3.0
Group:   Other
URL:     http://ultracopier.first-world.info
VCS:     https://github.com/alphaonex86/Ultracopier

Source: %name-%version.tar
Patch0: %name-alt-QDebug-includes.patch

BuildRequires(pre): qt6-base-devel qt6-tools

%description
Ultracopier is free and open source software licensed under GPLv3 that acts as
a replacement for files copy dialogs.

Main features include:
* task queue
* pause / resume
* resume unfinished jobs
* dynamic speed limitation
* collision management
* plugin support

%prep
%setup
%patch0 -p1

%build
%qmake_qt6 %name.pro
%make_build
lrelease-qt6 %name.pro

%install
%install_qt6
install -Dpm0755 %name %buildroot%_bindir/%name
install -Dpm0644 resources/ultracopier-128x128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -Dpm0644 resources/ultracopier.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc *.md
%_bindir/%name
%_iconsdir/hicolor/128x128/apps/%name.png
%_desktopdir/%name.desktop

%changelog
* Thu Oct 09 2025 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- Initial build for Sisyphus.
