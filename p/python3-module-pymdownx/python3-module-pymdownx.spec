%define _unpackaged_files_terminate_build 1

Name: python3-module-pymdownx
Version: 9.5
Release: alt1

Summary: Extensions for Python Markdown
License: MIT BSD
Group: Development/Python3
Url: https://github.com/facelessuser/pymdown-extensions
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(markdown)
BuildRequires: python3(hatchling)
BuildRequires: python3(yaml)

%description
%summary

%prep
%setup

%build
%pyproject_build

cp LICENSE.md %_builddir

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE.md
%python3_sitelibdir/*

%changelog
* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 9.5-alt1
- initial build for Sisyphus

