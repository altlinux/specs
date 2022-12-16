Name: mednaffe
Version: 0.9.2
Release: alt1

Summary: A front-end (GUI) for mednafen emulator
License: GPL-3.0
Group: Other
Url: https://github.com/AmatCoder/mednaffe

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: libgtk+3-devel
Requires: mednafen
%description
Front-end (GUI) for mednafen emulator

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING ChangeLog README AUTHORS
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_pixmapsdir/%name.png

%changelog
* Fri Dec 16 2022 Artyom Bystrov <arbars@altlinux.org> 0.9.2-alt1
- Initial build for Sisyphus
