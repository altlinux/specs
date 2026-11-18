%define _unpackaged_files_terminate_build 1

Name: sysout-over-slf4j
Version: 1.0.2
Release: alt1

Summary: Redirect System.out and System.err to SLF4J
License: MIT
Group: Development/Java
URL: https://github.com/Mahoney/sysout-over-slf4j
VCS: https://github.com/Mahoney/sysout-over-slf4j.git

Source: %name-%version.tar
Patch: independent-test-fixtures.patch
Patch1: java21-stacktrace-origin.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: slf4j2
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: tomcat-servlet-4.0-api
BuildRequires: mvn(ch.qos.logback:logback-core)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(ch.qos.reload4j:reload4j)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)

%description
Redirect raw System.out and System.err output to SLF4J, preserving the
calling class context and supporting servlet lifecycle integration.

%javadoc_package

%prep
%setup
%autopatch -p1
# The legacy javax API remains available from Tomcat 9.
%pom_change_dep javax.servlet:servlet-api \
    org.apache.tomcat:tomcat-servlet-api:9.0.121
# Current javac supports Java 8 as its oldest bytecode target.
%pom_xpath_set "//pom:configuration/pom:source" 8
%pom_xpath_set "//pom:configuration/pom:target" 8
# Match the genuine SLF4J 2 provider used by the qualified Logback tests.
%pom_change_dep org.slf4j:slf4j-api org.slf4j:slf4j-api:2
%pom_xpath_set pom:properties/pom:logback.version 1.6.7
# Use the genuine Log4j 1.x implementation for its ConsoleAppender test.
%pom_change_dep log4j:log4j ch.qos.reload4j:reload4j:1.2.26

# Only PowerMock-based suites and their exclusive helpers need these providers.
%pom_remove_dep org.powermock.modules:powermock-module-junit4
%pom_remove_dep org.powermock.api:powermock-api-easymock
# CrossClassLoaderTestUtils uses Javassist independently of PowerMock.
%pom_add_dep org.javassist:javassist:3.30.2.GA:test

rm src/test/java/uk/org/lidalia/sysoutslf4j/PowerMockSysOutOverSLF4JTestCase.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/common/TestExceptionUtils.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/common/TestReflectionUtils.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/context/PrintStreamCoordinatorFactoryTest.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/context/TestLoggerAppenderImpl.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/context/TestLoggingSystemRegister.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/context/TestSLF4JPrintStreamManager.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/context/TestSysOutOverSLF4J.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/context/TestSysOutOverSLF4JInitialiser.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/context/TestSysOutOverSLF4JServletContextListener.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/system/TestLoggerAppenderProxy.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/system/TestLoggerAppenderStore.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/system/TestSLF4JPrintStreamConfigurator.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/system/TestSLF4JPrintStreamDelegate.java \
   src/test/java/uk/org/lidalia/sysoutslf4j/system/TestSLF4JPrintStreamImpl.java \
   src/test/java/uk/org/lidalia/testutils/ClassCreationUtils.java

%mvn_package "*:*:jar:sources" __noinstall

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
