%define _unpackaged_files_terminate_build 1
%define pypi_name autopep8

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.0
Release: alt1

Summary: A tool that automatically formats Python code to conform to the PEP 8 style guide
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/autopep8/
Vcs: https://github.com/hhatto/autopep8

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pydiff
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
%endif

%description
autopep8 automatically formats Python code to conform to the PEP 8
style guide. It uses the pycodestyle utility to determine what parts
of the code needs to be formatted. autopep8 is capable of fixing most
of the formatting issues that can be reported by pycodestyle.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst AUTHORS.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__/%pypi_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 31 2024 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- Updated to 2.2.0.

* Thu May 30 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.2-alt1
- Updated to 2.1.2.

* Thu May 23 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.1-alt1
- Updated to 2.1.1.

* Sat Mar 30 2024 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- Updated to 2.1.0.

* Thu Feb 08 2024 Anton Zhukharev <ancieg@altlinux.org> 2.0.4-alt1.gitaf7399d
- Updated to af7399d (fixed FTBFS).

* Sun Aug 27 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.4-alt1
- Updated to 2.0.4.

* Sat Aug 26 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.3-alt1
- Updated to 2.0.3.

* Sat Mar 25 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.2-alt1
- New version.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.1-alt1
- 1.7.0 -> 2.0.1

* Sun Oct 02 2022 Anton Zhukharev <ancieg@altlinux.org> 1.7.0-alt1
- initial build for Sisyphus

