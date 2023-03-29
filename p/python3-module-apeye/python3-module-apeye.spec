%define _unpackaged_files_terminate_build 1
%define pypi_name apeye

# tests disabled due to Internet connection requirement
%def_without check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Handy tools for working with URLs and APIs
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/apeye/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(flit)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(pytest_timeout)
BuildRequires: python3(pytest_httpserver)
BuildRequires: python3(pytest-datadir)
BuildRequires: python3(coverage)
BuildRequires: python3(coverage-pyver-pragma)
BuildRequires: python3(tox)
BuildRequires: python3(tox-envlist)
BuildRequires: python3(coincidence)
BuildRequires: python3(cachecontrol)
BuildRequires: python3(cherrypy)
BuildRequires: python3(yaml)
BuildRequires: python3-module-ruamel-yaml
BuildRequires: python3-module-ruamel-yaml.clib
%endif

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- New version.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- initial build for Sisyphus

