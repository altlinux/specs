%define pypi_name django-tree-queries
%define mod_name tree_queries

%def_with check

Name:    python3-module-%pypi_name
Version: 0.19
Release: alt1

Summary: Adjacency-list trees for Django using recursive common table expressions
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/feincms/django-tree-queries

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary. Supports PostgreSQL, sqlite, MySQL and MariaDB.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=$PWD/tests
export DJANGO_SETTINGS_MODULE=tests.testapp.settings
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/django_tree_queries-%version.0.dist-info/

%changelog
* Tue Mar 18 2025 Alexander Burmatov <thatman@altlinux.org> 0.19-alt1
- Initial build for Sisyphus.
