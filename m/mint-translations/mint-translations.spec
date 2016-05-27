Name:           mint-translations
Version:        2016.05.24
Release:        alt1
License:        GPLv2+ and MIT
Summary:        Translation files for Linux Mint applications

Group:          Graphical desktop/GNOME
Url:            http://packages.linuxmint.com/pool/main/m/mint-translations/
Source:         http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%version.tar.xz

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
* Fri May 27 2016 Andrey Cherepanov <cas@altlinux.org> 2016.05.24-alt1
- New version

* Tue Apr 26 2016 Andrey Cherepanov <cas@altlinux.org> 2016.04.21-alt1
- New version
- Tarball now uses xz compression

* Thu Dec 03 2015 Andrey Cherepanov <cas@altlinux.org> 2015.11.28-alt1
- New version

* Tue Nov 17 2015 Andrey Cherepanov <cas@altlinux.org> 2015.11.13-alt1
- New version

* Mon Nov 09 2015 Andrey Cherepanov <cas@altlinux.org> 2015.11.06-alt1
- New version

* Sun Jun 28 2015 Andrey Cherepanov <cas@altlinux.org> 2015.06.26-alt1
- New version

* Fri Jun 05 2015 Andrey Cherepanov <cas@altlinux.org> 2015.06.02-alt1
- New version

* Fri Apr 24 2015 Andrey Cherepanov <cas@altlinux.org> 2015.02.25-alt1
- Initial build for ALT Linux
