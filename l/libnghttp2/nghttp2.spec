Name: libnghttp2
Version: 0.4.0
Release: alt2.9ca63de9

Summary: HTTP/2.0 C Library
Group: System/Libraries
License: MIT

Url: http://tatsuhiro-t.github.io/nghttp2/
Source: %name-%version.tar

BuildRequires: zlib-devel libevent-devel libxml2-devel libjansson-devel libssl-devel gcc-c++

%description
%summary

%package devel
Group: Development/C
Summary: HTTP/2.0 C Library headers
Requires: %name = %version-%release
%description devel
%summary

%package tools
Group: Networking/WWW
Summary: HTTP/2.0 client, server and proxy
Requires: %name = %version-%release
%description tools
%summary

%prep
%setup -q

%build
%autoreconf
%configure

%install
%makeinstall_std

%files tools
%_bindir/nghttp
%_bindir/nghttpd
%_bindir/nghttpx
%_bindir/h2load
%_man1dir/nghttp.1*
%_man1dir/nghttpd.1*
%_man1dir/nghttpx.1*

%files devel
%_includedir/nghttp2/nghttp2.h
%_includedir/nghttp2/nghttp2ver.h
%_libdir/libnghttp2.so
%_libdir/pkgconfig/libnghttp2.pc
%doc README.rst AUTHORS COPYING ChangeLog

%files 
%_libdir/libnghttp2.so.*

%changelog
* Thu May 01 2014 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt2.9ca63de9
- http2 draft-12 (commit 9ca63de9)

* Fri Apr 11 2014 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1.27a91fc3
- http2 draft-11 (commit 27a91fc3)

* Thu Feb 27 2014 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt0.ddf61625
- experimental release (commit ddf61625)

