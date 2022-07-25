%define _unpackaged_files_terminate_build 1

Name: python3-module-rcslice
Version: 1.1.0
Release: alt1

Summary: Provides Python module to slice a list of sliceables (1 indexed)
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/neurobin/rcslice
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
This package provides Python module to slice a list of sliceables (1 indexed,
both start and end index are inclusive). Helps to slice file content line by
line or column by column or a combination of both.

%prep
%setup

%build
%pyproject_build

cp LICENSE README.md %_builddir/

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/*

%changelog
* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 1.1.0-alt1
- initial build for Sisyphus

