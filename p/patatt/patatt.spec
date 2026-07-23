%define _unpackaged_files_terminate_build 1
%def_with check

Name: patatt
Version: 0.8.0
Release: alt1

Summary: CLI for adding end-to-end cryptographic attestation to patches
License: MIT-Zero
Group: Development/Tools
Url: https://git.kernel.org/pub/scm/utils/patatt/patatt.git/about/
Vcs: https://git.kernel.org/pub/scm/utils/patatt/patatt.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest

BuildRequires: git-core
BuildRequires: gnupg2
BuildRequires: python3-module-pynacl
%endif

%description
Patatt provides a CLI for adding end-to-end cryptographic
attestation to patches sent via email. It adapts the DKIM email
signature standard to include cryptographic signatures via
the X-Developer-Signature header.

Patatt features include:
* DKIM-like signature headers that don't corrupt patch content
* Multiple signing algorithms: ed25519, OpenPGP, OpenSSH
* In-repository keyring management via git refs
* Automatic signing via git sendemail-validate hook


%package -n python3-module-%name
Summary: Python library for adding end-to-end cryptographic attestation to patches
Group: Development/Python

Requires: gnupg2
Requires: python3-module-pynacl

%description -n python3-module-%name
Patatt provides a Python library for adding end-to-end cryptographic
attestation to patches sent via email. It adapts the DKIM email
signature standard to include cryptographic signatures via
the X-Developer-Signature header.

Patatt features include:
* DKIM-like signature headers that don't corrupt patch content
* Multiple signing algorithms: ed25519, OpenPGP, OpenSSH
* In-repository keyring management via git refs
* Automatic signing via git sendemail-validate hook


%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%_bindir/%name
%_man5dir/%{name}*

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}/

%changelog
* Thu Jul 23 2026 Ivan A. Melnikov <iv@altlinux.org> 0.8.0-alt1
- build for Sisyphus
- use gpg2 as the default GnuPG binary
