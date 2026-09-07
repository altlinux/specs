%define _unpackaged_files_terminate_build 1
%define pypi_name ssh-audit
%define mod_name ssh_audit

Name: python3-module-%pypi_name
Version: 3.9.0
Release: alt1

Summary: SSH server and client configuration security auditing tool
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/ssh-audit/
Vcs: https://github.com/jtesta/ssh-audit

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
ssh-audit is a tool for SSH server and client configuration auditing.
It grabs banners, recognizes device or software and operating system,
detects compression, gathers key-exchange, host-key, encryption and
message authentication code algorithms, outputs algorithm information
(available since, removed/disabled, unsafe/weak/legacy, etc.), outputs
algorithm recommendations (append or remove based on recognized software
version), outputs security information (related issues, assigned CVE
list, etc.), analyzes SSH version compatibility based on algorithm
information, provides historical information from OpenSSH, Dropbear SSH
and libssh, runs on Linux and Windows, and has no dependencies.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
install -Dpm 0644 %pypi_name.1 %buildroot%_man1dir/%pypi_name.1

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%_bindir/%pypi_name
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%mod_name-*.dist-info/
%_man1dir/%pypi_name.1*

%changelog
* Mon Sep 07 2026 Denis Rastyogin <gerben@altlinux.org> 3.9.0-alt1
- Initial build for ALT Linux.
