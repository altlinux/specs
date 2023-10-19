%define _unpackaged_files_terminate_build 1
%define pypi_name pymdown-extensions
%define mod_name pymdownx

%def_with check

Name: python3-module-%pypi_name
Version: 10.3.1
Release: alt1

Summary: Extensions for Python Markdown
License: MIT and BSD
Group: Development/Python3
Url: https://pypi.org/project/pymdown-extensions/
Vcs: https://github.com/facelessuser/pymdown-extensions

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
%summary.

%prep
%setup
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

