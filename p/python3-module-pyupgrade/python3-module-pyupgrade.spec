%define _unpackaged_files_terminate_build 1
%define pypi_name pyupgrade

%def_with check

Name: python3-module-%pypi_name
Version: 3.12.0
Release: alt1

Summary: A tool (and pre-commit hook) to automatically upgrade syntax for newer versions of the language
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyupgrade/
Vcs: https://github.com/asottile/pyupgrade

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
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Sep 22 2023 Anton Zhukharev <ancieg@altlinux.org> 3.12.0-alt1
- Updated to 3.12.0.

* Sat Sep 16 2023 Anton Zhukharev <ancieg@altlinux.org> 3.11.0-alt1
- Updated to 3.11.0.

* Tue Aug 01 2023 Anton Zhukharev <ancieg@altlinux.org> 3.10.1-alt1
- Updated to 3.10.1.

* Wed Jul 26 2023 Anton Zhukharev <ancieg@altlinux.org> 3.9.0-alt1
- Updated to 3.9.0.

* Wed May 10 2023 Anton Zhukharev <ancieg@altlinux.org> 3.4.0-alt1
- New version.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 3.3.1-alt1
- 3.2.2 -> 3.3.1

* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 3.2.2-alt1
- 2.38.2 -> 3.2.2

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 2.38.2-alt1
- initial build for Sisyphus

