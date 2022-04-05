%define oname suds-py3

Name: python3-module-suds
Version: 1.4.5.0
Release: alt1

Summary: Lightweight SOAP python client for consuming Web Services

License: LGPLv3+
Group: Development/Python3
Url: https://github.com/cackharot/suds-py3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

#BuildRequires: python3-module-setuptools

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
%python3_build

%install
%python3_install
%python3_prune

%files
%doc README.md
%python3_sitelibdir/suds/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.5.0-alt1
- new version 1.4.5.0 (with rpmrb script)

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.1.0-alt1
- build python3 package separately, cleanup spec
- switched to suds-py3 upstream (fork of the original suds)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4-alt2.2
- (NMU) rebuild with python3.6

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
