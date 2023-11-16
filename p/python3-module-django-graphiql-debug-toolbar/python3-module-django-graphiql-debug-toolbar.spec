%define pypi_name django-graphiql-debug-toolbar

%def_with check

Name:    python3-module-%pypi_name
Version: 0.2.0
Release: alt2

Summary: Django Debug Toolbar for GraphiQL IDE and Graphene
License: MIT
Group:   Development/Python3
URL:     https://github.com/flavors/django-graphiql-debug-toolbar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-graphene-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-debug-toolbar
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
rm -f %buildroot%python3_sitelibdir/LICENSE
rm -f %buildroot%python3_sitelibdir/README.md

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/graphiql_debug_toolbar/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 16 2023 Alexander Burmatov <thatman@altlinux.org> 0.2.0-alt2
- Move doc files in the right place.

* Tue Sep 26 2023 Alexander Burmatov <thatman@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus.
