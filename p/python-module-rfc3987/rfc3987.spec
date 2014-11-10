%define oname rfc3987

%def_with python3

Name: python-module-%oname
Version: 1.3.4
Release: alt1.git20140310
Summary: Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/rfc3987/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dgerber/rfc3987.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-regex
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-regex
%endif

%py_provides %oname
%py_requires regex

%description
This module provides regular expressions according to RFC 3986 "Uniform
Resource Identifier (URI): Generic Syntax" and RFC 3987
"Internationalized Resource Identifiers (IRIs)", and utilities for
composition and relative resolution of references.

%package -n python3-module-%oname
Summary: Parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
Group: Development/Python3
%py3_provides %oname
%py3_requires regex

%description -n python3-module-%oname
This module provides regular expressions according to RFC 3986 "Uniform
Resource Identifier (URI): Generic Syntax" and RFC 3987
"Internationalized Resource Identifiers (IRIs)", and utilities for
composition and relative resolution of references.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.git20140310
- Initial build for Sisyphus

