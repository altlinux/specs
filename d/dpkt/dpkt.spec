Name: dpkt
Version: 1.7
Release: alt1.1
Url: http://monkey.org/~dugsong/dpkt/
License: BSD
Group: Development/Python
%setup_python_module %name
Summary: Examples and tests for %packagename
Source: %name-%version.tar.gz
Buildarch: noarch
Requires: %packagename = %version

BuildRequires: python-modules-xml python-module-epydoc >= 3.0.1

%description
%summary

%package -n %packagename
Group: Development/Python
Summary: Fast, simple packet creation and parsing
%description -n %packagename
Fast, simple packet creation / parsing, with definitions for the basic TCP/IP
protocols.

Authors:
--------
    Dug Song <dugsong+dpkt@monkey.org>

%prep
%setup

%build
%python_build
%make_build doc

%install
%python_install

%files
%doc examples tests

%files -n %packagename
%doc doc AUTHORS CHANGES HACKING LICENSE README
%python_sitelibdir/%modulename

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7-alt1.1
- Rebuild with Python-2.7

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Thu Jul 28 2011 Fr. Br. George <george@altlinux.ru> 1.6-alt3
Clean up spec
New upstream URL

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt2.1
- Rebuilt with python 2.6

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 1.6-alt2
- Repocop bug fixed

* Sat Jan 10 2009 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Initial build from OpenSuSE

* Sun Jan 28 2007 - Cristian Rodriguez <judas_iscariote@shorewall.net>
- update to version 1.6
* Wed Sep 06 2006 - James Oakley <jfunk@funktronics.ca> - 1.5-1
- Initial release
