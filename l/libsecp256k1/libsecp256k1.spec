# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname	secp256k1

%global major	0
%global libname	lib%{oname}_%{major}
%global devname	lib%{oname}-devel

Name:		libsecp256k1
Summary:	Optimized C library for EC operations on curve secp256k1
Version:	0.25.4
Release:	alt1_2
License:	MIT
Group:		System/Libraries
Url:		https://github.com/Bitcoin-ABC/secp256k1
Source0:	https://github.com/Bitcoin-ABC/secp256k1/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires(pre): rpm-macros-valgrind
%ifarch %valgrind_arches
BuildRequires: valgrind-devel
%endif
BuildRequires:	pkgconfig(libcrypto)
Source44: import.info

%description
Optimized C library for EC operations on curve secp256k1.

Features:
* secp256k1 ECDSA signing/verification and key generation.
* Adding/multiplying private/public keys.
* Serialization/parsing of private keys, public keys, signatures.
* Constant time, constant memory access signing and pubkey generation.
* Derandomized DSA (via RFC6979 or with a caller provided function.)
* Very efficient implementation.

%package -n %{libname}
Summary:	Optimized C library for EC operations on curve secp256k1
Group:		System/Libraries

%description -n %{libname}
Optimized C library for EC operations on curve secp256k1.

Features:
* secp256k1 ECDSA signing/verification and key generation.
* Adding/multiplying private/public keys.
* Serialization/parsing of private keys, public keys, signatures.
* Constant time, constant memory access signing and pubkey generation.
* Derandomized DSA (via RFC6979 or with a caller provided function.)
* Very efficient implementation.

%package -n %{devname}
Summary:	Development files and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files and headers for %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
autoreconf -vfi
export CC=gcc
export CC_FOR_BUILD=gcc
export CFLAGS_FOR_BUILD="%{optflags}"
%configure \
	--enable-module-recovery \
	--enable-module-ecdh \
%ifnarch x86_64 %{ix86}
	--with-asm=no \
%endif
	--disable-static
%make_build

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%check
make check

%files -n %{libname}
%{_libdir}/libsecp256k1.so.%{major}*

%files -n %{devname}
%{_includedir}/secp256k1.h
%{_includedir}/secp256k1_preallocated.h
%{_includedir}/secp256k1_schnorr.h
%{_libdir}/libsecp256k1.so
%{_libdir}/pkgconfig/libsecp256k1.pc
%{_includedir}/secp256k1_ecdh.h
%{_includedir}/secp256k1_recovery.h


%changelog
* Wed Nov 01 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.25.4-alt1_2
- NMU: fixed build requirements for LoongArch (valgrind is not available)

* Wed May 11 2022 Igor Vlasenko <viy@altlinux.org> 0.25.4-alt1_1
- update by mgaimport

* Wed Sep 22 2021 Igor Vlasenko <viy@altlinux.org> 0.24.1-alt1_1
- enabled asm on i586

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 0.24.1-alt1
- new version (0.24.1) with rpmgs script
- add --enable-module-ecdh, disable asm for non x86_64

* Fri Aug 13 2021 Igor Vlasenko <viy@altlinux.org> 0.22.0-alt2_1
- enabled module recovery (closes: #40719)

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.22.0-alt1_1
- update by mgaimport

* Mon Feb 17 2020 Igor Vlasenko <viy@altlinux.ru> 0.20.10-alt1_1
- update by mgaimport

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_0.0.git20171221.2
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_0.0.git20171221.1
- new version

