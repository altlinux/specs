%define oname jsonschema

%def_with python3

Name:		python-module-%oname
Version:	2.4.0
Release:	alt1
Summary:	An implementation of JSON Schema validation for Python

License:	MIT
Group:		Development/Python
URL:		http://pypi.python.org/pypi/jsonschema/
Source0:	%name-%version.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json python-module-nose python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-mock
%endif

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%package -n python3-module-%oname
Summary: An implementation of JSON Schema validation for Python
Group: Development/Python3

%description -n python3-module-%oname
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst COPYING
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst COPYING
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0
- Added module for Python 3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt1
- Initial release for Sisyphus (based on Fedora)
