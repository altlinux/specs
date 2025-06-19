Name:    spnavcfg
Version: 1.1
Release: alt1

Summary: Spacenav interactive configuration GUI
License: GPL-3.0
Group:   System/Configuration/Hardware
Url:     https://github.com/FreeSpacenav/spnavcfg

Source: %name-%version.tar

BuildRequires: gcc-c++ qt5-base-devel libspnav-devel
Requires: spacenavd

%description
%summary

%prep
%setup

%build
%configure --disable-debug
%make_build UIC=uic-qt5 MOC=moc-qt5 RCC=rcc-qt5 src/ui.moc.o # work around Makefile glitch
%make_build UIC=uic-qt5 MOC=moc-qt5 RCC=rcc-qt5
strip spnavcfg

%install
%makeinstall_std

%files
%doc COPYING README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Fri Mar 21 2025 Sergey Palcheh <minergenon@altlinux.org> 1.1-alt1
- Initial build for Sisyphus

