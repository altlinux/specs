%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: Distributed task queue with full async support 
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/taskiq/
Vcs: https://github.com/taskiq-python/taskiq

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%set_pyproject_deps_check_filter types-
%add_pyproject_deps_check_filter autoflake
%add_pyproject_deps_check_filter wemake-python-styleguide
%add_pyproject_deps_check_filter yesqa
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Taskiq is an asynchronous distributed task queue for python. This
project takes inspiration from big projects such as Celery and Dramatiq.
But taskiq can send and run both the sync and async functions. Also, we
use PEP-612 to provide the best autosuggestions possible. But since it's
a new PEP, I encourage you to use taskiq with VS code because Pylance
understands all types correctly.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_poetry dev
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
* Fri Sep 22 2023 Anton Zhukharev <ancieg@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Sun Sep 03 2023 Anton Zhukharev <ancieg@altlinux.org> 0.8.7-alt1
- Updated to 0.8.7.

* Tue Jul 25 2023 Anton Zhukharev <ancieg@altlinux.org> 0.8.6-alt1
- Updated to 0.8.6.

* Thu Jul 20 2023 Anton Zhukharev <ancieg@altlinux.org> 0.8.4-alt1
- Updated to 0.8.4.

* Wed Jun 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.7.1-alt1
- New version.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.3-alt1
- New version.

* Sun May 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.2-alt1
- New version.

* Fri May 05 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt2
- Use rpm-build-pyproject macros.
- Don't package MIT license file.

* Mon Apr 10 2023 Anton Zhukharev <ancieg@altlinux.org> 0.4.0-alt1
- New version.

* Mon Apr 03 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.5-alt1
- New version.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.4-alt1
- New version.
- Enabled %%check.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.3-alt1
- New version.

* Tue Mar 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.0-alt1
- 0.1.4 -> 0.2.0.

* Mon Dec 19 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.4-alt1
- 0.1.4

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 0.1.3-alt1
- initial build for Sisyphus
