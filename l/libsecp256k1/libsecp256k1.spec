# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname	secp256k1

%global major	0
%global libname	lib%{oname}_%{major}
%global devname	lib%{oname}-devel

%global gdate	20171221
%global rel	1

Name:		libsecp256k1
Summary:	Optimized C library for EC operations on curve secp256k1
Version:	0.1
Release:	alt1_%{?gdate:0.0.git%gdate.}%{rel}
License:	MIT
Group:		System/Libraries
Url:		https://github.com/bitcoin-core/secp256k1
Source0:	%{oname}-%{gdate}.tar.xz
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
%setup -qn %{oname}-%{?gdate}%{?!gdate:%version}

%build
autoreconf -vfi
%configure \
	--disable-static
%make_build

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%{_libdir}/libsecp256k1.so.%{major}*

%files -n %{devname}
%{_includedir}/secp256k1.h
%{_libdir}/libsecp256k1.so
%{_libdir}/pkgconfig/libsecp256k1.pc



%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_0.0.git20171221.1
- new version

