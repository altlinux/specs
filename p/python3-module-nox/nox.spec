%define pypi_name nox

%def_with check

Name:    python3-module-%pypi_name
Version: 2026.2.9
Release: alt1

Summary: Flexible test automation for Python

License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/nox
VCS:     https://github.com/wntrblm/nox

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-argcomplete
BuildRequires: python3-module-colorlog
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-tox
BuildRequires: python3-module-dependency-groups
BuildRequires: python3-module-attrs
BuildRequires: python3-module-cowsay
BuildRequires: python3-module-humanize
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
nox is a command-line tool that automates testing in multiple Python
environments, similar to tox. Unlike tox, Nox uses a standard Python file
for configuration.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# Skipped tests:
# - test__create_venv_options requires conda
# - test_main_requires requires alternative Python interpreters
# - test_noxfile_script_mode installs from PyPI
# - test_download_python_* uses uv to install alternative Python interpreters
%pyproject_run_pytest -k "not test__create_venv_options[nox.virtualenv.CondaEnv.create-conda-CondaEnv] and \
            not test_main_requires[sessions2-expected_order2] and not test_main_requires[sessions1-expected_order1] and\
            not test_noxfile_script_mode and not test_noxfile_no_script_mode and not test_download_python_"

%files
%doc LICENSE *.md
%_bindir/nox
%_bindir/tox-to-nox
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Wed Feb 11 2026 Grigory Ustinov <grenka@altlinux.org> 2026.2.9-alt1
- Automatically updated to 2026.2.9.

* Fri Feb 06 2026 Grigory Ustinov <grenka@altlinux.org> 2025.11.12-alt1
- Automatically updated to 2025.11.12.

* Tue May 06 2025 Grigory Ustinov <grenka@altlinux.org> 2025.5.1-alt1
- Automatically updated to 2025.5.1.

* Tue Feb 11 2025 Grigory Ustinov <grenka@altlinux.org> 2025.2.9-alt1
- Automatically updated to 2025.2.9.

* Thu Oct 10 2024 Grigory Ustinov <grenka@altlinux.org> 2024.10.9-alt1
- Automatically updated to 2024.10.9.

* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 2024.4.15-alt2
- Fixed version of package.

* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 2024.04.15-alt1
- Automatically updated to 2024.04.15.

* Tue Apr 02 2024 Grigory Ustinov <grenka@altlinux.org> 2024.03.02-alt2
- Packaged also executables.

* Mon Apr 01 2024 Grigory Ustinov <grenka@altlinux.org> 2024.03.02-alt1
- Initial build for Sisyphus (Closes: #49605).
