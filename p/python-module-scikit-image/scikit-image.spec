%define oname scikit-image

%def_with python3

Name: python-module-%oname
Version: 0.11
Release: alt1.dev.git20141124
Summary: Image processing routines for SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikit-image/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/scikit-image/scikit-image.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-matplotlib
BuildPreReq: python-module-scipy libnumpy-devel
BuildPreReq: python-module-six python-module-networkx
BuildPreReq: python-module-Pillow
BuildPreReq: python-module-sphinx-devel python-module-numpydoc xvfb-run
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-matplotlib
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-six python3-module-networkx
BuildPreReq: python3-module-Pillow
%endif

%py_provides skimage

%description
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Image processing routines for SciPy
Group: Development/Python3
%py3_provides skimage

%description -n python3-module-%oname
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

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
%make -C doc pickle
xvfb-run make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%if_disabled check
rm -f requirements.txt
%endif

%check
python setup.py test
rm -f requirements.txt
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html doc/examples viewer_examples

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20141124
- New snapshot
- Moved all tests into tests subpackage

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20141123
- Initial build for Sisyphus

