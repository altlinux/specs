%define oname ed25519ll

%def_with python3

Name: python-module-%oname
Version: 0.6
Release: alt1
Summary: A low-level ctypes wrapper for Ed25519 digital signatures
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ed25519ll/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python-tools-2to3
%endif

%py_provides %oname

%description
Ed25519 is a public-key signature system with several attractive
features including:

* Fast single-signature verification.
* Very fast signing.
* Fast key generation.
* High security level.
* Small signatures. Signatures fit into 64 bytes.
* Small keys. Public keys consume only 32 bytes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Ed25519 is a public-key signature system with several attractive
features including:

* Fast single-signature verification.
* Very fast signing.
* Fast key generation.
* High security level.
* Small signatures. Signatures fit into 64 bytes.
* Small keys. Public keys consume only 32 bytes.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A low-level ctypes wrapper for Ed25519 digital signatures
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Ed25519 is a public-key signature system with several attractive
features including:

* Fast single-signature verification.
* Very fast signing.
* Fast key generation.
* High security level.
* Small signatures. Signatures fit into 64 bytes.
* Small keys. Public keys consume only 32 bytes.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Ed25519 is a public-key signature system with several attractive
features including:

* Fast single-signature verification.
* Very fast signing.
* Fast key generation.
* High security level.
* Small signatures. Signatures fit into 64 bytes.
* Small keys. Public keys consume only 32 bytes.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1
- Initial build for Sisyphus

