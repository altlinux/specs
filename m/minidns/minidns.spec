Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          minidns
Version:       0.1.7
Release:       alt1_3jpp8
Summary:       Minimal DNS library for Java and Android systems
License:       ASL 2.0 or LGPLv2+ or WTFPL
URL:           https://github.com/rtreffer/minidns
Source0:       https://github.com/rtreffer/minidns/archive/%{version}.tar.gz
Source1:       http://central.maven.org/maven2/de/measite/minidns/minidns/%{version}/minidns-%{version}.pom
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:     noarch
Source44: import.info

%description
MiniDNS is a minimal dns client library for Java and Android.
It can parse a basic set of resource records (A, AAAA, NS,
SRV) and is easy to use and extend.

This library is not intended to be used as a DNS server.
You might want to look into dnsjava for such functionality.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# cleanup
find . -name "*.class" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.jar" -print  -delete

cp -p %{SOURCE1} pom.xml

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 . "
<configuration>
  <source>1.7</source>
  <target>1.7</target>
  <encoding>UTF-8</encoding>
</configuration>"

%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 . "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}</Bundle-SymbolicName>
    <Bundle-Name>\${project.name}</Bundle-Name>
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

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:2.4 . "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <addMavenDescriptor>false</addMavenDescriptor>
  </archive>
</configuration>"

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENCE*

%files javadoc -f .mfiles-javadoc
%doc LICENCE*

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt1_2jpp8
- java 8 mass update

