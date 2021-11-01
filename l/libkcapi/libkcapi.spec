# Shared object version of libkcapi.
%global vmajor            1
%global vminor            3
%global vpatch            1

Name: libkcapi
Version: %vmajor.%vminor.%vpatch
Release: alt1
Summary: User space interface to the Linux Kernel Crypto API
Group: System/Libraries
License: BSD or GPLv2
Url: http://www.chronox.de/%name.html
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: libkcapi-1.3.1-fedora-Use-GCCs-__symver__-attribute.patch
BuildRequires: /proc
BuildRequires: clang
BuildRequires: cppcheck
BuildRequires: docbook-utils-pdf
BuildRequires: gcc
BuildRequires: git
BuildRequires: hardlink
BuildRequires: glibc-kernheaders
BuildRequires: openssl
BuildRequires: perl
BuildRequires: systemd
BuildRequires: xmlto
%{?!_without_check:%{?!_disable_check:BuildRequires: rpm-build-vm /proc}}

%description
libkcapi allows user-space to access the Linux kernel crypto API.

This library uses the netlink interface and exports easy to use APIs
so that a developer does not need to consider the low-level netlink
interface handling.

The library does not implement any cipher algorithms.  All consumer
requests are sent to the kernel for processing.  Results from the
kernel crypto API are returned to the consumer via the library API.

The kernel interface and therefore this library can be used by
unprivileged processes.

%package -n %name%vmajor
Group: System/Libraries
Summary: User space interface to the Linux Kernel Crypto API

%description -n %name%vmajor
libkcapi allows user-space to access the Linux kernel crypto API.

This library uses the netlink interface and exports easy to use APIs
so that a developer does not need to consider the low-level netlink
interface handling.

The library does not implement any cipher algorithms.  All consumer
requests are sent to the kernel for processing.  Results from the
kernel crypto API are returned to the consumer via the library API.

The kernel interface and therefore this library can be used by
unprivileged processes.


%package devel
Group: Development/C
Summary: Development files for the %name package
Requires: %name%vmajor == %EVR

%description devel
Header files for applications that use %name.

%package doc
Group: Development/C
Summary: User documentation for the %name package
BuildArch: noarch
Requires: %name%vmajor == %EVR

%description doc
User documentation for %name.

%package fipscheck
Group: System/Base
Summary: Drop-in replacements for fipscheck/fipshmac provided by the %name package
%description fipscheck
Provides drop-in replacements for fipscheck and fipshmac tools (from
package fipscheck) using %name.

%package hmaccalc
Group: System/Base
Summary: Drop-in replacements for hmaccalc provided by the %name package
Requires: %name%vmajor  == %EVR

%description hmaccalc
Provides drop-in replacements for sha*hmac tools (from package
hmaccalc) using %name.

%package checksum
Group: System/Base
Summary: Drop-in replacements for coreutils checksum provided by the %name package
Requires: %name%vmajor == %EVR

%description checksum
Provides drop-in replacements for checksum tools (from package
coreutils) using %name.

%package tools
Group: System/Base
Summary: Utility applications for the %name package
Requires: %name%vmajor == %EVR

%description tools
Utility applications that are provided with %name.  This includes
tools to use message digests, symmetric ciphers and random number
generators implemented in the Linux kernel from command line.

%package tests
Summary: Testing scripts for the %name package
Group: Development/C
Requires: %name%vmajor  == %EVR
Requires: %name-tools == %EVR
Requires: %name-hmaccalc == %EVR
#Requires: %name-checksum == %EVR
Requires: openssl
Requires: perl

%description tests
Auxiliary scripts for testing %name.

%prep
%setup
%patch0 -p1
%patch1 -p1


%build
%autoreconf
%configure               \
  --libdir=/%_lib      \
  --disable-silent-rules \
  --enable-kcapi-encapp  \
  --enable-kcapi-dgstapp \
  --enable-kcapi-hasher  \
  --enable-kcapi-rngapp  \
  --enable-kcapi-speed   \
  --enable-kcapi-test    \
  --enable-shared        \
  --disable-static        \
  --enable-sum-prefix=   \
  --enable-sum-dir=/%_lib \
  --with-pkgconfigdir=%_libdir/pkgconfig
%make_build all

%install
%makeinstall_std

# We don't ship autocrap dumplings.
%_bindir/find %buildroot -type f -name '*.la' -print -delete

# HMAC checksums are generated during __spec_install_post.
%_bindir/find %buildroot -type f -name '*.hmac' -print -delete

# Remove 0-size files.
%_bindir/find %buildroot -type f -size 0 -print -delete

# Remove checksum calculation tools to avoid conlict with coreutils.
rm -f %buildroot%_bindir/*sum

%check
# don't run compile test
sed -i '/^[^#]/ s/\(^.*compile-test\.sh.*$\)/#\1/' test/test-invocation.sh
vm-run --kvm=cond "
pushd test
ENABLE_FUZZ_TEST=1 \
NO_32BIT_TEST=1    \
  ./test-invocation.sh
popd
"

%files -n %name%vmajor
%doc README.md COPYING*
/%_lib/%name.so.%vmajor
/%_lib/%name.so.%version

%files devel
%doc CHANGES.md
%doc TODO
%_includedir/kcapi.h
%_mandir/man3/kcapi_*.3.*
/%_lib/%name.so
%_libdir/pkgconfig/%name.pc

# TODO
#%files doc
#%files checksum

%files fipscheck
%_bindir/fips*

%files hmaccalc
%_bindir/sha*hmac

%files tools
%_bindir/kcapi*
%_mandir/man1/kcapi*.1.*

%files tests
%dir %_libexecdir/%name
%_libexecdir/%name/*

%changelog
* Mon Oct 25 2021 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Thu Jul 09 2020 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- first build for ALT

