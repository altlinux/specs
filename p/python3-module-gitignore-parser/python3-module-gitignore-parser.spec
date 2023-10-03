%define _unpackaged_files_terminate_build 1
%define pypi_name gitignore-parser
%define mod_name gitignore_parser

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.7
Release: alt1

Summary: A spec-compliant gitignore parser for Python 3.5+
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/gitignore-parser/
Vcs: https://github.com/mherrmann/gitignore_parser

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
A spec-compliant gitignore parser for Python.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 03 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.7-alt1
- Updated to 0.1.7.

* Fri Aug 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.6-alt1
- Updated to 0.1.6.

* Fri Aug 04 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.5-alt1
- Updated to 0.1.5.

* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.3-alt1
- New version.

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.2-alt1
- initial build for Sisyphus
