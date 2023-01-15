# spec file for lsyncd daemon
#

Name: lsyncd
Version: 2.3.1
Release: alt1

Summary: Live Syncing Daemon to synchronize local directories with remote targets

License: %gpl2plus
Group: Networking/File transfer
Url: https://github.com/lsyncd/lsyncd

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name.init
Source2: %name.service
Source3: %name.logrotate

Requires: rsync >= 3.1

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Sat Jan 14 2023
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libsasl2-3 libstdc++-devel lua5.4 python-modules python2-base python3-base sh4
BuildRequires: cmake gcc-c++ libssl-devel lua-devel lua5.3


%if_with tests
BuildRequires: lua5-posix rsync openssh /proc
%endif

%description
Lsyncd (Live Syncing Daemon) watches a local directory trees
event monitor interface (inotify or fsevents). It aggregates
and combines events for a few seconds and then spawns one
(or more) process(es) to synchronize the changes. By default
this is rsync.

Lsyncd is thus a light-weight live mirror solution that is
comparatively easy to install not requiring new file systems
or block devices and does not hamper local file system
performance.

Lsyncd is designed to synchronize a local directory tree with
low profile of expected changes to a remote mirror(s) and
is especially useful to sync data from a secure area to a
not-so-secure area.


%define lsyncd_group     _lsyncd

%prep
%setup
%patch0 -p1

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2.0 %_docdir/%name/COPYING) COPYING

sed -e 's!/path/to/trg/!%_sysconfdir!' -i examples/lecho.lua
sed -e 's!/path/to/trg/!%_sysconfdir!' -i examples/lbash.lua
sed -e 's!src!%_sysconfdir!'           -i examples/lecho.lua

%build
%cmake -DCMAKE_INSTALL_MANDIR=%_mandir/
%cmake_build


%install
%cmakeinstall_std

[ -d %buildroot/usr/doc ] && rm -rf -- %buildroot/usr/doc

# Configuration:
mkdir -p %buildroot%_sysconfdir/%name/
install -m 0644 examples/lecho.lua %buildroot%_sysconfdir/%name/lsyncd.conf.lua

# Init and unit files:
mkdir -p %buildroot%_initdir
install -m 0755 %SOURCE1 %buildroot%_initdir/%name
mkdir -p %buildroot%_unitdir
install -m 0644 %SOURCE2  %buildroot%_unitdir/%name.service

# Logrotate file:
mkdir -p %buildroot%_logrotatedir
install -D -m 0644 %SOURCE3 %buildroot%_logrotatedir/%name

# Log directory:
mkdir -p %buildroot%_logdir/%name


%pre
# Add the "_lsyncd" group
%_sbindir/groupadd -r -f %lsyncd_group 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md ChangeLog examples/
%doc --no-dereference COPYING

%_bindir/%name

%attr(0750,root,%lsyncd_group) %dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*

%attr(1770,root,%lsyncd_group) %dir %_logdir/%name

%config %_initdir/%name
%_unitdir/%name.service
%_man1dir/%name.1*

%config %_logrotatedir/%name

%attr(1770,root,%lsyncd_group) %dir %_logdir/%name


%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 2.3.1-alt1
- Restore from orphaned
- New version

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.4-alt1.git.3c9f8833.1
- NMU: rebuild with new lua 5.3

* Wed Jun 05 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.4-alt1.git.3c9f8833
- Update to last git version
- Move to git
- Add init script
- Add config file

* Sat Jan  7 2012 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- Initial build for ALT Linux Sisyphus
