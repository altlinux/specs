%define  oname pkcs11

%def_with check

Name:    python3-module-%oname
Version: 0.7.0
Release: alt1

Summary: PKCS#11/Cryptoki support for Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/danni/python-pkcs11

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-Cython

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-cached-property
BuildRequires: python3-module-asn1crypto
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-oscrypto
BuildRequires: softhsm libsofthsm openssl
%endif

Source:  %name-%version.tar

# https://github.com/archlinux/svntogit-community/blob/packages/python-python-pkcs11/trunk/python-pkcs11_mark-tests-as-xfail.patch
Patch: python-pkcs11_mark-tests-as-xfail.patch

%description
A high level, "more Pythonic" interface to the PKCS#11 (Cryptoki) standard
to support HSM and Smartcard devices in Python.

The interface is designed to follow the logical structure of a HSM, with useful
defaults for obscurely documented parameters. Many APIs will optionally accept
iterables and act as generators, allowing you to stream large data blocks
for symmetric encryption.

python-pkcs11 also includes numerous utility functions to convert between
PKCS #11 data structures and common interchange formats including PKCS #1 and X.509.

python-pkcs11 is fully documented and has a full integration test suite for all
features, with continuous integration against multiple HSM platforms including:
* Thales nCipher
* Opencryptoki TPM
* OpenSC/Smartcard-HSM/Nitrokey HSM

%prep
%setup
%patch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
mkdir -p ~/.config/softhsm2
cat > ~/.config/softhsm2/softhsm2.conf << EOF
# SoftHSM v2 configuration file
directories.tokendir = /usr/src/RPM/BUILD/python3-module-pkcs11-%version
objectstore.backend = file
# ERROR, WARNING, INFO, DEBUG
log.level = INFO
# If CKF_REMOVABLE_DEVICE flag should be set
slots.removable = false
# Enable and disable PKCS#11 mechanisms using slots.mechanisms.
slots.mechanisms = ALL
# If the library should reset the state on fork
library.reset_on_fork = false
EOF
softhsm2-util --init-token --free --label TEST --pin 1234 --so-pin 5678
export PKCS11_MODULE=%_libdir/libsofthsm2.so
export PKCS11_TOKEN_LABEL=TEST
export PKCS11_TOKEN_PIN=1234
export PKCS11_TOKEN_SO_PIN=5678
export PYTHONPATH="%buildroot/%python3_sitelibdir"
py.test-3 -v --import-mode=append

%files
%doc *.rst
%python3_sitelibdir/pkcs11
%python3_sitelibdir/python_pkcs11-%version-py%_python3_version.egg-info

%changelog
* Fri Jul 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
