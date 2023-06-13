%define _unpackaged_files_terminate_build 1
%define oname django-auth-ldap

%def_with check

Name: python3-module-%oname
Version: 4.3.0
Release: alt1

Summary: Django authentication backend that authenticates against an LDAP service.
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/django-auth-ldap/django-auth-ldap.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-ldap

%if_with check
BuildRequires: openldap-clients
BuildRequires: openldap-servers
BuildRequires: python3(django)
BuildRequires: python3-module-django-dbbackend-sqlite3
%endif

%description
This is a Django authentication backend that authenticates against
an LDAP service. Configuration can be as simple as a single
distinguished name template, but there are many rich configuration
options for working with users, groups, and permissions.

%prep
%setup

%build
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
* Tue Jun 13 2023 Dmitry Lyalyaev <fruktime@altlinux.org> 4.3.0-alt1
- new version 4.3.0

* Tue Aug 30 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 4.1.0-alt1
- Initial build for ALT Linux
