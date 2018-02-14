Summary: Openfire XMPP Server
Name: openfire
Version: 4.2.2
Release: alt1

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Group: Networking/Instant messaging
License: Apache Software License 2.0
Url: http://www.igniterealtime.org/
BuildArch: noarch

%define prefix %_datadir
%define firedir %prefix/%name

Requires: jre-openjdk >= 1.7.0

BuildPreReq: /proc rpm-build-java java-1.8.0-openjdk-devel
# Automatically added by buildreq on Sat Jul 12 2014
BuildRequires: ant-apache-bsf ant-apache-log4j ant-apache-resolver ant-commons-logging ant-commons-net ant-junit

%description
Openfire is a leading Open Source, cross-platform IM server based on the
XMPP (Jabber) protocol. It has great performance, is easy to setup and use,
and delivers an innovative feature set.

%prep
%setup -q
%patch0 -p1

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
%__install -p -m 644 target/%name/conf/security.xml %buildroot%_sysconfdir/%name/security.xml
%__install -p -m 755 %name.init %buildroot%_initdir/%name
%__install -p -m 755 target/%name/bin/extra/embedded-db.rc %buildroot%_bindir/embedded-db.rc
%__install -p -m 755 target/%name/bin/extra/embedded-db-viewer.sh %buildroot%_bindir/embedded-db-viewer.sh
%__cp -aRf target/%name/lib %buildroot%firedir/
%__cp -aRf target/%name/plugins %buildroot%_localstatedir/%name/
%__cp -aRf target/%name/resources/database %buildroot%firedir/resources/
%__cp -aRf target/%name/resources/security %buildroot%_sysconfdir/%name

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
%doc documentation/dist/changelog.html documentation/dist/LICENSE.html documentation/dist/README.html
%_bindir/*
%attr(-,_%name,_%name) %firedir
%attr(-,_%name,_%name) %_localstatedir/%name
%config %_initrddir/%name
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/%name.xml
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/security.xml
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/security/keystore
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/security/truststore
%config(noreplace) %attr(640,_%name,_%name) %_sysconfdir/%name/security/client.truststore
%config(noreplace) %attr(644,root,root) %_sysconfdir/sysconfig/openfire
%dir %attr(750,_%name,_%name) %_sysconfdir/%name/security
%dir %attr(750,_%name,_%name) %_sysconfdir/%name
%dir %attr(3770,_%name,_%name) %_logdir/%name

%changelog
* Wed Feb 14 2018 Alexei Takaseev <taf@altlinux.org> 4.2.2-alt1
- 4.2.2

* Mon Oct 30 2017 Alexei Takaseev <taf@altlinux.org> 4.1.6-alt2
- Rebuild with java-1.8.0-openjdk-devel

* Fri Oct 06 2017 Alexei Takaseev <taf@altlinux.org> 4.1.6-alt1
- 4.1.6

* Mon Jul 03 2017 Alexei Takaseev <taf@altlinux.org> 4.1.5-alt1
- 4.1.5

* Fri May 05 2017 Alexei Takaseev <taf@altlinux.org> 4.1.4-alt1
- 4.1.4

* Tue Apr 25 2017 Alexei Takaseev <taf@altlinux.org> 4.1.3-alt2
- Fix ALT#33415

* Fri Mar 03 2017 Alexei Takaseev <taf@altlinux.org> 4.1.3-alt1
- 4.1.3

* Mon Jan 23 2017 Alexei Takaseev <taf@altlinux.org> 4.1.1-alt1
- 4.1.1

* Mon Dec 26 2016 Alexei Takaseev <taf@altlinux.org> 4.1.0-alt1
- 4.1.0

* Fri Dec 02 2016 Alexei Takaseev <taf@altlinux.org> 4.0.4-alt1
- 4.0.4

* Thu Aug 18 2016 Alexei Takaseev <taf@altlinux.org> 4.0.3-alt1
- 4.0.3

* Tue Mar 22 2016 Alexei Takaseev <taf@altlinux.org> 4.0.2-alt1
- 4.0.2

* Wed Jan 27 2016 Alexei Takaseev <taf@altlinux.org> 4.0.1-alt1
- 4.0.1

* Wed Jan 13 2016 Alexei Takaseev <taf@altlinux.org> 4.0.0-alt1
- 4.0.0

* Wed Nov 18 2015 Alexei Takaseev <taf@altlinux.org> 3.10.3-alt1
- 3.10.3

* Tue Jun 23 2015 Alexei Takaseev <taf@altlinux.org> 3.10.2-alt1
- 3.10.2

* Wed Jun 17 2015 Alexei Takaseev <taf@altlinux.org> 3.10.1-alt1
- 3.10.1

* Wed Apr 22 2015 Alexei Takaseev <taf@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sat Jul 12 2014 Alexei Takaseev <taf@altlinux.org> 3.9.3-alt3
- Rebuild with java-1.7.0-openjdk

* Thu Jul 03 2014 Alexei Takaseev <taf@altlinux.org> 3.9.3-alt2
- Add lost config file

* Tue Jun 03 2014 Alexei Takaseev <taf@altlinux.org> 3.9.3-alt1
- 3.9.3

* Sat Feb 08 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 3.9.1-alt1
- New version

* Tue May 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.8.2-alt1
- New version (closes #29006)

* Sat May 25 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.8.1-alt1
- New version (closes #29006)

* Fri Feb 08 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.8.0-alt1
- New version (closes #28522)

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
