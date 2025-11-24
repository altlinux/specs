%define ppp_ver %((%{__awk} '/^#define PPPD_VERSION/ { print $NF }' /usr/include/pppd/pppdconf.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')

Name: ppp-pptp
Version: 0.8.7.1
Release: alt1
Summary: PPTP VPN plugin for pppd
License: GPLv2
Group: System/Servers
Url: https://github.com/winterheart/accel-pptp/

Requires: ppp = %ppp_ver

Source0: %name-%version.tar

BuildRequires(pre): ppp-devel cmake
BuildRequires: gcc-c++

%description
The  PPTP  plugin for pppd performs interaction with pptp kernel module
and has built-in call manager (client part of PPTP).  It pasees  neces-
sary  paremeters  from options into kernel module to configure ppp-pptp
channel. If it runs in client  mode,  then  additionally  call  manager
starts up. PPTPD daemon automaticaly invokes this plugin in server mode
and passes  necessary  options,  so  additional  configuration  is  not
needed.

%prep
%setup

%build
%cmake \
      -DCMAKE_INSTALL_PREFIX=%prefix \
      -DEXT_INCLUDE="`pwd`" \
      -DPPP_PLUGIN_PATH=%_libdir/pppd/%ppp_ver

%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/pppd/%ppp_ver/*.so
%_man8dir/*.8*

%changelog
* Sun Nov 23 2025 Alexei Takaseev <taf@altlinux.org> 0.8.7.1-alt1
- 0.8.7.1
- rebuild with ppp 2.5.2
- Use cmake

* Tue Mar 10 2020 Alexey Shabalin <shaba@altlinux.org> 0.8.5-alt3
- rebuild with ppp 2.4.8

* Mon Jan 19 2015 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt2
- rebuild with ppp 2.4.7

* Thu Jan 13 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.5-alt1
- initial release

