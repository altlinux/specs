%define _unpackaged_files_terminate_build 1

%def_with check

Name: docktui
Version: 1.4.0
Release: alt1
Summary: A lightweight, zero-dependency TUI dashboard for managing Docker containers and images dynamically in the terminal.
License: MIT
Group: Sound
Url: https://github.com/strmax195-hue/docktui

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(twine)
BuildRequires: python3(ruff)
BuildRequires: python3(mypy)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-cov)
%endif

%description
DockTUI is a fast, zero-dependency terminal dashboard for monitoring,
debugging, and managing local Docker containers and images.
It is written in pure Python, talks to Docker through the Docker CLI,
and keeps your existing Docker permissions and context intact.

%prep
%setup -q
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Fri Jul 31 2026 Pavel Shilov <zerospirit@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.