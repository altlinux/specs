%define pypi_name slicer

%def_with check

Name:    python3-module-%pypi_name
Version: 0.0.8
Release: alt3

Summary: Unified slicing for all Python data structures
License: MIT
Group:   Development/Python3
URL: 	 https://pypi.org/project/slicer
Vcs:     https://github.com/interpretml/slicer.git

BuildRequires(pre): rpm-build-python3 rpm-macros-ml
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pandas 
BuildRequires: python3-module-torch
%endif

%remove_torch_deps
Requires: pytorch

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
* Wed Feb 25 2026 Nikita Shmatko <nash@altlinux.org> 0.0.8-alt3
- Switched to rpm-macros-ml.

* Wed Feb 04 2026 Nikita Shmatko <nash@altlinux.org> 0.0.8-alt2
- Disabled python3 autorequires to avoid torch dependencies.
- Switched to virtual dependency on pytorch.

* Thu Nov 06 2025 Nikita Shmatko <nash@altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus.
