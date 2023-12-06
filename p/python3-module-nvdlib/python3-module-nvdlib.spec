%define _unpackaged_files_terminate_build 1
%define pypi_name nvdlib

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.6
Release: alt1

Summary: A simple wrapper for the National Vulnerability CVE/CPE API
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/nvdlib/
Vcs: https://github.com/Vehemont/nvdlib

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check
%endif

%description
NVDlib is a Python library that allows you to interface with the NIST
National Vulnerability Database (NVD), pull vulnerabilities (CVEs),
and Common Platform Enumeration (CPEs) into easily accessible objects.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md HISTORY.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Dec 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.7.6-alt1
- Built for ALT Sisyphus.

