%define oname datatables

%def_with python3

Name: python-module-%oname
Version: 0.4.9
Release: alt1.git20150106
Summary: Integrates SQLAlchemy with DataTables (framework agnostic)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/datatables/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/orf/datatables.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-coveralls
BuildPreReq: python-module-fake-factory python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-coveralls
BuildPreReq: python3-module-fake-factory python3-modules-sqlite3
%endif

%py_provides %oname

%description
Integrates SQLAlchemy with DataTables (framework agnostic).

%package -n python3-module-%oname
Summary: Integrates SQLAlchemy with DataTables (framework agnostic)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Integrates SQLAlchemy with DataTables (framework agnostic).

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20150106
- Version 0.4.9

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20141222
- Initial build for Sisyphus

