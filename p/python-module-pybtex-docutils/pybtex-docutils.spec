%define oname pybtex-docutils

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.a0.git20141208
Summary: A docutils backend for pybtex
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pybtex-docutils
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mcmtroffaes/pybtex-docutils.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-docutils python-module-pybtex
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-coverage
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-docutils python3-module-pybtex
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides pybtex_docutils
%py_requires docutils pybtex six

%description
A docutils backend for pybtex.

%if_with python3
%package -n python3-module-%oname
Summary: A docutils backend for pybtex
Group: Development/Python3
%py3_provides pybtex_docutils
%py3_requires docutils pybtex six

%description -n python3-module-%oname
A docutils backend for pybtex.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A docutils backend for pybtex.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
%make -C doc pickle
%make -C doc html
install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=$PWD
coverage run --source=pybtex_docutils $(type -p nosetests) -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=$PWD
coverage3 run --source=pybtex_docutils $(type -p nosetests3) -vv
popd
%endif

%files
%doc *.rst doc/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.a0.git20141208
- Initial build for Sisyphus

