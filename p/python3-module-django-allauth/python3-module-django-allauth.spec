%define _unpackaged_files_terminate_build 1
%define pypi_name django-allauth
%define mod_name allauth

%def_with check

Name: python3-module-%pypi_name
Version: 65.19.4
Release: alt1
Summary: Integrated set of Django applications for account authentication
License: MIT
Group: Development/Python3
URL: https://allauth.org/
VCS: https://codeberg.org/allauth/django-allauth.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

# manually manage dependencies
AutoReq: yes, nopython3
%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-django-dbbackend-sqlite3
#not packaged in Sisyphus
%add_pyproject_deps_check_filter django-ninja
%add_pyproject_deps_check_filter djlint
%add_pyproject_deps_check_filter pylsp-rope
%pyproject_builddeps_check
%endif

%description
Integrated set of Django applications addressing authentication,
registration, account management as well as 3rd party (social)
account authentication.

%prep
%setup
%pyproject_scm_init %version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

# django-ninja is not packaged in Sisyphus. Use the account-only test settings
# to skip optional headless/socialaccount/idp/mfa tests that need unavailable
# dependencies (including the SAML xmlsec runtime).
%check
export DJANGO_SETTINGS_MODULE=tests.projects.account_only.settings
%pyproject_run_pytest -vra --ds=tests.projects.account_only.settings

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Sep 21 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 65.19.4-alt1
- Initial build for ALT.
