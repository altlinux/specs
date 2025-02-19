%define oname ldapdomaindump

Name:    python3-module-%oname
Version: 0.9.4
Release: alt1

Summary: Active Directory information dumper via LDAP

Group:   Development/Python3
License: MIT
URL:     https://pypi.org/project/ldapdomaindump/

# https://files.pythonhosted.org/packages/ac/7c/16f9d8a257bd82de90bd5963556a9a17f8105596f181dee5777437ef8900/ldapdomaindump-0.9.4.tar.gz
Source0: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Active Directory information dumper via LDAP

%prep
%setup -n %oname-%version
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%build
%pyproject_build

%install
%pyproject_install

%files
%doc Readme.md LICENSE
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Feb 19 2025 L.A. Kostis <lakostis@altlinux.ru> 0.9.4-alt1
- Initial build for ALTLinux.

