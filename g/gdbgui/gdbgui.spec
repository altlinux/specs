%define _unpackaged_files_terminate_build 1

%def_with check

Name:    gdbgui
Version: 0.15.2.0
Release: alt2

Summary: Browser-based frontend to gdb (gnu debugger)
License: GPL-3.0
Group:   Development/Python3
URL:     https://www.gdbgui.com/
VCS:     https://github.com/cs01/gdbgui

BuildRequires(pre): rpm-build-pyproject
BuildRequires: /proc
BuildRequires: yarn
BuildRequires: node-webpack-cli
BuildRequires: node-cross-env
BuildRequires: node-cross-spawn

%pyproject_runtimedeps_metadata 
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: node_modules.tar.gz

Patch: %name-%version-alt.patch

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
%setup -n %name-%version
%setup -a 2
%patch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
yarn build --offline
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}

%files docs
%doc docs/*
%doc examples

%changelog
* Sat Oct 28 2023 Andrey Limachko <liannnix@altlinux.org> 0.15.2.0-alt2
- Fix missing js files

* Fri Oct 20 2023 Andrey Limachko <liannnix@altlinux.org> 0.15.2.0-alt1
- Initial build for Sisyphus
