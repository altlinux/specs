%define _unpackaged_files_terminate_build 1
%define pypi_name django-bulk-signals
%define mod_name bulk_signals

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.2
Release: alt2

Summary: A product aggregation function to a postgres database and makes it available with django
License: MIT
Group: Development/Python3
Url: https://github.com/awmath/django-bulk-signals
Vcs: https://github.com/awmath/django-bulk-signals.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-django-dbbackend-sqlite3
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This django library adds signals for the bulk database actions
provided by django (bulk_create, bulk_update and QuerySet.update).

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
rm -r %buildroot/%python3_sitelibdir/%mod_name/tests

%check
%pyproject_run_pytest

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jul 11 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.4.2-alt2
- Removed tests from package installation (closes: #55176).

* Thu Jul 03 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 0.4.2-alt1
- Initial build for ALT.
