%global _unpackaged_files_terminate_build 1
%define pypi_name pyjpegls

%def_with check

Name: python3-module-pyjpegls
Version: 1.5.1
Release: alt1
Summary: JPEG-LS for Python via CharLS C++ Library
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/pyjpegls/
VCS: https://github.com/pydicom/pyjpegls
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

# ALT: build against the system-wide CharLS, the lib/charls submodule is not shipped
Patch1: %name-%version-alt-system-charls.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: gcc-c++
BuildRequires: libnumpy-py3-devel
BuildRequires: libCharLS-devel
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
JPEG-LS for Python via CharLS C++ Library

# pyjpegls

%prep
%setup
%patch1 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/jpeg_ls/
%python3_sitelibdir/_CharLS.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Aug 08 2026 Anton Farygin <rider@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux.

