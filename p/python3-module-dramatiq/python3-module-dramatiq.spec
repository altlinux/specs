%define _unpackaged_files_terminate_build 1
%define pypi_name dramatiq

# tests require rabbitmq, redis, prometheus running services
%def_without check

Name: python3-module-%pypi_name
Version: 1.14.2
Release: alt1

Summary: A fast and reliable distributed task processing library for Python 3
License: GPL-3.0 or LGPL-3.0
Group: Development/Python3
Vcs: https://github.com/Bogdanp/dramatiq
Url: https://pypi.org/project/dramatiq/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
BuildRequires: python3(pytest-benchmark)
BuildRequires: python3(prometheus-client)
BuildRequires: python3(pylibmc)
BuildRequires: python3(redis)
BuildRequires: python3(pika)
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
%tox_check_pyproject

%files
%doc COPYING COPYING.LESSER README.md
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.14.2-alt1
- New version.

* Wed Oct 05 2022 Anton Zhukharev <ancieg@altlinux.org> 1.13.0-alt1
- initial build for Sisyphus

