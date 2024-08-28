%define _unpackaged_files_terminate_build 1
%def_with check

%define pypi_name sysrsync
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1.gita601c299

Summary: Simple and safe native rsync wrapper for Python 3
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sysrsync/
Vcs: https://github.com/gchamon/sysrsync

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

Requires: rsync
%add_pyproject_deps_runtime_filter toml$
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: rsync
%endif

%description
%summary

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 28 2024 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.1-alt1.gita601c299
- Initial build for ALT Sisyphus.

