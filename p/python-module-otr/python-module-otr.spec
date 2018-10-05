%define  modulename otr

Name:    python-module-%modulename
Version: 1.2.1
Release: alt1

Summary: Off-The-Record Messaging protocol implementation for Python
License: LGPLv2+
Group:   Development/Python
URL:     https://github.com/AGProjects/python-otr

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  python-%modulename-%version.tar

%description
This package implements the Off-The-Record Messaging protocol in pure
python.

Off-The-Record Messaging (OTR) is a cryptographic protocol that provides
encryption for instant messaging conversations. OTR uses a combination
of AES symmetric-key algorithm with 128 bits key length, the
Diffie-Hellman key exchange with 1536 bits group size, and the
SHA-1/SHA-256 hash functions.

%prep
%setup -n python-%modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
