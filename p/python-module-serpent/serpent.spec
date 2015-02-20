%define oname serpent

%def_with python3

Name: python-module-%oname
Version: 1.8
Release: alt1.git20150108
Summary: Serializer for literal Python expressions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/serpent
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/irmen/Serpent.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flake8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flake8
%endif

%py_provides %oname

%description
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using
ast.literal_eval(), the serialized data is safe to transport to other
machines (over the network for instance) and de-serialize it there.

%package -n python3-module-%oname
Summary: Serializer for literal Python expressions
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using
ast.literal_eval(), the serialized data is safe to transport to other
machines (over the network for instance) and de-serialize it there.

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
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|python|python3|g' Makefile
%make test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.git20150108
- Version 1.8

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.git20140713
- Initial build for Sisyphus

