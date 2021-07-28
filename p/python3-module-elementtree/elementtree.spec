%define modulename elementtree
%define rver 20050316

%define version 1.2.6
%define release alt1.%rver
Summary: ElementTree - a light-weight XML object model for Python.
Name: python3-module-%modulename
Version: %version
Release: alt2.20050316
URL: http://effbot.org/zone/element-index.htm
Source: %modulename-%version-%rver.tar.gz
Patch1: %modulename-TidyHTMLTreeBuilder-fix.patch
Patch2: elementtree-1.2.6-alt-python3.patch
Copyright: Python (MIT style)
Group: Development/Python3
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

%description
The Element type is a flexible container object, designed to store
hierarchical data structures in memory.  Element structures can be
converted to and from XML.

%prep
%setup -q -n %modulename-%version-%rver
%patch1 -p1
%patch2 -p2

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc docs samples CHANGES README benchmark.py selftest.py
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.6-alt2.20050316
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.6-alt1.20050316.1.1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.6-alt1.20050316.1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.20050316.1.1.1
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt0.20050316.1.1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt0.20050316.1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.2.6-alt0.20050316.1.1
- Rebuilt with python-2.5.

* Fri May  6 2005 Konstantin Klimchev <koka@altlinux.ru> 1.2.6-alt0.20050316.1
- new 1.2.6-20050316
- python2.4

* Wed Dec 22 2004 Konstantin Klimchev <koka@altlinux.ru> 1.2.3-alt0.20041205.1
- initial build for Sisyphus
