Name: swapd
Version: 1.0.5
Release: alt1
License: GPL-2.0-only
Group: System/Kernel and hardware
Summary: Swap file daemon
URL: http://www.rkeene.org/oss/swapd/

Source0: http://www.rkeene.org/files/oss/swapd/swapd-1.0.5.tar.gz
Source1: swapd.conf
Source2: swapd.init

%description
"Swapd" is a daemon that watches free memory and manages swap files. If free
memory drops too low, additional swap files are created. Additionally, if
there is too much free memory, swap files are deactivated and disk space may
be reclaimed.

%prep
%setup

%build
%configure
%make

%install
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_initddir
mkdir -p %buildroot%_man8dir
mkdir -p %buildroot%_man5dir

cp %SOURCE1     %buildroot%_sysconfdir/swapd.conf
cp %SOURCE2     %buildroot%_initddir/swapd
cp swapd        %buildroot%_sbindir/swapd
cp swapd.8      %buildroot%_man8dir/swapd.8
cp swapd.conf.5 %buildroot%_man5dir/swapd.conf.5

%post
%post_service swapd

%preun
%preun_service swapd

%files
%doc README ChangeLog LICENSE
%config %_sysconfdir/swapd.conf
%attr(0755,root,root) %_initddir/swapd
%_sbindir/swapd
%_man8dir/swapd.*
%_man5dir/swapd.conf.*

%changelog
* Mon Sep 06 2021 Sergey Y. Afonin <asy@altlinux.org> 1.0.5-alt1
- Initial build for ALT Linux
