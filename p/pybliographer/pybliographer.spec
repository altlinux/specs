%define major 1.4
Name: pybliographer
Version: %major.0
Release: alt1

Summary: Framework for working with bibliographic databases
Summary(ru_RU.UTF-8): Среда для работы с библиографическими базами данных

License: GPL
Group: Databases
Url: http://www.pybliographer.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://download.gnome.org/sources/pybliographer/%major/pybliographer-%version.tar.xz
Source: %name-%version.tar

BuildArch: noarch

Obsoletes: pybliographic
Provides: pybliographic = %version-release
Obsoletes: pyblio
Provides: pyblio = %version-release

BuildRequires: itstool
BuildRequires: python-module-pygtk-devel >= 2.24.0
BuildRequires: python-module-bibtex >= 1.2.2

%description
Pybliographer is a tool for managing bibliographic databases. It can be
used for searching, editing, reformatting, etc. In fact, it's a simple
framework that provides easy to use python classes and functions, and
therefore can be extended to many uses (generating HTML pages according
to bibliographic searches, etc).
In addition to the scripting environment, a graphical Gnome interface
is available. It provides powerful editing capabilities, a nice
hierarchical search mechanism, direct insertion of references into LyX,
direct queries on Medline, and more. It currently supports the following
file formats: BibTeX, ISI, Medline, Ovid, Refer.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS COPYING* ChangeLog* NEWS README TODO
%_bindir/pybliocheck
%_bindir/pybliocompact
%_bindir/pyblioconvert
%_bindir/pyblioformat
%_bindir/pybliographer
%_bindir/pybliographic
%_bindir/pybliotex
%_bindir/pybliotext
%_datadir/%name/
%_datadir/appdata/pybliographic.appdata.xml
%_desktopdir/pybliographic.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Wed Jun 20 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Tue Jan 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt0.1
- new version

* Tue Dec 06 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.7-alt1
- new version

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.6.2-alt2
- fix python strict requires
- add menu file
- add Pyblio provides

* Mon Mar 21 2005 Vitaly Lipatov <lav@altlinux.ru> 1.2.6.2-alt1
- new version
- rebuild with python 2.4
- remove gconf using

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt2
- some spec's fix
- enable strict requires find

* Mon Nov 29 2004 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- first build for ALT Linux Sisyphus

* Fri Nov 26 2004 Zoltan Kota <z.kota at gmx.net> - 0:1.2.5-1.rhfdr_core_3
- initial RPM package of 1.2.5 for Fedora Core 3
