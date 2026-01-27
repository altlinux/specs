%define _unpackaged_files_terminate_build 1

%def_without check

Name:    python3-module-espeak
Version: 0.6.3
Release: alt4

Summary: Python C extension for the eSpeak speech synthesizer
License: GPL-3.0
Group:   Development/Python3
Url:     https://github.com/asrp/python-espeak
VCS:     https://github.com/asrp/python-espeak.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: libespeak-devel
BuildRequires: gcc-c++

%description
This is a modified version of python-espeak.
It is a Python binding over the eSpeak speech synthesizer
C library and does not simply make calls to the `espeak` binary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/espeak/*
%python3_sitelibdir/python_espeak-%version.dist-info/*

%changelog
* Tue Jan 27 2026 Artem Semenov <savoptik@altlinux.org> 0.6.3-alt4
- Fixed FTBFS after espeak ng update

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 0.6.3-alt3
- Added description
- Cleaned-up the spec

* Sat Nov 02 2024 Artem Semenov <savoptik@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus
