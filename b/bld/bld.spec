%define bld_user bld
%define bld_group bld
%define bld_home %_localstatedir/%name
Name: bld
Version: 0.3.4.1
Release: alt2

Summary: BLD stands for "blacklist daemon" and is intended to serve a blacklist.
Group: System/Servers
License: BSD
Url: http://bld.r14.freenix.org/
Source0: %name-%version.tar
Source1: %name.init
Source2: %name.conf
# patch from debian
Patch0: 01-fix_potential_core_dump 
Packager: Alexey Morsov <swi@altlinux.ru>

BuildRequires: perl-devel

%description
BLD stands for "blacklist daemon" and is intended to serve a blacklist.
The blacklist is built by simply inserting IP addresses or by using
submission rate limits based on a maximum number of submissions of the
same IP address within a minimum time interval. You can build a BLD
cluster by configuring the daemon to notify other similar daemon(s)
every time an IP address is added to the blacklist. BLD was primarily
designed to fight against dictionary-based spams (by making the MTA
report to BLD any host that tries to send a mail to an unknown user)
but can be used by any program.

See %_defaultdocdir/%name-%version/COPYRIGHT for license.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
# dirs
install -d -m1711 %buildroot%_localstatedir/%name
install -d -m1755 %buildroot%_var/run/%name
install -d -m1755 %buildroot%_sysconfdir/%name

# files
install -pD -m0755 %SOURCE1 %buildroot%_initdir/%name
install -p -m0644 %SOURCE2 %buildroot%_sysconfdir
touch %buildroot%_sysconfdir/%name/bld_whitelist.conf
touch %buildroot%_sysconfdir/%name/bld_acl.conf

# docs
mkdir -p %buildroot%_defaultdocdir/%name-%version
cp COPYRIGHT ChangeLog README.postfix TODO bld.conf.sample %buildroot%_defaultdocdir/%name-%version/
rm -f %buildroot%_sbindir/bld-mrtg.pl # it's broken

%pre
/usr/sbin/groupadd -r -f %bld_group ||:
/usr/sbin/useradd -g %bld_group -c 'blacklist daemon' \
        -d %bld_home -s /dev/null -r %bld_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name


%files
%doc COPYRIGHT ChangeLog README* TODO bld.conf.sample
%_initdir/%name
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/%name/*
%dir %attr(1771,root,%bld_group) %_localstatedir/%name
%dir %attr(1775,root,%bld_group) %_var/run/%name
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Fri Jan 29 2010 Alexey Morsov <swi@altlinux.ru> 0.3.4.1-alt2
- fix init file
- fix conf file

* Thu Jan 28 2010 Alexey Morsov <swi@altlinux.ru> 0.3.4.1-alt1
- initial build

