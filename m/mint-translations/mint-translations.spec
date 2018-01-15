Name:    mint-translations
Version: 2018.01.06
Release: alt1
License: GPLv2+ and MIT
Summary: Translation files for Linux Mint applications

Group:   Graphical desktop/GNOME
Url:     http://packages.linuxmint.com/pool/main/m/mint-translations/
Source:  http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%version.tar.xz

Source1: mint-translations.watch

BuildArch: noarch

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
* Mon Jan 15 2018 Andrey Cherepanov <cas@altlinux.org> 2018.01.06-alt1
- New version.

* Sat Nov 25 2017 Andrey Cherepanov <cas@altlinux.org> 2017.11.23-alt1
- New version.

* Wed Nov 15 2017 Andrey Cherepanov <cas@altlinux.org> 2017.11.12-alt1
- New version.

* Sun Nov 05 2017 Andrey Cherepanov <cas@altlinux.org> 2017.11.03-alt1
- New version

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 2017.06.28-alt1
- New version

* Thu May 25 2017 Andrey Cherepanov <cas@altlinux.org> 2017.05.23-alt1
- New version

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 2017.05.06-alt1
- New version

* Fri Dec 16 2016 Andrey Cherepanov <cas@altlinux.org> 2016.12.12-alt1
- New version

* Sat Nov 12 2016 Andrey Cherepanov <cas@altlinux.org> 2016.11.10-alt1
- New version

* Wed Jun 29 2016 Andrey Cherepanov <cas@altlinux.org> 2016.06.25-alt1
- New version

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
