%define  modulename otr

Name:    python3-module-%modulename
Version: 2.0.1
Release: alt1

Summary: Off-The-Record Messaging protocol implementation for Python
License: LGPL-2.1+
Group:   Development/Python3
URL:     https://github.com/AGProjects/python3-otr

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-application
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-gmpy2

BuildArch: noarch

Source: python3-%modulename-%version.tar

%description
This package implements the Off-The-Record Messaging protocol in pure
python.

Off-The-Record Messaging (OTR) is a cryptographic protocol that provides
encryption for instant messaging conversations. OTR uses a combination
of AES symmetric-key algorithm with 128 bits key length, the
Diffie-Hellman key exchange with 1536 bits group size, and the
SHA-1/SHA-256 hash functions.

%prep
%setup -n python3-%modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
