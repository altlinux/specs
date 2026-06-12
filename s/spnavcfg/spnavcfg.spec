Name:    spnavcfg
Version: 1.3
Release: alt1

Summary: Spacenav interactive configuration GUI
License: GPL-3.0
Group:   System/Configuration/Hardware
Url:     https://github.com/FreeSpacenav/spnavcfg

Source: %name-%version.tar

BuildRequires: gcc-c++ qt6-base-devel libspnav-devel
Requires: spacenavd

%description
%summary

%prep
%setup

%build
%configure --disable-debug
%make_build src/ui.moc.o
%make_build
strip spnavcfg

%install
%makeinstall_std

%files
%doc COPYING README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 1.3-alt1
- new version 1.3

* Fri Mar 21 2025 Sergey Palcheh <minergenon@altlinux.org> 1.1-alt1
- Initial build for Sisyphus

