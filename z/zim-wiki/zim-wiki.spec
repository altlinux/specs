%def_enable snapshot

%define real_name zim

Name: zim-wiki
Version: 0.75.1
Release: alt2

Summary: A desktop wiki and outliner
Group: Editors
License: GPLv2
Url: https://www.zim-wiki.org/

%if_disabled snapshot
Source: https://zim-wiki.org/downloads/%real_name-%version.tar.gz
%else
Source: %name-%version.tar
Patch: %name-%version-%release.patch
%endif

Patch1: AyatanaAppindicator.patch

BuildArch: noarch
Requires: typelib(Gtk) = 3.0
# see README.md and PKG-INFO
Requires: python3-module-pyxdg xdg-utils
# Mac-specific
%add_typelib_req_skiplist typelib(GtkosxApplication)
# typelib(AppIndicator3)

Conflicts: zim

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-wheel python3-module-setuptools
BuildRequires: python3-module-pygobject3 python3-modules-sqlite3
BuildRequires: typelib(Gtk) = 3.0

%description
Zim is a graphical text editor used to maintain a collection of wiki
pages. Each page can contain links to other pages, simple formatting and
images. Pages are stored in a folder structure, like in an outliner, and
can have attachments. Creating a new page is as easy as linking to a
nonexistent page. All data is stored in plain text files with wiki
formatting. Various plugins provide additional functionality, like a task
list manager, an equation editor, a tray icon, and support for version
control.

%prep
%setup
%patch -p1
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install
%find_lang %real_name

%files -f %real_name.lang
%_bindir/%real_name
%_datadir/%real_name
%_desktopdir/%real_name.desktop
%python3_sitelibdir/*
%_man1dir/%{real_name}*
%_datadir/mime/*
%_datadir/metainfo/*
%_iconsdir/*/*/*/*.svg
%exclude %_iconsdir/ubuntu*

%doc README.md CHANGELOG.md

%changelog
* Thu Mar 09 2023 Anton Midyukov <antohami@altlinux.org> 0.75.1-alt2
- NMU: switch to use AyatanaAppindicator

* Fri Nov 11 2022 Yuri N. Sedunov <aris@altlinux.org> 0.75.1-alt1
- 0.75.1

* Fri Sep 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.75.0-alt1
- 0.75.0

* Fri Dec 10 2021 Yuri N. Sedunov <aris@altlinux.org> 0.74.3-alt1
- updated to 0.74.3-2-g69fd0c59

* Wed Oct 13 2021 Yuri N. Sedunov <aris@altlinux.org> 0.74.2-alt1
- 0.74.2

* Mon Oct 11 2021 Yuri N. Sedunov <aris@altlinux.org> 0.74.1-alt1
- 0.74.1

* Tue Feb 02 2021 Yuri N. Sedunov <aris@altlinux.org> 0.73.5-alt1
- 0.73.5

* Thu Dec 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.73.4-alt1
- 0.73.4 (ported to Python 3)

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1.qa1
- NMU: applied repocop patch

* Sun Oct 15 2017 Pavel Vyazovoy <paulelms@altlinux.org> 0.67-alt1
- Updated to 0.67.

* Fri May 27 2016 Evgeny Sinelnikov <sin@altlinux.ru> 0.65-alt1
- Update to latest release

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


