%define _unpackaged_files_terminate_build 1
%define oname django-auth-ldap

Name: python3-module-%oname
Version: 4.1.0
Release: alt1

Summary: Django authentication backend that authenticates against an LDAP service.
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/django-auth-ldap/django-auth-ldap.git
BuildArch: noarch

Source: %name-%version.tar
Patch1: add_setup_py.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-ldap

%description
This is a Django authentication backend that authenticates against
an LDAP service. Configuration can be as simple as a single
distinguished name template, but there are many rich configuration
options for working with users, groups, and permissions.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install --install-lib=%python3_sitelibdir

%files
%doc *.rst LICENSE
%python3_sitelibdir/*


%changelog
* Tue Aug 30 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 4.1.0-alt1
- Initial build for ALT Linux
