Name: basic256
Version: 2.0.0.11
Release: alt2.1
Summary: Simple BASIC IDE that allows young children to learn to programming
License: GPL-2.0+
Group: Development/Other
URL: http://basic256.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: http://ovh.dl.sourceforge.net/sourceforge/kidbasic/%name-%version.tar.gz
Source1: basic256.desktop
Source2: basic256_ru.ts

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-serialport-devel
BuildRequires: qt5-tools
BuildRequires: libespeak-ng-devel
BuildRequires: libSDL-devel
BuildRequires: libSDL_mixer-devel
BuildRequires: libsqlite3-devel
BuildRequires: flex
BuildRequires: bison

%description
BASIC-256 is a simple BASIC IDE that allows young children to learn to program.
It was written in response to David Brin's article, "Why Johnny Can't Code,"
in which he bemoans the lack of a simple, line-oriented programming language
for children that runs on modern computers. It features a byte-code compiler
and interpreter, a debugger, easy to use graphical and text output, and an
editor.

%prep
%setup
install -Dpm0644 %SOURCE2 Translations/basic256_ru.ts
lupdate-qt5 *.pro

%build
%add_optflags -I%_includedir/espeak
qmake-qt5
%make_build CXXFLAGS="%optflags \$(DEFINES)"
lrelease-qt5 Translations/*.ts

%install
mkdir -p %buildroot
%make_install INSTALL_ROOT=%buildroot install
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dpm0644 resources/icons/basic256.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

%files
%doc CONTRIBUTORS
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
* Tue Jun 11 2024 Artem Semenov <savoptik@altlinux.org> 2.0.0.11-alt2.1
- Changed espeak to espeak-ng

* Thu Jun 24 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0.11-alt2
- Complete Russian translations (thanks Olesya Gerasimenko).

* Tue Jun 22 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0.11-alt1
- New version.

* Wed May 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt8
- Fix executable name in dekstop file

* Mon May 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt7
- Fix localization of desktop file
- Fix license
- Fix build with new gcc

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.9.6-alt6.1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt6.1
- Fixed build with glibc 2.16

* Mon Jan 10 2011 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt6
- Updated to 0.9.6.58.

* Mon Dec 20 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt5
- Check and correct the syntax highlighting keywords
- Added buttons back, forward, home, exit - in the help window

* Wed Dec 15 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt4
- Updated to 0.9.6.53.
- Fixed Group and CXXFLAGS.
- Make new patch for say function.

* Sun Dec 12 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt3
- Updated to 0.9.6.51 - add sqr() and exp() functions.
- Help files (ru|en) updated.

* Fri Dec 03 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt2
- Updated to 0.9.6.49.
- Russian translation and help files (ru|en) updated.

* Thu Nov 04 2010 Sergey Irupin <lamp@altlinux.org> 0.9.6-alt1
- Updated to 0.9.6w.
- Russian translation updated.
- Fixed locale problem and seek, lower, upper statements.
- Change help system and add russian help.
- Change some icons toolbar.

* Sat Apr 10 2010 Sergey Irupin <lamp@altlinux.org> 0.9.5-alt1
- Updated to 0.9.5.
- Russian translation updated.

* Tue Sep 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt4
- Fixed build.

* Sat Mar 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt3
- Packaged examples.

* Sat Mar 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt2
- Enable non-ASCII strings.
- Added .desktop file.

* Fri Mar 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.9.2-alt1
- Initial build for ALT Linux.
- Russian translation added.
- Search for translation in %%_datadir/%%name.
