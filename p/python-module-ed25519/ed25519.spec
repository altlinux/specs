%define oname ed25519

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20140928.1
Summary: Python bindings to the Ed25519 public-key signature system
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ed25519/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/warner/python-ed25519.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests git
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: git-core python-devel python-modules-unittest python3-devel rpm-build-python3

%description
This offers a comfortable python interface to a C implementation of the
Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using
the portable 'ref' code from the 'SUPERCOP' benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys,
short (64-byte) signatures, and fast (2-6ms) operation. Please see the
README for more details.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This offers a comfortable python interface to a C implementation of the
Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using
the portable 'ref' code from the 'SUPERCOP' benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys,
short (64-byte) signatures, and fast (2-6ms) operation. Please see the
README for more details.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python bindings to the Ed25519 public-key signature system
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This offers a comfortable python interface to a C implementation of the
Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using
the portable 'ref' code from the 'SUPERCOP' benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys,
short (64-byte) signatures, and fast (2-6ms) operation. Please see the
README for more details.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This offers a comfortable python interface to a C implementation of the
Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using
the portable 'ref' code from the 'SUPERCOP' benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys,
short (64-byte) signatures, and fast (2-6ms) operation. Please see the
README for more details.

This package contains tests for %oname.

%prep
%setup

sed -i 's|@VERSION@|%version|' src/ed25519/_version.py
git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version -m "%version"

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc NEWS *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc NEWS *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20140928.1
- NMU: Use buildreq for BR.

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140928
- Initial build for Sisyphus

