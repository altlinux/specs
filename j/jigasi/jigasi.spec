%set_verify_elf_method textrel=relaxed
%define         pseudouser_name jigasi
%define _localstatedir %{_var}

Name:           jigasi
Version:        1.1
Release:        alt0.3

Summary:        Jitsi Gateway for SIP
#Group:          Networking/Instant messaging
Group:          System/Servers
License:        Apache-2.0
URL:            http://www.jitsi.org
# VCS:          https://github.com/jitsi/jigasi.git

#ExclusiveArch:  %ix86 x86_64
ExclusiveArch:  x86_64

Source0:        %name-%version.tar
Source1:        m2-%name-%version.tar
Source2:        %name.sh

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel-default
#BuildRequires:  ant
BuildRequires:  maven
BuildRequires:  unzip
BuildRequires:	libmatthew-java

Requires:	java
Requires:	libmatthew-java
#Requires:	dnsjava

%description
Jitsi Meet is a WebRTC JavaScript application that uses Jitsi
Videobridge to provide high quality, scalable video conferences.

It is a web interface to Jitsi Videobridge for audio and video
forwarding and relaying, configured to work with nginx

This package contains the jigasi (Jitsi Gateway for SIP) daemon,
which allows SIP accounts to be invited in Jitsi Meet conferences.

%prep
tar -x -C ~ -f %SOURCE1
%setup

%build
#ant rebuild
mvn install -Dassembly.skipAssembly=false

%install
%ifarch x86_64
find lib/native/linux-64/ -maxdepth 1 -type f -execdir install -Dm644 {} "%buildroot%_libdir/%name/lib/native/"{} \; 2>/dev/null ||:
%else
find lib/native/linux/ -maxdepth 1 -type f -execdir install -Dm644 {} "%buildroot%_libdir/%name/lib/native/"{} \; 2>/dev/null ||:
%endif

mkdir -p %buildroot%_sysconfdir/jitsi/%name
install -m 644 jigasi-home/sip-communicator.properties jigasi-home/callstats-java-sdk.properties jigasi-home/log4j2.xml %buildroot%_sysconfdir/jitsi/%name/

mkdir -p %buildroot%_datadir/%name/lib
install -m 755 script/collect-dump-logs.sh script/graceful_shutdown.sh %buildroot%_datadir/%name/

mkdir ASSEMBLY
cd ASSEMBLY
%ifarch x86_64
unzip ../target/jigasi-linux-x64-1.1-SNAPSHOT.zip
cd jigasi-linux-x64-1.1-SNAPSHOT
%else
unzip ../target/jigasi-linux-x86-1.1-SNAPSHOT.zip
cd jigasi-linux-x86-1.1-SNAPSHOT
%endif
# -- use system libmattew-java ------
%if 1
rm lib/unix-0.5.1.jar
rm lib/libunix-0.5.1.so
ln -s /usr/lib/java/unix.jar %buildroot%_datadir/%name/lib/
%else
mv lib/libunix-0.5.1.so %buildroot%_datadir/%name/lib/
%endif
# -- end use system libmattew-java --
install -m644 lib/*.jar %buildroot%_datadir/%name/lib/
#install -m 644 lib/logging.properties %buildroot%_datadir/%name/lib
install -m 644 lib/logging.properties %buildroot%_sysconfdir/jitsi/%name/
rm graceful_shutdown.sh jigasi.sh lib/logging.properties lib/*.jar
rm -r lib/native
rmdir lib
mv jigasi-1.1-SNAPSHOT.jar %buildroot%_datadir/%name/
ln -s jigasi-1.1-SNAPSHOT.jar %buildroot%_datadir/%name/jigasi-1.1.jar
ln -s jigasi-1.1-SNAPSHOT.jar %buildroot%_datadir/%name/jigasi.jar
cd ../..

# Install executable start script
install -Dm0755 %SOURCE2 %buildroot%_bindir/%name
install -Dm0755 %SOURCE2 %buildroot%_datadir/%name/%name.sh

# debian
install -D -m 644 debian/%name.service %buildroot%_unitdir/%name.service
install -D -m 644 debian/init.d %buildroot%_initdir/%name

mkdir -p %buildroot%_localstatedir/log/jitsi

# config; filled by %_sbindir/%{name}-configure
touch %buildroot%_sysconfdir/jitsi/%name/{config,sip-communicator.properties}

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %pseudouser_name -G %name  -c 'Jitsi Gateway for SIP' \
        -s /sbin/nologin  -d %_datadir/%name %pseudouser_name 2>/dev/null ||:

%post
#if ! [ -s /etc/jitsi/%name/config ]; then
#    %_sbindir/%{name}-configure
#fi
%post_service %name

%preun
%preun_service %name


%files
%doc LICENSE
%doc README.md
%dir %_sysconfdir/jitsi
%dir %_sysconfdir/jitsi/%name
%config(noreplace) %_sysconfdir/jitsi/%name/config
%config(noreplace) %_sysconfdir/jitsi/%name/sip-communicator.properties
%config %_sysconfdir/jitsi/%name/callstats-java-sdk.properties
%config %_sysconfdir/jitsi/%name/log4j2.xml
%config %_sysconfdir/jitsi/%name/logging.properties
%_bindir/%name
%_libdir/%name
%_datadir/%name
%_unitdir/%name.service
%_initdir/%name

%changelog
* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.3
- Sisyphus build

* Mon Apr 13 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.2
- initial build

