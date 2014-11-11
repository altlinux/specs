%define oname projex_orb

%def_without python3

Name: python-module-%oname
Version: 4.0.0
Release: alt1.git20140719
Summary: ORB stands for Object Relation Builder and is simple to use database class generator
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/projex_orb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/orb.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-projex python-module-pytz
BuildPreReq: python-module-tzlocal python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-projex python3-module-pytz
BuildPreReq: python3-module-tzlocal
%endif

%py_provides orb
%py_requires json

%description
Object-oriented database object-relation mapping architecture for
Python.

%package -n python3-module-%oname
Summary: ORB stands for Object Relation Builder and is simple to use database class generator
Group: Development/Python3
%py3_provides orb
%py3_requires json

%description -n python3-module-%oname
Object-oriented database object-relation mapping architecture for
Python.

%prep
%setup

mv src/* ./

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.git20140719
- Initial build for Sisyphus

