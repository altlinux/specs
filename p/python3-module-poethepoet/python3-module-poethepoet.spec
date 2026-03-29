%define _unpackaged_files_terminate_build 1
%define pypi_name poethepoet

Name: python3-module-%pypi_name
Version: 0.42.1
Release: alt1.1

Summary: A task runner that works well with poetry and uv
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/poethepoet
Vcs: https://github.com/nat-n/poethepoet

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
A task runner that works well with poetry and uv.

Poethepoet (or just "poe") is a simple task runner that works particularly
well with Python projects that use Poetry as their build tool. It provides
a standard way to define and run tasks for your project, from the command
line or from within your preferred editor or IDE.

Key features:
- Define project tasks in your pyproject.toml
- Support for shell commands, Python scripts, and more
- Environment variable management
- Task dependencies and conditional execution
- Poetry plugin integration

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/poe
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.42.1-alt1.1
- Demodernized packaging.

* Tue Mar 10 2026 Denis Rastyogin <gerben@altlinux.org> 0.42.1-alt1
- Updated to 0.42.1.

* Tue Sep 02 2025 Denis Sergeev <zeff@altlinux.org> 0.37.0-alt1
- 0.36.0 -> 0.37.0.

* Tue Jul 01 2025 Denis Sergeev <zeff@altlinux.org> 0.36.0-alt1
- Initial build for ALT.
