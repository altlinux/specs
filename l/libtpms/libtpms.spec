%define _unpackaged_files_terminate_build 1
# error make check on ppc64le
# ld: ./.libs/libtpms.so: ABI version 2 is not compatible with ABI version 0 output
%ifarch ppc64le
%def_disable check
%endif

# Valid crypto subsystems are 'freebl' and 'openssl'
%define crypto_subsystem openssl

Summary: Library providing Trusted Platform Module (TPM) functionality
Name: libtpms
Version: 0.9.5
Release: alt1
License: BSD
Group: System/Libraries
Url: http://github.com/stefanberger/libtpms
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: %name-%crypto_subsystem = %EVR

BuildRequires: gcc-c++
BuildRequires: /usr/bin/pod2man
%if "%crypto_subsystem" == "openssl"
BuildRequires: libssl-devel
%else
BuildRequires: libnss-devel
%endif

Requires: gmp

%description
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package devel
Summary: Include files for libtpms
Group: Development/C
Requires: %name = %EVR

%description devel
Libtpms header files and documentation.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
%if "%crypto_subsystem" == "openssl"
        --with-openssl \
        --with-tpm2 \
%endif
        --disable-static

%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc LICENSE README CHANGES
%_libdir/%name.so.*

%files devel
%_libdir/%name.so
%_includedir/*
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.5-alt1
- new version 0.9.5

* Thu Mar 24 2022 Alexey Shabalin <shaba@altlinux.org> 0.9.3-alt1
- new version 0.9.3

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 0.9.2-alt1
- new version 0.9.2

* Thu Dec 02 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.1-alt1
- new version 0.9.1

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Fri Aug 27 2021 Alexey Shabalin <shaba@altlinux.org> 0.8.4-alt1
- Initial build.

