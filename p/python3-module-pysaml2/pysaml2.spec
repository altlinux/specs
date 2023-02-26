%define pypi_name pysaml2

%def_without check

Name:    python3-module-%pypi_name
Version: 7.4.1
Release: alt1

Summary: Python implementation of SAML2
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/IdentityPython/pysaml2

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-pytz
BuildRequires: python3-module-OpenSSL
BuildRequires: python3-module-xmlschema
%endif

%add_python3_req_skip ConfigParser cookielib repoze.who.plugins.form urlparse

BuildArch: noarch

Source: %name-%version.tar

%description
PySAML2 is a pure python implementation of SAML Version 2 Standard.
It contains all necessary pieces for building a SAML2 service provider
or an identity provider. The distribution contains examples of both.
Originally written to work in a WSGI environment there are extensions
that allow you to use it with other frameworks.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%_bindir/make_metadata
%_bindir/mdexport
%_bindir/merge_metadata
%_bindir/parse_xsd2
%python3_sitelibdir/saml2
%python3_sitelibdir/saml2test
%python3_sitelibdir/utility
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Feb 26 2023 Grigory Ustinov <grenka@altlinux.org> 7.4.1-alt1
- Automatically updated to 7.4.1.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 7.4.0-alt1
- Automatically updated to 7.4.0.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 4.6.5-alt2
- Drop python2 support.

* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 4.6.5-alt1
- 4.6.5
- add python3 package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- Initial build


