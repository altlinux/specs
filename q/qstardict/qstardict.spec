
Name: qstardict
Version: 2.0.2
Release: alt10

Group: System/Internationalization
Summary: QStarDict Qt clone of StarDict
License: GPL-3.0-or-later
Url: http://qstardict.ylsoftware.com

Requires: qt6-translations

Provides: stardict = 2.4.5
Provides: qstardict-kde5 = %EVR
Obsoletes: qstardict-kde5 < %EVR

Source: %name-%version.tar
Source10: qstardict-ru_RU.ts
Patch1: alt-l10n.patch
Patch2: alt-ftbfs.patch
Patch3: alt-qt6.patch
Patch4: alt-help-not-avail.patch

BuildRequires(pre): rpm-macros-qt6
BuildRequires: glib2-devel qt6-base-devel qt6-5compat-devel qt6-tools zlib-devel libzim-devel
BuildRequires: desktop-file-utils

%description
QStarDict is a dictionary application for learning foreign languages written
using Qt.

The main features:
* Support of Kiwix dictionaries
* Support of StarDict 2.x and 3.x dictionaries
* Background mode
* Showing translations for words selected by mouse in any application in
  a popup window
* Pronuncation of words

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#cat %SOURCE10 > translations/qstardict-ru_RU.ts

%build
%qmake_qt6 \
    PLUGINS_DIR=%_libdir/%name/plugins \
    DOCS_DIR=%_datadir/%name/docs \
    #
%make

%install
%install_qt6

LC_ALL=en_US.UTF-8 desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=TextTools \
	--add-category=Office \
	--set-key="Comment[ru]" \
	--set-value="Qt-версия словаря StarDict" \
	%buildroot%_desktopdir/qstardict.desktop

%find_lang %name --all-name --with-qt

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog THANKS
%_bindir/%name
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/docs/
%_desktopdir/*.desktop
%_datadir/pixmaps/qstardict.*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins/
%_libdir/%name/plugins/*.so

%changelog
* Wed Nov 13 2024 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt10
- port to Qt6

* Tue Nov 12 2024 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version
- fix FTBFS (closes: 51994)

* Mon Oct 09 2023 Sergey V Turchin <zerg@altlinux.org> 1.4-alt1
- new version

* Wed Jul 10 2019 Sergey V Turchin <zerg@altlinux.org> 1.3-alt1
- new version

* Mon Apr 08 2019 Sergey V Turchin <zerg@altlinux.org> 1.2-alt4
- update russian translation

* Fri Apr 05 2019 Sergey V Turchin <zerg@altlinux.org> 1.2-alt3
- fix desktop-file translation

* Fri Apr 05 2019 Sergey V Turchin <zerg@altlinux.org> 1.2-alt2
- fix load Qt translation

* Mon Dec 18 2017 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Mon May 28 2012 Terechkov Evgenii <evg@altlinux.org> 1.0.1-alt1
- 1.0.1

* Fri Apr 27 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1.2
- rebuilt with rpm optflags

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.1
- Fixed build with new glib2

* Thu Jul  7 2011 Terechkov Evgenii <evg@altlinux.org> 1.0-alt1
- 1.0

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.13.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qstardict

* Fri May  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt2
- Build with gcc4.4 fixed

* Wed Feb 25 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt1.1
- Provide: stardict added (closes #18960)

* Fri Feb 20 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13.1-alt1
- 0.13.1

* Sun Feb  8 2009 Terechkov Evgenii <evg@altlinux.ru> 0.13-alt1
- 0.13

* Sat Jun 14 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12.9-alt1.1
- Build for x86_64 fixed (brain-deat upstream defaults)

* Fri Jun 13 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12.9-alt1
- 0.12.9

* Sat Mar 29 2008 Terechkov Evgenii <evg@altlinux.ru> 0.12-alt1
- 0.12

* Wed Mar 26 2008 Terechkov Evgenii <evg@altlinux.ru> 0.10-alt1
- 0.10

* Sun Mar 23 2008 Terechkov Evgenii <evg@altlinux.ru> 0.09-alt1
- 0.09

* Sat Sep 22 2007 Terechkov Evgenii <evg@altlinux.ru> 0.07-alt1
- 0.07
- License changed to GPLv2 (package relicensed)

* Tue Aug 14 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1.2
- Wrong Provides: tag removed (Shame on me!)

* Fri Aug 10 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1.1
- gpl3 changed to gpl3plus (due change to rpm-build-licenses)

* Sat Jul 28 2007 Terechkov Evgenii <evg@altlinux.ru> 0.04-alt1
- 0.04

* Sun Jul  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.03-alt2
- "Fix" conflict with stardict-gtk (see #12267,#12268) by providing stardict=2.4.2

* Sun Jul  8 2007 Terechkov Evgenii <evg@altlinux.ru> 0.03-alt1
- Initial build for Sisyphus
