%define _unpackaged_files_terminate_build 1
%define oname django-auth-ldap

%def_with check

Name: python3-module-%oname
Version: 5.1.0
Release: alt1

Summary: Django authentication backend that authenticates against an LDAP service.
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/django-auth-ldap/django-auth-ldap.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3-module-ldap

%if_with check
BuildRequires: openldap-clients
BuildRequires: openldap-servers
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
This is a Django authentication backend that authenticates against
an LDAP service. Configuration can be as simple as a single
distinguished name template, but there are many rich configuration
options for working with users, groups, and permissions.

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_DJANGO_AUTH_LDAP=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SETUPTOOLS_SCM_PRETEND_VERSION_FOR_DJANGO_AUTH_LDAP=%version
%pyproject_build

%install
%pyproject_install

%check
export BIN="$PATH:%_sbindir"
python3 -Wa -b -m django test --settings tests.settings

%files
%doc *.rst LICENSE
%python3_sitelibdir/*


%changelog
* Mon Apr 07 2025 Evgeny Sinelnikov <sin@altlinux.org> 5.1.0-alt1
- 4.8.0 -> 5.1.0

* Wed Apr 10 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 4.8.0-alt1
- 4.3.0 -> 4.8.0

* Tue Jun 13 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 4.3.0-alt1
- new version 4.3.0

* Tue Aug 30 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 4.1.0-alt1
- Initial build for ALT Linux
