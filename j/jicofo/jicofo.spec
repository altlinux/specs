%set_verify_elf_method textrel=relaxed

%define jicofo_user _jicofo

Name:           jicofo
Version:        1.1.9258
Release:        alt1

Summary:        JItsi Meet COnference FOcus
Group:          System/Servers
License:        Apache-2.0
URL:            http://www.jitsi.org
VCS:            https://github.com/jitsi/jicofo.git

ExclusiveArch:  x86_64

Source0: %name-%version.tar

AutoReqProv: yes,noosgi

BuildRequires(pre): rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)
BuildRequires: mvn(org.xmlunit:xmlunit-core)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.jxmpp:jxmpp-core)
BuildRequires: mvn(org.jxmpp:jxmpp-jid)

Requires: java

%description
Jicofo is a conference focus agent for Jitsi Meet.

%prep
%setup

%build
mvn -Dmaven.repo.local=${PWD}/m2/repository -DskipTests -Dassembly.skipAssembly=false install
mvn -Dmaven.repo.local=${PWD}/m2/repository -DskipTests -Dassembly.skipAssembly=true package
mvn -Dmaven.repo.local=${PWD}/m2/repository dependency:copy-dependencies -DincludeScope=runtime

%install
mkdir -p %buildroot%_datadir/jicofo/lib/ %buildroot%_sysconfdir/jitsi/jicofo/ %buildroot%_sysconfdir/logrotate.d/
install -m644 jicofo/target/dependency/*           %buildroot%_datadir/jicofo/lib/
install -m644 lib/logging.properties          %buildroot%_sysconfdir/jitsi/jicofo/
install -m644 jicofo/target/jicofo-*-SNAPSHOT.jar  %buildroot%_datadir/jicofo/jicofo.jar
install -m755 resources/jicofo.sh             %buildroot%_datadir/jicofo/
install -m644 resources/collect-dump-logs.sh  %buildroot%_datadir/jicofo/
install -m644 resources/config/jicofo-logrotate.d %buildroot%_sysconfdir/logrotate.d/jicofo
mkdir -p %buildroot%_bindir/ %buildroot%_unitdir/
install -m755 resources/alt-jicofo-launcher.sh %buildroot%_bindir/jicofo
install -m644 resources/alt-jicofo.service %buildroot%_unitdir/%name.service

%files
%dir %_datadir/jicofo
%_datadir/jicofo/lib
%_datadir/jicofo/jicofo.jar
%_datadir/jicofo/jicofo.sh
%_bindir/jicofo
%_datadir/jicofo/collect-dump-logs.sh
%dir %attr(700,%jicofo_user,root) %_sysconfdir/jitsi/jicofo
%config %_sysconfdir/jitsi/jicofo/logging.properties
%config %_sysconfdir/logrotate.d/jicofo
%_unitdir/%name.service

%pre
%_sbindir/useradd -r -d /dev/null -s /dev/null -n %jicofo_user \
        2> /dev/null > /dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%changelog
* Thu Feb 22 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.9258-alt1
- New version.
- Built with openjdk17.

* Thu Dec 07 2023 Andrey Cherepanov <cas@altlinux.org> 1.1.9111-alt1
- New version.

* Thu Sep 02 2021 Igor Vlasenko <viy@altlinux.org> 1.1-alt0.4
- build with java 8

* Wed Jun 10 2020 Arseny Maslennikov <arseny@altlinux.org> 1.1-alt0.3
- Added launcher executable.
- Added a systemd service unit.

* Thu May 28 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.2
- initial build

