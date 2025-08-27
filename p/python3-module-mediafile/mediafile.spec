%define _unpackaged_files_terminate_build 1
%define pypi_name mediafile

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1
Summary: elegant audio file tagging
License: MIT
Group: Development/Python3
Url: https://github.com/beetbox/mediafile
Vcs: https://pypi.org/project/mediafile/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch
Patch1: fix-wav-frames.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-flit-core
BuildRequires: python3-module-mutagen
BuildRequires: python3-module-filetype
BuildRequires: python3(six)


%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject


%files
%doc *.rst
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.