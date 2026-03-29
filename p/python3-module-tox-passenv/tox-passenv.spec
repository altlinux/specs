%define _unpackaged_files_terminate_build 1
%define pypi_name tox-passenv
%define mod_name tox_passenv

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.0
Release: alt1.1
Summary: Additional environment variable names to pass into tox test env
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tox-passenv
Vcs: https://github.com/stanislavlevin/tox-passenv
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-pytest
%endif

%description
This is the backport of `tox3` functionality of `TOX_TESTENV_PASSENV` for `tox4`:

> If defined the TOX_TESTENV_PASSENV environment variable (in the tox invocation
  environment) can define additional space-separated variable names that are to
  be passed down to the test command environment.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra tests/

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.1.0-alt1.1
- Demodernized packaging.

* Thu Jan 30 2025 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
