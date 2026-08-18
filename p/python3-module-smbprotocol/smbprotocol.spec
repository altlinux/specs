%global _unpackaged_files_terminate_build 1
%define pypi_name smbprotocol

%def_with check

Name: python3-module-smbprotocol
Version: 1.17.0
Release: alt1
Summary: Python SMBv2 and SMBv3 client library
Group: Development/Python3
License: MIT
BuildArch: noarch
Url: https://pypi.org/project/smbprotocol/
VCS: https://github.com/jborean93/smbprotocol
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
SMBv2 and SMBv3 client for Python, implemented from the MS-SMB2 protocol
specification. It supports protocol negotiation from SMB 2.0.2 up to
SMB 3.1.1, NTLM and Kerberos authentication, message signing and
encryption, opening files, pipes and directories, IOCTL commands and
message compounding.

The package also provides the smbclient module - a higher-level API
that mimics Python's os, os.path and shutil interfaces for working
with files on SMB shares.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/smbprotocol/
%python3_sitelibdir/smbclient/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 18 2026 Anton Farygin <rider@altlinux.org> 1.17.0-alt1
- initial build for ALT Linux

