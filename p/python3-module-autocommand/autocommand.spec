%define _unpackaged_files_terminate_build 1
%define pypi_name autocommand

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.2
Release: alt1

Summary: A library to create a command-line program from a function
License: LGPLv3
Group: Development/Python3
VCS: https://github.com/Lucretiel/autocommand.git
Url: https://pypi.org/project/autocommand

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
A library to automatically generate and run simple argparse parsers from
function signatures.

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
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 21 2022 Stanislav Levin <slev@altlinux.org> 2.2.2-alt1
- 2.2.1 -> 2.2.2.

* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus.
