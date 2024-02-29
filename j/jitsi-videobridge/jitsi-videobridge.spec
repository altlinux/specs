%define pseudouser_name _jvb
%define service_name jitsi-videobridge
%define _localstatedir %{_var}


Name:    jitsi-videobridge
Version: 2.3.9258
Release: alt1
Epoch:   1

Summary: Jitsi Videobridge - WebRTC compatible Selective Forwarding Unit
License: Apache-2.0
Group:   System/Servers
URL: http://www.jitsi.org
VCS: https://github.com/jitsi/jitsi-videobridge.git

ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source2: %name-configure

AutoReqProv: yes,noosgi

BuildRequires(pre): rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)

Requires: java

%description
Jitsi Videobridge - WebRTC compatible Selective Forwarding Unit (SFU) for
multiuser video communication

%prep
%setup
subst 's/3\.5\.1/3.8.1/;s/>11</>17</' rtp/pom.xml jvb/pom.xml jitsi-media-transform/pom.xml
subst 's|/var/run|/run|' debian/jitsi-videobridge2.service

%build
mvn -Dmaven.repo.local=${PWD}/m2/repository -DskipTests -Dassembly.skipAssembly=true install
mvn -Dmaven.repo.local=${PWD}/m2/repository -DskipTests -Dassembly.skipAssembly=true package
mvn -Dmaven.repo.local=${PWD}/m2/repository dependency:copy-dependencies -DincludeScope=runtime

%install
mkdir -p %buildroot%_sysconfdir/jitsi/videobridge
install -m 644 jvb/lib/logging.properties %buildroot%_sysconfdir/jitsi/videobridge/
install -D -m644 config/logrotate %buildroot%_sysconfdir/logrotate.d/jitsi-videobridge
install -D -m644 config/20-jvb-udp-buffers.conf %buildroot%_sysconfdir/sysctl.d/20-jvb-udp-buffers.conf

mkdir -p %buildroot%_datadir/%name/lib
install -m 644 jvb/lib/videobridge.rc %buildroot%_datadir/%name/lib/
install -m 644 jvb/target/dependency/* %buildroot%_datadir/%name/lib/
install -m 755 jvb/resources/jvb.sh %buildroot%_datadir/%name/
install -m 644 resources/graceful_shutdown.sh %buildroot%_datadir/%name/
install -m 644 resources/collect-dump-logs.sh %buildroot%_datadir/%name/
install -m 644 jvb/target/jitsi-videobridge-2.3-SNAPSHOT.jar %buildroot%_datadir/%name/
ln -s jitsi-videobridge-2.3-SNAPSHOT.jar %buildroot%_datadir/%name/jitsi-videobridge.jar

# Install executable configure script
install -Dm0755 %SOURCE2 %buildroot%_sbindir/%{name}-configure

# debian
install -D -m 644 debian/manpage.1 %buildroot%_man1dir/%name.1
install -D -m 644 debian/jitsi-videobridge2.service %buildroot%_unitdir/%service_name.service
sed -i 's,User=jvb,User=%pseudouser_name,' %buildroot%_unitdir/%service_name.service
install -D -m 755 debian/init.d %buildroot%_initdir/%service_name
sed -i 's,NAME=jvb,NAME=%buildroot%_initdir/%service_name,' %buildroot%_initdir/%service_name

mkdir -p %buildroot%_localstatedir/log/jitsi

# config; filled by %_sbindir/%{name}-configure
touch %buildroot%_sysconfdir/jitsi/videobridge/{config,sip-communicator.properties}

%pre
%_sbindir/groupadd -r -f %pseudouser_name 2>/dev/null ||:
%_sbindir/useradd -r -g %pseudouser_name -G %pseudouser_name  -c 'Jitsi Videobridge Daemon' \
        -s /sbin/nologin  -d %_datadir/%name %pseudouser_name 2>/dev/null ||:

%post
if ! [ -s /etc/jitsi/videobridge/sip-communicator.properties ]; then
    %_sbindir/%{name}-configure
fi
%post_service %service_name

%preun
%preun_service %service_name


%files
%doc LICENSE
%doc README.md CONFIG.md
%dir %_sysconfdir/jitsi
%dir %_sysconfdir/jitsi/videobridge
%config(noreplace) %_sysconfdir/jitsi/videobridge/config
%config(noreplace) %_sysconfdir/jitsi/videobridge/sip-communicator.properties
%config %_sysconfdir/jitsi/videobridge/logging.properties
%config %_sysconfdir/sysctl.d/20-jvb-udp-buffers.conf
%config %_sysconfdir/logrotate.d/jitsi-videobridge
%_man1dir/%name.1*
%_unitdir/%service_name.service
%_initdir/%service_name
%_sbindir/%{name}-configure
%_datadir/%name
%dir %attr(0755,_jvb,_jvb) %_localstatedir/log/jitsi

%changelog
* Wed Feb 28 2024 Andrey Cherepanov <cas@altlinux.org> 1:2.3.9258-alt1
- New version
- Built with openjdk17

* Thu Dec 07 2023 Andrey Cherepanov <cas@altlinux.org> 1:2.3.9111-alt1
- New version

* Thu Oct 26 2023 Andrey Cherepanov <cas@altlinux.org> 1:2.0.8960-alt1
- New version

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 2.1-alt0.8
- java17 support (closes: #45385)

* Mon Jan 24 2022 Igor Vlasenko <viy@altlinux.org> 2.1-alt0.7
- fixed init script permissions (closes: #41778)

* Thu Sep 02 2021 Igor Vlasenko <viy@altlinux.org> 2.1-alt0.6
- build with java8

* Mon Jul 06 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.1-alt0.5
- /var/log/jitsi ownership fixed

* Fri Jun 12 2020 Arseny Maslennikov <arseny@altlinux.org> 2.1-alt0.4
- Made the daemon executable.
- Implemented system pseudouser policy: jvb -> _jvb.

* Mon Jun 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.3
- added service files
- added default configuration

* Mon Apr 13 2020 Igor Vlasenko <viy@altlinux.ru> 2.1-alt0.1
- initial build

