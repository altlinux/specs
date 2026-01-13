%define _unpackaged_files_terminate_build 1
%define pypi_name prison
%define mod_name prison

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.1
Release: alt1
Summary: Python encoder/decoder for Rison
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/prison/
Vcs: https://github.com/betodealmeida/python-rison
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-six
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
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jan 13 2026 Alexey Rodygin <alehandro@altlinux.org> 0.2.1-alt1
- Initial build for ALT Linux
