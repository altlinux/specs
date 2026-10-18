%define _unpackaged_files_terminate_build 1
%define pypi_name django_countries

Name: python3-module-django-countries
Version: 9.1.0
Release: alt0.1

Summary: Provides a country field for Django models

License: MIT
Group: Development/Python3
Url: https://github.com/SmileyChris/django-countries

BuildArch: noarch

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-uv-build

# optional integrations, the user project provides them if it uses them
%add_python3_req_skip PIL graphene graphene_django rest_framework django_filters

%description
Provides a country field for Django models.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# tests need test-only dependencies
rm -rv %buildroot%python3_sitelibdir/django_countries/tests

%files
%python3_sitelibdir/django_countries/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Oct 18 2026 Vitaly Lipatov <lav@altlinux.ru> 9.1.0-alt0.1
- NMU: new version 9.1.0 (required by authentik)
- built with pyproject (uv_build) instead of setup.py, package is noarch now.
- updated license to MIT.
- do not package tests, skip requires on optional integrations.

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.0-alt2
- disable python2

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141027.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141027.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20141027
- Version 3.0.1

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.git20140829
- Version 2.1.2
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- build for ALT
