Summary: Openfire XMPP Server
Name: openfire
Version: 3.7.1
Release: alt2

Source0: openfire_src_3_7_1.tar.gz
Source1: openfire.init
Group: Networking/Instant messaging
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
License: Apache
Url: http://www.igniterealtime.org/
BuildArch: noarch

%define prefix %_datadir
%define firedir %prefix/%name

Requires: /usr/bin/java

BuildPreReq: /proc rpm-build-java java-1.6.0-sun-devel
# Automatically added by buildreq on Sun Apr 06 2008
BuildRequires: ant-bsf ant-commons-logging ant-commons-net ant-junit ant-log4j ant-xml-resolver antlr jakarta-oro sun-jaf xalan-j2

%description
Openfire is a leading Open Source, cross-platform IM server based on the
XMPP (Jabber) protocol. It has great performance, is easy to setup and use,
and delivers an innovative feature set.

%prep
%setup -q -n openfire_src

%build
cd build
ant openfire
ant -Dplugin=search plugin
cd ..

%install

%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_logdir/%name
%__mkdir_p %buildroot%firedir/{resources,bin}
%__mkdir_p %buildroot%_initrddir
%__mkdir_p %buildroot%_sysconfdir/sysconfig
%__mkdir_p %buildroot%_sysconfdir/%name/security
%__mkdir_p %buildroot%_localstatedir/%name/embedded-db
#%__mkdir_p %buildroot%firedir/resources/nativeAuth

%__install -p -m 644 target/%name/bin/extra/redhat/openfire-sysconfig %buildroot%_sysconfdir/sysconfig/%name
%__install -p -m 644 target/%name/conf/openfire.xml %buildroot%_sysconfdir/%name/%name.xml
%__install -p -m 755 %SOURCE1 %buildroot%_initrddir/%name
%__install -p -m 755 target/%name/bin/extra/embedded-db.rc %buildroot%_bindir/embedded-db.rc
%__install -p -m 755 target/%name/bin/extra/embedded-db-viewer.sh %buildroot%_bindir/embedded-db-viewer.sh
%__cp -aRf target/%name/lib %buildroot%firedir/
%__cp -aRf target/%name/plugins %buildroot%_localstatedir/%name/
%__cp -aRf resources/i18n %buildroot%firedir/resources/
%__cp -aRf target/%name/resources/database %buildroot%firedir/resources/
%__cp -aRf target/%name/resources/security %buildroot%_sysconfdir/%name
#%__cp -aRf target/%name/resources/spank %buildroot%firedir/resources/

ln -s %_sysconfdir/%name %buildroot%firedir/conf
ln -s %_sysconfdir/%name/security %buildroot%firedir/resources/security
ln -s %_localstatedir/%name/embedded-db %buildroot%firedir/embedded-db
ln -s %_localstatedir/%name/plugins %buildroot%firedir/plugins
ln -s %_logdir/%name %buildroot%firedir/logs
ln -s %_bindir/embedded-db-viewer.sh %buildroot%firedir/bin/embedded-db-viewer.sh
ln -s %_bindir/embedded-db.rc %buildroot%firedir/bin/embedded-db.rc

%pre
/usr/sbin/useradd -r -d %firedir -c 'Openfire XMPP server' -s /bin/sh  _%name &> /dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc documentation/docs
%doc changelog.html LICENSE.html README.html
%_bindir/*
%attr(-,_%name,_%name) %firedir
%attr(-,_%name,_%name) %_localstatedir/%name
%config %_initrddir/%name
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/%name.xml
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/security/keystore
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/security/truststore
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/security/client.truststore
%config(noreplace) %attr(644,root,root) %_sysconfdir/sysconfig/openfire
%dir %attr(750,_%name,_%name) %_sysconfdir/%name/security
%dir %attr(750,_%name,_%name) %_sysconfdir/%name
%dir %attr(3770,_%name,_%name) %_logdir/%name

%exclude %firedir/lib/*.dll

%changelog
* Wed May 09 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.7.1-alt2
- Fix build

* Wed Oct 19 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.7.1-alt1
- New version

* Thu Mar 17 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.7.0-alt2
- Fix repocop warnings
- Fix init script

* Sat Mar 05 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 3.7.0-alt1
- New version

* Wed Oct 22 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 3.6.0a-alt1
- New version

* Thu Apr 03 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 3.4.5-alt1
- Build for ALT
