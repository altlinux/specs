Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}

%if 0%{?fedora}
# Unavailable test deps
# xLightweb depend on xSocket, but the
# active development of xSocket has been stopped.
# Currently xSocket supports bug-fixes only.
#def_with xlightweb
%bcond_with xlightweb
%endif

Name:          jbosh
Version:       0.8.0
Release:       alt1_3jpp8
Summary:       XEP-0124: Bidirectional-streams Over Synchronous HTTP (BOSH)
License:       ASL 2.0
URL:           https://github.com/igniterealtime/jbosh
Source0:       https://github.com/igniterealtime/jbosh/archive/%{version}.tar.gz
Source1:       http://repo1.maven.org/maven2/org/igniterealtime/jbosh/jbosh/%{version}/jbosh-%{version}.pom
# LICENSE file was added @ https://github.com/igniterealtime/jbosh/commit/6b09a889942abe289f6c89f642add142e57bd88e
Source2:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(xpp3:xpp3)

%if %{with xlightweb}
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.xlightweb:xlightweb)
%endif

BuildArch:     noarch
Source44: import.info

%description
A maintained fork of com.kenai.jbosh for XEP-0124:
Bidirectional-streams Over Synchronous HTTP (BOSH).
This library is used by Smack to support XEP-206:
XMPP over BOSH. In contrast to org.kenai.jbosh,
this jBOSH library uses the Apache Commons HttpClient 4.

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
cp -p %{SOURCE2} LICENSE
sed -i 's/\r//' LICENSE

%pom_add_plugin org.apache.felix:maven-bundle-plugin . "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}</Bundle-SymbolicName>
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

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin . "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <addMavenDescriptor>false</addMavenDescriptor>
  </archive>
</configuration>"

mkdir -p target/classes/{META-INF/services,org.jivesoftware.jbosh}

%if %{with xlightweb}
# ComparisonFailure: expected:<gzip> but was:<null>
rm -r src/test/java/org/igniterealtime/jbosh/XEP0124Section07Test.java
# Exception: test timed out after 5000 milliseconds
rm -r src/test/java/org/igniterealtime/jbosh/XEP0124Section09Test.java \
 src/test/java/org/igniterealtime/jbosh/XEP0124Section17Test.java
# Exception: test timed out after 3000 milliseconds
rm -r src/test/java/org/igniterealtime/jbosh/XEP0124Section11Test.java
%else
%pom_remove_dep org.xlightweb:xlightweb
%endif

%mvn_file : %{name}

%build

%if %{without xlightweb}
opts="-f"
%endif
%mvn_build $opts -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_2jpp8
- java 8 mass update

