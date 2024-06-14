%define pypi_name graphene-django
%define mod_name  graphene_django

%def_with check

Name:    python3-module-%pypi_name
Version: 3.2.2
Release: alt1

Summary: Build powerful, efficient, and flexible GraphQL APIs with seamless Django integration
License: MIT
Group:   Development/Python3
URL:     https://github.com/graphql-python/graphene-django

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-graphql-relay
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-promise
BuildRequires: python3-module-graphene
BuildRequires: python3-module-text-unidecode
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-pytest-random-order
BuildRequires: python3-module-django-filter
BuildRequires: python3-module-djangorestframework
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Graphene-Django is an open-source library that provides seamless integration
between Django, a high-level Python web framework, and Graphene,
a library for building GraphQL APIs. The library allows developers to create
GraphQL APIs in Django quickly and efficiently while maintaining
a high level of performance.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/*.py
%python3_sitelibdir/%mod_name/__pycache__/
%python3_sitelibdir/%mod_name/filter/
%python3_sitelibdir/%mod_name/forms/
%python3_sitelibdir/%mod_name/management/
%python3_sitelibdir/%mod_name/rest_framework/
%python3_sitelibdir/%mod_name/static/
%python3_sitelibdir/%mod_name/templates/
%python3_sitelibdir/%mod_name/utils/
%python3_sitelibdir/%mod_name/debug/
%python3_sitelibdir/%mod_name/tests/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Jun 13 2024 Anton Vyatkin <toni@altlinux.org> 3.2.2-alt1
- (NMU) New version 3.2.2.

* Mon Apr 15 2024 Anton Vyatkin <toni@altlinux.org> 3.2.1-alt1
- (NMU) New version 3.2.1.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 3.2.0-alt1
- New 3.2.0 version.

* Wed Oct 04 2023 Alexander Burmatov <thatman@altlinux.org> 3.1.5-alt1
- Initial build for Sisyphus.
