%define _unpackaged_files_terminate_build 1
%define pypi_name ffmpy

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.0
Release: alt1
Summary: Pythonic interface for FFmpeg and FFprobe command line
License: MIT
Group: Development/Python3
Url: https://github.com/Ch00k/ffmpy
Vcs: https://pypi.org/project/ffmpy/
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(psutil)
BuildRequires: psutils 
BuildRequires: python3-module-psutil-home-assistant
BuildRequires: python3-module-uv-build
BuildRequires: ffmpeg
BuildRequires: uv-build
BuildRequires: python3
BuildRequires: uv
BuildRequires: python3(mypy)
BuildRequires: python3-module-mypy_extensions
BuildRequires: python3-module-pathspec
BuildRequires: python3-module-coverage
BuildRequires: python3-module-typing_extensions
BuildRequires: python3(iniconfig)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3-module-pytest-mypy
BuildRequires: python3-module-pytest-mypy-plugins
BuildRequires: python3-module-pytest-cov
%endif

Requires: ffmpeg

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
#no audio during build 
#pyproject_run_pytest

%files
%doc README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
