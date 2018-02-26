Name: ziproxy
Version: 3.2.0
Release: alt1

Summary: Ziproxy is a forwarding (non-caching) compressing HTTP proxy server. 

Group: System/Servers
License: GPL
URL: http://ziproxy.sourceforge.net/
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: %name.tar
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

%build
%configure
%make

%install
%makeinstall

%files
%_bindir/%name
%_bindir/ziproxylogtool
%_man1dir/*

%changelog
* Tue Feb 15 2011 Sergey Alembekov <rt@altlinux.ru> 3.2.0-alt1
- initial build for ALTLinux

