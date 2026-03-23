%define _unpackaged_files_terminate_build 1
%define pypi_name jc

Name: python3-module-%pypi_name
Version: 1.25.6
Release: alt1

Summary: Converts the output of popular command-line tools and file-types to JSON
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/jc/
Vcs: https://github.com/kellyjonbrazil/jc
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
jc JSONifies the output of many CLI tools, file-types, and common strings for
easier parsing in scripts. This allows further command-line processing of
output with tools like jq or jello by piping commands. jc can also be used as
a python library.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Mar 23 2026 Arseniy Kostevich <faux@altlinux.org> 1.25.6-alt1
- Initial build for ALT.
