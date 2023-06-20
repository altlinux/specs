%define _unpackaged_files_terminate_build 1
%define pypi_name json5

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.14
Release: alt1

Summary: A Python implementation of the JSON5 data format
License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/json5/
VCS: https://github.com/dpranke/pyjson5
BuildArch: noarch
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%_bindir/pyjson5
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jun 16 2023 Anton Vyatkin <toni@altlinux.org> 0.9.14-alt1
- Initial build for Sisyphus
