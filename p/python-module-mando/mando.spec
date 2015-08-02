%define oname mando

%def_with python3

Name: python-module-%oname
Version: 0.3.3
Release: alt1.git20150714
Summary: Create Python CLI apps with little to no effort at all!
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mando
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rubik/mando.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coveralls python-module-ParamUnittest
BuildPreReq: python-module-coverage python-module-tox
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coveralls python3-module-ParamUnittest
BuildPreReq: python3-module-coverage python3-module-tox
%endif

%py_provides %oname

%description
mando is a wrapper around argparse, and allows you to write complete CLI
applications in seconds while maintaining all the flexibility.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
mando is a wrapper around argparse, and allows you to write complete CLI
applications in seconds while maintaining all the flexibility.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Create Python CLI apps with little to no effort at all!
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
mando is a wrapper around argparse, and allows you to write complete CLI
applications in seconds while maintaining all the flexibility.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
mando is a wrapper around argparse, and allows you to write complete CLI
applications in seconds while maintaining all the flexibility.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
mando is a wrapper around argparse, and allows you to write complete CLI
applications in seconds while maintaining all the flexibility.

This package contains pickles for %oname.

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
export PYTHONPATH=%buildroot%python_sitelibdir
python mando/tests/run.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 mando/tests/run.py -v
popd
%endif

%files
%doc *.rst examples docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1.git20150714
- Initial build for Sisyphus

