%define pypi_name pytest-console-scripts

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.1
Release: alt1

Summary: Pytest plugin for testing console scripts
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pytest-console-scripts/
VCS: https://github.com/kvas-it/pytest-console-scripts

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Pytest-console-scripts is a pytest plugin for running python scripts from
within tests. It's quite similar to subprocess.run(), but it also has an
in-process mode, where the scripts are executed by the interpreter that's
running pytest (using some amount of sandboxing).

%prep
%setup -n %pypi_name-%version
%pyproject_scm_init

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%python3_sitelibdir/pytest_console_scripts
%python3_sitelibdir/%{pyproject_distinfo pytest_console_scripts}

%changelog
* Wed Jun 14 2023 Anton Vyatkin <toni@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
