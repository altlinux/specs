%define oname ldapdomaindump

Name:    python3-module-%oname
Version: 0.10.0
Release: alt1

Summary: Active Directory information dumper via LDAP

Group:   Development/Python3
License: MIT
URL:     https://pypi.org/project/ldapdomaindump/
Vcs:     https://github.com/dirkjanm/ldapdomaindump.git

# https://github.com/dirkjanm/ldapdomaindump/commit/413ceec72fb36832b92b7afdeaa7b164ee1837fc
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
%doc README.md LICENSE
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Jul 14 2025 L.A. Kostis <lakostis@altlinux.ru> 0.10.0-alt1
- 0.10.0.

* Wed Feb 19 2025 L.A. Kostis <lakostis@altlinux.ru> 0.9.4-alt1
- Initial build for ALTLinux.

