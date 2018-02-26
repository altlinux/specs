%define user _dcd

Name: dcd
Version: 1.1.1
Release: alt6
Summary: DConnect Daemon - Hub D****ct Connect for Linux
License: %gpl2only
Group: Networking/File transfer
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: ftp://pollux.ds.pg.gda.pl/pub/Linux/DConnect/sources/stable/%name-%version.tar.bz2
Source1: %name.logrotate
Url: http://www.dc.ds.pg.gda.pl/

# Automatically added by buildreq on Tue Jul 17 2007
BuildRequires: gcc-c++ libwrap-devel

BuildPreReq: rpm-build-licenses

# To fix net-scripts req:
AutoReq: yes, noshell

%description
This is Linux D*** Connect Hub implementation for Linux. It works in
daemon mode and utilizes threads.

This daemon will be run by %user user.

%prep
%setup

%build
libtoolize
aclocal
autoconf
automake
%configure --with-config-dir=%_sysconfdir/%name --with-user=%user --with-group=%user
make

%install
mkdir -p %buildroot{%_sysconfdir/{sysconfig,logrotate.d},/var/log/%name} %buildroot%_initdir

%make_install install DESTDIR=%buildroot sbindir=%_bindir

pushd %buildroot%_man1dir
mkdir -p ../pl/man1
mv -v -- * ../pl/man1
mv -v -- ../man2/* .
for i in *.2*
do
mv -v -- $i ${i/.2/.1}
done
rmdir -v ../man2
popd

install contrib/%name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
sed -i 's|\+0|-10|g;s|^SERVICE|#SERVICE|g' %buildroot%_sysconfdir/sysconfig/%name

install %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name

sed -i 's|@LOG_DIR@|%_logdir/%name|g' %buildroot%_sysconfdir/%name/*

install contrib/PLD/%name.init %buildroot%_initdir/%name
sed -i 's|busy|#busy|;
s|msg_net|#msg_net|g;
s|msg_start|#msg_start|g;
s|msg_stop|#msg_stop|g;
s|daemon %name|start_daemon --expect-user %user -- %name|g;
s|killproc %name|stop_daemon --expect-user %user -- %name|g;
s|-- %name -HUP|-HUP -- %name|g;
s/restart)/restart|condrestart)/g;
s| %name \$OPTIONS| $SERVICE_RUN_NICE_LEVEL %name $OPTIONS|;
s|sysconfig/%name *$|sysconfig/%name\n[ ! -z $SERVICE_RUN_NICE_LEVEL ] \&\& SERVICE_RUN_NICE_LEVEL="nice -n $SERVICE_RUN_NICE_LEVEL"|;
' %buildroot%_initdir/%name

%pre
/usr/sbin/groupadd -r -f %user ||:
/usr/sbin/useradd -r -g %user -d %_logdir/%name -s /dev/null -n %user ||:

%post
%post_service %name

%preun
%preun_service %name

%triggerpostun -- %name < 0.3.5
echo "Upgrading from version < 0.3.5"
if [ -e %_sysconfdir/%name/console.users.rpmsave ]; then
	cp %_sysconfdir/%name/%name.users %_sysconfdir/%name/%name.users.rpmnew
	cp %_sysconfdir/%name/console.users.rpmsave %_sysconfdir/%name/%name.users
fi
umask 002
echo "Remember to review config - console users has been changed into dcd.users"
cp %_sysconfdir/%name/%name.conf %_sysconfdir/%name/%name.conf.rpmsave
sed -i 's/console.users/%name.users/g' %_sysconfdir/%name/%name.conf

%triggerpostun -- %name < 0.4.6
echo "Upgrading from version < 0.4.6"
sed -i 's/minimum_sleep_time\b/minimal_sleep_time/' %_sysconfdir/%name/%name.conf

%triggerpostun -- %name < 0.4.9
echo "Upgrading from version < 0.4.9"
sed -i 's/ping_timeout/idle_timeout/' %_sysconfdir/%name/%name.conf

%triggerpostun -- %name < 0.5.5
echo "Upgrading from version < 0.5.5"
sed -i 's/listen_interface/bind_address/' %_sysconfdir/%name/%name.conf

%files
%defattr(644,root,root,755)
%attr(750,%user,root) %dir %_sysconfdir/%name
%attr(460,%user,%user) %config(noreplace) %_sysconfdir/%name/console.allow
%attr(460,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.users
%attr(460,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.banned
%attr(460,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.hublinks
%attr(460,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.usercommands
%attr(644,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.penalties
%attr(464,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.conf
%attr(464,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.motd
%attr(464,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.welcome
%attr(464,%user,%user) %config(noreplace) %_sysconfdir/%name/nicks.allow
%attr(464,%user,%user) %config(noreplace) %_sysconfdir/%name/%name.rules
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%attr(755,root,root) %_bindir/*
%attr(755,root,root) %_initdir/%name
%attr(550,%user,%user) %dir %_logdir/%name
%_man1dir/*
%_mandir/pl/man1/*

%doc AUTHORS BUGS FAQ NEWS README TODO USERCOMMANDS SYSLOG

%changelog
* Fri Aug 20 2010 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt6
- fix requires

* Wed Aug  8 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1.1-alt5
- Files/dirs permissions cleaning (hardening)
- Logrotate config separated

* Thu Jul 26 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1.1-alt4
- Spec cleanup
- SERVICE_RUN_NICE_LEVEL now working

* Fri Jul 20 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1.1-alt3
- Sending HUP after rotating fixed
- %user now created in group %user

* Wed Jul 18 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1.1-alt2
- Configs ownership fixed

* Wed Jul 18 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1.1-alt1
- Initial build for Sisyphus
