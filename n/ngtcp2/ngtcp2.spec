%global _unpackaged_files_terminate_build 1
%define ngtcpsoname 16
%define ngtcp2_crypto_gnutls 8
%ifarch %ix86
%define relax ||:
%else
%define relax %nil
%endif

Name: ngtcp2
Version: 1.24.0
Release: alt1
Summary: An implementation of the RFC9000 QUIC protocol

License: MIT
Group: System/Libraries
Url: https://github.com/ngtcp2/ngtcp2
Vcs: https://github.com/ngtcp2/ngtcp2.git
Source: %name-%version.tar

Source100: %name-%version-tests-munit.tar
Source101: %name-%version-third-party-urlparse.tar
Source102: %name-%version-third-party-urlparse-http-parser.tar
Source103: %name-%version-third-party-urlparse-munit.tar

BuildRequires: gcc-c++ CUnit-devel
# need openssl-quic branch
#BuildRequires: pkgconfig(openssl) >= 1.1.1
BuildRequires: pkgconfig(gnutls) >= 3.7.2
BuildRequires: pkgconfig(libnghttp3) >= 1.12.0
BuildRequires: libev-devel

%description
%summary.

%package -n lib%name.%ngtcpsoname
Summary: An implementation of the RFC9000 QUIC protocol
Group: System/Libraries
Requires: lib%{name}_crypto_gnutls%{ngtcp2_crypto_gnutls} = %EVR

%description -n lib%name.%ngtcpsoname
%summary.

%package -n lib%{name}_crypto_gnutls%{ngtcp2_crypto_gnutls}
Summary: %name GnuTLS crypto library
Group: System/Libraries

%description -n lib%{name}_crypto_gnutls%{ngtcp2_crypto_gnutls}
%summary.

%package -n lib%name-devel
Summary: Files needed for building applications with libngtcp2
Group: Development/C
Requires: lib%name.%ngtcpsoname = %EVR
Requires: lib%{name}_crypto_gnutls%{ngtcp2_crypto_gnutls} = %EVR

%description -n lib%name-devel
The libngtcp2-devel package includes libraries and header files needed
for building applications with libngtcp2.

%prep
%setup -a100 -a101 -a102 -a103

%build
%autoreconf
%configure --disable-static --with-gnutls
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_defaultdocdir/%name

%check
%make_build check %relax
[ -f "tests/test-suite.log" ] && cat "tests/test-suite.log"

%files -n lib%name.%ngtcpsoname
%_libdir/lib%{name}.so.%{ngtcpsoname}.*
%_libdir/lib%{name}.so.%{ngtcpsoname}

%files -n lib%{name}_crypto_gnutls%{ngtcp2_crypto_gnutls}
%_libdir/lib%{name}_crypto_gnutls.so.%{ngtcp2_crypto_gnutls}*

%doc README.rst

%files -n lib%name-devel
%_includedir/%name
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Tue Jun 30 2026 Anton Farygin <rider@altlinux.org> 1.24.0-alt1
- 1.23.0 -> 1.24.0

* Thu Jun 04 2026 Anton Farygin <rider@altlinux.org> 1.23.0-alt1
- 1.22.1 -> 1.23.0

* Sat Apr 18 2026 Anton Farygin <rider@altlinux.org> 1.22.1-alt1
- 1.22.0 -> 1.22.1

* Tue Apr 07 2026 Anton Farygin <rider@altlinux.org> 1.22.0-alt1
- 1.21.0 -> 1.22.0

* Fri Feb 27 2026 Anton Farygin <rider@altlinux.org> 1.21.0-alt1
- 1.20.0 -> 1.21.0

* Thu Feb 05 2026 Anton Farygin <rider@altlinux.org> 1.20.0-alt1
- 1.19.0 -> 1.20.0

* Fri Dec 26 2025 Anton Farygin <rider@altlinux.org> 1.19.0-alt1
- 1.18.0 -> 1.19.0

* Mon Dec 08 2025 Anton Farygin <rider@altlinux.org> 1.18.0-alt1
- 1.17.0 -> 1.18.0

* Mon Nov 10 2025 Anton Farygin <rider@altlinux.com> 1.17.0-alt1
- 1.15.1 -> 1.17.0

* Thu Sep 11 2025 Anton Farygin <rider@altlinux.com> 1.15.1-alt1
- 1.13.0 -> 1.15.1

* Sat May 31 2025 Anton Farygin <rider@altlinux.com> 1.13.0-alt1
- 1.12.0 -> 1.13.0

* Sun Apr 27 2025 Anton Farygin <rider@altlinux.com> 1.12.0-alt1
- 1.11.0 -> 1.12.0

* Thu Feb 27 2025 Anton Farygin <rider@altlinux.ru> 1.11.0-alt2
- ignored test results in %%check section for i586 architecture.

* Mon Feb 24 2025 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.10.0 -> 1.11.0

* Tue Dec 24 2024 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- 1.9.1 -> 1.10.0

* Mon Dec 02 2024 Anton Farygin <rider@altlinux.ru> 1.9.1-alt1
- 1.7.0 -> 1.9.1

* Fri Aug 30 2024 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- 1.6.0  -> 1.7.0

* Mon Jul 01 2024 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- 1.5.0 -> 1.6.0

* Sun May 19 2024 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- 1.4.0 -> 1.5.0

* Fri Mar 29 2024 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.2.0 -> 1.4.0

* Sat Jan 27 2024 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- 1.0.1 -> 1.2.0

* Tue Oct 24 2023 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- 0.16.0 -> 1.0.1

* Sun Jun 25 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.15.0 -> 0.16.0
- The library package was renamed in accordance with the Shared Libs Policy.

* Thu May 18 2023 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.13.1 -> 0.15.0

* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 0.13.1-alt1
- New version 0.13.1.

* Tue Mar 21 2023 Alexey Shabalin <shaba@altlinux.org> 0.13.0-alt1
- Initial build.
