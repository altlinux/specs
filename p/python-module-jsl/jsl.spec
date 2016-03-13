%define oname jsl

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20150812.1.1
Summary: A Python DSL for defining JSON schemas
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jsl
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aromanovich/jsl.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-jsonschema python-module-coverage
#BuildPreReq: python-module-pytest-cov python-module-mock
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-jsonschema python3-module-coverage
#BuildPreReq: python3-module-pytest-cov python3-module-mock
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-coverage python-module-cssselect python-module-funcsigs python-module-functools32 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pbr python-module-pluggy python-module-py python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-unittest2 xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-jsonschema python-module-mock python-module-objects.inv python-module-pytest-cov python-module-setuptools-tests python3-module-html5lib python3-module-jsonschema python3-module-mock python3-module-pytest-cov python3-module-setuptools-tests rpm-build-python3 time

%description
JSL is a Python DSL for defining JSON Schemas.

%if_with python3
%package -n python3-module-%oname
Summary: A Python DSL for defining JSON schemas
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip UserDict

%description -n python3-module-%oname
JSL is a Python DSL for defining JSON Schemas.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
JSL is a Python DSL for defining JSON Schemas.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
JSL is a Python DSL for defining JSON Schemas.

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

%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
PYVER=%_python_version ./test.sh
%if_with python3
pushd ../python3
python3 setup.py test -v
PYVER=%_python3_version ./test.sh
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20150812.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1.git20150812.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150812
- Initial build for Sisyphus

