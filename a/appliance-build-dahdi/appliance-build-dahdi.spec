Name: appliance-build-dahdi
Summary: Packages required for build zaptel/dahdi
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires: bison
Requires: dahdi-linux-headers
Requires: flex
Requires: gcc-c++
Requires: groff-base
Requires: kernel-source-dahdi
Requires: kernel-source-wanpipe
Requires: less
Requires: libtinfo-devel
Requires: libnewt-devel
Requires: libreadline
Requires: libusb-compat-devel
Requires: ppp-devel
Requires: rpm-build-kernel
Requires: rsync
Requires: wget

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

