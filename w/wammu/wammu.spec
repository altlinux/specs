Name: wammu
Version: 0.36
Release: alt1.1

Summary: Mobile phone manager
License: GPL
Group: Communications

Url: http://wammu.eu
Source: %name-%version.tar.bz2
Packager: L.A. Kostis <lakostis@altlinux.ru>

BuildArch: noarch

Requires: python-module-gammu >= 0.10
Requires: python-module-pybluez
%py_requires wx

BuildRequires: python-devel >= %_python_version
BuildRequires: python-module-gammu >= 0.10
BuildRequires: python-module-pybluez
BuildRequires: python-module-wx >= 2.8
# as of 0.35, 2.9 is known as unsupported
BuildConflicts: python-module-wx >= 2.9

%description
Mobile phone manager using Gammu as its backend.
It works with any phone Gammu supports -
many Nokias, Siemens, Alcatel, ...

%prep
%setup

%build
SKIPWXCHECK=yes python setup.py build

%install
SKIPWXCHECK=yes python setup.py install --root %buildroot --optimize=2 --record=INSTALLED_FILES
subst '/man1/ D' INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README AUTHORS COPYING FAQ PKG-INFO
%dir %python_sitelibdir/Wammu
#dir %python_sitelibdir/Wammu/wxcomp
%_man1dir/*
%_mandir/*/man1/*

%changelog
* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36-alt1.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Michael Shigorin <mike@altlinux.org> 0.36-alt1
- 0.36
  + Linux 3.0 compatible (tm)
- rebuilt with wxGTK 2.8 as it's the officially supported version

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.35-alt2.1
- Rebuilt with wxGTK 2.9

* Fri Mar 11 2011 Michael Shigorin <mike@altlinux.org> 0.35-alt2
- clarified (Build)Requires: to ensure build against wxpython-2.8

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 0.35-alt1
- 0.35
- added intl manpages
- malfunctions with python-module-wx2.9, use python-module-wx

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.30.1-alt2.1
- Rebuilt with python 2.6

* Fri Sep 11 2009 Michael Shigorin <mike@altlinux.org> 0.30.1-alt2
- rebuild (see also #21307)

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.30.1-alt1
- 0.30.1 built against gammu 1.23.1

* Wed Jan 07 2009 Michael Shigorin <mike@altlinux.org> 0.29-alt0.1
- NMU: 0.29
- updated Url:
- spec cleanup

* Tue Sep 02 2008 L.A. Kostis <lakostis@altlinux.ru> 0.28-alt1
- 0.28.
- add missing wxcomp dir.
- add PKG-INFO.

* Sun Sep 16 2007 L.A. Kostis <lakostis@altlinux.ru> 0.22-alt1
- 0.22.

* Sun Jan 07 2007 L.A. Kostis <lakostis@altlinux.ru> 0.17-alt1.1
- make it noarch.
- cleanup .spec.

* Sun Jan 07 2007 L.A. Kostis <lakostis@altlinux.ru> 0.17-alt1
- 0.17.

* Fri Sep 08 2006 L.A. Kostis <lakostis@altlinux.ru> 0.15-alt1
- 0.15.

* Fri Sep 08 2006 L.A. Kostis <lakostis@altlinux.ru> 0.13-alt2.1
- prepare for git.

* Sat Apr 22 2006 LAKostis <lakostis at altlinux dot ru> 0.13-alt2
- rebuild with pyBlueZ support.

* Sat Apr 01 2006 LAKostis <lakostis at altlinux dot ru> 0.13-alt1
- 0.13.
- remove menu file (use .desktop instead).

* Sun Oct 30 2005 LAKostis <lakostis at altlinux dot ru> 0.8-alt2.1
- fix #6043.

* Sun Oct 30 2005 LAKostis <lakostis at altlinux dot ru> 0.8-alt2
- s/python-gammu/python-module-gammu/.
- spec cleanup.

* Wed Mar 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.8-alt1.1
- Rebuilt with python-2.4.

* Fri Sep 15 2004 LAKostis <lakostis at altlinux dot ru> 0.8-alt1
- 0.8
- updated buidreq/req

* Sun May 18 2004 LAKostis <lakostis at altlinux dot ru> 0.6-alt1.1
- updated buidreq/req

* Sun May 16 2004 LAKostis <lakostis at altlinux dot ru> 0.6-alt1
- 0.6
- fix for bug #4113

* Sun Feb 15 2004 LAKostis <lakostis at altlinux dot ru> 0.5.1-alt1
- initial build for Sisyphus.
