Name: libmesode
Version: 0.10.1
Release: alt1
Summary: Profanity project fork of libstrophe, an XMPP client library written in C
Group: System/Libraries
License: GPLv3
Source: %version.tar.gz

# Automatically added by buildreq on Sun Jul 22 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcom_err-devel libkrb5-devel perl pkg-config python-base
BuildRequires: doxygen libexpat-devel libssl-devel gcc14
%set_gcc_version 14

%description
Libmesode is a fork of libstrophe (http://strophe.im/libstrophe/),
a lightweight XMPP client library written in C,
for use in Profanity (http://www.profanity.im/).

Reasons for forking:

    Remove Windows support
    Support only one XML Parser implementation (expat)
    Support only one SSL implementation (OpenSSL)

This simplifies maintenance of the library when used in Profanity.

Whilst Profanity will run against libstrophe, libmesode provides
extra TLS functionality such as manual SSL certificate verification.

%package devel
Group: Development/C
Summary: Development environment for %name
Requires: %name = %version-%release
%description devel
Development environment for %name

%prep
%setup
# XXX enable TLS1.0
sed -i '/SSL_OP_NO_TLSv1/s|^|//|' "src/tls_openssl.c"

%build
%autoreconf
%configure CC=gcc-14
%make_build
doxygen

%install
%makeinstall

rm -fv %buildroot%_libdir/*.a

%check
make check

%files
%_libdir/*.so.*

%files devel
%doc README.markdown docs
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Wed Jun 17 2026 Fr. Br. George <george@altlinux.org> 0.10.1-alt1
- Autobuild version bump to 0.10.1
- Use old GCC

* Wed Oct 20 2021 Grigory Ustinov <grenka@altlinux.org> 0.9.3-alt2
- Fixed FTBFS.

* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 0.9.3-alt1
- Autobuild version bump to 0.9.3

* Mon Mar 11 2019 Fr. Br. George <george@altlinux.ru> 0.9.2-alt2
- Enable some insecure protocols

* Fri Sep 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1
- Updated to upstream version 0.9.2.

* Sun Jul 22 2018 Fr. Br. George <george@altlinux.ru> 0.9.1-alt1
- Autobuild version bump to 0.9.1

* Sun Jul 22 2018 Fr. Br. George <george@altlinux.ru> 0.9.0-alt1
- Initial  fork from libstrophe

