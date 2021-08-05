%define oname numpydoc

Name: python3-module-%oname
Version: 0.7.0
Release: alt2
Epoch: 1

Summary: Numpy's Sphinx extensions
License: BSD
Group: Development/Python3
Url: http://numpy.scipy.org/
BuildArch: noarch

# https://github.com/numpy/numpydoc.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%description
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this ``numpydoc`` package, in case you want to make use
of them in third-party projects.

%package tests
Summary: Tests for numpydoc
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description tests
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this ``numpydoc`` package, in case you want to make use
of them in third-party projects.

This package contains tests for numpydoc.

%prep
%setup

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Thu Aug 05 2021 Grigory Ustinov <grenka@altlinux.org> 1:0.7.0-alt2
- Drop python2 support.

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.7.0-alt1
- Updated to upstream version 0.7.0.
- Enabled build for python3.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6-alt1.dev.git20150712
- New snapshot

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6-alt1.dev.git20150409
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6-alt1.dev.git20140907
- New snapshot

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.6-alt1.dev.git20140608
- Version 0.6.dev

* Wed Oct 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.5-alt1.dev.git20131021
- Initial build for Sisyphus

