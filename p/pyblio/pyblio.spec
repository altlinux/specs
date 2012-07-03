Name: pyblio
Version: 1.3.4
Release: alt3.2.1

Summary: Framework for working with bibliographic databases
Summary(ru_RU.KOI8-R): Среда для работы с библиографическими базами данных

License: GPL
Group: Databases
Url: http://www.pybliographer.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/pybliographer/%name-%version.tar.bz2

BuildArch: noarch

Obsoletes: pybliographic
Provides: pybliographic

Requires(post): GConf2
Requires(post,postun): librarian
Requires(post,postun): desktop-file-utils

# manually removed: captive 
# Automatically added by buildreq on Sat Jan 05 2008
BuildRequires: gnome-control-center librarian python-module-bibtex python-module-pyblio-core python-module-pygnome-bonobo python-module-pygnome-gconf python-module-pygnome-gnome-vfs python-module-pygtk-libglade python-modules-compiler python-modules-encodings
BuildPreReq: desktop-file-utils GConf2 librarian-devel rpm-build-gnome

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
rm -f %buildroot%_desktopdir/mimeinfo.cache
rm -rf %buildroot%_localstatedir/scrollkeeper
ln -s pybliographic-1.3 %buildroot%_bindir/pybliographic
%find_lang %name

%files -f %name.lang
%doc README doc/
%doc AUTHORS COPYING* ChangeLog* NEWS README TODO
%_bindir/py*-1.3
%_bindir/pybliographic
%_desktopdir/pyblio.desktop
%_datadir/gnome/help/pyblio
%_datadir/mime-info/*
%_omfdir/pyblio/
%_pixmapsdir/*
%dir %_datadir/pyblio-1.3/
%_datadir/pyblio-1.3/Legacy/
%_datadir/pyblio-1.3/Styles/
%_datadir/pyblio-1.3/pybcheck.py*
%_datadir/pyblio-1.3/pybcompact.py*
%_datadir/pyblio-1.3/pybconvert.py*
%_datadir/pyblio-1.3/pybformat.py*
%_datadir/pyblio-1.3/pybliographic.py*
%_datadir/pyblio-1.3/pybtex.py*
%_datadir/pyblio-1.3/pybtext.py*
%_datadir/pyblio-1.3/pybrc.py*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.4-alt3.2.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt3.2
- Rebuilt with python 2.6

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt3.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for pyblio

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 1.3.4-alt3.1
- Rebuilt with python-2.5.

* Tue Jan 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt3
- add rpm-build-gnome

* Sun Jan 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- remove captive :) from buildreq

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus

* Fri Sep 15 2007 Zoltan Kota <z.kota at gmx.net> - 1.3.4-0.1.fc7
- rpm release of 1.3.4
