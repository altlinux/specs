%define oname pynzb
Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20090510.1
Summary: Unified API for parsing NZB files, several concrete implementations included
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pynzb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ericflo/pynzb.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-lxml python-module-nose

%py_provides %oname
%py_requires lxml
%add_python_req_skip xml

%description
NZB is an XML-based file format for retrieving posts from NNTP (Usenet)
servers. Since NZB is XML-based, it's relatively easy to build one-off
parsers to parse NZB files. This project is an attempt to consolidate
those many one-off NZB parsers into one simple interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
NZB is an XML-based file format for retrieving posts from NNTP (Usenet)
servers. Since NZB is XML-based, it's relatively easy to build one-off
parsers to parse NZB files. This project is an attempt to consolidate
those many one-off NZB parsers into one simple interface.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
nosetests

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.git20090510.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20090510
- Initial build for Sisyphus

