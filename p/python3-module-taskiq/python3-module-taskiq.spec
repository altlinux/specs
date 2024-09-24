%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.7
Release: alt1

Summary: Distributed task queue with full async support
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/taskiq/
Vcs: https://github.com/taskiq-python/taskiq

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%set_pyproject_deps_check_filter types-
%pyproject_builddeps_metadata_extra orjson
%pyproject_builddeps_metadata_extra cbor
%pyproject_builddeps_metadata_extra msgpack
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
%autopatch -p1

# set version manually, not via poetry
sed -i '/^version =/s/.*/version="%version"/' pyproject.toml

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
* Tue Sep 24 2024 Anton Zhukharev <ancieg@altlinux.org> 0.11.7-alt1
- Updated to 0.11.7.

* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 0.11.6-alt1
- Updated to 0.11.6.

* Thu May 16 2024 Anton Zhukharev <ancieg@altlinux.org> 0.11.3-alt1
- Updated to 0.11.3.

* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 0.11.0-alt1
- Updated to 0.11.0.

* Wed Dec 27 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.4-alt1
- Updated to 0.10.4.

* Thu Oct 19 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.2-alt1
- Updated to 0.10.2.

* Thu Oct 19 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.1-alt1
- Updated to 0.10.1.

* Wed Oct 18 2023 Anton Zhukharev <ancieg@altlinux.org> 0.10.0-alt1
- Updated to 0.10.0.

* Wed Oct 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.9.3-alt1
- Updated to 0.9.3.

* Mon Oct 02 2023 Anton Zhukharev <ancieg@altlinux.org> 0.9.2-alt1
- Updated to 0.9.2.

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
