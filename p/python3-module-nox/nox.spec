%define pypi_name nox

%def_with check

Name:    python3-module-%pypi_name
Version: 2025.2.9
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
%endif

BuildArch: noarch

Source: %name-%version.tar

Patch: c1e1d8cda77a51a67b58ba0ccd8983d027f5de73.patch

%description
nox is a command-line tool that automates testing in multiple Python
environments, similar to tox. Unlike tox, Nox uses a standard Python file
for configuration.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
# test__create_venv_options uses conda
%pyproject_run_pytest -k 'not test__create_venv_options and not test_noxfile_no_script_mode'

%files
%doc LICENSE *.md
%_bindir/nox
%_bindir/tox-to-nox
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
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
