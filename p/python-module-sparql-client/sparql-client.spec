%define oname sparql-client

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 1.7
Release: alt1.dev.git20140915
Summary: Python API to query a SPARQL endpoint
License: MPLv1.1
Group: Development/Python
Url: https://pypi.python.org/pypi/sparql-client/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/sparql-client.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dateutil python-module-pycurl2
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dateutil python3-module-pycurl2
BuildPreReq: python3-module-mock
%endif

%py_provides sparql
%py_requires dateutil

%description
sparql-client is a library to query a SPARQL endpoint. It will
automatically convert literals to the coresponding Python types.

%package -n python3-module-%oname
Summary: Python API to query a SPARQL endpoint
Group: Development/Python3
%py3_provides sparql
%py3_requires dateutil

%description -n python3-module-%oname
sparql-client is a library to query a SPARQL endpoint. It will
automatically convert literals to the coresponding Python types.

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
pushd tests
export PYTHONPATH=%buildroot%python_sitelibdir
for i in *.py; do
	python $i
done
popd
%if_with python3
pushd ../python3
python3 setup.py test
pushd tests
export PYTHONPATH=%buildroot%python3_sitelibdir
for i in *.py; do
	python3 $i
done
popd
popd
%endif

%files
%doc *.rst docs/*.txt docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.txt docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev.git20140915
- Initial build for Sisyphus

