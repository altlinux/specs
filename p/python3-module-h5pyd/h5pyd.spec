%define _unpackaged_files_terminate_build 1
%define pypi_name h5pyd
%define mod_name %pypi_name

# requires local HSDS
%def_without check

Name: python3-module-%pypi_name
Version: 0.24.0
Release: alt1
Summary: h5py compatible client lib for HDF REST API
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/h5pyd
Vcs: https://github.com/HDFGroup/h5pyd
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary.

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
# https://github.com/HDFGroup/h5pyd#testing
# requires local HSDS

%files
%_bindir/hsacl
%_bindir/hsconfigure
%_bindir/hscopy
%_bindir/hscp
%_bindir/hsdel
%_bindir/hsdiff
%_bindir/hsget
%_bindir/hsinfo
%_bindir/hsload
%_bindir/hsls
%_bindir/hsmv
%_bindir/hsrm
%_bindir/hsstat
%_bindir/hstouch
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 27 2026 Stanislav Levin <slev@altlinux.org> 0.24.0-alt1
- Initial build for sisyphus.
