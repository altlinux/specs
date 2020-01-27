%define oname pathod

Name: python3-module-%oname
Version: 0.11
Release: alt2

Summary: A pathological HTTP/S daemon for testing and stressing clients
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pathod/
BuildArch: noarch

# https://github.com/mitmproxy/pathod.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3
BuildRequires: python3-module-flask
BuildRequires: python3-module-netlib
BuildRequires: python3-module-requests

%py3_provides libpathod


%description
pathod is a collection of pathological tools for testing and torturing
HTTP clients and servers. The project has three components:

* pathod, an pathological HTTP daemon.
* pathoc, a perverse HTTP client.
* libpathod.test, an API for easily using pathod and pathoc in unit
  tests.

%package test
Summary: Test for %oname
Group: Development/Python3
Requires: %name = %EVR

%description test
pathod is a collection of pathological tools for testing and torturing
HTTP clients and servers. The project has three components:

* pathod, an pathological HTTP daemon.
* pathoc, a perverse HTTP client.
* libpathod.test, an API for easily using pathod and pathoc in unit
  tests.

This package contains test for %oname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
%__python3 setup.py test

%files
%doc CHANGELOG README.* examples
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*

%files test
%python3_sitelibdir/*/test.*


%changelog
* Mon Jan 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.11-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11-alt1.git20141111.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20141111
- Initial build for Sisyphus

