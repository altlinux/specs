#TODO:
# -
%define nagios_confdir   %_sysconfdir/nagios
%define nagios_usr nagios
%define nagios_grp nagios
%define realname nsca

Name: nagios-%realname
Version: 2.7.2
Release: alt3

Summary: NSCA -- Nagios(R) Service Checks Acceptor daemon
License: GPL
Group: Monitoring
URL: http://www.nagios.org
Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Requires: nagios

Source0: %realname-%version.tar.gz
Source1: nsca-init

Patch0: %realname-2.7.2-alt-config.patch
Patch1: %realname-2.7.2-alt-warnings.patch

Prefix: %prefix

# Automatically added by buildreq on Mon Feb 13 2006
BuildRequires: libmcrypt-devel libwrap-devel

%package -n nagios-%realname-sender
Summary: Service checks sender for NSCA.
License: GPL
Group: Monitoring

%description
The %name packages contains the Nagios(R) Service Checks Acceptor
-- daemon which allow you to send service check results to a
central monitoring server running Nagios in a secure manner.
This program runs as a daemon on the central server that runs Nagios.
It listens for host and service check results from remote machines
(sent using the send_nsca program from nagios-nsca-sender package).

%description -n nagios-%realname-sender
This package conotains the client program that is used to send
service check information from a remote machine to the nsca daemon
on the central machine that runs Nagios.

%prep
%setup -n %realname-%version
%patch0 -p1 -b .p0
%patch1 -p1 -b .p1

%build
%configure \
 --with-nsca-user=%nagios_usr \
 --with-nsca-grp=%nagios_grp \
 --with-nsca-port=65533

%__make

%install
mkdir -p %buildroot/%nagios_confdir

# install binaries
install -pDm0755 %SOURCE1 %buildroot/%_initdir/nsca
install -pDm0711 src/nsca %buildroot/%_sbindir/nsca
install -pDm0711 src/send_nsca %buildroot/%_bindir/send_nsca

# install config
install -pDm0640 sample-config/nsca.cfg %buildroot/%nagios_confdir/nsca.cfg
install -pDm0640 sample-config/send_nsca.cfg %buildroot/%_sysconfdir/send_nsca.cfg

%post
%post_service %realname

%preun
%preun_service %realname


%files
%attr(0640,root,%nagios_grp) %config(noreplace) %nagios_confdir/nsca.cfg
%_initdir/nsca
%_sbindir/nsca
%doc Changelog sample-config/nsca.xinetd README SECURITY


%files -n nagios-%realname-sender
%attr(0640,root,%nagios_grp) %config(noreplace) %_sysconfdir/send_nsca.cfg
%_bindir/send_nsca
%doc Changelog README SECURITY

%changelog
* Mon Jan 12 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 2.7.2-alt3
- fixes according to repocop repotrts:
  + add LSB headers to init-script
  + add 'Packager' tag to spec-file

* Thu May 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.7.2-alt2
- start NSCA daemon via init-script. By default:
  + bind to 127.0.0.1:65533
- fix Requires for nagios-nsca and nagios-nsca-sender packages

* Fri Mar 14 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.7.2-alt1
- 2.7.2

* Sun May 06 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Sat Jan 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.7-alt1
- 2.7

* Sat Jul 01 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.6-alt1
- 2.6

* Mon Feb 13 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.5-alt1
- 2.5

* Wed Mar 10 2004 Denis Smirnov <mithraen@altlinux.ru> 2.4-alt2
- libdb4.0 req deleted

* Thu Oct 09 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4-alt1
- initial package for ALT Llinux
