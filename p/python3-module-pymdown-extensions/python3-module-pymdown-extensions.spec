%define _unpackaged_files_terminate_build 1
%define pypi_name pymdown-extensions
%define mod_name pymdownx

%def_with check

Name: python3-module-%pypi_name
Version: 10.9
Release: alt1

Summary: Extensions for Python Markdown
License: MIT and BSD
Group: Development/Python3
Url: https://pypi.org/project/pymdown-extensions/
Vcs: https://github.com/facelessuser/pymdown-extensions

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md LICENSE.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Jul 28 2024 Anton Zhukharev <ancieg@altlinux.org> 10.9-alt1
- Updated to 10.9.

* Thu May 16 2024 Anton Zhukharev <ancieg@altlinux.org> 10.8.1-alt1.gitf1e2fad
- Updated to 10.8.1 (f1e2fad).

* Thu Apr 11 2024 Anton Zhukharev <ancieg@altlinux.org> 10.7.1-alt1.git509e93d
- Updated to 10.7.1 (509e93d).

* Sun Dec 31 2023 Anton Zhukharev <ancieg@altlinux.org> 10.7-alt1
- Updated to 10.7.

* Wed Dec 27 2023 Anton Zhukharev <ancieg@altlinux.org> 10.6-alt1
- Updated to 10.6.

* Mon Dec 11 2023 Anton Zhukharev <ancieg@altlinux.org> 10.5-alt1
- Updated to 10.5.

* Wed Nov 15 2023 Anton Zhukharev <ancieg@altlinux.org> 10.4-alt1
- Updated to 10.4.

* Thu Oct 19 2023 Anton Zhukharev <ancieg@altlinux.org> 10.3.1-alt1
- Updated to 10.3.1.

* Sun Sep 03 2023 Anton Zhukharev <ancieg@altlinux.org> 10.3-alt1
- Updated to 10.3.

* Wed Aug 30 2023 Anton Zhukharev <ancieg@altlinux.org> 10.2.1-alt1
- Updated to 10.2.1.

* Tue Aug 29 2023 Anton Zhukharev <ancieg@altlinux.org> 10.2-alt1
- Updated to 10.2.

* Fri Aug 18 2023 Anton Zhukharev <ancieg@altlinux.org> 10.1-alt1
- Updated to 10.1.

* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 9.5-alt1
- initial build for Sisyphus

