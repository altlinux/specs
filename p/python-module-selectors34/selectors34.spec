%define oname selectors34

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.git20150715
Summary: Backport of the selectors module from Python 3.4
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/selectors34
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/berkerpeksag/selectors34.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-mock
%endif

%py_provides %oname selectors
%py_requires six

%description
selectors34 is a backport of the selectors module from Python 3.4. The
selectors module written by Charles-Fran??ois Natali. This port is based
on Victor Stinner's trollius/selectors.py port.

%if_with python3
%package -n python3-module-%oname
Summary: Backport of the selectors module from Python 3.4
Group: Development/Python3
%py3_provides %oname selectors
%py3_requires six

%description -n python3-module-%oname
selectors34 is a backport of the selectors module from Python 3.4. The
selectors module written by Charles-Fran??ois Natali. This port is based
on Victor Stinner's trollius/selectors.py port.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
ln -s %oname.py %buildroot%python_sitelibdir/selectors.py

%if_with python3
pushd ../python3
%python3_install
popd
ln -s %oname.py %buildroot%python3_sitelibdir/selectors.py
%endif

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python -c "import selectors"
python setup.py test -v
py.test -vv tests/
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c "import selectors"
python3 setup.py test -v
py.test-%_python3_version -vv tests/
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150715
- Initial build for Sisyphus

