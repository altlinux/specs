%define _unpackaged_files_terminate_build 1

%def_with check

%define oname cron_descriptor

Name: python3-module-cron-descriptor
Version: 2.0.6
Release: alt1

Summary: A Python library that converts cron expressions into human readable strings
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/cron-descriptor
VCS: https://github.com/Salamek/cron-descriptor

BuildArch: noarch

Source0: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%description
A Python library that converts cron expressions
into human readable strings. Ported to Python from
https://github.com/bradyholt/cron-expression-descriptor.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/tools

%changelog
* Sat Mar 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.0.6-alt1
- NMU: 1.4.5 -> 2.0.6 (ALT #58141)

* Tue Oct 15 2024 Yaroslav Bahtin <alpacost@altlinux.org> 1.4.5-alt1
- Initial build
