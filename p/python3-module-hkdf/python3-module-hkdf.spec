%define modulename hkdf

Name:           python3-module-hkdf
Version:        0.0.3
Release:        alt1

Summary:        HMAC-based Extract-and-Expand Key Derivation Function (HKDF)

Url:            https://github.com/casebeer/python-hkdf
License:        BSD 2-clause "Simplified" License
Group:          Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/h/%modulename/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-dev python3-module-setuptools

BuildArch: noarch

%description
This module implements the HMAC Key Derivation function, defined at
    http://tools.ietf.org/html/draft-krawczyk-hkdf-01

There are two interfaces: a functional interface, with separate extract
and expand functions as defined in the draft RFC, and a wrapper class for
these functions.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/__pycache__/hkdf*
%python3_sitelibdir/hkdf.py*
%python3_sitelibdir/*.egg-info/


%changelog
* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.3-alt1
- Initial build for ALT Sisyphus
