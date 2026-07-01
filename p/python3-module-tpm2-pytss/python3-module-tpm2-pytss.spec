%define _unpackaged_files_terminate_build 1
%define pypi_name tpm2-pytss
%define _name tpm2_pytss
%def_enable check

Name: python3-module-%pypi_name
Version: 2.3.0
Release: alt3
Summary: TPM 2.0 TSS Bindings for Python
Group: Development/Python3
License: BSD-2-Clause
Url: https://github.com/tpm2-software/tpm2-pytss
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: tpm2-pytss-2.3.0-fix-cryptography-47-support.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pycparser
BuildRequires: python3-module-pkgconfig
BuildRequires: python3-devel
BuildRequires: python3-module-pip
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pycparser
BuildRequires: python3-module-pkgconfig
BuildRequires: python3-module-packaging
BuildRequires: python3-module-cffi
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-asn1crypto
BuildRequires: python3-module-yaml
BuildRequires: libtpm2-tss-devel >= 2.0.0

%if_enabled check
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
%autopatch -p1
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

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
* Wed Jul 01 2026 Anton Vyatkin <toni@altlinux.org> 2.3.0-alt3
- Fix FTBFS.

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt2.1
- Demodernized packaging.

* Fri Jul 18 2025 Alexey Shabalin <shaba@altlinux.org> 2.3.0-alt2
- Fix FTBFS: backport commits from upstream master.

* Tue Mar 25 2025 Alexey Shabalin <shaba@altlinux.org> 2.3.0-alt1
- 2.3.0.

* Fri May 03 2024 Alexey Shabalin <shaba@altlinux.org> 2.2.1-alt1
- Initial package.
