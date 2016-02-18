%define oname PyMca

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 5.0.0
Release: alt1.git20150221.1
Summary: X-Ray Fluorescence Analysis Toolkit and Application
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PyMca/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vasole/pymca.git
Source: %name-%version.tar
# https://github.com/vasole/fisx.git
Source1: fisx.tar

#BuildPreReq: gcc-c++ libqhull-devel libGLU-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-scipy python-module-PySide
#BuildPreReq: python-module-sphinx-devel python-modules-json
#BuildPreReq: python-modules-logging python-modules-xml
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
#BuildPreReq: python3-module-scipy python3-module-PySide
%endif

%py_provides %oname
%py_requires json numpy scipy PySide logging xml
%add_python_req_skip pyopencl

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils fontconfig ipython ipython3 libGL-devel libpyside-qt4 libqt4-core libqt4-gui libqt4-opengl libqt4-svg libstdc++-devel python-base python-devel python-module-OpenGL python-module-OpenGL_accelerate python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-greenlet python-module-ipykernel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-notebook python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jupyter_client python3-module-jupyter_core python3-module-markupsafe python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xz
BuildRequires: gcc-c++ libGLU-devel libnumpy-devel libqhull-devel python-module-Cython python-module-PySide python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-numpy-testing python-module-objects.inv python-module-scipy python3-module-Cython python3-module-html5lib python3-module-jinja2-tests python3-module-notebook python3-module-numpy-testing python3-module-scipy rpm-build-python3 time

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
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 5.0.0-alt1.git20150221.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt1.git20150221
- Initial build for Sisyphus

