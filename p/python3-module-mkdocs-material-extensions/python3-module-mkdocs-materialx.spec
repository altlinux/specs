%define _unpackaged_files_terminate_build 1
%define pypi_name mkdocs-material-extensions
%define mod_name materialx

%def_with check

Name: python3-module-%pypi_name
Version: 1.3
Release: alt1

Summary: Markdown extension resources for MkDocs Material
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mkdocs-material-extensions/
Vcs: https://github.com/facelessuser/mkdocs-material-extensions

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Markdown extension resources for MkDocs for Material

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
%doc LICENSE.md README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 19 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3-alt1
- Updated to 1.3.

* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2-alt1
- Updated to 1.2.

* Mon Aug 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt2
- Fixed FTBFS.

* Wed Mar 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- New version.

* Fri Aug 25 2022 Anton Zhukharev <ancieg@altlinux.org> 1.0.3-alt1
- initial build for Sisyphus

