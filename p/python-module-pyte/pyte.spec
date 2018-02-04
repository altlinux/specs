%define oname pyte

%def_with python3

Name: python-module-%oname
Version: 0.4.9
Release: alt1.git20141204.1.1.1
Summary: Simple VTXXX-compatible terminal emulator
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pyte/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/selectel/pyte.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python3-module-setuptools rpm-build-python3 time
BuildRequires: python-module-pytest
BuildRequires: python3-module-pytest

%description
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

%package -n python3-module-%oname
Summary: Simple VTXXX-compatible terminal emulator
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
It's an in memory VTXXX-compatible terminal emulator. XXX stands for a
series of video terminals, developed by DEC between 1970 and 1995. The
first, and probably the most famous one, was VT100 terminal, which is
now a de-facto standard for all virtual terminal emulators. pyte follows
the suit.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
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

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS CHANGES README examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.9-alt1.git20141204.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.9-alt1.git20141204.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1.git20141204.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20141204
- Initial build for Sisyphus

