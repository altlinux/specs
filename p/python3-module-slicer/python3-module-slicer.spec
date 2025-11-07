%define pypi_name slicer

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.8
Release: alt1

Summary: Unified slicing for all Python data structures
License: MIT
Group:   Development/Python3
URL: 	 https://pypi.org/project/slicer/
Vcs:     https://github.com/interpretml/slicer.git

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pandas 
BuildRequires: python3-module-torch
%endif

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

%description
slicer wraps tensor-like objects and provides a uniform
slicing interface via __getitem__.

It supports many data types including:
   numpy | pandas | scipy | pytorch | list | tuple | dict

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%python3_install "--install-purelib" "%python3_sitelibdir"

%check
%pyproject_run_pytest -v

%files
%doc *.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version-*.egg-info

%changelog
* Thu Nov 06 2025 Nikita Shmatko <nash@altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus.
