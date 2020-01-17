%define oname pynzb

Name: python3-module-%oname
Version: 0.1.0
Release: alt2

Summary: Unified API for parsing NZB files, several concrete implementations included
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pynzb/
BuildArch: noarch

# https://github.com/ericflo/pynzb.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-lxml python3-module-nose

%py3_provides %oname
# %%py3_requires lxml
# %%add_python3_req_skip xml


%description
NZB is an XML-based file format for retrieving posts from NNTP (Usenet)
servers. Since NZB is XML-based, it's relatively easy to build one-off
parsers to parse NZB files. This project is an attempt to consolidate
those many one-off NZB parsers into one simple interface.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
NZB is an XML-based file format for retrieving posts from NNTP (Usenet)
servers. Since NZB is XML-based, it's relatively easy to build one-off
parsers to parse NZB files. This project is an attempt to consolidate
those many one-off NZB parsers into one simple interface.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
nosetests3
%endif

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.git20090510.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20090510
- Initial build for Sisyphus

