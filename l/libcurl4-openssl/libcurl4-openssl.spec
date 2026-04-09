%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%def_with nghttp2
%def_without libssh2
%def_without check

%def_with openssl
%def_without gnutls
%def_without ngtcp2
%def_without nghttp3

%define libname libcurl-openssl
%define soname 4

Name: libcurl4-openssl
Version: 8.16.0
Release: alt3

Summary: libcurl library built with openssl

License: MIT
Group: Networking/File transfer
Url: https://curl.se/
VCS: https://github.com/curl/curl

# Source-url: %url/download/curl-%version.tar.xz
Source: %name-%version.tar

BuildRequires: /usr/bin/rename
BuildRequires: /usr/bin/patchelf
BuildRequires: groff-base
BuildRequires: libidn2-devel libkrb5-devel libgsasl-devel
BuildRequires: zlib-devel libzstd-devel libpsl-devel libldap-devel libbrotli-devel

%{?_with_openssl:BuildRequires: libssl-devel}
%{?_with_gnutls:BuildRequires: libgnutls-devel libnettle-devel}
%{?_with_libssh2:BuildRequires: libssh2-devel}
%{?_with_nghttp2:BuildRequires: libnghttp2-devel}
%{?_with_ngtcp2:BuildRequires: libngtcp2-devel >= 0.15.0}
%{?_with_nghttp3:BuildRequires: libnghttp3-devel}

Requires: ca-certificates

%description
This package contains libcurl shared library of functions for
sending and receiving files through various protocols, including
http and ftp.

You can apply it to your application via LD_LIBRARY_PATH=%_libdir/%name


%prep
%setup

%build
export PATH=/sbin:/usr/sbin:$PATH
./scripts/maketgz %version only
%autoreconf
%configure \
	--disable-static \
	%{subst_with openssl} \
	%{subst_with ngtcp2} \
	%{subst_with nghttp3} \
	--with-libidn2 \
	--enable-ipv6 \
	--enable-ldap \
	--enable-threaded-resolver \
	--enable-openssl-auto-load-config \
	--with-gssapi \
	--enable-websockets \
	--enable-versioned-symbols \
	%{subst_with libssh2} \
	--with-ca-bundle=%_datadir/ca-certificates/ca-bundle.crt

cd lib
%make_build

%install
cd lib
%makeinstall_std
rm -v %buildroot%_libdir/*.so
rename -v libcurl %libname %buildroot%_libdir/libcurl.so.*
# libname.so.4 will restored during packaging
patchelf --set-soname "%libname.so.%soname" %buildroot%_libdir/%libname.so.%soname.*
mkdir -p %buildroot%_libdir/%name/
ln -s ../%libname.so.%soname %buildroot%_libdir/%name/libcurl.so.%soname

%files
%_libdir/%libname.so.%soname
%_libdir/%libname.so.%soname.*
%dir %_libdir/%name/
%_libdir/%name/libcurl.so.%soname
%doc CHANGES.md README* docs/{FAQ,FEATURES.md}
 
%changelog
* Thu Apr 09 2026 Vitaly Lipatov <lav@altlinux.ru> 8.16.0-alt3
- drop ExclusiveArch: x86_64 (altbug #58624)

* Mon Nov 03 2025 Vitaly Lipatov <lav@altlinux.ru> 8.16.0-alt2
- spec: pack libdir/name dir

* Fri Oct 31 2025 Vitaly Lipatov <lav@altlinux.ru> 8.16.0-alt1
- initial build for ALT Sisyphus
