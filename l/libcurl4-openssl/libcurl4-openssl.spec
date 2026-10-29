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
Version: 8.23.0
Release: alt1

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
%doc CHANGES.md README* docs/{FAQ.md,FEATURES.md}
 
%changelog
* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 8.23.0-alt1
- new version 8.23.0
- fixes:
  + CVE-2026-107928: info leak uploading over WebSockets with GnuTLS
  + CVE-2026-107929: local interface connection reuse mixup
  + CVE-2026-86412: server-set cookie erases cookie jar
  + CVE-2026-86413: negotiate credentials sent to redirected origin
  + CVE-2026-86414: leaking host credentials to HTTP proxy
  + CVE-2026-86415: auto client cert connection reuse mixup
  + CVE-2026-87861: cross-origin reuse of a negotiate connection
  + CVE-2026-87862: HSTS cache import drops longer-lived child
  + CVE-2026-87863: HSTS response erases persisted entries
  + CVE-2026-87865: knownhost callback mismatches key as missing
  + CVE-2026-87866: wolfSSL public-key pinning bypass
  + CVE-2026-92386: server-set cookie aborts cookie jar load
  + CVE-2026-92387: never-ending loop via server response omission
  + CVE-2026-92388: FTP wildcard write callback mixup
  + CVE-2026-92389: TFTP direction confusion
  + CVE-2026-92390: -J no-clobber guarantee bypassed with 103 early hints
  + CVE-2026-92391: curl_mime_free stack overflow by recursion
  + CVE-2026-92392: HTTP/2 upload use-after-free
  + CVE-2026-94265: authorization: negotiate sent to foreign origin
  + CVE-2026-94266: password leak in CURLINFO_EFFECTIVE_URL

* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 8.22.0-alt1
- new version 8.22.0

* Thu Apr 09 2026 Vitaly Lipatov <lav@altlinux.ru> 8.16.0-alt3
- drop ExclusiveArch: x86_64 (altbug #58624)

* Mon Nov 03 2025 Vitaly Lipatov <lav@altlinux.ru> 8.16.0-alt2
- spec: pack libdir/name dir

* Fri Oct 31 2025 Vitaly Lipatov <lav@altlinux.ru> 8.16.0-alt1
- initial build for ALT Sisyphus
