%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var
%def_disable check

Name: tpm2-pkcs11
Version: 1.9.0
Release: alt1
Summary: PKCS#11 interface for TPM 2.0 hardware
Group: System/Configuration/Hardware

License: BSD
Url: https://github.com/tpm2-software/tpm2-pkcs11
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf-archive
BuildRequires: libgcrypt-devel
BuildRequires: libyaml-devel
BuildRequires: libssl-devel >= 1.1.0
BuildRequires: libp11-kit-devel
BuildRequires: libsqlite3-devel
BuildRequires: tpm2-tools
BuildRequires: libtpm2-tss-devel
# for tests
BuildRequires: libcmocka-devel
BuildRequires: dbus
# for tools
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pyasn1-modules
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-tpm2-pytss

%description
PKCS #11 is a Public-Key Cryptography Standard that defines a standard method
to access cryptographic services from tokens/ devices such as hardware security
modules (HSM), smart cards, etc. In this project we intend to use a TPM2 device
as the cryptographic token.

%package -n python3-module-%name
Summary: The tools required to setup and configure TPM2 for PKCS#11
Group: Development/Python3
Provides: %name-tools = %EVR
BuildArch: noarch

%description -n python3-module-%name
The tools required to setup and configure TPM2 for PKCS#11.

%prep
%setup
%patch -p1
echo %version > VERSION

%build
./bootstrap
#%%autoreconf
%configure --disable-static --enable-unit
%make_build
pushd tools
%python3_build
popd

%install
%makeinstall_std

pushd tools
%python3_install
install -Dpm 755 tpm2_ptool $RPM_BUILD_ROOT%_bindir/tpm2_ptool
popd

# Cleanup
rm -f %buildroot%_libdir/pkcs11/*.la
rm -rf %buildroot%_pkgconfigdir

%check
%make check
pushd tools
%python3_setup test
popd

%files
%doc LICENSE
%_datadir/p11-kit/modules/tpm2_pkcs11.module
%_libdir/pkcs11/libtpm2_pkcs11.so
%_libdir/pkcs11/libtpm2_pkcs11.so.0*

%files -n python3-module-%name
%_bindir/tpm2_ptool
%python3_sitelibdir_noarch/*

%changelog
* Fri May 03 2024 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- New version 1.9.0.

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- new version 1.7.0

* Sat Aug 28 2021 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial build.

