%define oname scikit-learn

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.19.1
Release: alt1
Summary: A set of python modules for machine learning and data mining
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikit-learn/

# https://github.com/scikit-learn/scikit-learn.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: gcc-c++ liblapack-devel python-module-numpy-testing python-module-objects.inv python-module-scipy
BuildRequires: libnumpy-devel python-module-six python-module-joblib python-module-Cython python2.7(nose)
BuildRequires: python2.7(matplotlib) python-module-Pillow xvfb-run
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel python3-module-numpy-testing python3-module-scipy python3-module-zope python3-module-pytest
BuildRequires: python3-module-six python3-module-joblib python3-module-Cython python3(nose)
%endif

%py_provides sklearn

%description
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A set of python modules for machine learning and data mining
Group: Development/Python3
%py3_provides sklearn

%description -n python3-module-%oname
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
scikit-learn is a Python module for machine learning built on top of
SciPy and distributed under the 3-Clause BSD license.

This package contains pickles for %oname.

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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
export BLAS=openblas
%add_optflags -fno-strict-aliasing -I%_includedir/numpy-py3
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

# build of docs is infinite; need help
#export PYTHONPATH=%buildroot%python_sitelibdir
#make -C doc pickle
#make -C doc html

%check
export PYTHONPATH=%buildroot%python_sitelibdir
rm -fR build
python setup.py build_ext -i
xvfb-run py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
rm -fR build
python3 setup.py build_ext -i
xvfb-run py.test3 -vv
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%files docs
%doc examples doc

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
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

