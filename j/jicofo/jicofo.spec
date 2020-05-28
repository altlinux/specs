%set_verify_elf_method textrel=relaxed
Name:           jicofo
Version:        1.1
Release:        alt0.2

Summary:        JItsi Meet COnference FOcus
#Group:          Networking/Instant messaging
Group:          System/Servers
License:        Apache-2.0
URL:            http://www.jitsi.org
# VCS:          https://github.com/jitsi/jicofo.git

#ExclusiveArch:  %ix86 x86_64
ExclusiveArch:  x86_64
#BuildArch: noarch

Source0:        %name-%version.tar
Source1:        m2-%name-%version.tar
#Source2:        %name.sh

AutoReqProv: yes,noosgi

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel-default
BuildRequires:  maven
BuildRequires:  unzip

Requires:	java

%description
Jicofo is a conference focus for Jitsi Meet application.

%prep
tar -x -C ~ -f %SOURCE1
%setup

%build
mvn install -Dassembly.skipAssembly=false
mvn -DskipTests -Dassembly.skipAssembly=true package
mvn dependency:copy-dependencies -DincludeScope=runtime

%install
mkdir -p %buildroot%_datadir/jicofo/lib/ %buildroot%_sysconfdir/jitsi/jicofo/ %buildroot%_sysconfdir/logrotate.d/
install -m644 target/dependency/*             %buildroot%_datadir/jicofo/lib/
install -m644 lib/logging.properties          %buildroot%_sysconfdir/jitsi/jicofo/
install -m644 target/jicofo-%version-SNAPSHOT.jar  %buildroot%_datadir/jicofo/jicofo.jar
install -m644 resources/jicofo.sh             %buildroot%_datadir/jicofo/
install -m644 resources/collect-dump-logs.sh  %buildroot%_datadir/jicofo/
install -m644 resources/config/jicofo-logrotate.d %buildroot%_sysconfdir/logrotate.d/jicofo

%files
%dir %_datadir/jicofo
%_datadir/jicofo/lib
%_datadir/jicofo/jicofo.jar
%_datadir/jicofo/jicofo.sh
%_datadir/jicofo/collect-dump-logs.sh
%dir %_sysconfdir/jitsi/jicofo
%config %_sysconfdir/jitsi/jicofo/logging.properties
%config %_sysconfdir/logrotate.d/jicofo

%changelog
* Thu May 28 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.2
- initial build

