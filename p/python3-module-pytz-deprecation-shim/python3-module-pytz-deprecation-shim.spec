%define _unpackaged_files_terminate_build 1
%define pypi_name pytz-deprecation-shim
%define mod_name pytz_deprecation_shim

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.0.post0
Release: alt2

Summary: Shims to help you safely remove pytz
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/pytz-deprecation-shim/
VCS: https://github.com/pganssle/pytz-deprecation-shim
BuildArch: noarch
Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Requires: tzdata

BuildRequires: rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
BuildRequires: tzdata
%endif

%description
%summary

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%doc README.rst CHANGELOG.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Feb 09 2023 Stanislav Levin <slev@altlinux.org> 0.1.0.post0-alt2
- Dropped dependency on python-tzdata (metadata).

* Thu Apr 21 2022 Egor Ignatov <egori@altlinux.org> 0.1.0.post0-alt1
- Initial build for ALT
