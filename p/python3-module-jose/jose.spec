%define _unpackaged_files_terminate_build 1

%define oname jose

Name: python3-module-%oname
Version: 3.3.0
Release: alt2
Summary: JOSE implementation in Python
Group: Development/Python3
License: MIT
URL: https://github.com/mpdavis/python-jose

BuildArch: noarch

# https://github.com/mpdavis/python-jose.git
Source: %name-%version.tar

# Due to version of ecdsa 0.15, which is available in YUM repo already
# https://github.com/mpdavis/python-jose/issues/176#issuecomment-642352816
Patch1: %oname-fedora-disable-test_key_too_short.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-wheel
BuildRequires: python3(setuptools)
BuildRequires: python3(six)
# Backends
BuildRequires: python3(cryptography)
BuildRequires: python3(Crypto)
BuildRequires: python3(ecdsa)
BuildRequires: python3(rsa)
BuildRequires: python3(pyasn1)
# Run tests
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_cov)

%description
A JOSE implementation in Python

The JavaScript Object Signing and Encryption (JOSE) technologies - JSON Web
Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), and JSON Web
Algorithms (JWA) - collectively can be used to encrypt and/or sign content
using a variety of algorithms. While the full set of permutations is extremely
large, and might be daunting to some, it is expected that most applications
will only use a small set of algorithms to meet their needs.

Documentation: https://python-jose.readthedocs.org/en/latest/

%prep
%setup
%patch1 -p0

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -e compatibility

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/jose
%python3_sitelibdir/python_jose-%version.dist-info

%changelog
* Wed Dec 21 2022 Anton Farygin <rider@altlinux.ru> 3.3.0-alt2
- built without python3-module-pytest-runner (closes: #44634)

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.

* Wed Sep 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt1
- Initial build for ALT.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 17 2020 Chenxiong Qi <qcxhome@gmail.com> - 3.1.0-1
- Initial package.
