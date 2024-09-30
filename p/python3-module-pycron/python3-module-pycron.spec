%define _unpackaged_files_terminate_build 1
%define pypi_name pycron

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.1
Release: alt1

Summary: Simple cron-like parser for Python, which determines if current datetime matches conditions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pycron
Vcs: https://github.com/kipe/pycron.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: python3(pytz)
BuildRequires: python3(pendulum)
BuildRequires: python3(arrow)
BuildRequires: python3(udatetime)
BuildRequires: python3(delorean)
%endif

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Sep 30 2024 Anton Vyatkin <toni@altlinux.org> 3.1.1-alt1
- New version 3.1.1.

* Tue May 02 2023 Anton Vyatkin <toni@altlinux.org> 3.0.0-alt2
- Fix BuildRequires

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 3.0.0-alt1
- initial build for Sisyphus
