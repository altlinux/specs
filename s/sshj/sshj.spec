Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          sshj
Version:       0.13.0
Release:       alt1_4jpp8
Summary:       SSHv2 library for Java
License:       ASL 2.0
URL:           https://github.com/hierynomus/sshj
Source0:       https://github.com/hierynomus/sshj/archive/v%{version}.tar.gz

BuildRequires: gradle-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(com.jcraft:jzlib) >= 1.1.0
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.iharder:base64)
BuildRequires: mvn(org.apache.sshd:sshd-core)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: /usr/bin/perl

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
find . -name "*.jar" -print -delete

# Enable local mode
perl -p -e "s/mavenCentral/xmvn()\n  mavenCentral/" build.gradle > build.gradle.temp
mv  build.gradle.temp  build.gradle

# fix non ASCII chars
native2ascii -encoding UTF8 \
  src/main/java/net/schmizz/sshj/SSHClient.java \
  src/main/java/net/schmizz/sshj/SSHClient.java

# Remove bundle library
rm -r src/main/java/net/schmizz/sshj/common/Base64.java
sed -i "s|net.schmizz.sshj.common.Base64|net.iharder.Base64|" \
  src/main/java/net/schmizz/sshj/transport/verification/OpenSSHKnownHosts.java \
  src/main/java/net/schmizz/sshj/userauth/keyprovider/OpenSSHKeyFile.java \
  src/main/java/net/schmizz/sshj/userauth/keyprovider/PuTTYKeyFile.java
perl -p -e 's/compile "com.jcraft:jzlib:1.1.3"/compile "net.iharder:base64:2.3.8"\n  compile "com.jcraft:jzlib:1.1.3"/' \
 build.gradle > build.gradle.temp
mv build.gradle.temp build.gradle

# Fix javadoc task
perl -p -e 's/task javadocJar/task javadocs(type: Javadoc) {\n  source = sourceSets.main.allJava\n}\n\ntask javadocJar/' \
 build.gradle > build.gradle.temp
mv build.gradle.temp build.gradle

# https://discuss.gradle.org/t/rootproject-name-in-settings-gradle-vs-projectname-in-build-gradle/5704/2
echo 'rootProject.name="sshj"' >> settings.gradle

# Test fails on koji only, cause: authenticated FAILED 
rm -r src/test/java/com/hierynomus/sshj/userauth/GssApiTest.java

%mvn_file com.hierynomus:%{name} %{name}
%mvn_alias com.hierynomus:%{name} net.schmizz:%{name}

%build

# Disable test suite
# On ARM builder test fails @ random
# com.hierynomus.sshj.transport.DisconnectionTest > listenerNotifiedOnServerDisconnect FAILED
#     net.schmizz.sshj.transport.TransportException at DisconnectionTest.java:36
#         Caused by: java.util.concurrent.TimeoutException at DisconnectionTest.java:36
# ? Test com.hierynomus.sshj.transport.DisconnectionTest; Executed: 4/3/1
# 69 tests completed, 1 failed
gradle -s --offline -x javadocs install

%install
%mvn_artifact build/poms/pom-default.xml build/libs/%{name}-%{version}.jar
%mvn_install -J build/docs/javadoc

%files -f .mfiles
%doc CONTRIBUTORS README.adoc
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_4jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_2jpp8
- new version

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

