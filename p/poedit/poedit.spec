# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: poedit
Version: 1.4.6.1
Release: alt2

Summary: Cross-platform translation files editor
Summary(ru_RU.CP1251): Кроссплатформенный редактор файлов переводов
License: MIT
Url: http://www.poedit.net/
Group: Editors
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://prdownloads.sourceforge.net/poedit/%name-%version.tar.gz

Requires: gettext-tools
BuildPreReq: desktop-file-utils
BuildRequires: gcc-c++ wxGTK-devel libdb4-devel libgtkspell-devel

%description
This program is GUI frontend to GNU Gettext utilities and catalogs
editor/source code parser. It helps with translating application into
another language. For details on principles of the solution used, see
GNU Gettext documentation or wxWindows' wxLocale class reference.

%description -l ru_RU.CP1251
Эта программа является оболочкой для утилит GNU Gettext. С её помощью
удобно переводить сообщения приложений на разные языки. Более подробно
принципы работы описаны в документации для GNU Gettext и класса
wxLocale библиотеки wxWindows.

%prep
%setup

%build
%configure
%make_build --silent --no-print-directory

%install
%makeinstall_std --silent --no-print-directory
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/%name
%_man1dir/%name.1.*
%_datadir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Sun Sep 05 2010 Slava Semushin <php-coder@altlinux.ru> 1.4.6.1-alt2
- Added gettext-tools to Requires (Closes: #24017)

* Sun May 23 2010 Slava Semushin <php-coder@altlinux.ru> 1.4.6.1-alt1
- Updated to 1.4.6.1

* Wed Feb 10 2010 Slava Semushin <php-coder@altlinux.ru> 1.4.5-alt1
- Updated to 1.4.5

* Sun Sep 20 2009 Slava Semushin <php-coder@altlinux.ru> 1.4.3-alt1
- Updated to 1.4.3
- Fixed Exec entry in desktop file (noted by repocop)

* Wed Aug 26 2009 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt4
- Rebuild (again) with wxGTK to fix crash after start (Closes: #21187)

* Sat Aug 22 2009 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt3
- Rebuild with wxGTK to fix crash after start (Closes: #21187)

* Sat Dec 13 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt2
- Partially fixed desktop file (noted by repocop)
- Removed obsolete %%update_menus/%%update_desktopdb calls (noted by repocop)

* Mon Sep 08 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.2-alt1
- Updated to 1.4.2

* Thu Jun 19 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.1-alt2
- Rebuilt with libdb4.7

* Wed Apr 09 2008 Slava Semushin <php-coder@altlinux.ru> 1.4.1-alt1
- Updated to 1.4.1 version

* Thu Mar 13 2008 Slava Semushin <php-coder@altlinux.ru> 1.4-alt1
- Updated to 1.4 version
- Removed desktop-file-utils from post and postun Requires
- Running make with --no-print-directory and --silent options

* Wed Dec 19 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.9-alt1
- Updated to 1.3.9 version (bugfix release for MacOS X)

* Tue Dec 11 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.8-alt1
- Updated to 1.3.8 version

* Sat Oct 20 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.7-alt2
- Rebuilt with wxWidgets 2.8
- Really updated Url tag

* Sat Jul 21 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.7-alt1
- Updated to 1.3.7 version
- Updated Url tag
- Spec cleanup:
  + s/%%setup -q/%%setup/
  + Removed trailing space in %%changelog

* Tue Jan 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3.6-alt1.1
- NMU based on php-coder@ spec.

* Tue Jan 16 2007 Slava Semushin <php-coder@altlinux.ru> 1.3.6-alt1
- 1.3.6 (bugfix release)

* Fri Oct 06 2006 Slava Semushin <php-coder@altlinux.ru> 1.3.5-alt3
- Changed Group to Editors

* Thu Oct 05 2006 Slava Semushin <php-coder@altlinux.ru> 1.3.5-alt2
- Rebuilt with libdb4.4 again
  (during updates BuildRequires I revert libdb back to 4.3)

* Wed Sep 27 2006 Slava Semushin <php-coder@altlinux.ru> 1.3.5-alt1
- 1.3.5
- New maintainer
- Fixed #8255 (sources of libexpat removed from program in upstream)
- Fixed #9159
  + Converted Summary and %%description to CP1251 charset
  + Updated Url
  + Changed License to MIT
  + Removed no_desktop_menus.patch
  + Removed menu-file
- Updated BuildRequires
- Formatted %%description
- Added full url to Source tag
- More strict names in %%files section
- Enable _unpackaged_files_terminate_build
- Using macros %%make_install instead of %%makeinstall
- Using %%{update,clean}_desktopdb for registry MimeType

* Sat Mar 25 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.4-alt1.1
- Rebuilt with libdb4.4.

* Thu Dec 01 2005 Andrey Astafiev <andrei@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Mon Apr 18 2005 Andrey Astafiev <andrei@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Sat Jan 29 2005 Andrey Astafiev <andrei@altlinux.ru> 1.3.1-alt2
- Rebuilt with unicode support.

* Fri Nov 05 2004 Andrey Astafiev <andrei@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Sun Feb 29 2004 Andrey Astafiev <andrei@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Wed Nov 05 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Fri Jun 20 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.2-alt2
- Rebuilt with new wxGTK.

* Mon May 19 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Wed Apr 23 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.1-alt3
- Fixed Group tag.

* Wed Mar 12 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.1-alt2
- Now builds in Gnome and KDE environment.

* Fri Mar 07 2003 Andrei Astafiev <andrei@altlinux.ru> 1.2.1-alt1
- First version of RPM package.
