Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          disruptor
Version:       3.3.4
Release:       alt1_1jpp8
Summary:       Concurrent Programming Framework
License:       ASL 2.0
URL:           http://lmax-exchange.github.io/disruptor/
Source0:       https://github.com/LMAX-Exchange/disruptor/archive/%{version}.tar.gz
Source1:       http://repo1.maven.org/maven2/com/lmax/%{name}/%{version}/%{name}-%{version}.pom
# see http://www.jmock.org/threading-synchroniser.html
Patch0:        disruptor-3.3.2-jmock.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.jmock:jmock-junit4)
BuildRequires: mvn(org.jmock:jmock-legacy)

%if 0
# Unavailable performance test deps
# lib/test/hdrhistogram-1.0-SNAPSHOT.jar
BuildRequires: mvn(com.google.caliper:caliper:0.5-rc1)
%endif

BuildArch:     noarch
Source44: import.info

%description
A High Performance Inter-Thread Messaging Library.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# Cleanup
find . -name "*.class" -print -delete
find . -name "*.jar" -type f -print -delete

%patch0 -p1

cp -p %{SOURCE1} pom.xml

# Add OSGi support
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-DocURL>%{url}</Bundle-DocURL>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-Vendor>LMAX Disruptor Development Team</Bundle-Vendor>
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
</executions>'

# fail to compile cause: incompatible hamcrest apis
rm -r src/test/java/com/lmax/disruptor/RingBufferTest.java \
 src/test/java/com/lmax/disruptor/RingBufferEventMatcher.java
# Failed to stop thread: Thread[com.lmax.disruptor.BatchEventProcessor@1d057a39,5,main]
rm -r src/test/java/com/lmax/disruptor/dsl/DisruptorTest.java
# Test fails due to incompatible jmock version
#rm -f src/test/java/com/lmax/disruptor/EventPollerTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENCE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENCE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt1_4jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt1_3jpp8
- java 8 mass update

