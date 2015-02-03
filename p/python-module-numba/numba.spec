%define oname numba

%def_with python3

Name: python-module-%oname
Version: 0.16.0
Release: alt1.git20150202
Summary: NumPy aware dynamic compiler for Python
License: BSD-like
Group: Development/Python
Url: http://numba.pydata.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/numba/numba.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
#BuildPreReq: libnumpy-devel python-module-Cython python-module-llvmmath
BuildPreReq: libnumpy-devel python-module-Cython
BuildPreReq: python-module-llvmlite python-module-setuptools-tests
BuildPreReq: python-module-funcsigs
BuildPreReq: gcc-c++ git python-module-sphinx-devel
BuildPreReq: python-module-sphinxjp.themecore
BuildPreReq: python-module-sphinxjp.themes.basicstrap
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: libnumpy-py3-devel python3-module-Cython
BuildPreReq: python3-module-llvmlite python3-module-setuptools-tests
BuildPreReq: python3-module-funcsigs
%endif

%py_requires funcsigs

%description
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

%package -n python3-module-%oname
Summary: NumPy aware dynamic compiler for Python
Group: Development/Python3
%py3_requires funcsigs

%description -n python3-module-%oname
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

%package -n python3-module-%oname-tests
Summary: Tests for numba
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

This package contains tests for numba.

%package tests
Summary: Tests for numba
Group: Development/Python
Requires: %name = %EVR

%description tests
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

This package contains tests for numba.

%package docs
Summary: Documentation for numba
Group: Development/Documentation
BuildArch: noarch

%description docs
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

This package contains documentation for numba.

%package pickles
Summary: Pickles for numba
Group: Development/Python

%description pickles
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

This package contains pickles for numba.

%prep
%setup

sed -i 's|@VERSION@|%version|' %oname/_version.py

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag %version

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%add_optflags -fno-strict-aliasing
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS CHANGE_LOG LICENSE *.md *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if 0
%files tests
%python_sitelibdir/*/test*
%python_sitelibdir/*/*/test*
%endif

%files docs
#doc docs/*.pdf docs/*.txt docs/ams_presentation/*.pdf
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGE_LOG LICENSE *.md *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.0-alt1.git20150202
- Version 0.16.0

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.1-alt1.git20141208
- Version 0.15.1

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.4-alt2.git20140815
- Avoid requirement on llvm (in future need llvmlite)

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.4-alt1.git20140815
- Version 0.13.4
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.3-alt1.git20140711
- Version 0.13.3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2.git20131120
- New snapshot

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2.git20130917
- Excluded tests

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.git20130917
- Version 0.11

* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20130304
- Initial build for Sisyphus

