%define oname mirakuru

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20141013.1.1.1
Summary: Process executor for tests
License: LGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/mirakuru/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ClearcodeHQ/mirakuru.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-pytest-cov python-module-mock
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-pytest-cov python3-module-mock
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-coverage python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pbr python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-unittest2
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-mock python-module-objects.inv python-module-pytest-cov python-module-setuptools python3-module-html5lib python3-module-mock python3-module-pytest-cov python3-module-setuptools rpm-build-python3 time

%description
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

%package -n python3-module-%oname
Summary: Process executor for tests
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Maybe you want to be able to start database only when you start your
program, or maybe you need just to set up additional processes for your
tests, this is where you should consider using mirakuru, to add
superpowers to your program, or tests.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
touch tests/__init__.py
python setup.py test
%if_with python3
pushd ../python3
touch tests/__init__.py
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20141013.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141013.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141013.1
- NMU: Use buildreq for BR.

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141013
- Initial build for Sisyphus

