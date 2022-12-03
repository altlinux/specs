Name:    mint-translations
Version: 2022.12.02
Release: alt1

License: GPL-2.0+ and MIT
Summary: Translation files for Linux Mint applications

Group:   Graphical desktop/GNOME
Url:     http://packages.linuxmint.com/pool/main/m/mint-translations/
Source:  http://packages.linuxmint.com/pool/main/m/mint-translations/mint-translations_%version.tar.xz

Source1: mint-translations.watch
Patch: mintmenu-ru-with-menubutton-l10n.patch

BuildArch: noarch

%description
Translation files for Linux Mint applications.

%prep
%setup
%patch -p2

%build
%make_build

%install
mkdir -p %buildroot%_datadir
cp -a usr/share/linuxmint/locale %buildroot%_datadir

%files
%doc README.md
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Sat Dec 03 2022 Andrey Cherepanov <cas@altlinux.org> 2022.12.02-alt1
- New version.

* Mon Jul 25 2022 Andrey Cherepanov <cas@altlinux.org> 2022.07.24-alt1
- New version.

* Wed Jun 29 2022 Andrey Cherepanov <cas@altlinux.org> 2022.06.27-alt1
- New version.

* Sat Jan 01 2022 Andrey Cherepanov <cas@altlinux.org> 2021.12.31-alt1
- New version.

* Tue Dec 07 2021 Andrey Cherepanov <cas@altlinux.org> 2021.12.06-alt1
- New version.

* Sun Jun 27 2021 Andrey Cherepanov <cas@altlinux.org> 2021.06.25-alt1
- New version.

* Sat Jun 12 2021 Andrey Cherepanov <cas@altlinux.org> 2021.06.10-alt1
- New version.

* Mon Jan 04 2021 Andrey Cherepanov <cas@altlinux.org> 2021.01.02-alt1
- New version.

* Sun Dec 13 2020 Andrey Cherepanov <cas@altlinux.org> 2020.12.13-alt1
- New version.

* Fri Jun 26 2020 Andrey Cherepanov <cas@altlinux.org> 2020.06.24-alt1
- New version.

* Fri Jun 19 2020 Andrey Cherepanov <cas@altlinux.org> 2020.06.17-alt1
- New version.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 2020.05.12-alt1
- New version.
- Fix License tag according to SPDX.

* Wed Jan 08 2020 Andrey Cherepanov <cas@altlinux.org> 2020.01.06-alt1
- New version.

* Fri Dec 13 2019 Andrey Cherepanov <cas@altlinux.org> 2019.12.11-alt1
- New version.

* Mon Dec 02 2019 Andrey Cherepanov <cas@altlinux.org> 2019.11.26-alt1
- New version.

* Fri Aug 02 2019 Andrey Cherepanov <cas@altlinux.org> 2019.07.28-alt1
- New version.

* Fri Jul 12 2019 Andrey Cherepanov <cas@altlinux.org> 2019.07.10-alt1
- New version.

* Thu Dec 13 2018 Andrey Cherepanov <cas@altlinux.org> 2018.12.11-alt1
- New version.

* Fri Nov 30 2018 Andrey Cherepanov <cas@altlinux.org> 2018.11.27-alt1
- New version.

* Mon Aug 20 2018 Andrey Cherepanov <cas@altlinux.org> 2018.08.14-alt1
- New version.

* Sun Jul 01 2018 Andrey Cherepanov <cas@altlinux.org> 2018.06.26-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 2018.05.22-alt1
- New version.

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 2018.01.06-alt2
- Add Russian translation of menubutton of mintmenu.

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
