%define oname jsondatabase

%def_with python3

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150214.1.1
Summary: A flat file database for json objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jsondatabase/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gunthercox/jsondb.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname jsondb
%py_requires json

%description
This is a utility for managing content in a database which stores
content in JSON format.

%package -n python3-module-%oname
Summary: A flat file database for json objects
Group: Development/Python3
%py3_provides %oname jsondb
%py3_requires json

%description -n python3-module-%oname
This is a utility for managing content in a database which stores
content in JSON format.

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
%doc *.rst *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.3-alt1.git20150214.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150214.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150214
- Initial build for Sisyphus

