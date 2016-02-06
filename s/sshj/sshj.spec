Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          sshj
Version:       0.8.1
Release:       alt3_10jpp8
Summary:       SSHv2 library for Java
License:       ASL 2.0
URL:           http://schmizz.net/sshj/
Source0:       https://github.com/shikhar/sshj/archive/v%{version}.tar.gz
# Thanks to Michal Srb
# Update bouncycastle to 1.50
Patch0:        sshj-0.8.1-port-to-bouncycastle-1.50.patch

BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(ch.qos.logback:logback-core)
BuildRequires: mvn(com.jcraft:jzlib) >= 1.1.0
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.mina:mina-core)
BuildRequires: mvn(org.apache.sshd:sshd-core)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:slf4j-api)

BuildArch:     noarch
Source44: import.info

%description
SSH, scp and sftp library for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# SmokeTest.setUp:37 ? NoClassDefFound org/apache/mina/core/service/IoHandler
%pom_add_dep org.apache.mina:mina-core::test

# NoClassDefFound org/bouncycastle/openssl/PEMReader apache sshd
rm -r src/test/java/net/schmizz/sshj/SmokeTest.java
# NoClassDefFoundError: Could not initialize class org.mockito.internal.creation.jmock.ClassImposterizer$3
rm -r src/test/java/net/schmizz/sshj/sftp/PacketReaderTest.java \
 src/test/java/net/schmizz/sshj/sftp/SFTPClientTest.java

# Some classes moved from JUnit to hamcrest
sed -i -e 's/org.junit.internal.matchers/org.hamcrest.core/' src/test/java/net/schmizz/sshj/transport/verification/OpenSSHKnownHostsTest.java
%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CONTRIBUTORS README.rst
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_10jpp8
- java 8 mass update

* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_4jpp7
- fixed build with new junit

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt3_1jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_1jpp7
- new version

