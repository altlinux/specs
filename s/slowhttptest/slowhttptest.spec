Name: slowhttptest
Version: 1.8.2
Release: alt1

Summary: SlowHTTPTest is a highly configurable tool that simulates some Application Layer Denial of Service attacks

Group: File tools
License: GPLv2+
Url: https://github.com/shekyan/slowhttptest

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/shekyan/slowhttptest/archive/v%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Mon Jan 16 2012
# optimized out: libcom_err-devel libkrb5-devel libstdc++-devel
BuildRequires: gcc-c++ libssl-devel

%description
SlowHTTPTest is a highly configurable tool that simulates some Application
Layer Denial of Service attacks.

It implements most common low-bandwidth Application Layer DoS attacks,
such as slowloris, Slow HTTP POST, Slow Read attack (based on TCP persist
timer exploit) by draining concurrent connections pool, as well as Apache
Range Header attack by causing very significant memory and CPU usage on
the server.

%prep
%setup

%build
# missed in upstream
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/*

%changelog
* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Tue Jan 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version (1.7) with rpmgs script

* Fri Mar 21 2014 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt2
- new version 1.6 (with rpmrb script)

* Mon Jan 16 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Linux Sisyphus
