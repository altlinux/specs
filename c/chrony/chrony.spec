Name: chrony
Version: 1.26
Release: alt1

Summary: Chrony clock synchronization program
License: GPLv2 only
Group: System/Configuration/Other

Url: http://chrony.tuxfamily.org/
Source0: http://download.tuxfamily.org/chrony/chrony-%version.tar.gz
Source1: chronyd.init
Source2: chrony.conf
Source3: chrony.keys
Source4: chrony.logrotate
Patch0: chrony-1.24-conflocation.patch

# Automatically added by buildreq on Sat Jun 11 2011
BuildRequires: libcap-devel libncurses-devel libreadline-devel

Conflicts: ntpd openntpd

%description
A pair of programs for keeping computer clocks accurate. chronyd is a daemon
program and chronyc is a command-line interface to it. Time reference sources
for chronyd can be RFC1305 NTP servers, human (via keyboard and chronyc), and
the computer's real-time clock at boot time. chronyd can determine the rate at
which the computer gains or loses time and compensate for it whilst no external
reference is present. chronyd's use of NTP servers can be switched on and off
(through chronyc) to support computers with dial-up/intermittent access to the
Internet. chronyd can also act as an RFC1305-compatible NTP server.

%prep
%setup
%patch0 -p1

%build
CFLAGS="%optflags" \
./configure --prefix=/usr --mandir=%_mandir
%make_build

%install
%makeinstall_std
install -pD -m755 %_sourcedir/chronyd.init %buildroot%_initrddir/chronyd
install -pD -m644 %_sourcedir/chrony.conf %buildroot%_sysconfdir/chrony/chrony.conf
install -pD -m644 %_sourcedir/chrony.keys %buildroot%_sysconfdir/chrony/chrony.keys
install -pD -m644 %_sourcedir/chrony.logrotate %buildroot%_sysconfdir/logrotate.d/chrony
rm -rf %buildroot/usr/doc
install -d %buildroot/var/lib/chrony

%post
%post_service chronyd

%preun
%preun_service chronyd

%files
%exclude %_docdir/chrony
%doc chrony.txt
%config(noreplace) %_initrddir/chronyd
%dir %_sysconfdir/chrony
%config(noreplace) %_sysconfdir/chrony/chrony.conf
%config(noreplace) %_sysconfdir/chrony/chrony.keys
%config(noreplace) %_sysconfdir/logrotate.d/chrony
%_bindir/*
%_sbindir/*
%dir /var/lib/chrony
%_man1dir/*
%_man5dir/*
%_man8dir/*

%changelog
* Mon Jul 18 2011 Victor Forsiuk <force@altlinux.org> 1.26-alt1
- 1.26

* Sat Jun 11 2011 Victor Forsiuk <force@altlinux.org> 1.25-alt1
- 1.25

* Mon Feb 08 2010 Victor Forsiuk <force@altlinux.org> 1.24-alt1
- 1.24. Contains security fixes for CVE-2010-0292, CVE-2010-0293, CVE-2010-0294.

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 1.23-alt2
- Project homepage moved, so fix Url.

* Mon Feb 25 2008 Victor Forsyuk <force@altlinux.org> 1.23-alt1
- Initial build.
