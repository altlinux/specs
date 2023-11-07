%define _unpackaged_files_terminate_build 1
%define pypi_name comm
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt1
Summary: Python Comm implementation for the Jupyter kernel protocol
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/comm/
VCS: https://github.com/ipython/comm
BuildArch: noarch
Source: %name-%version.tar

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(traitlets)
%endif

%description
It provides a way to register a Kernel Comm implementation, as per the Jupyter
kernel protocol. It also provides a base Comm implementation and a default
CommManager that can be used.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v --color=no

%files
%doc *.md LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 07 2023 Anton Vyatkin <toni@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Thu Aug 03 2023 Anton Vyatkin <toni@altlinux.org> 0.1.4-alt1
- New version 0.1.4.

* Fri Jun 09 2023 Anton Vyatkin <toni@altlinux.org> 0.1.3-alt1
- New version 0.1.3

* Sat Mar 11 2023 Anton Vyatkin <toni@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus
