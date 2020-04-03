%define oname scikit-learn

%def_disable check

Name: python3-module-%oname
Version: 0.19.1
Release: alt3

Summary: A set of python modules for machine learning and data mining
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/scikit-learn/

# https://github.com/scikit-learn/scikit-learn.git
Source: %name-%version.tar
Patch1: %oname-%version-upstream-cython.patch
Patch2: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ liblapack-devel xvfb-run
BuildRequires: libnumpy-py3-devel python3-module-numpy-testing python3-module-scipy python3-module-zope python3-module-pytest
BuildRequires: python3-module-six python3-module-joblib python3-module-Cython python3(nose)

%py3_provides sklearn

%description
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1

# don't use bundled stuff
rm -rf sklearn/externals

find . -type f -print0 | xargs -0 sed -i \
	-e 's:import sklearn\.externals\.:import :g' \
	-e 's:from sklearn\.externals\.:from :g' \
	-e 's:from sklearn\.externals ::g' \
	-e 's:from \.\.externals\.:from :g' \
	-e 's:from \.\.externals ::g' \
	-e 's:from \.externals\.:from :g' \
	-e 's:from \.externals ::g'

sed -i -e "s:'externals',::" sklearn/__init__.py
sed -i -e "/config\.add_subpackage('externals')/d" sklearn/setup.py

%build
export BLAS=openblas
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
rm -fR build
%__python3 setup.py build_ext -i
xvfb-run py.test3 -vv

%files
%doc *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*

%files docs
%doc examples doc

%changelog
* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.19.1-alt3
- Build for python2 disabled.

* Thu Mar 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt2
- Fixed build with new cython.

* Tue Dec 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.19.1-alt1
- Updated to upstream version 0.19.1.

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17-alt1.dev0.git20150820.2
- Updated build dependencies.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.17-alt1.dev0.git20150820.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.17-alt1.dev0.git20150820.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.dev0.git20150820
- New snapshot

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.dev0.git20150424
- New snapshot

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1.dev0.git20150321
- Version 0.17.dev0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.git20150115
- New snapshot

* Sat Nov 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1.git20141113
- Initial build for Sisyphus

