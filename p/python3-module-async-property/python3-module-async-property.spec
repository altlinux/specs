%define _unpackaged_files_terminate_build 1
%define pypi_name async-property
%define mod_name async_property

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.2
Release: alt1

Summary: Python decorator for async properties.
License: MIT
Group: Development/Python3
Url: https://github.com/ryananguiano/async_property.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(anyio)
BuildRequires: python3(pytest-asyncio)
BuildRequires: python3-module-pytest-trio
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests

%files
%doc *.rst LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 24 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.2.2-alt1
- Initial build for ALT Linux

