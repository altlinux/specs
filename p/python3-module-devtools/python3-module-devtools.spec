%define _unpackaged_files_terminate_build 1
%define pypi_name devtools

%def_with check

Name: python3-module-%pypi_name
Version: 0.12.2
Release: alt1

Summary: Dev tools for python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devtools/
Vcs: https://github.com/samuelcolvin/python-devtools

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Python's missing debug print command and other development tools.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/testing.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Don't use %%pyproject_run_pytest because it can't run the tests
# for the package properly (pytest plugins conflict).
%__python3 -m pytest

%files
%doc README.md HISTORY.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Sep 04 2023 Anton Zhukharev <ancieg@altlinux.org> 0.12.2-alt1
- Updated to 0.12.2.

* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 0.12.1-alt1
- Updated to 0.12.1.

* Fri Aug 18 2023 Anton Zhukharev <ancieg@altlinux.org> 0.12.0-alt1
- Updated to 0.12.0.

* Tue Jul 25 2023 Anton Zhukharev <ancieg@altlinux.org> 0.11.0-alt1
- Updated to 0.11.0.

* Tue May 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt2
- Temporary ignore SQLAlchemy's deprecation warning.
- Don't package LICENSE file.

* Sun Aug 07 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus

