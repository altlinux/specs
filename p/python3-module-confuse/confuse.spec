%define _unpackaged_files_terminate_build 1
%define pypi_name confuse

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.1
Release: alt1
Summary: Painless YAML configuration
License: MIT
Group: Development/Python3
Url: https://github.com/beetbox/confuse
Vcs: https://pypi.org/project/confuse/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-flit-core
BuildRequires: python3-module-yaml

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus.

