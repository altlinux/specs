%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libnghttp2
Version: 1.51.0
Release: alt1

Summary: HTTP/2.0 C Library
Group: System/Libraries
License: MIT

Url: https://github.com/nghttp2/nghttp2
Source: %name-%version.tar

BuildRequires: zlib-devel libev-devel libevent-devel libxml2-devel libjansson-devel libssl-devel gcc-c++ CUnit-devel libjemalloc-devel libcares-devel
BuildRequires: libsystemd-devel

%description
%summary

%package devel
Group: Development/C
Summary: HTTP/2.0 C Library headers
Requires: %name = %EVR
%description devel
%summary

%package tools
Group: Networking/WWW
Summary: HTTP/2.0 client, server and proxy
Requires: %name = %EVR
%description tools
%summary

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files tools
%_bindir/nghttp
%_bindir/nghttpd
%_bindir/nghttpx
%_bindir/h2load
%_bindir/deflatehd
%_bindir/inflatehd
%_man1dir/nghttp.1*
%_man1dir/nghttpd.1*
%_man1dir/nghttpx.1*
%_man1dir/h2load.1*

%files devel
%_includedir/nghttp2/nghttp2.h
%_includedir/nghttp2/nghttp2ver.h
%_libdir/libnghttp2.so
%_libdir/pkgconfig/libnghttp2.pc
%doc README.rst AUTHORS COPYING ChangeLog

%files
%_libdir/libnghttp2.so.*
%exclude %_libdir/libnghttp2.a
%exclude %_datadir/doc/nghttp2/README.rst
%exclude %_datadir/nghttp2/fetch-ocsp-response

%changelog
* Thu Nov 24 2022 Anton Farygin <rider@altlinux.ru> 1.51.0-alt1
- 1.50.0 -> 1.51.0

* Mon Oct 03 2022 Anton Farygin <rider@altlinux.ru> 1.50.0-alt1
- 1.48.0 -> 1.50.0

* Sat Jun 25 2022 Anton Farygin <rider@altlinux.ru> 1.48.0-alt1
- 1.47.0 -> 1.48.0

* Sun Mar 27 2022 Anton Farygin <rider@altlinux.ru> 1.47.0-alt1
- 1.46.0 -> 1.47.0

* Tue Dec 28 2021 Anton Farygin <rider@altlinux.ru> 1.46.0-alt1
- 1.46.0

* Mon Oct 11 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.41.0-alt2
- Fixed build.

* Sat Jun 20 2020 Vladimir Lettiev <crux@altlinux.org> 1.41.0-alt1
- 1.40.1 (Closes: #38626)
- Security fix: CVE-2020-11080

* Fri Jan 17 2020 Vladimir Lettiev <crux@altlinux.org> 1.40.0-alt1
- 1.40.0 (Closes: #37840)

* Sun Sep 01 2019 Vladimir Lettiev <crux@altlinux.org> 1.39.2-alt1
- 1.39.2 (Closes: #37170)
- Security fixes: CVE-2019-9511, CVE-2019-9513

* Thu Oct 11 2018 Anton Farygin <rider@altlinux.ru> 1.34.0-alt1
- 1.34.0

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.26.0-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 1.26.0-alt1
- 1.26.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.24.0-alt1
- 1.24.0

* Tue Sep 27 2016 Vladimir Lettiev <crux@altlinux.ru> 1.15.0-alt1
- 1.15.0

* Mon Sep 12 2016 Vladimir Lettiev <crux@altlinux.ru> 1.14.1-alt1
- 1.14.1

* Tue Mar 01 2016 Vladimir Lettiev <crux@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Wed Dec 23 2015 Vladimir Lettiev <crux@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Tue Dec 08 2015 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sun Oct 25 2015 Vladimir Lettiev <crux@altlinux.ru> 1.4.0-alt1
- 1.4.0
- enabled tests

* Fri May 16 2014 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt3
- 0.4.0

* Thu May 01 2014 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt2.9ca63de9
- http2 draft-12 (commit 9ca63de9)

* Fri Apr 11 2014 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1.27a91fc3
- http2 draft-11 (commit 27a91fc3)

* Thu Feb 27 2014 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt0.ddf61625
- experimental release (commit ddf61625)

