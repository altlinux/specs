Name: hardlinkpy
Version: 0.0.20071114
Release: alt1.1.1

Summary: Rewrite in python of the hardlink utility
License: GPL
Group: File tools

Url: http://hardlinkpy.googlecode.com/
Source0: %url/svn/trunk/hardlink.py
Source1: %url/svn/trunk/COPYING
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires: python >= 2.2.3
Requires: python >= 2.2.3

Obsoletes: hardlink++
Provides: hardlink++ = %name-%version

%description
A rewrite of the hardlink utility in python, which recursively parses
directory structures and creates hard links for identical files found.

%prep
%setup -cT
cp -av %SOURCE0 hardlink.py
cp -av %SOURCE1 COPYING

%install
install -pDm755 hardlink.py %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.20071114-alt1.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.20071114-alt1.1
- Rebuilt with python 2.6

* Mon Aug 10 2009 Michael Shigorin <mike@altlinux.org> 0.0.20071114-alt1
- built for ALT Linux (based on DAG's package)
- spec cleanup
