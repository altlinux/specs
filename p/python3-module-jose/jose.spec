%define _unpackaged_files_terminate_build 1
%define pypi_name python-jose
%define oname jose

%def_with check

Name: python3-module-%oname
Version: 3.4.0
Release: alt1
Summary: JOSE implementation in Python
Group: Development/Python3
License: MIT
URL: https://pypi.org/project/python-jose
Vcs: https://github.com/mpdavis/python-jose.git

BuildArch: noarch

Source: %name-%version.tar

Provides: python3-module-%pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3(setuptools)
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-ecdsa
BuildRequires: python3-module-rsa
BuildRequires: python3-module-pyasn1
%endif

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

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/jose
%python3_sitelibdir/python_jose-%version.dist-info

%changelog
* Fri Apr 04 2025 Anton Vyatkin <toni@altlinux.org> 3.4.0-alt1
- New version 3.4.0.

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 3.3.0-alt3
- (NMU) Added missing provide.

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
