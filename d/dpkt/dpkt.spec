%def_without python3

Name: dpkt
Version: 1.8.6
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
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest-cov
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytest-cov
BuildPreReq: python-tools-2to3
%endif

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

%if_with python3
%package -n python3-module-dpkt
Summary: Fast, simple packet creation and parsing
Group: Development/Python3

%description -n python3-module-dpkt
Fast, simple packet creation / parsing, with definitions for the basic TCP/IP
protocols.

Authors:
--------
    Dug Song <dugsong+dpkt@monkey.org>
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

epydoc -o doc -n dpkt -u %url --docformat=plaintext ./dpkt/

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test -vv %name
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv %name
popd
%endif

#files
#doc examples tests

%files -n %packagename
%doc doc AUTHORS CHANGES LICENSE README*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-dpkt
%doc doc AUTHORS CHANGES LICENSE README*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1
- Version 1.8.6

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8
- Fix docs build

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
