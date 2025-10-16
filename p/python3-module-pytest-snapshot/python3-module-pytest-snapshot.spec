%define pypi_name pytest-snapshot
%define mod_name pytest_snapshot

%def_with check

Name:    python3-module-%pypi_name
Version: 0.9.0
Release: alt3

Summary: A plugin for snapshot testing with pytest
License: MIT
Group:   Development/Python3
URL:     https://github.com/joseph-roitman/pytest-snapshot

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_assert_match_failure_bytes"

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Thu Oct 16 2025 Alexander Burmatov <thatman@altlinux.org> 0.9.0-alt3
- Fix version.

* Fri Mar 22 2024 Alexander Burmatov <thatman@altlinux.org> 0.9.0-alt2
- Fix test.

* Thu Oct 19 2023 Alexander Burmatov <thatman@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
