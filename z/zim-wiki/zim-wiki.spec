%define real_name zim
Summary: A desktop wiki and outliner
Name: zim-wiki
Version: 0.48
Release: alt5.1
Packager: Anton A. Vinogradov <arc@altlinux.org>

Source: %name-%version.tar
License: GPLv2
Group: Editors
Url: http://www.zim-wiki.org/

BuildRequires: python-dev
BuildRequires: python-module-pygobject-devel
BuildRequires: python-modules-json python-module-pygtk python-module-pyxdg xdg-utils
Requires: python
Requires: python-module-pygtk
Requires: python-module-pygobject
Requires: python-modules-json
Requires: python-module-pyxdg
Requires: xdg-utils

Conflicts: zim

BuildArch: noarch

%description
Zim is a WYSIWYG text editor written in Gtk2-python which aims to bring
the concept of a wiki to your desktop. Every page is saved as a text
file with wiki markup. Pages can contain links to other pages, and are
saved automatically. Creating a new page is as easy as linking to a
non-existing page. Pages are ordered in a hierarchical structure that
gives it the look and feel of an outliner. This tool is intended to
keep track of TODO lists or to serve as a personal scratch book.

%prep
%setup

%build
%python_build

%install
%python_install --skip-xdg-cmd
%find_lang %real_name

%files -f %real_name.lang
%doc README.txt CHANGELOG.txt LICENSE.txt
%_bindir/%real_name
%_datadir/%real_name/*
%_desktopdir/%real_name.desktop
%python_sitelibdir/*
%_man1dir/%{real_name}*
%_datadir/mime/*
%_iconsdir/hicolor/*/*/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.48-alt5.1
- Rebuild with Python-2.7

* Sun Oct 31 2010 Anton A. Vinogradov <arc@altlinux.org> 0.48-alt5
- some ro.po fix
- some spec cleanup

* Mon Oct 18 2010 Anton A. Vinogradov <arc@altlinux.org> 0.48-alt3
- rename to zim-wiki

* Thu Sep 30 2010 Anton A. Vinogradov <arc@altlinux.org> 0.48-alt2
- some spec cleanup by crux@

* Sat Jul 24 2010 Anton A. Vinogradov <arc@altlinux.org> 0.48-alt1
-  New version 0.48

* Mon Jun 21 2010 Anton A. Vinogradov <arc@altlinux.org> 0.47-alt1
- New version 0.47
- Switch to python 

* Sun Feb 22 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.28-alt1
- New version 0.28

* Sun Nov 16 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.27-alt1
- New version 0.27
- Fix repocop test shared-mime-info
- Fix build with Module::Build 0.30
- Remove obsolete update_menus/clean_menus calls

* Mon Aug 04 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt2
- Fix typos in russian translation (Closes: #16543)
- Mark l10n files with %%lang (Closes: #16544)

* Sun Jul 20 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt1
- New version 0.25
- Fix repocop issues on desktop file

* Tue Apr 29 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.24-alt0.1
- New version 0.24:
  * Added translations for German, French, Italian and Hebrew
  * Improved support for attaching files and images
  * Added daemon component to make seperate instances communicate
  * Other improvements, see Changes for details

* Mon Apr 07 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.23-alt3
- Add %%update_desktopdb call
- Fix Exec line in .desktop file
- Add missed dependency on perl-Gtk2-TrayIcon

* Mon Mar 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.23-alt2
- Fix 'About' dialog (#14839)
- Use 'BROWSER' environment variable in defaults
- Add pre-scaled icons

* Fri Feb 29 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.23-alt1
- New version 0.23
  * Added translation support
  * Renamed "repository" to "notebook" for better conceptual mapping
  * Several bug fixes
  * Added key bindings to side pane: '\' and '*' for collapse and expand all

* Fri Oct 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.22-alt1
- New version 0.22
  * Added an EquationEditor plugin using latex and dvipng
  * Added a "Open in external editor" menu item
  * Added a InsertScreenshot plugin
  * Made read_only property switch per page
  * Added current format style to status bar
  * Several bug fixes

* Sun Aug 19 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- New version 0.20
  * Added config file to control display styles of text formatting
  * Added template to control the look of new pages which can be customized
  * Added default repository to GUI, replaces "default_root"
  * Added a document root setting to the repository properties which can
    be used as a top level directory for external files
  * Added option to name the index page for Html export
  * Added option to handle autosave on slow filesystems by caching
  * Improved rendering of links in Html output
  * Improved robustness of error handling when writing a page fails
  * Updated the undo mechanism to also understand links and formats
  * Fixed bug causing infinite loop after "Link" on some platforms
  * Fixed bug that could corrupt links when updating links after move
  * Fixed win32 bug when executing external programs
  * Fixed bug with TrayIcon menu
  * Fixed bug in Txt2tags output - fix by Pierre Duquesne
  * Fixed type in "--quiet" commandline option
- Updated project's URL 

* Fri Aug 10 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt2
- Fix typo in package description

* Thu Apr 19 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt1
- new version 0.19: bugfix release
  * history is initialized properly
- Fix unicode label in Calendar window

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- new version, cleanup spec

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt1
- New version 0.16
  * major feature enhancements, see Changes for details
- Fix for #9931

* Mon Jan 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt0.1
- initial build for ALT Linux Sisyphus


