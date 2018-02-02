%define oname json_resource_http

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.1.1
Summary: HTTP queryset backend for json resources
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/json_resource_http/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-json_resource python-module-nose
BuildPreReq: python-module-requests python-module-mock
BuildPreReq: python-module-json_patch
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-json_resource python3-module-nose
BuildPreReq: python3-module-requests python3-module-mock
BuildPreReq: python3-module-json_patch
%endif

%py_provides %oname

%description
HTTP queryset backend for json resources. Makes it possible to use
json-schema api's as if they were local.

%package -n python3-module-%oname
Summary: HTTP queryset backend for json resources
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
HTTP queryset backend for json resources. Makes it possible to use
json-schema api's as if they were local.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

