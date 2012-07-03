Name: tkdiff
Version: 4.1.4
Release: alt1.qa1
%define tarname %name-%version-unix

Summary: An tcl/tk based graphical interface to the DIFF utility
Summary(ru_RU.KOI8-R): Графический интерфейс к DIFF

License: GPL
Group: Development/Other
Url: http://sourceforge.net/projects/tkdiff/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%name/%tarname.tar.bz2
Source2: %name.desktop
Source3: %name.png

Patch: %name.patch

Requires: tk diffutils

BuildArch: noarch
Autoreq: yes, noshell

%description
TkDiff is a graphical front-end for the standard Unix 'diff' utility.
Its features include highlighted difference regions (with a quick
overview/navigation bar) and linked scrolling of files. It provides
file-merge and change-summary facilities, line number toggling (for easier
cut & paste) and support for Subversion, RCS, CVS and SCCS.

%prep
%setup -q -n %tarname
%patch -p1

%install
install -D -m755 tkdiff %buildroot%_bindir/tkdiff
install -D -m644 %name.1 %buildroot%_man1dir/%name.1
install -D -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -D -m644 %SOURCE3 %buildroot%_liconsdir/%name.png

%files
%doc Changelog
%_bindir/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_man1dir/*

%changelog
* Tue Dec 01 2009 Repocop Q. A. Robot <repocop@altlinux.org> 4.1.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for tkdiff
  * update_menus for tkdiff
  * postclean-05-filetriggers for spec file

* Wed Jan 09 2008 Vitaly Lipatov <lav@altlinux.ru> 4.1.4-alt1
- new version 4.1.4
- cleanup spec, change Packager
- add man, desktop (thanks Debian)
- update description, remove COPYING, add Changelog

* Wed Jul  6 2005 Sergey Kalinin <banzaj@altlinux.ru> 4.1.0-alt1
- Clearcase support
- Better Subversion support
- -L command line option allows you to control the labels above the diff file panes.
- tkdiff --help or -h print a usage message for command line without invoking the GUI.
- The New Diff Dialog is expanded so you can specify all the options that way.
- The two panes can be resized relative to each other using a sash
  widget.  Tk8.4 is recommended, since the implemetation is much better.

* Wed Feb  9 2005 Sergey Kalinin <banzaj@altlinux.ru> 4.0.2-alt1
- new version release

* Mon May 16 2004 Sergey Kalinin <banzaj@altlinux.ru> 4.0.0-alt2
- SPEC file changes - Summary fixed

* Tue Mar 30 2004 Sergey Kalinin <banzaj@altlinux.ru> 4.0.0-alt1
- Inline diff highlighting
- Current line comparison window
- Support for Subversion
- better tolerance of Windows filenames
- CDE, Windows, and MacOSX aware
