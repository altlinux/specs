%define oname wrapt

%def_with python3

Name: python-module-%oname
Version: 1.9.0
Release: alt1.git20140822.1
Summary: A Python module for decorators, wrappers and monkey patching
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/wrapt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/GrahamDumpleton/wrapt.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tox
#BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tox
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python-module-tox python3-devel python3-module-tox rpm-build-python3 time python3-module-pytest

%description
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%package -n python3-module-%oname
Summary: A Python module for decorators, wrappers and monkey patching
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The aim of the wrapt module is to provide a transparent object proxy for
Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html blog

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.git20140822.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.git20140822
- Initial build for Sisyphus

