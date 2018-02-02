%define oname json_resource

%def_with python3

Name: python-module-%oname
Version: 0.2.11
Release: alt1.1
Summary: JSON resources are dict, and list, etc. types
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/json_resource/

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-json_pointer python-module-jsonschema
BuildPreReq: python-module-json_patch python-module-pymongo
BuildPreReq: python-module-behave
BuildPreReq: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-json_pointer python3-module-jsonschema
BuildPreReq: python3-module-json_patch python3-module-pymongo
BuildPreReq: python3-module-behave
BuildPreReq: python-tools-2to3
BuildPreReq: python3-module-pytest
%endif

%py_provides %oname

%description
JSON resources are dict, and list, etc. types. They behave like oridnary
python dicts and lists, but have extra functionality from several json
standards.

%package -n python3-module-%oname
Summary: JSON resources are dict, and list, etc. types
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JSON resources are dict, and list, etc. types. They behave like oridnary
python dicts and lists, but have extra functionality from several json
standards.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
py.test json_resource/tests/test_instance.py json_resource/tests/test_resource.py
%if_with python3
pushd ../python3
py.test3 json_resource/tests/test_instance.py json_resource/tests/test_resource.py
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.11-alt1
- Updated to upstream version 0.2.11.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

