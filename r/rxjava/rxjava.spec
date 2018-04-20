Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionals to help with missing test dependencies
%if 0%{?fedora}
%bcond_with checker
%endif

Name:          rxjava
Version:       1.1.8
Release:       alt1_4jpp8
Summary:       Reactive Extensions for the JVM
License:       ASL 2.0
URL:           https://github.com/ReactiveX/RxJava
Source0:       https://github.com/ReactiveX/RxJava/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       http://central.maven.org/maven2/io/reactivex/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
%if %{with checker}
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.pushtorefresh.java-private-constructor-checker:checker)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.mockito:mockito-core)
%endif

# RxJava adaptation of jctools
Provides:      bundled(jctools-core) = 1.2-SNAPSHOT

BuildArch:     noarch
Source44: import.info

%description
RxJava a library for composing asynchronous and
event-based programs using observable sequences
for the Java VM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n RxJava-%{version}
# Cleanup
find . -name '*.class' -print -delete
find . -name '*.jar' -print -delete

cp -p %{SOURCE1} pom.xml

# Add OSGi support
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>io.reactivex.rxjava</Bundle-SymbolicName>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-Vendor>ReactiveX</Bundle-Vendor>
    <Bundle-Version>${project.version}</Bundle-Version>
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

# Fix javadoc plugin configuration
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin:2.9.1 . '
<configuration>
  <excludePackageNames>*.internal.*</excludePackageNames>
</configuration>'

%if %{with checker}

# Add test deps
%pom_add_dep junit:junit:4.12:test
%pom_add_dep org.mockito:mockito-core:1.10.19:test
%pom_add_dep com.google.guava:guava:19.0:test
%pom_add_dep com.pushtorefresh.java-private-constructor-checker:checker:1.2.0:test

# This test take too much time on ARM builder e.g.:
# Time elapsed: 3.027 sec  <<< ERROR!
# org.junit.runners.model.TestTimedOutException: test timed out after 3000 milliseconds
rm src/test/java/rx/internal/operators/OperatorMergeMaxConcurrentTest.java \
 src/test/java/rx/internal/operators/OperatorMergeTest.java \
 src/test/java/rx/internal/operators/OperatorPublishTest.java \
 src/test/java/rx/internal/operators/OperatorRepeatTest.java \
 src/test/java/rx/internal/operators/OperatorRetryTest.java \
 src/test/java/rx/subjects/ReplaySubjectBoundedConcurrencyTest.java \
 src/test/java/rx/subjects/ReplaySubjectConcurrencyTest.java
# Require OperatorRetryTest
rm src/test/java/rx/internal/operators/OperatorRetryWithPredicateTest.java

%endif

%mvn_file io.reactivex:%{name} %{name}

%build

%if %{without checker}
opts="-f"
%endif
# Test skipped unavailable test dep
%mvn_build $opts -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_3jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_1jpp8
- new version

