%define _unpackaged_files_terminate_build 1
%define pypi_name hvac

%def_with check

Name: python3-module-%pypi_name
Version: 2.4.0
Release: alt1

Summary: HashiCorp Vault API client
License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/hvac
VCS: https://github.com/hvac/hvac
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%if_with check
BuildRequires: python3(parameterized)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(requests_mock)
BuildRequires: python3(xdist)
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
# integration tests requires vault with incompatible license
%pyproject_run_pytest -vra --ignore=tests/integration_tests

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 11 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2.4.0-alt1
- Initial build for ALT.

