%def_enable qt5
%def_enable qt6

%define oname qtspell
Name: libqtspell
Version: 1.0.1
Release: alt1

Summary: Spell checking for Qt text widgets
License: GPLv3+
Group: Text tools

Url: https://github.com/manisandro/qtspell
# Source-url: https://github.com/manisandro/qtspell/archive/%version.tar.gz
Source: %oname-%version.tar
Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++ libenchant-devel
BuildRequires: doxygen graphviz

%if_enabled qt5
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
%endif

%if_enabled qt6
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
%endif

Requires: iso-codes

%description
QtSpell adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.


%package qt5
Group: Text tools
Summary: Spell checking for Qt5 text widgets

%description qt5
QtSpell adds spell-checking functionality to Qt5's text widgets, using the
enchant spell-checking library.

%package qt5-devel
Group: Text tools
Summary: Development files for %name-qt5
Requires: %name-qt5 = %version-%release

%description qt5-devel
The %name-qt5-devel package contains libraries and header files for
developing applications that use %name-qt5.

%package qt5-translations
Group: Text tools
Summary: Translations for %name-qt5
BuildArch: noarch
Requires: %name-qt5 = %version-%release
Requires: qt5-translations

%description qt5-translations
The %name-qt5-translations contains translations for %name-qt5.


%package qt6
Group: Text tools
Summary: Spell checking for Qt6 text widgets

%description qt6
QtSpell adds spell-checking functionality to Qt6's text widgets, using the
enchant spell-checking library.

%package qt6-devel
Group: Text tools
Summary: Development files for %name-qt6
Requires: %name-qt6 = %EVR

%description qt6-devel
The %name-qt6-devel package contains libraries and header files for
developing applications that use %name-qt6.

%package qt6-translations
Group: Text tools
Summary: Translations for %name-qt6
BuildArch: noarch
Requires: %name-qt6 = %EVR
Requires: qt6-translations

%description qt6-translations
The %name-qt6-translations contains translations for %name-qt6.


%package doc
Group: Text tools
Summary: Developer documentation for %name
BuildArch: noarch

%description doc
The %name-doc package contains the documentation for developing applications
that use %name.

%prep
%setup -n %oname-%version

%build
%ifarch %e2k
# lcc-1.23.12 sets -std=c++03 by default, not c++11
%add_optflags -std=c++11
%endif

%if_enabled qt5
%define _cmake__builddir build-qt5
%cmake -DQT_VER=5
%cmake_build
%cmake_build -t doc
%endif

%if_enabled qt6
%define _cmake__builddir build-qt6
%cmake -DQT_VER=6
%cmake_build
%cmake_build -t doc
%endif

%install
%if_enabled qt5
# install qt5 build
%define _cmake__builddir build-qt5
%cmake_install
%endif

%if_enabled qt6
# install qt6 build
%define _cmake__builddir build-qt6
%cmake_install
%endif

%if_enabled qt5
%files qt5
%doc COPYING
%_libdir/libqtspell-qt5.so.*

%files qt5-devel
%_includedir/QtSpell-qt5/
%_libdir/libqtspell-qt5.so
%_pkgconfigdir/QtSpell-qt5.pc

%files qt5-translations
%_qt5_translationdir/QtSpell_*.qm
%endif

%if_enabled qt6
%files qt6
%doc COPYING
%_libdir/libqtspell-qt6.so.*

%files qt6-devel
%_includedir/QtSpell-qt6/
%_libdir/libqtspell-qt6.so
%_pkgconfigdir/QtSpell-qt6.pc

%files qt6-translations
%_qt6_translationdir/QtSpell_*.qm
%endif

%files doc
%doc COPYING
%if_enabled qt6
%doc build-qt6/doc/html
%else
%doc build-qt5/doc/html
%endif

%changelog
* Thu Jun 05 2025 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1
- enable build Qt6 build

* Fri Nov 12 2021 Sergey V Turchin <zerg@altlinux.org> 0.8.5-alt3
- build without Qt4

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.8.5-alt2.1
- NMU: spec: adapted to new cmake macros.

* Wed May 08 2019 Michael Shigorin <mike@altlinux.org> 0.8.5-alt2
- E2K: explicit -std=c++11

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.8.5-alt1
- new version 0.8.5 (with rpmrb script)

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt1
- initial build for ALT Linux Sisyphus

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Sandro Mani <manisandro@gmail.com> - 0.7.4-1
- QtSpell 0.7.4

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Sandro Mani <manisandro@gmail.com> - 0.7.2-1
- QtSpell 0.7.2

* Mon Feb 09 2015 Sandro Mani <manisandro@gmail.com> - 0.7.1-1
- QtSpell 0.7.1

* Thu Feb 05 2015 Sandro Mani <manisandro@gmail.com> - 0.7.0-1
- QtSpell 0.7.0

* Sat Dec 27 2014 Sandro Mani <manisandro@gmail.com> - 0.6.0-1
- QtSpell 0.6.0

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 0.5.0-2
- Use %%license
- Add -Wl,--as-needed

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 0.5.0-1
- QtSpell 0.5.0
