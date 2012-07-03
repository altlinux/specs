# SPEC file for Zim

%define realname Zim

Name: zim
Version: 0.29
Release: alt3

Summary: a desktop wiki and outliner
Summary(ru_RU.UTF-8): настольный wiki и outliner

License: %perl_license
Group: Editors
#URL: http://zoidberg.student.utwente.nl/zim/
#URL: http://www.pardus.nl/projects/zim/
URL: http://zim-wiki.org/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

BuildArch: noarch

Source: %realname-%version.tar
#http://www.zim-wiki.org/downloads/%realname-%version.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png

Patch0: Zim-0.28-alt-desktop_l10n.patch
Patch2: Zim-0.24-alt-icons_load.patch
Patch3: Zim-0.23-alt-fix_obsolete_Gtk2.patch
Patch4: Zim-0.23-alt-default_browser.patch
Patch5: Zim-0.25-alt-fix_typos.patch
Patch6: Zim-0.26-alt-extended_warings.patch
Patch7: Zim-0.29-alt-strftime.patch
Patch8: Zim-0.29-alt-insert_image.patch
Patch9: Zim-0.29-alt-Gtk2_build.patch

# Due to intersection on files
Conflicts: zim-wiki

Requires: perl-unicore perl-Gtk2-TrayIcon
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): perl-devel perl-Module-Build
BuildRequires(pre): desktop-file-utils

# Automatically added by buildreq on Mon Nov 29 2010
BuildRequires: desktop-file-utils man perl-File-MimeInfo perl-Gtk2-Spell perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

BuildRequires: perl-Gtk2-TrayIcon perl-podlators

%description
Zim  is a WYSIWYG text editor written in Gtk2-Perl which aims to
bring the concept of a wiki to your desktop. Every page is saved
as a  text file  with wiki markup.  Pages  can contain  links to
other pages, and are saved automatically. Creating a new page is
as easy as linking to a non-existing page.  Pages are ordered in
a hierarchical structure  that gives it the  look and feel of an
outliner.  This tool is intended to keep track  of TODO lists or
to serve as a personal scratch book.

%description -l ru_RU.UTF-8
Zim - написанный на Gtk2-Perl текстовый редактор WYSIWYG, который
стремиться  принести  концепцию  wiki  на рабочий  стол.   Каждая
страница сохраняется как текстовый файл с разметкой в стиле wiki.
Страницы могут содержать  ссылки на другие страницы и сохраняются
автоматически.  Создать новую страницу так же просто, как создать
ссылки  на несуществующую страницу.  Страницы  упорядочиваются  в
иерархическую структуру,  которую можно  рассматривать  как некое
подобие аутлайнера.  Данная утилита предназначена преимущественно
для хранения списков задач или для использования в качестве
персональной записной книжки.

# There are only sample scripts in doc/ notebook
%add_findreq_skiplist %_datadir/%name/doc/*.sh

# Define XDG_DATA_DIRS for find-requires
%{expand: %%global __find_requires export XDG_DATA_DIRS="%_datadir:%buildroot%_datadir";%__find_requires}

%prep
%setup -n %realname-%version
%patch0
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9

# These tests includes GTK2->init and thus fails when build by gear.
rm -- t/70_gui_pageview.t
rm -- t/81_TODO_plugin.t

# This test fails to load default icon without X environment
rm -- t/60_hyper_text_buffer.t

# This test fails under gear/hasher due to sync problems
rm -- t/71_gui_daemon.t
# This test needs Baazar
rm -- t/16_Bazaar.t

%build
# Lingua.PL overrides desktop file: keep original one
cp share/applications/zim.desktop share/applications/zim.desktop.bak
perl Lingua.PL
cp -f share/applications/zim.desktop.bak share/applications/zim.desktop

# Define XDG_DATA_DIRS for tests
export XDG_DATA_DIRS="%_datadir:../share/:share/"
%perl_vendor_build

%install
%perl_vendor_install
# Adding INSTALLMAN1DIR=%%_man1dir to %%perl_vendor_build doesn't build zim(1)
mkdir -p %buildroot%_man1dir
/usr/bin/pod2man %buildroot%_bindir/%name > %buildroot%_man1dir/%name.1

%find_lang --custom-file-script="
s:%buildroot::
s:\(.*/share/zim/lingua/\)\([a-z]\+\):%%lang(\2) \1\2:
s:^[^%%].*::" %name

mkdir -p --	%buildroot%_miconsdir %buildroot%_liconsdir \
		%buildroot%_niconsdir %buildroot%_iconsdir/hicolor/64x64/apps

cp -f -- share/pixmaps/zim.png %buildroot%_iconsdir/hicolor/64x64/apps/
install -m0644 -- %SOURCE1 %buildroot%_miconsdir/zim.png
install -m0644 -- %SOURCE2 %buildroot%_niconsdir/zim.png
install -m0644 -- %SOURCE3 %buildroot%_liconsdir/zim.png

%files -f %name.lang
%doc Changes

%_bindir/%name

%_man1dir/%{name}*

%perl_vendor_privlib/Gtk2/Ex/*
%perl_vendor_privlib/%{realname}*
%dir %_datadir/%name
%dir %_datadir/%name/lingua
%_datadir/%name/doc*
%_datadir/%name/plugins*
%_datadir/%name/templates*
%_datadir/%name/*.*

%_desktopdir/%name.desktop
%_pixmapsdir/*
%_xdgmimedir/packages/%{name}.xml

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*
%_iconsdir/hicolor/64x64/apps/%{name}*

%exclude /.perl.req

%changelog
* Sat Sep 03 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.29-alt3
- Fix build with shared-mime-info 0.90-alt3

* Fri Mar 11 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.29-alt2
- Fix build with perl-Gtk2 1.223

* Mon Jul 19 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.29-alt1
- New version 0.29
- Fix image insert (Closes: #23601)
- Fix build with Perl 5.12

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
