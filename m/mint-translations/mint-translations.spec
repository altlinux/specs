Name:           mint-translations
Version:        2015.02.25
Release:        alt1
License:        GPLv2+ and MIT
Summary:        Translation files for Linux Mint applications

Group:          Graphical desktop/GNOME
Url:            http://packages.linuxmint.com/pool/main/m/mintmenu/
# VCS:		https://github.com/linuxmint/mintmenu.git
Source:         http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%version.tar.gz

Source1:	mint-translations.watch

BuildArch:      noarch

%description
Translation files for Linux Mint applications.

%prep
%setup

%build
%make_build

%install
mkdir -p %buildroot%_datadir
cp -a usr/share/linuxmint/locale %buildroot%_datadir

%files
%doc README.md
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Fri Apr 24 2015 Andrey Cherepanov <cas@altlinux.org> 2015.02.25-alt1
- Initial build for ALT Linux
