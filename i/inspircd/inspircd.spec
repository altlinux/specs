%define _inspircd_user _inspircd
%define _inspircd_group _inspircd
ExcludeArch: %ix86

Name: inspircd
Version: 4.12.0
Release: alt1

Summary: InspIRCd is a modular Internet Relay Chat (IRC) server 
Group: Networking/IRC
License: GPLv2

URL: https://www.inspircd.org
VCS: https://github.com/inspircd/inspircd/

Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source3: logrotate
Patch0: alt-main-mk.patch

BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: pkg-config

%description
It was created from scratch to be stable, modern and lightweight.
It avoids a number of design flaws and performance issues that plague other 
more established projects, such as UnrealIRCd, while providing the same level
of feature parity.

It provides a tunable number of features through the use of an advanced but 
well documented module system. By keeping core functionality to a minimum we 
hope to increase the stability, security and speed of InspIRCd while also
making it customisable to the needs of many different users.


%prep
%setup
%patch0 -p1

%build
%add_optflags %optflags_shared
export CXXFLAGS='%optflags'

# handmade perl configure; CXXFLAGS already appended by upstream makefile
./configure \
	--disable-interactive \
	--disable-ownership \
	--prefix=%_prefix \
	--binary-dir=%_bindir \
	--module-dir=%_libdir/%name \
	--config-dir=%_sysconfdir/%name \
	--log-dir=%_logdir/%name \
	--data-dir=%_localstatedir/%name \
	--runtime-dir=%_runtimedir/%name \
	--script-dir=%_datadir/%name \
	--example-dir=%_sysconfdir/%name/examples \
	--manual-dir=%_mandir/man1
%make_build

%install
%makeinstall_std
install -pD -m0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pD -m0755 %SOURCE2 %buildroot%_initdir/%name
install -pD -m0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -pD -m0644 %buildroot%_sysconfdir/%name/examples/%name.example.conf \
	%buildroot%_sysconfdir/%name/%name.conf
install -d -m0755 %buildroot%_runtimedir/%name
install -d -m0755 %buildroot%_localstatedir/%name
install -d -m0755 %buildroot%_logdir/%name
# perl test helper; pulls IO::Socket::SSL, not needed for the daemon
rm -f %buildroot%_bindir/%name-testssl \
	%buildroot%_mandir/man1/%name-testssl.1*

%pre
/usr/sbin/groupadd -r %_inspircd_group &>/dev/null ||:
/usr/sbin/useradd  -r -g %_inspircd_group -s /bin/false -c "InspIRCd irc server" \
    -d %_localstatedir/%name %_inspircd_user &>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%dir %_libdir/%name
%dir %_sysconfdir/%name
%dir %_datadir/%name
%dir %attr(0775,root,%_inspircd_group) %_runtimedir/%name
%dir %attr(0770,root,%_inspircd_group) %_localstatedir/%name
%dir %attr(0770,root,%_inspircd_group) %_logdir/%name

%_bindir/%name
%_initdir/%name
%_libdir/%name/*.so
%_datadir/%name/*
%_mandir/man1/%name.1*
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/help.txt
%config(noreplace) %_logrotatedir/%name
%_sysconfdir/%name/examples
%_unitdir/%name.service
%doc README.md

%changelog
* Fri Sep 11 2026 Anton Farygin <rider@altlinux.org> 4.12.0-alt1
- 2.0.29 -> 4.12.0

* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.29-alt1
- Updated to upstream version 2.0.29 (Fixes: CVE-2019-20917, CVE-2020-25269).

* Tue Jun 26 2018 Pavel Akopov <pak@altlinux.org> 2.0.26-alt1
- initial build

