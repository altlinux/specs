%define _unpackaged_files_terminate_build 1
%define pypi_name lap

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.12
Release: alt1
Summary: Linear Assignment Problem solver
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/gatagat/lap
Vcs: https://pypi.org/project/lap/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(numpy)
BuildRequires: python3(Cython)
BuildRequires: gcc-c++
BuildRequires: clang
BuildRequires: libnumpy-py3-devel
BuildRequires: boost-python3-devel


%if_with check
BuildRequires: python3(pytest)
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
#package don't have tests
#pyproject_run_pytest tests


%files
%doc README.md
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 0.5.12-alt1
- Initial build for Sisyphus.