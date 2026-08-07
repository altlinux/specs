%define _unpackaged_files_terminate_build 1
%define pypi_name meshcore
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.3.8
Release: alt1
Summary: Python bindings for meshcore
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/meshcore
VCS: https://github.com/meshcore-dev/meshcore_py.git

BuildArch: noarch

Source: %name-%version.tar

# PyPI wellknown name
%py3_provides %pypi_name

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-asyncio)
BuildRequires: python3(Crypto)
BuildRequires: python3(bleak)
BuildRequires: python3(pycayennelpp)
BuildRequires: python3(pyserial-asyncio-fast)
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 05 2026 Vasiliy Doylov <neko@altlinux.org> 2.3.8-alt1
- Initial build for ALT.
