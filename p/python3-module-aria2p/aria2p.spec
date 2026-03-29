%define _unpackaged_files_terminate_build 1
%define pypi_name aria2p

# tests require the Internet connection, so they are disabled
%def_without check

Name: python3-module-%pypi_name
Version: 0.12.1
Release: alt1.1

Summary: Command-line tool and library to interact with an aria2c
License: ISC
Group: Networking/File transfer
Url: https://pypi.org/project/aria2p/
VCS: https://github.com/pawamoy/aria2p

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-randomly
BuildRequires: python3-module-pytest-rerunfailures
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-responses
BuildRequires: python3-module-uvicorn

BuildRequires: python3-module-asciimatics
BuildRequires: python3-module-loguru
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-pyperclip
BuildRequires: python3-module-requests
BuildRequires: python3-module-websocket-client
BuildRequires: python3-modules-curses
%endif

%description
Command-line tool and Python library to interact
with an aria2c daemon process through JSON-RPC.

%prep
%setup
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.12.1-alt1.1
- Demodernized packaging.

* Thu Jul 24 2025 Alexey Volkov <qualimock@altlinux.org> 0.12.1-alt1
- new version 0.12.1

* Sun Mar 10 2024 Alexey Volkov <qualimock@altlinux.org> 0.12.0-alt2
- Add aria2 to dependencies

* Mon Feb 14 2024 Alexey Volkov <qualimock@altlinux.org> 0.12.0-alt1
- Initial build for ALT
