# Spec file for JubJub daemon

%define subname jubjub
%define cname jabber-jubjub
%define username _jabber_%subname

Summary: a daemon for server side logging of XMPP packages

Name: %cname

Version: 1.0.2
Release: alt1

License: %gpl3plus
Group: System/Servers
URL: http://devel.ossg.ru/projects/jubjub

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-licenses jabber-common
BuildRequires: perl-Net-Jabber perl-XML-Simple perl-DBI

Requires(pre): shadow-utils jabber-common
Requires(post): %post_service xmlstarlet
Requires(preun): %preun_service

Source0: %subname-%version.tar.bz2

Source1: %subname.init
Source2: config.xml
Source3: %subname.adapter
Source4: %subname.sysconfig
Source5: %subname.logrotate

BuildArch: noarch

%description
JubJub  is a daemon for  server side logging of  XMPP packages.
It based upon module architecture so it is possible to flexible
reassign handlers for different types of XMPP packages.
JubJub named after collateral character of the famous poem by
L. Carroll.

%define appdir   %_datadir/%cname
%define confdir  %_sysconfdir/%cname
%define logdir   %_logdir/%cname
%define piddir   /var/run/%cname

%define _perl_lib_path %appdir

%prep
%setup -n %subname-%version

%install
mkdir -p %buildroot%appdir  \
	%buildroot%logdir \
	%buildroot%piddir

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/LICENSE) LICENSE

install -m0755 jubjub.pl   %buildroot%appdir/jubjub.pl
cp -r -- JubJub/ %buildroot%appdir/

# init script, jabber-common adapter, logrotate script
install -pD -m0755 %SOURCE1 %buildroot%_initdir/%cname
install -pD -m0644 %SOURCE2 %buildroot%confdir/%cname.xml
install -pD -m0755 %SOURCE3 %buildroot%_jabber_component_dir/%subname
install -pD -m0644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%cname
install -pD -m0644 %SOURCE5 %buildroot%_sysconfdir/logrotate.d/%cname

[ -f VERSION ] || echo "%version, SVN trunk commit $(echo "%release" | sed -n 's/.*svn\([0-9]\+\).*/\1/p')" > VERSION

# Substitute proper values in various scripts
%__subst 's#@logfile@#%logdir/%subname.log#g' %buildroot%confdir/%cname.xml \
						%buildroot%_sysconfdir/logrotate.d/%cname
%__subst 's#@lockfile@#/var/lock/subsys/%{cname}#g' %buildroot%_initdir/%cname
%__subst 's#@pidfile@#%piddir/%subname.pid#g' %buildroot%_initdir/%cname \
						%buildroot%confdir/%cname.xml
%__subst 's#@username@#%{username}#g' %buildroot%_sysconfdir/sysconfig/%cname
%__subst 's#@sysconfigfile@#%_sysconfdir/sysconfig/%{cname}#g' %buildroot%_initdir/%cname
%__subst 's#@basedir@#%{appdir}#g' %buildroot%_initdir/%cname
%__subst 's#@scriptname@#%subname.pl#g' %buildroot%_initdir/%cname
%__subst 's#@configfile@#%confdir/%cname.xml#g' %buildroot%_initdir/%cname \
						%buildroot%_sysconfdir/sysconfig/%cname \
						%buildroot%_jabber_component_dir/%subname

%pre
%_sbindir/groupadd -r -f %username 2>/dev/null ||:
%_sbindir/useradd  -r -g %username -c 'JubJub Jabber service' \
	-d %appdir -s /dev/null %username 2>/dev/null ||:

%post
%_jabber_config
%post_service %name

%preun
%preun_service %name

%files
%doc README.en README.ru VERSION config.xml schema.sql
%doc --no-dereference LICENSE

%attr(0750,root,%username) %dir %confdir
%config(noreplace) %confdir/%cname.xml

%config(noreplace) %_sysconfdir/sysconfig/%cname

%config %_sysconfdir/logrotate.d/%cname

%_jabber_component_dir/%subname

%attr(1770,root,%username) %dir %logdir
%attr(1775,root,%username) %dir %piddir
%_initdir/%cname
%{appdir}*


%changelog
* Sat Mar 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.2-alt1
- Initial build for ALT Linux Sisyphus
