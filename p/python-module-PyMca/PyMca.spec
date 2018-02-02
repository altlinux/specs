%define oname PyMca

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 5.2.2
Release: alt1.1
Summary: X-Ray Fluorescence Analysis Toolkit and Application
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PyMca/

# https://github.com/vasole/pymca.git
Source: %name-%version.tar
# https://github.com/vasole/fisx.git
Source1: fisx.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: gcc-c++ libqhull-devel libGLU-devel
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-Cython libnumpy-devel
BuildRequires: python-module-scipy python-module-PySide
BuildRequires: python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-numpy-testing python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-scipy python3-module-PySide
BuildRequires: python3-module-html5lib python3-module-jinja2-tests python3-module-notebook python3-module-numpy-testing
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

%if_with python3
%package -n python3-module-%oname
Summary: X-Ray Fluorescence Analysis Toolkit and Application
Group: Development/Python3
%py3_provides %oname
%py3_requires json numpy scipy PySide logging xml
%add_python3_req_skip pyopencl pyopencl.array

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
%endif

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
%patch1 -p1

rm -fR third-party/{qhull,fisx}
mkdir -p third-party
pushd third-party
tar -xf %SOURCE1
rm -f fisx/python/cython/_fisx.pyx
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.2-alt1
- Update to upstream version 5.2.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.0-alt1.git20150221.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 5.0.0-alt1.git20150221.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1.git20150221
- Initial build for Sisyphus

