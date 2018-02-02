%define oname selectors34

%def_with python3

Name: python-module-%oname
Version: 1.2.0
Release: alt1.1
Summary: Backport of the selectors module from Python 3.4
License: Python
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/selectors34

# https://github.com/berkerpeksag/selectors34.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-mock
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-mock
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-unittest2
BuildRequires: python3-module-pytest
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
py.test3 -vv tests/
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.0-alt1
- Updated to upstream version 1.2.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150715.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.git20150715.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150715
- Initial build for Sisyphus

