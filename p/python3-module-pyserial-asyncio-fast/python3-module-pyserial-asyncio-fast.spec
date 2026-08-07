%define _unpackaged_files_terminate_build 1
%define pypi_name pyserial-asyncio-fast
%define mod_name serial_asyncio_fast

%def_with check

Name: python3-module-%pypi_name
Version: 0.16
Release: alt1
Summary: Fast asyncio extension for pyserial that implements eager writes
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/meshcore
VCS: https://github.com/meshcore-dev/meshcore_py.git

BuildArch: noarch

Source: %name-%version.tar
Patch: 0.16-neko-fix-tests.patch

# PyPI wellknown name
%py3_provides %pypi_name

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(serial)
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE.txt README.rst CREDITS.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 05 2026 Vasiliy Doylov <neko@altlinux.org> 0.16-alt1
- Initial build for ALT.
