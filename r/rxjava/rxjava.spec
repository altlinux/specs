Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          rxjava
Version:       1.0.13
Release:       alt1_3jpp8
Summary:       Reactive Extensions for the JVM
License:       ASL 2.0
URL:           https://github.com/ReactiveX/RxJava
Source0:       https://github.com/ReactiveX/RxJava/archive/v%{version}.tar.gz
Source1:       http://central.maven.org/maven2/io/reactivex/%{name}/%{version}/%{name}-%{version}.pom
# Remove bundle jctools library
Patch0:        rxjava-1.0.13-use-system-jctools.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jctools:jctools-core)
BuildRequires: mvn(org.mockito:mockito-core)

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

%patch0 -p1
rm -rf src/main/java/rx/internal/util/unsafe/ConcurrentCircularArrayQueue.java \
 src/main/java/rx/internal/util/unsafe/ConcurrentSequencedCircularArrayQueue.java \
 src/main/java/rx/internal/util/unsafe/MessagePassingQueue.java \
 src/main/java/rx/internal/util/unsafe/MpmcArrayQueue.java \
 src/main/java/rx/internal/util/unsafe/Pow2.java \
 src/main/java/rx/internal/util/unsafe/SpmcArrayQueue.java \
 src/main/java/rx/internal/util/unsafe/SpscArrayQueue.java \
 src/main/java/rx/internal/util/unsafe/BaseLinkedQueue.java \
 src/main/java/rx/internal/util/unsafe/MpscLinkedQueue.java \
 src/main/java/rx/internal/util/unsafe/SpscLinkedQueue.java

# Add test deps
%pom_add_dep junit:junit:4.10:test
%pom_add_dep org.mockito:mockito-core:1.8.5:test
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

# This test take too much time on ARM builder e.g.:
# Time elapsed: 3.027 sec  <<< ERROR!
# org.junit.runners.model.TestTimedOutException: test timed out after 3000 milliseconds
rm -r src/test/java/rx/internal/operators/OperatorMergeMaxConcurrentTest.java \
 src/test/java/rx/internal/operators/OperatorMergeTest.java \
 src/test/java/rx/internal/operators/OperatorPublishTest.java \
 src/test/java/rx/internal/operators/OperatorRepeatTest.java \
 src/test/java/rx/internal/operators/OperatorRetryTest.java \
 src/test/java/rx/observables/AbstractOnSubscribeTest.java \
 src/test/java/rx/schedulers/CachedThreadSchedulerTest.java \
 src/test/java/rx/schedulers/ExecutorSchedulerTest.java \
 src/test/java/rx/subjects/ReplaySubjectBoundedConcurrencyTest.java \
 src/test/java/rx/subjects/ReplaySubjectConcurrencyTest.java
# Require OperatorRetryTest
rm -r src/test/java/rx/internal/operators/OperatorRetryWithPredicateTest.java
 
%mvn_file io.reactivex:%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_3jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_1jpp8
- new version

