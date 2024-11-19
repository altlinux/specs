%define _unpackaged_files_terminate_build 1
%define mod_name %pypi_name
%define pypi_name srt

%def_with check

Name: python3-module-%pypi_name

Version: 3.5.3
Release: alt1
Summary: srt is a tiny but featureful Python library for parsing, modifying, and composing SRT files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/srt/
Vcs: https://github.com/cdown/srt

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(sphinx)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-cov
BuildRequires: python3(hypothesis)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%_bindir/*
%python3_sitelibdir/%pypi_name.*
%python3_sitelibdir/srt_tools/
%python3_sitelibdir/__pycache__/%pypi_name.cpython*
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
* Tue Nov 12 2024 Pavel Shilov <zerospirit@altlinux.org> 3.5.3-alt1
- initial build for Sisyphus
