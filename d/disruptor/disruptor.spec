Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          disruptor
Version:       3.4.2
Release:       alt1_6jpp8
Summary:       Concurrent Programming Framework
License:       ASL 2.0
URL:           https://lmax-exchange.github.io/disruptor/
BuildArch:     noarch

Source0:       https://github.com/LMAX-Exchange/disruptor/archive/%{version}/%{name}-%{version}.tar.gz
Source1:       https://repo1.maven.org/maven2/com/lmax/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
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

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENCE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENCE.txt

%changelog
* Mon May 30 2022 Igor Vlasenko <viy@altlinux.org> 3.4.2-alt1_6jpp8
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.4.2-alt1_3jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_5jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.6-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt1_4jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.2-alt1_3jpp8
- java 8 mass update

