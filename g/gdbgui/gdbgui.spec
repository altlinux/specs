%define _unpackaged_files_terminate_build 1

%def_with check

Name:    gdbgui
Version: 0.15.3.0
Release: alt1

Summary: Browser-based frontend to gdb (gnu debugger)
License: GPL-3.0
Group:   Development/Python3
URL:     https://www.gdbgui.com/
VCS:     https://github.com/cs01/gdbgui

BuildRequires(pre): rpm-build-python3
BuildRequires: /proc python3-module-setuptools
BuildRequires: yarn python3-module-wheel
BuildRequires: node-webpack-cli
BuildRequires: node-cross-env
BuildRequires: node-cross-spawn

%if_with check
BuildRequires: python3-module-pytest python3-module-flask-socketio
BuildRequires: python3-module-pygdbmi python3-module-flask-compress
# required by some tests (e.g. tests/test_ptylib.py::test_pty)
BuildRequires: /dev/pts
%endif

BuildArch: noarch

Source: %name-%version.tar
Source1: node_modules.tar

%description
Gdbgui is a browser-based frontend to gdb, the gnu debugger.
You can add breakpoints, view stack traces, and more in C, C++, Go, and Rust!
It's perfect for beginners and experts. Simply run gdbgui from the terminal to
start the gdbgui server, and a new tab will open in your browser.

%package docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description docs
Gdbgui is a browser-based frontend to gdb, the gnu debugger.
You can add breakpoints, view stack traces, and more in C, C++, Go, and Rust!
It's perfect for beginners and experts. Simply run gdbgui from the terminal to
start the gdbgui server, and a new tab will open in your browser.

This package contains documentation for %name.

%prep
%setup -a1

%build
yarn build --offline
%pyproject_build

%install
%pyproject_install

%check
# see .github/workflows/tests.yml and noxfile.py
%pyproject_run_pytest -vra -k 'not test_connect'

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%files docs
%doc docs/*
%doc examples

%changelog
* Sun May 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.15.3.0-alt1
- 0.15.2.0 -> 0.15.3.0

* Tue Feb 04 2025 Stanislav Levin <slev@altlinux.org> 0.15.2.0-alt3
- Fixed FTBFS (tox 4).

* Sat Oct 28 2023 Andrey Limachko <liannnix@altlinux.org> 0.15.2.0-alt2
- Fix missing js files

* Fri Oct 20 2023 Andrey Limachko <liannnix@altlinux.org> 0.15.2.0-alt1
- Initial build for Sisyphus
