BuildRequires: desktop-file-utils
Name: treeline
Version: 3.1.5
Release: alt1

Summary: Treeline stores almost any kind of information

License: GPL
Group: Text tools
Url: http://treeline.bellz.org/

# Source-url: https://github.com/doug-101/TreeLine/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 04 2017 (-bi)
# optimized out: python-base python3 python3-base rpm-build-python3
BuildRequires: python3-dev

%description
Some would call TreeLine an Outliner, others would call it a
PIM. Basically, it just stores almost any kind of information. A tree
structure makes it easy to keep things organized. And each node in the
tree can contain several fields, forming a mini-database. The output
format for each node can be defined, and the output can be shown on the
screen, printed, or exported to html.

%prep
%setup

%build
%install
python3 install.py -b %buildroot -p %prefix -x
rm %buildroot%_datadir/%name/setup.py 

install -D -m 0644 treeline.desktop %buildroot%_desktopdir/%name.desktop
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
%_iconsdir/*/*/apps/*

%changelog
* Mon Dec 19 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.5-alt1
- new version 3.1.5 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.4-alt1
- new version 3.1.4 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.2-alt1
- new version 3.1.2 (with rpmrb script)

* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt1.qa1
- NMU: applied repocop patch

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 2.9.0-alt1
- Autobuild version bump to 2.9.0

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 2.1.2-alt1
- Autobuild version bump to 2.1.2
- Drop outdated translations

* Tue Nov 13 2012 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1

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

