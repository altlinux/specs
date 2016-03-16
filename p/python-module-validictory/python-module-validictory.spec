%define module_name validictory

%def_with python3

Name: python-module-%module_name
Version: 1.0.0
Release: alt1.a2.1
Summary: A general purpose Python data validator.
License: MIT
Group: Development/Python
Url: http://github.com/sunlightlabs/validictory

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module %module_name

%description
A general purpose Python data validator.
Works with Python 2.6+ (Including Python 3)
Schema format based on JSON Schema Proposal (http://json-schema.org)
Contains code derived from jsonschema, by Ian Lewis and Yusuke Muraoka.

%package -n python3-module-%module_name
Summary: A general purpose Python data validator
Group: Development/Python3

%description -n python3-module-%module_name
A general purpose Python data validator.
Works with Python 2.6+ (Including Python 3)
Schema format based on JSON Schema Proposal (http://json-schema.org)
Contains code derived from jsonschema, by Ian Lewis and Yusuke Muraoka.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS.txt LICENSE.txt README.rst
%python_sitelibdir/%module_name
%python_sitelibdir/%module_name-*.egg-info
%exclude %python_sitelibdir/%module_name/tests

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS.txt LICENSE.txt README.rst
%python3_sitelibdir/%module_name
%python3_sitelibdir/%module_name-*.egg-info
%exclude %python3_sitelibdir/%module_name/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.a2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.a2
- Version 1.0.0a2
- Added module for Python 3

* Mon Aug 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt1
- Initial build for ALT Linux
