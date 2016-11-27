Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jxmpp
%define version 0.4.2
%global githash ffd7bd4f3bece632c3bb0e8e30a2a1195946e0df

%global namedreltag %nil
%global namedversion %{version}%{?namedreltag}

Name:          jxmpp
Version:       0.4.2
Release:       alt1_2jpp8
Summary:       An Open Source XMPP Java base-library
License:       ASL 2.0
URL:           https://github.com/igniterealtime/jxmpp
Source0:       https://github.com/igniterealtime/jxmpp/archive/%{githash}/%{name}-%{githash}.tar.gz

Source1:       http://repo1.maven.org/maven2/org/jxmpp/jxmpp-core/%{namedversion}/jxmpp-core-%{namedversion}.pom
Source2:       http://repo1.maven.org/maven2/org/jxmpp/jxmpp-jid/%{namedversion}/jxmpp-jid-%{namedversion}.pom
Source4:       http://repo1.maven.org/maven2/org/jxmpp/jxmpp-stringprep-libidn/%{namedversion}/jxmpp-stringprep-libidn-%{namedversion}.pom
Source5:       http://repo1.maven.org/maven2/org/jxmpp/jxmpp-util-cache/%{namedversion}/jxmpp-util-cache-%{namedversion}.pom

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.gnu.inet:libidn)

BuildArch:     noarch
Source44: import.info

%description
JXMPP is an Open Source Java base library for XMPP. It
provides often used functionality needed to build a XMPP stack.

%package core
Group: Development/Java
Summary:       JXMPP Core

%description core
JXMPP core components.

%package jid
Group: Development/Java
Summary:       JXMPP JID

%description jid
JID classes from JXMPP.

%package stringprep-libidn
Group: Development/Java
Summary:       JXMPP Stringprep Libidn

%description stringprep-libidn
JXMPP Stringprep with libidn.

%package util-cache
Group: Development/Java
Summary:       JXMPP Util Cache

%description util-cache
A minimalistic and efficient bounded LRU Cache
with optional expiration.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}
# cleanup
find . -name "*.class" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.jar" -print  -delete

cp -p %{SOURCE1} %{name}-core/pom.xml
cp -p %{SOURCE2} %{name}-jid/pom.xml
cp -p %{SOURCE4} %{name}-stringprep-libidn/pom.xml
cp -p %{SOURCE5} %{name}-util-cache/pom.xml

# This is a dummy POM added just to ease building in the RPM platforms
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>org.jxmpp</groupId>
  <artifactId>jxmpp-parent</artifactId>
  <version>%{namedversion}</version>
  <packaging>pom</packaging>
  <name>jxmpp parent</name>
  <modules>
    <module>jxmpp-core</module>
    <module>jxmpp-stringprep-libidn</module>
    <module>jxmpp-jid</module>
    <module>jxmpp-util-cache</module>
  </modules>
</project>
EOF

for p in core jid stringprep-libidn util-cache;do

%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" %{name}-${p}
%pom_xpath_set "pom:name" "JXMPP ${p}" %{name}-${p}
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 %{name}-${p} "
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

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.3 %{name}-${p} "
<configuration>
 <source>1.7</source>
 <target>1.7</target>
 <encoding>UTF-8</encoding>
</configuration>"

done

%mvn_package :%{name}-parent __noinstall

%mvn_alias org.jxmpp: org.igniterealtime.jxmpp:

%build

%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files core -f .mfiles-%{name}-core
%doc LICENSE

%files jid -f .mfiles-%{name}-jid
%doc LICENSE

%files stringprep-libidn -f .mfiles-%{name}-stringprep-libidn
%doc LICENSE

%files util-cache -f .mfiles-%{name}-util-cache
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_2jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_3jpp8
- new version

