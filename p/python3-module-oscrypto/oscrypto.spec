%define  oname oscrypto

%def_with check

Name:    python3-module-%oname
Version: 1.3.0
Release: alt1

Summary: Compiler-free Python crypto library backed by the OS, supporting CPython and PyPy

License: MIT
Group:   Development/Python3
URL:     https://github.com/wbond/oscrypto

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-asn1crypto
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
TLS (SSL) sockets, key generation, encryption, decryption, signing, verification
and KDFs using the OS crypto libraries. Does not require a compiler, and relies
on the OS for patching. Works on Windows, OS X and Linux/BSD.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# TLSTests need network connectivity -> disabled with regular expression
%__python3 run.py tests ^\(\?\!test_tls\)

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
