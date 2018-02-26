Name: treeline
Version: 1.2.1
Release: alt1.1.qa1.1

Summary: Treeline stores almost any kind of information

License: GPL
Group: Text tools
Url: http://treeline.bellz.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.berlios.de/treeline/%name-%version.tar.bz2
Source1: http://download.berlios.de/treeline/%name-i18n-%{version}a.tar.bz2
Source2: %name.desktop

BuildArchitectures: noarch

%add_python_req_skip py2exe

# Automatically added by buildreq on Tue Jan 06 2009 (-bi)
BuildRequires: aspell-en python-module-PyQt4 python-module-PyXML python-modules-compiler python-modules-email

BuildRequires: desktop-file-utils

%description
Some would call TreeLine an Outliner, others would call it a
PIM. Basically, it just stores almost any kind of information. A tree
structure makes it easy to keep things organized. And each node in the
tree can contain several fields, forming a mini-database. The output
format for each node can be defined, and the output can be shown on the
screen, printed, or exported to html.

%prep
%setup -q -n TreeLine -b1

%install
python install.py -b %buildroot -p %prefix

install -D -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Office \
	--add-category=Database \
	%buildroot%_desktopdir/treeline.desktop

%files
%_bindir/*
%_desktopdir/%name.desktop
# NOTE: as in install script
%_datadir/icons/%name/
%_datadir/%name/
%_docdir/%name/
%_libexecdir/%name/

%changelog
* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt1.1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.1-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for treeline

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.1
- Rebuilt with python 2.6

* Tue Jan 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)
- drop out post/postun sections
- update buildreq

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2.1.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for treeline

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 1.0.2-alt2.1
- Rebuilt with python-2.5.

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 1.0.2-alt2
- Use _libexecdir macro while packaging

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)
- update buildreq, use desktop menu file

* Tue Mar 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- new version 1.0.1 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt0.1
- new version 1.0.0 (with rpmrb script)

* Tue Mar 07 2006 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt1
- add translations

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt0.1
- new version (0.14.1)

* Thu Nov 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.13.1-alt1
- new version

* Mon Aug 29 2005 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt0.1
- first build for ALT Linux Sisyphus

