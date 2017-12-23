%define _qt4_translationdir %_datadir/qt4/translations

%define oname qtspell
Name: libqtspell
Version: 0.8.4
Release: alt1

Summary: Spell checking for Qt text widgets

License: GPLv3+
Group: Text tools
Url: https://github.com/manisandro/qtspell

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/manisandro/qtspell/archive/%version.tar.gz
Source: %oname-%version.tar

# manually removed: i586-libxcb libfreetype-infinality libqt4-sql-interbase libqt4-sql-mysql libqt4-sql-odbc libqt4-sql-postgresql libqt4-sql-sqlite2 libqt4-webkit-devel phonon-devel python3 python3-module-zope qt4-designer qt5-imageformats qt5-tools-devel ruby ruby-stdlibs
# Automatically added by buildreq on Sat Aug 15 2015
# optimized out: cmake cmake-modules fontconfig glib2-devel libEGL-devel libGL-devel libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt5-core libqt5-gui libqt5-widgets libqt5-xml libstdc++-devel pkg-config python3-base qt5-base-devel qt5-tools
BuildRequires: ccmake doxygen gcc-c++ graphviz libenchant-devel

BuildRequires: cmake
BuildRequires: libqt4-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel

Requires: iso-codes

%description
QtSpell adds spell-checking functionality to Qt's text widgets, using the
enchant spell-checking library.

%package qt4
Group: Text tools
Summary: Spell checking for Qt4 text widgets

%description qt4
QtSpell adds spell-checking functionality to Qt4's text widgets, using the
enchant spell-checking library.

%package qt4-devel
Group: Text tools
Summary: Development files for %name-qt4
Requires: %name-qt4 = %version-%release

%description qt4-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

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
%cmake -DUSE_QT5=OFF
%cmake_build
%cmake_build doc
mv BUILD build-qt4

%cmake -DUSE_QT5=ON
%cmake_build
mv BUILD build-qt5

%install
# install qt4 build
rm -rf BUILD
cp -al build-qt4 BUILD
%cmakeinstall_std

# install qt5 build
rm -rf BUILD
cp -al build-qt5 BUILD
%cmakeinstall_std

%files qt4
%doc COPYING
%_libdir/libqtspell-qt4.so.*
%_qt4_translationdir/QtSpell_*.qm

%files qt4-devel
%_includedir/QtSpell-qt4/
%_libdir/libqtspell-qt4.so
%_pkgconfigdir/QtSpell-qt4.pc

%files qt5
%doc COPYING
%_libdir/libqtspell-qt5.so.*

%files qt5-devel
%_includedir/QtSpell-qt5/
%_libdir/libqtspell-qt5.so
%_pkgconfigdir/QtSpell-qt5.pc

%files qt5-translations
%_qt5_translationdir/QtSpell_*.qm

%files doc
%doc COPYING
%doc build-qt4/doc/html

%changelog
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
