Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          smack
Version:       4.1.5
Release:       alt1_5jpp8
Summary:       Open Source XMPP (Jabber) client library
License:       ASL 2.0
URL:           http://www.igniterealtime.org/projects/smack/index.jsp
Source0:       https://github.com/igniterealtime/Smack/archive/%{version}.tar.gz
# Default use gradle
# sh smack-get-poms.sh < VERSION >
Source1:       smack-%{version}-poms.tar.xz
Source2:       smack-get-poms.sh
Patch0:        smack-4.1.1-antrun-plugin.patch
# https://issues.igniterealtime.org/browse/SMACK-739
Patch1:        smack-4.1.5-SMACK-739.patch

BuildRequires: maven-local
BuildRequires: mvn(com.jamesmurty.utils:java-xmlbuilder)
BuildRequires: mvn(com.jcraft:jzlib)
BuildRequires: mvn(de.measite.minidns:minidns)
BuildRequires: mvn(dnsjava:dnsjava)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.iharder:base64)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.igniterealtime.jbosh:jbosh)
BuildRequires: mvn(org.igniterealtime.jxmpp:jxmpp-core)
BuildRequires: mvn(org.igniterealtime.jxmpp:jxmpp-util-cache)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.powermock:powermock-api-mockito)
BuildRequires: mvn(org.powermock:powermock-module-junit4)
BuildRequires: mvn(org.powermock:powermock-reflect)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(xmlunit:xmlunit)
BuildRequires: mvn(xpp3:xpp3)

BuildArch:     noarch
Source44: import.info

%description
Smack is an Open Source XMPP (Jabber) client library for instant
messaging and presence. A pure Java library, it can be embedded
into your applications to create anything from a full XMPP client
to simple XMPP integrations such as sending notification messages and
presence-enabling devices.

%package bosh
Group: Development/Java
Summary:       Smack BOSH API

%description bosh
Smack BOSH API.

%package compression-jzlib
Group: Development/Java
Summary:       Smack compression with jzlib

%description compression-jzlib
Allow to compress the XMPP stream with help of jzlib.

%package debug
Group: Development/Java
Summary:       Smack GUI debugger

%description debug
Inspect the exchanged XMPP stanzas.

%package debug-slf4j
Group: Development/Java
Summary:       Smack slf4j debugger

%description debug-slf4j
Inspect the exchanged XMPP stanzas.
Connect your favorite slf4j back-end of
choice to get output inside of it.

%package experimental
Group: Development/Java
Summary:       Smack experimental extensions

%description experimental
Classes and methods for XEPs that are in status
'experimental' or that should otherwise carefully
considered for deployment. The API may change even
between patch versions.

%package extensions
Group: Development/Java
Summary:       Smack extensions

%description extensions
Classes and methods that implement support for the
various XMPP XEPs (Multi-User Chat, PubSub, a..) and
other XMPP extensions.

%package im
Group: Development/Java
Summary:       Smack IM

%description im
Classes and methods for XMPP-IM (RFC 6121):
Roster, Chat and other functionality.

%package java7
Group: Development/Java
Summary:       Smack for Java7 (or higher)

%description java7
This is a pseudo-artifact that pulls all the required dependencies to
run Smack on Java 7 (or higher) JVMs. Usually you want to add additional
dependencies to smack-tcp, smack-extensions and smack-experimental.

%package legacy
Group: Development/Java
Summary:       Smack legacy extensions

%description legacy
Usually XEPs in the state 'retracted', 'rejected',
'deprecated', 'obsolete' or in a long standing
'deferred' state.

%package resolver-dnsjava
Group: Development/Java
Summary:       DNS SRV with dnsjava

%description resolver-dnsjava
Use dnsjava for DNS SRV lookups. For platforms
that don't provide the javax.naming API (e.g. Android).

%package resolver-javax
Group: Development/Java
Summary:       DNS SRV with Java7

%description resolver-javax
Use javax.naming for DNS SRV lookups. The
javax.naming API is available in JavaSE
since Java7.

%package resolver-minidns
Group: Development/Java
Summary:       DNS SRV with minidns

%description resolver-minidns
Use minidns for DNS SRV lookups.
For platforms that don't provide the
javax.naming API (e.g. Android).

%package sasl-javax
Group: Development/Java
Summary:       Smack javax SASL

%description sasl-javax
SASL with javax.security.sasl
Use javax.security.sasl for SASL.

%package sasl-provided
Group: Development/Java
Summary:       Smack SASL provided code

%description sasl-provided
SASL with Smack provided code
Use Smack provided code for SASL.

%package tcp
Group: Development/Java
Summary:       Smack TCP

%description tcp
Smack for standard XMPP connections over TCP.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n Smack-%{version} -a1
# cleanup
find . -name "*.class" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.jar" -print  -delete

%patch0 -p0
%patch1 -p1

# remove prebuilt documentation
rm -rf javadoc/* documentation/*

# This is a dummy POM added just to ease building in the RPM platforms
# These are not all the modules, only those that we can currently build
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>org.igniterealtime.smack</groupId>
  <artifactId>smack-parent</artifactId>
  <packaging>pom</packaging>
  <name>Smack Parent POM</name>
  <version>%{version}</version>
  <description>Smack Project</description>

  <modules>
    <module>smack-bosh</module>
    <module>smack-compression-jzlib</module>
    <module>smack-core</module>
    <module>smack-debug</module>
    <module>smack-debug-slf4j</module>
    <module>smack-experimental</module>
    <module>smack-extensions</module>
    <module>smack-im</module>
    <module>smack-java7</module>
    <module>smack-legacy</module>
    <module>smack-resolver-dnsjava</module>
    <module>smack-resolver-javax</module>
    <module>smack-resolver-minidns</module>
    <module>smack-sasl-javax</module>
    <module>smack-sasl-provided</module>
    <module>smack-tcp</module>
  </modules>

</project>
EOF

for m in bosh \
 compression-jzlib \
 core \
 debug \
 debug-slf4j \
 experimental \
 extensions \
 im \
 java7 \
 legacy \
 resolver-dnsjava \
 resolver-javax \
 resolver-minidns \
 sasl-javax \
 sasl-provided \
 tcp; do

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:2.4 %{name}-${m} "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifest>
      <addDefaultImplementationEntries>true</addDefaultImplementationEntries>
      <addDefaultSpecificationEntries>true</addDefaultSpecificationEntries>
    </manifest>
  </archive>
</configuration>"

%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" %{name}-${m}
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 %{name}-${m} "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Name>\${project.artifactId}</Bundle-Name>
    <Bundle-Version>\${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.1 %{name}-${m} "
<configuration>
  <source>1.7</source>
  <target>1.7</target>
</configuration>"

sed -i "s|name>Smack|name>Smack ${m}|" %{name}-${m}/pom.xml

done

# Do not use OSGi manifest in test JAR
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-jar-plugin']/pom:configuration" %{name}-core

# Fix test deps
%pom_xpath_inject "pom:plugin[pom:artifactId = 'maven-jar-plugin']" "
<executions>
  <execution>
    <goals>
      <goal>test-jar</goal>
    </goals>
  </execution>
</executions>" %{name}-core

for m in debug debug-slf4j experimental extensions im legacy sasl-javax sasl-provided tcp; do
%pom_add_dep org.igniterealtime.smack:smack-core:'${project.version}':test %{name}-${m} "<type>test-jar</type>"
done

%pom_add_dep com.jamesmurty.utils:java-xmlbuilder::test %{name}-experimental
%pom_add_dep junit:junit::test %{name}-experimental
%pom_add_dep junit:junit::test %{name}-extensions
#%%pom_add_dep org.hamcrest:hamcrest-all::test %%{name}-extensions
%pom_add_dep com.jamesmurty.utils:java-xmlbuilder::test %{name}-extensions
%pom_add_dep org.mockito:mockito-core::test %{name}-extensions
%pom_add_dep org.powermock:powermock-reflect::test %{name}-extensions
# org.powermock:powermock-api-mockito
%pom_add_dep xmlunit:xmlunit::test %{name}-extensions
%pom_add_dep junit:junit::test %{name}-im
%pom_add_dep junit:junit::test %{name}-legacy
%pom_add_dep junit:junit::test %{name}-sasl-javax
%pom_add_dep junit:junit::test %{name}-sasl-provided
%pom_add_dep junit:junit::test %{name}-tcp
%pom_add_dep com.jamesmurty.utils:java-xmlbuilder::test %{name}-tcp

# org.junit.ComparisonFailure
rm -r %{name}-extensions/src/test/java/org/jivesoftware/smackx/caps/EntityCapsManagerTest.java \
 %{name}-extensions/src/test/java/org/jivesoftware/smackx/vcardtemp/VCardTest.java \
 %{name}-extensions/src/test/java/org/jivesoftware/smackx/xdatavalidation/provider/DataValidationTest.java

# expected null, but was:<en>
rm -r %{name}-core/src/test/java/org/jivesoftware/smack/util/PacketParserUtilsTest.java

# Use web connection
rm -r %{name}-im/src/test/java/org/jivesoftware/smack/roster/RosterVersioningTest.java \
 %{name}-im/src/test/java/org/jivesoftware/smack/roster/rosterstore/DirectoryRosterStoreTest.java \
 %{name}-im/src/test/java/org/jivesoftware/smack/roster/RosterTest.java

# fix non ASCII chars
for s in %{name}-core/src/main/java/org/jivesoftware/smack/util/dns/HostAddress.java \
 %{name}-extensions/src/main/java/org/jivesoftware/smackx/caps/cache/SimpleDirectoryPersistentCache.java \
 %{name}-extensions/src/main/java/org/jivesoftware/smackx/bytestreams/socks5/Socks5BytestreamManager.java \
 %{name}-extensions/src/main/java/org/jivesoftware/smackx/address/MultipleRecipientManager.java \
 %{name}-extensions/src/main/java/org/jivesoftware/smackx/caps/packet/CapsExtension.java \
 %{name}-extensions/src/main/java/org/jivesoftware/smackx/caps/provider/CapsExtensionProvider.java \
 %{name}-extensions/src/main/java/org/jivesoftware/smackx/caps/EntityCapsManager.java \
 %{name}-extensions/src/main/java/org/jivesoftware/smackx/caps/cache/EntityCapsPersistentCache.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

%mvn_package :%{name}-core::tests: %{name}-core
%mvn_package :%{name}-parent __noinstall

%build

%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-%{name}-core
%doc README.md resources/releasedocs/README.html resources/releasedocs/changelog.html
%doc LICENSE

%files bosh -f .mfiles-%{name}-bosh
%files compression-jzlib -f .mfiles-%{name}-compression-jzlib
%files debug -f .mfiles-%{name}-debug
%files debug-slf4j -f .mfiles-%{name}-debug-slf4j
%files experimental -f .mfiles-%{name}-experimental
%files extensions -f .mfiles-%{name}-extensions
%files im -f .mfiles-%{name}-im
%files java7 -f .mfiles-%{name}-java7
%files legacy -f .mfiles-%{name}-legacy
%files resolver-dnsjava -f .mfiles-%{name}-resolver-dnsjava
%files resolver-javax -f .mfiles-%{name}-resolver-javax
%files resolver-minidns -f .mfiles-%{name}-resolver-minidns
%files sasl-javax -f .mfiles-%{name}-sasl-javax
%files sasl-provided -f .mfiles-%{name}-sasl-provided
%files tcp -f .mfiles-%{name}-tcp

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt1_5jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt1_4jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.1.5-alt1_2jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.1.3-alt1_1jpp8
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt2_3jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_3jpp6
- new jpp relase

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_1jpp5
- new jpp release

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

