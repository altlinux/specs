Name: ziproxy
Version: 3.3.2
Release: alt1

Summary: Ziproxy is a forwarding (non-caching) compressing HTTP proxy server. 

Group: System/Servers
License: GPL-2.0
URL: http://ziproxy.sourceforge.net/
Packager: Sergey Alembekov <rt@altlinux.ru>

Source: %name.tar
Source1: %name.watch
Patch1: ziproxy-ziproxyconf.patch

BuildRequires: libpng-devel libgif-devel libjasper-devel libjpeg-devel zlib-devel libsasl2-devel

%description
Ziproxy is a forwarding (non-caching) compressing HTTP proxy server.
Basically, it squeezes images by converting them to lower quality JPEGs
or JPEG 2000 and compresses (gzip) HTML and other text-like data.
It also provides other features such as: HTML/JS/CSS optimization,
preemptive hostname resolution, transparent proxying, IP ToS marking
(QoS), Ad-Blocker, detailed logging and more.

%prep
%setup -n %name
%patch1 -p1
%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_bindir/ziproxylogtool
%_man1dir/*

%changelog
* Mon Apr 12 2021 Andrey Cherepanov <cas@altlinux.org> 3.3.2-alt1
- New version.
- Add watch file.

* Thu Jun 11 2020 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.
- Fix build for giflib 5.x.
- Fix License tag according to SPDX.

* Wed Oct 16 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.0-alt1.2
- NMU: rebuilt with cyrus-sasl 2.1.26

* Thu Oct 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1.1
- Rebuilt with libpng15

* Tue Feb 15 2011 Sergey Alembekov <rt@altlinux.ru> 3.2.0-alt1
- initial build for ALTLinux

