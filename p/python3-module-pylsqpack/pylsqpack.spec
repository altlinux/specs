%define _unpackaged_files_terminate_build 1
%define pypi_name pylsqpack

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.17
Release: alt1

Summary: Python bindings for ls-qpack
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/pylsqpack
Vcs: https://github.com/aiortc/pylsqpack

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: submodules.tar

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
Pylsqpack is a wrapper around the ls-qpack library. It provides Python
Decoder and Encoder objects to read or write HTTP/3 headers compressed
with QPACK.

%prep
%setup -a2
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 07 2023 Alexandr Shashkin <dutyrok@altlinux.org> 0.3.17-alt1
- Initial build for ALT Sisyphus

