%define _unpackaged_files_terminate_build 1

Name: kernel-hardening-checker
Version: 0.6.17.1
Release: alt1

Summary: Tool for checking Linux kernel security hardening options
License: GPL-3.0-or-later
Group: System/Kernel and hardware
URL: https://github.com/a13xp0p0v/kernel-hardening-checker

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
This tool checks the configuration of the running Linux kernel for insecure or
weak options and provides recommendations to improve kernel security hardening.
It is useful for administrators and users who want to audit and strengthen
their kernel settings.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

install -Dm0644 -t %buildroot%_man1dir/ \
                   man/kernel-hardening-checker.1

%files
%doc LICENSE.txt README.md
%_bindir/kernel-hardening-checker
%_man1dir/kernel-hardening-checker.*
%python3_sitelibdir/kernel_hardening_checker/
%python3_sitelibdir/%{pyproject_distinfo kernel_hardening_checker}

%changelog
* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.6.17.1-alt1
- Initial build for Sisyphus
