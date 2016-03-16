%define module_name suds

%def_with python3

Name: python-module-%module_name
Version: 0.4
Release: alt2.1

Summary: Lightweight SOAP python client for consuming Web Services
License: LGPLv3+
Group: Development/Python

BuildArch: noarch

Url: https://fedorahosted.org/suds/
Source: %name-%version.tar

%setup_python_module %module_name

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
The suds project is a python soap web services client lib.  Suds
leverages python meta programming to provide an intuative API for
consuming web services.  Objectification of types defined in the WSDL is
provided without class generation.  Programmers rarely need to read the
WSDL since services and WSDL based objects can be easily inspected.
Supports pluggable soap bindings.

%package -n python3-module-%module_name
Summary: Lightweight SOAP python client for consuming Web Services
Group: Development/Python3

%description -n python3-module-%module_name
The suds project is a python soap web services client lib.  Suds
leverages python meta programming to provide an intuative API for
consuming web services.  Objectification of types defined in the WSDL is
provided without class generation.  Programmers rarely need to read the
WSDL since services and WSDL based objects can be easily inspected.
Supports pluggable soap bindings.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec \
	sed -i 's|urllib2|urllib.request|g' '{}' +
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%python_sitelibdir/%module_name/
%python_sitelibdir/*.egg-info
%doc README

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/*.egg-info
%doc README
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added module for Python 3

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.9-alt1.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.3.9-alt1
- initial build
