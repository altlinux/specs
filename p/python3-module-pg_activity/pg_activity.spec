%define pypi_name pg_activity

%def_with check

Name:    python3-module-%pypi_name
Version: 3.5.1
Release: alt1

Summary: Top like application for PostgreSQL server activity monitoring
License: PostgreSQL
Group:   Development/Python3
URL:     https://github.com/dalibo/pg_activity

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%if_with check
BuildRequires: codespell
BuildRequires: python3(attrs)
BuildRequires: python3(blessed)
BuildRequires: python3(humanize)
BuildRequires: python3(mypy)
BuildRequires: python3(psutil)
BuildRequires: python3(psycopg)
BuildRequires: python3(psycopg2)
BuildRequires: python3(typing_extensions)
BuildRequires: pkgconfig(libpq)
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%pypi_name is a top like application for PostgreSQL server activity monitoring.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# XXX: Exclude tests which requires orphaned and early removed modules
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest -k 'not test_data and not test_ui'

%files
%doc *.md LICENSE.txt
%_bindir/%pypi_name
%python3_sitelibdir/pgactivity
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Nov 28 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus.
