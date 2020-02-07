%define oname ed25519

Name: python3-module-%oname
Version: 1.5
Release: alt1

Summary: Python bindings to the Ed25519 public-key signature system
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ed25519/

# https://github.com/warner/python-ed25519.git
Source: %name-%version.tar
Patch0: fix-detecting-version.patch

BuildRequires(pre): rpm-build-python3
Conflicts: python-module-%oname


%description
This offers a comfortable python interface to a C implementation of the
Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using
the portable 'ref' code from the 'SUPERCOP' benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys,
short (64-byte) signatures, and fast (2-6ms) operation. Please see the
README for more details.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This offers a comfortable python interface to a C implementation of the
Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using
the portable 'ref' code from the 'SUPERCOP' benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys,
short (64-byte) signatures, and fast (2-6ms) operation. Please see the
README for more details.

This package contains tests for %oname.

%prep
%setup
%patch0 -p1

touch 'version.py'
echo "%version" > version.py

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc NEWS *.md
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt1
- Version updated to 1.5
- build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1.git20140928.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20140928.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20140928.1
- NMU: Use buildreq for BR.

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140928
- Initial build for Sisyphus

