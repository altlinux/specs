%define oname hawkauthlib

Name:       python3-module-%oname
Version:    0.1.1
Release:    alt2

Summary:    Low-level library for implementing MAC Access Authentication
License:    MPLv2.0
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/hawkauthlib/
BuildArch:  noarch

# https://github.com/mozilla-services/hawkauthlib.git
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-webob python3-module-requests

%py3_provides %oname


%description
This is a low-level library for implementing Hawk Access Authentication,
a simple HTTP request-signing scheme described in:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and a secret
key. They use these credentials to make signed requests to the server.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This is a low-level library for implementing Hawk Access Authentication,
a simple HTTP request-signing scheme described in:

    https://npmjs.org/package/hawk

To access resources using Hawk Access Authentication, the client must
have obtained a set of Hawk credentials including an id and a secret
key. They use these credentials to make signed requests to the server.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.git20131112.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20131112.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20131112
- Initial build for Sisyphus

