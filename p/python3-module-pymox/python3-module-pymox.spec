%define pypi_name pymox
%define mod_name mox

%def_with check

Name:    python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: Pymox - Powerful and intuitive mock object framework for Python
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/ivancrneto/pymox

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
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
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 16 2025 Alexander Burmatov <thatman@altlinux.org> 1.4.0-alt1
- New 1.4.0 version.

* Tue Jan 09 2024 Alexander Burmatov <thatman@altlinux.org> 1.3.0-alt1
- New 1.3.0 version.

* Mon Oct 23 2023 Alexander Burmatov <thatman@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
