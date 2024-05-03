%define _unpackaged_files_terminate_build 1
%define pypi_name tpm2-pytss
%define _name tpm2_pytss
%def_enable check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1
Summary: TPM 2.0 TSS Bindings for Python
Group: Development/Python3
License: BSD-2-Clause
Url: https://github.com/tpm2-software/tpm2-pytss
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-%release.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject rpm-build-python3
%pyproject_builddeps_build
BuildRequires: python3-devel python3-module-pip
BuildRequires: python3-module-setuptools python3-module-setuptools_scm python3-module-wheel
BuildRequires: python3-module-pycparser python3-module-pkgconfig python3-module-packaging
BuildRequires: python3-module-cffi python3-module-cryptography python3-module-asn1crypto
BuildRequires: python3-module-yaml
BuildRequires: libtpm2-tss-devel >= 2.0.0

%if_enabled check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
BuildRequires: swtpm
BuildRequires: tpm2-tools
%endif

%description
TPM2 TSS Python bindings for Enhanced System API (ESYS), Feature API (FAPI),
Marshaling (MU), TCTI Loader (TCTILdr) and RC Decoding (rcdecode) libraries.
It also contains utility methods for wrapping keys to TPM 2.0 data structures
for importation into the TPM, unwrapping keys and exporting them from the TPM,
TPM-less makecredential command and name calculations, TSS2 PEM Key format
support, importing Keys from PEM, DER and SSH formats, conversion from
tpm2-tools based command line strings and loading tpm2-tools context files.

%prep
%setup
%patch -p1
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri May 03 2024 Alexey Shabalin <shaba@altlinux.org> 2.2.1-alt1
- Initial package.
