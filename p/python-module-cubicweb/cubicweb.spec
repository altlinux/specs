%define oname cubicweb
Name: python-module-%oname
Version: 3.19.5
Release: alt2.hg20141124
Summary: A repository of entities / relations for knowledge management
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-logilab-common python-module-rql
BuildPreReq: python-module-logilab-mtconverter python-module-yams
BuildPreReq: python-module-lxml python-module-twisted-core
BuildPreReq: python-module-twisted-web
BuildPreReq: python-module-passlib python-module-docutils
BuildPreReq: python-module-Pyro4 python-module-Pillow
BuildPreReq: python-module-pycrypto python-module-fyzz
BuildPreReq: python-module-vobject python-module-rdflib
BuildPreReq: python-module-zmq python-module-logilab-constraint
BuildPreReq: python-module-yapps2 python-module-markdown
BuildPreReq: python-module-logilab-database-tests

%py_requires twisted.internet twisted.web logilab.common docutils rdflib
%py_requires logilab.mtconverter logilab.database Pyro4 PIL vobject
%py_requires cubicweb.devtools.testlib sqlite3

%description
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

%package -n %oname
Summary: RQL command line client to the repository and data files
Group: Development/Other
Requires: %name = %EVR

%description -n %oname
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

This package contains RQL command line client to the repository and data
files.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires logilab.common.testlib

%description tests
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
CubicWeb is a entities / relations based knowledge management system
developped at Logilab.

This package contains documentation for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

install -d %buildroot%_man1dir
install -p -m644 man/* %buildroot%_man1dir/

%check
python setup.py test

%files -n %oname
%doc README
%_bindir/*
%_man1dir/*
%_datadir/%oname

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/*/*/test*

%files docs
%doc doc/*

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.5-alt2.hg20141124
- Added necessary requirements

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.5-alt1.hg20141124
- New snapshot

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.19.5-alt1.hg20140730
- Initial build for Sisyphus

