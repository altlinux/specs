%define _unpackaged_files_terminate_build 1
%define pypi_name qstylizer

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.2
Release: alt1

Summary: Qt stylesheet generation utility for PyQt/PySide
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/qstylizer/
Vcs: https://github.com/blambright/qstylizer

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter pytest-catchlog
%pyproject_builddeps_metadata_extra test
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.2-alt1
- Built for ALT Sisyphus.

