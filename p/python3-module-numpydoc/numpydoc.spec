%define oname numpydoc

%def_with check

Name: python3-module-%oname
Version: 1.2.0
Release: alt1
Epoch: 1

Summary: Numpy's Sphinx extensions

License: BSD-2-Clause
Group: Development/Python3
Url: http://numpy.scipy.org/

# https://github.com/numpy/numpydoc.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-sphinx
%endif

BuildArch: noarch

%description
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this ``numpydoc`` package, in case you want to make use
of them in third-party projects.

%prep
%setup

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%python3_sitelibdir/%oname/tests

%check
# Deselected tests need to download an inventory from docs.python.org
%{__python3} -m pytest -v -k "not test_MyClass and not test_my_function"

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 04 2022 Grigory Ustinov <grenka@altlinux.org> 1:1.2.0-alt1
- Automatically updated to 1.2.0.
- Added check section.

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

