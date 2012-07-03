%define oname pyblio-core

Name: python-module-pyblio-core
Version: 1.3.4
Release: alt3.1

Summary: Pybliographer base package

License: GPL
Group: Databases
Url: http://www.pybliographer.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/pybliographer/%oname-%version.tar.bz2

BuildArch: noarch

# TODO: uno for OOo
%add_python_req_skip uno

Obsoletes: python-module-pybliographer
Provides: python-module-pybliographer

BuildPreReq: rpm-build-compat >= 1.2

# python buildreq is broken!
# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: python-module-MySQLdb python-modules-bsddb python-module-setuptools

%description
Pybliographer is a bibliographic database management toolkit. This
core package is a framework on which you can easily build parsers for
multiple publication database formats, or extend existing parsers;
define citation formats; modify, search and sort bibliographic data.

%prep
%setup -q -n %oname-%version

%build
%python_build

cd tests; ./testsuite.sh

%install
%python_install

%files
%doc README demo doc
%python_sitelibdir/Pyblio/

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.4-alt3.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt3
- Rebuilt with python 2.6

* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- update buildreq

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus

