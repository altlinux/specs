%define _unpackaged_files_terminate_build 1

%def_without check

Name:    python3-module-espeak
Version: 0.6.3
Release: alt1

Summary: Python C extension for the eSpeak speech synthesizer
License: GPL-3.0
Group:   Development/Python3
Url:     https://github.com/asrp/python-espeak

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel
BuildRequires: espeak-ng-devel
BuildRequires: gcc-c++

%description
%summary

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
* Sat Nov 02 2024 Artem Semenov <savoptik@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus
