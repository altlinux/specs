%define _unpackaged_files_terminate_build 1
%define pypi_name pyproject-parser
%define mod_name pyproject_parser

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.1
Release: alt1

Summary: Parser for 'pyproject.toml'
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyproject-parser/
Vcs: https://github.com/repo-helper/pyproject-parser

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra all
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
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%_bindir/check-pyproject
%_bindir/pyproject-fmt
%_bindir/pyproject-info
%_bindir/pyproject-parser
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 21 2024 Anton Zhukharev <ancieg@altlinux.org> 0.11.1-alt1
- Updated to 0.11.1.

* Thu Apr 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.11.0-alt1
- Updated to 0.11.0.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 0.7.0-alt1
- initial build for Sisyphus

