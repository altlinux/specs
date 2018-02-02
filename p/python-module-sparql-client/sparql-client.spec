%define _unpackaged_files_terminate_build 1
%define oname sparql-client

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 3.0
Release: alt1.1
Summary: Python API to query a SPARQL endpoint
License: MPLv1.1
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sparql-client/

# https://github.com/eea/sparql-client.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-dateutil python-module-eventlet
BuildRequires: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-dateutil python3-module-eventlet
BuildRequires: python3-module-mock
%endif

%py_provides sparql
%py_requires dateutil

%description
sparql-client is a library to query a SPARQL endpoint. It will
automatically convert literals to the coresponding Python types.

%if_with python3
%package -n python3-module-%oname
Summary: Python API to query a SPARQL endpoint
Group: Development/Python3
%py3_provides sparql
%py3_requires dateutil

%description -n python3-module-%oname
sparql-client is a library to query a SPARQL endpoint. It will
automatically convert literals to the coresponding Python types.
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0-alt1
- Updated to upstream version 3.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.6-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt2.dev.git20140915
- Fixed build

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev.git20140915
- Initial build for Sisyphus

