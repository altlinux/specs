%define module_name suds

Name: python-module-%module_name
Version: 0.3.9
Release: alt1.1

Summary: Lightweight SOAP python client for consuming Web Services
License: LGPLv3+
Group: Development/Python

BuildArch: noarch

Url: https://fedorahosted.org/suds/
Source: %name-%version.tar

Packager: Andrey Rahmatullin <wrar@altlinux.org>

%setup_python_module %module_name

BuildPreReq: python-module-setuptools

%description
The suds project is a python soap web services client lib.  Suds
leverages python meta programming to provide an intuative API for
consuming web services.  Objectification of types defined in the WSDL is
provided without class generation.  Programmers rarely need to read the
WSDL since services and WSDL based objects can be easily inspected.
Supports pluggable soap bindings.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%module_name/
%python_sitelibdir/*.egg-info
%doc README

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.9-alt1.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.3.9-alt1
- initial build
