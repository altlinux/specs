%define oname bynamodb

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141215
Summary: High-Level DynamoDB Interface for Pythonwrapping Low-Level Interface of boto
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bynamodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/teddychoi/BynamoDB.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-boto python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-boto
%endif

%py_provides %oname
%py_requires boto

%description
High-Level DynamoDB Interface for Python wrapping Low-Level Interface of
boto.

%package -n python3-module-%oname
Summary: High-Level DynamoDB Interface for Pythonwrapping Low-Level Interface of boto
Group: Development/Python3
%py3_provides %oname
%py3_requires boto

%description -n python3-module-%oname
High-Level DynamoDB Interface for Python wrapping Low-Level Interface of
boto.

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
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141215
- Initial build for Sisyphus

