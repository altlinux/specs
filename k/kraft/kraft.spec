Name: kraft
Version: 1.0
Release: alt1

Summary: Kraft - Software for small business
Summary(ru_RU.UTF-8): Kraft — программное обеспечение для малого бизнеса
License: GPL-2.0
Group: Office
# VCS: https://github.com/dragotin/kraft
URL: http://www.volle-kraft-voraus.de/

Requires: kde5-akonadi

Source0: kraft-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires(pre): rpm-build-python3
BuildRequires: extra-cmake-modules gcc-c++
BuildRequires: qt5-declarative-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kcontacts-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: libctemplate-devel
BuildRequires: grantlee5-devel
BuildRequires: qt5-svg-devel

%py3_requires reportlab

%description
Kraft is free software to help to handle documents like quotes and invoices in
your small business.

%prep
%setup -q -n %name-%version
subst 's|LIBRARY DESTINATION lib/kraft|LIBRARY DESTINATION ${LIB_INSTALL_DIR}|' src/CMakeLists.txt

%build
%K5init no_altplace
%K5build -DCMAKE_SKIP_RPATH=1

%install
%K5install
%find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS README.md TODO Changes.txt
%_bindir/*
%_datadir/%name
%_K5cfg/*
%_K5xdgapp/*.desktop
%_iconsdir/*/*/*/*.svg
%_iconsdir/hicolor/scalable/apps/%name.svg
%_K5xmlgui/%name
%_datadir/metainfo/*.appdata.xml

%changelog 
* Sun Dec 18 2022 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- New version.

* Sun Sep 04 2022 Andrey Cherepanov <cas@altlinux.org> 0.98-alt1
- New version.

* Thu Jan 27 2022 Andrey Cherepanov <cas@altlinux.org> 0.97-alt1
- New version.

* Mon Aug 09 2021 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt3
- NMU: fix requires (libctemplate is linked, trmltools is not used)

* Wed Jun 30 2021 Sergey V Turchin <zerg@altlinux.org> 0.96-alt2
- fix requires (ALT #40014)

* Mon May 17 2021 Andrey Cherepanov <cas@altlinux.org> 0.96-alt1
- New version (from upstream git tag).
- Build with Qt5/KF5 (ALT #40014).
- Fix License tag according to SPDX.

* Thu Mar 05 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.58-alt3
- Porting to python3.

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.58-alt2
- Build without Nepomuk support

* Sat Oct 03 2015 Andrey Cherepanov <cas@altlinux.org> 0.58-alt1
- New version 0.58
- Fix l10n build in cmake

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.55-alt1.1
- Rebuilt with new ctemplate

* Fri Jul 18 2014 Andrey Cherepanov <cas@altlinux.org> 0.55-alt1
- New version
- Application strictly requires Akonadi for work

* Tue Nov 26 2013 Andrey Cherepanov <cas@altlinux.org> 0.53-alt1
- new version 0.53

* Wed Mar 06 2013 Andrey Cherepanov <cas@altlinux.org> 0.50-alt1
- New version 0.50

* Fri Jun 08 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.45-alt2
- Fix build with RPATH: replace internal library to libdir
- Update package files list

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.30-alt4.1
- Removed bad RPATH

* Tue Jan 17 2012 Andrey Cherepanov <cas@altlinux.org> 0.45-alt1
- New version 0.45
- Build with new ctemplate

* Tue Feb 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.30-alt4
- Fix build

* Thu Dec 25 2008 Andrey Cherepanov <cas@altlinux.org> 0.30-alt3
- Fix dependence on renamed google-ctemplate

* Thu Dec 04 2008 Andrey Cherepanov <cas@altlinux.org> 0.30-alt2
- Fix python-module-Reportlab dependence

* Fri Nov 21 2008 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1
- Initial release

