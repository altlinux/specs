# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/flock /usr/bin/gunzip /usr/bin/less /usr/bin/renice /usr/bin/zcat perl(Text/ParseWords.pm)
# END SourceDeps(oneline)

# do not package fireqos due to bash4 bashisms (regexp in case)
# TODO: backport rate2bps() function in fireqos from bash 4
%def_without fireqos

Summary: An easy to use but powerfull iptables stateful firewall
Name: firehol
Version: 2.0.1
Release: alt1
License: GPL
Group: System/Configuration/Networking
Source0: %name-%version.tar
Source1: ftp_ssl.conf
Source2: firehol.service
Source3: fireqos.service
Patch1: firehol-sbin-alt-init.patch
Patch2: firehol-sbin-alt-iptables.patch
Url: http://firehol.org/

BuildArch: noarch

BuildRequires:  /sbin/insmod /sbin/modprobe
BuildRequires:  coreutils
BuildRequires:  iproute
BuildRequires:  iptables
BuildRequires:  procps-ng
BuildRequires:  systemd

Requires: which

%description
FireHOL uses an extremely simple but powerfull way to define firewall
rules which it turns into complete stateful iptables firewalls.  FireHOL
is a generic firewall generator, meaning that you can design any kind of
local or routing stateful packet filtering firewalls with ease.

Install FireHOL if you want an easy way to configure stateful packet
filtering firewalls on Linux hosts and routers.

You can run FireHOL with the 'helpme' argument, to get a configuration
file for the system run, which you can modify according to your needs.

The default configuration file will allow only client traffic on all
interfaces.

%prep
%setup
%patch1 -p2
%patch2 -p2

%build
%configure
%make

%install

%makeinstall_std

# Hack for documentation without crufts.
rm -frv %{buildroot}%{_docdir}
find doc/ examples/ -name "Makefile*" -delete -print

# Install systemd units.
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:2} %{S:3} %{buildroot}%{_unitdir}

mkdir -p %buildroot%_initdir
install -m 750 sbin/firehol %buildroot%_initdir/firehol

# Install runtime directories.
mkdir -p %{buildroot}%{_sysconfdir}/firehol/services
mkdir -p %{buildroot}%{_var}/spool/firehol

# Ghost configurations.
touch %{buildroot}%{_sysconfdir}/firehol/firehol.conf \
      %{buildroot}%{_sysconfdir}/firehol/fireqos.conf

%if 0
mkdir -p %buildroot%_sysconfdir/firehol/services
install -m 640 examples/client-all.conf %buildroot%_sysconfdir/firehol/firehol.conf
%endif

%if_without fireqos
# TODO: backport fireqos to bash3
rm -f %buildroot%_sbindir/fireqos %{buildroot}%{_unitdir}/fireqos.service
%endif

%pre
%post
if [ -f %_sysconfdir/firehol.conf -a ! -f %_sysconfdir/firehol/firehol.conf ]
then
	mv -f %_sysconfdir/firehol.conf %_sysconfdir/firehol/firehol.conf
	echo
	echo
	echo "FireHOL has now its configuration in %_sysconfdir/firehol/firehol.conf"
	echo "Your existing configuration has been moved to its new place."
	echo
fi
%post_service firehol
%if_with fireqos
%post_service fireqos
%endif

%preun
%preun_service firehol
%if_with fireqos
%post_service fireqos
%endif

%files
%doc AUTHORS COPYING NEWS README ChangeLog
%dir %_sysconfdir/firehol
%dir %_sysconfdir/firehol/services
%_sysconfdir/firehol/services/*
%_sbindir/*
%_initdir/firehol
%{_unitdir}/*
%_man1dir/*
%_man5dir/*
%config(noreplace) %_sysconfdir/firehol/firehol.conf
%config(noreplace) %_sysconfdir/firehol/fireqos.conf
%_sysconfdir/firehol/firehol.conf.example
%_sysconfdir/firehol/fireqos.conf.example
%doc examples
%doc doc/*

%changelog
* Tue Oct 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1
- new version
- still w/o fireqos due to bash4 bashisms

* Sat Nov 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2
- clean def_without fireqos

* Fri Nov 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- new version
- systemd support
- dropped custom RESERVED_IPS list, no need as ipv4 is allocated.
- do not package fireqos due to bash4 bashisms (regexp in case)
- TODO: backport rate2bps() function in fireqos from bash 4

* Tue Aug 24 2010 L.A. Kostis <lakostis@altlinux.ru> 1.282-alt2.cvs20090219
- Added patches:
  + {alt-get-iana,alt-check-iana}.patch: update to latest
    iana assignments URL and file format.

* Sat Apr 11 2009 L.A. Kostis <lakostis@altlinux.ru> 1.282-alt1.cvs20090219
- 2009-02-19 CVS snapshot.
- update RESERVED_IPS list.

* Fri Aug 29 2008 L.A. Kostis <lakostis@altlinux.ru> 1.268-alt1.cvs20080809
- 2008-08-09 CVS snapshot.
- add -iana scripts to documentation.
- add RESERVED_IPS as static file (feel free to update it manually/by cron).

* Sun Apr 29 2007 L.A. Kostis <lakostis@altlinux.ru> 1.226-alt3.cvs20070210
- update IANA ipv4 reserved address space.

* Sun Mar 18 2007 L.A. Kostis <lakostis@altlinux.ru> 1.226-alt2.cvs20070210
- fix start/stop init priority:
  - make it start early after network and stop before network.

* Sun Feb 11 2007 L.A. Kostis <lakostis@altlinux.ru> 1.226-alt1.cvs20070210
- initial build for ALTLinux.
- 2007-02-10 CVS snapshot.
- add ftp ssl/tls support services.
