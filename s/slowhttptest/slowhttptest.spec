Name: slowhttptest
Version: 1.3
Release: alt1

Summary: SlowHTTPTest is a highly configurable tool that simulates some Application Layer Denial of Service attacks

Group: File tools
License: GPLv2+
Url: http://code.google.com/p/slowhttptest/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://slowhttptest.googlecode.com/files/%name-%version.tar

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
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name

%changelog
* Mon Jan 16 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- initial build for ALT Linux Sisyphus
