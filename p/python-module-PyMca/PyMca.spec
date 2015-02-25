%define oname PyMca

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 5.0.0
Release: alt1.git20150221
Summary: X-Ray Fluorescence Analysis Toolkit and Application
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PyMca/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vasole/pymca.git
Source: %name-%version.tar
# https://github.com/vasole/fisx.git
Source1: fisx.tar

BuildPreReq: gcc-c++ libqhull-devel libGLU-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-scipy python-module-PySide
BuildPreReq: python-module-sphinx-devel python-modules-json
BuildPreReq: python-modules-logging python-modules-xml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-PySide
%endif

%py_provides %oname
%py_requires json numpy scipy PySide logging xml
%add_python_req_skip pyopencl

%description
Stand-alone application and Python tools for interactive and/or batch
processing analysis of X-Ray Fluorescence Spectra. Graphical user
interface (GUI) and batch processing capabilities provided.

The associated ROI Imaging Tool extends analysis capabilities to other
techniques in which data can be represented by a three-dimensional array
like in sample scanning experiments in which a spectrum is collected at
different sample points (Raman, FT-IR, XAS, XRF, ...).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Stand-alone application and Python tools for interactive and/or batch
processing analysis of X-Ray Fluorescence Spectra. Graphical user
interface (GUI) and batch processing capabilities provided.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: X-Ray Fluorescence Analysis Toolkit and Application
Group: Development/Python3
%py3_provides %oname
%py3_requires json numpy scipy PySide logging xml
%add_python3_req_skip pyopencl

%description -n python3-module-%oname
Stand-alone application and Python tools for interactive and/or batch
processing analysis of X-Ray Fluorescence Spectra. Graphical user
interface (GUI) and batch processing capabilities provided.

The associated ROI Imaging Tool extends analysis capabilities to other
techniques in which data can be represented by a three-dimensional array
like in sample scanning experiments in which a spectrum is collected at
different sample points (Raman, FT-IR, XAS, XRF, ...).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Stand-alone application and Python tools for interactive and/or batch
processing analysis of X-Ray Fluorescence Spectra. Graphical user
interface (GUI) and batch processing capabilities provided.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Stand-alone application and Python tools for interactive and/or batch
processing analysis of X-Ray Fluorescence Spectra. Graphical user
interface (GUI) and batch processing capabilities provided.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Stand-alone application and Python tools for interactive and/or batch
processing analysis of X-Ray Fluorescence Spectra. Graphical user
interface (GUI) and batch processing capabilities provided.

This package contains documentation for %oname.

%prep
%setup

rm -fR third-party/qhull
mkdir -p third-party
pushd third-party
tar -xf %SOURCE1
rm -f fisx/python/cython/_fisx.pyx
mv "fisx/src/fisx_beam .cpp" fisx/src/fisx_beam.cpp
sed -i '$s|\(.*\)|\1\n|' fisx/python/cython/*pyx
popd

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing
export QHULL_CFLAGS="-I%_includedir/qhull"
export QHULL_LIBS="-lqhull"
%python_build_debug --fisx

%if_with python3
pushd ../python3
%python3_build_debug --fisx
popd
%endif

%install
export QHULL_CFLAGS="-I%_includedir/qhull"
export QHULL_LIBS="-lqhull"
%if_with python3
pushd ../python3
%python3_install --fisx
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install --fisx

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
sphinx-build -b pickle -d _build/doctrees source _build/pickle
sphinx-build -b html -d _build/doctrees source _build/html
install -d %buildroot%python_sitelibdir/%oname
cp -fR _build/pickle %buildroot%python_sitelibdir/%oname/
popd

%check
export QHULL_CFLAGS="-I%_includedir/qhull"
export QHULL_LIBS="-lqhull"
python setup.py test --fisx
%if_with python3
pushd ../python3
python3 setup.py test --fisx
popd
%endif

%files
%doc *.txt README
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*
%_man1dir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt README
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1.git20150221
- Initial build for Sisyphus

