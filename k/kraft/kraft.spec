
Name:           kraft
Version:        0.58
Release:        alt2

Summary:        Kraft - Software for small business
Summary(ru_RU.UTF-8): Kraft — программное обеспечение для малого бизнеса
License:        GPL, LGPL
Group:          Office
URL:            http://www.volle-kraft-voraus.de/

Source0:        kraft-%{version}.tar.bz2
Patch:		kraft-fix-l10n-build-with-cmake.patch

BuildRequires(pre): kde4libs-devel
BuildRequires: 	gcc-c++
BuildRequires:  cmake
BuildRequires:  kde4pimlibs-devel
BuildRequires:  libctemplate-devel

Requires: 	libctemplate python-module-Reportlab trmltools
Requires:	akonadi

%description
Kraft is software for helping people drinving small businesses
in their daily communication with customers.

Authors:
--------
    Klaas Freitag <freitag@kde.org>

%prep
%setup -q -n %name-%version
%patch -p2

%build
sed -iorig 's|LIBRARY DESTINATION lib/kraft|LIBRARY DESTINATION ${LIB_INSTALL_DIR}|' src/CMakeLists.txt
%K4build -DCMAKE_SKIP_RPATH=1

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS COPYING INSTALL README TODO
%_bindir/*
%_K4datadir/apps/*
%_K4xdg_apps/*
%_K4cfg/*
%_iconsdir/*/*/*/*.png

%changelog 
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

