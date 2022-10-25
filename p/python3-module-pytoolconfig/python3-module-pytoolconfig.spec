%define _unpackaged_files_terminate_build 1
%define pypi_name pytoolconfig

%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.2
Release: alt2

Summary: Python tool configuration
License: LGPL-3.0
Group: Development/Python3
Vcs: https://github.com/bagel897/pytoolconfig
Url: https://pypi.org/project/pytoolconfig/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(pdm-pep517)

%if_with check
# deps
%if %tomli
BuildRequires: python3(tomli)
%endif
BuildRequires: python3(packaging)

BuildRequires: python3(pytest)
BuildRequires: python3(docutils)
BuildRequires: python3(sphinx)
BuildRequires: python3(tabulate)
BuildRequires: python3(appdirs)
%endif

BuildArch: noarch

%if %tomli
Requires: python3(tomli)
%endif

%description
The goal of this project is to manage configuration for python tools,
such as black and rope and add support for a pyproject.toml
configuration file.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 25 2022 Stanislav Levin <slev@altlinux.org> 1.2.2-alt2
- Fixed FTBFS (pdm-pep517 1.0.5).

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.2-alt1
- initial build for Sisyphus

