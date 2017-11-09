Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.9
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global oname spring-amqp

# https://bugzilla.redhat.com/show_bug.cgi?id=1231430
%bcond_with jinterface

Name:          springframework-amqp
Version:       1.3.9
Release:       alt1_7jpp8
Summary:       Support for Spring programming model with AMQP
License:       ASL 2.0
URL:           http://projects.spring.io/spring-amqp/
# Newer release require springframework >= 4.1.7.RELEASE
Source0:       https://github.com/spring-projects/spring-amqp/archive/v%{namedversion}.tar.gz
# Use gradle
Source1:       http://repo1.maven.org/maven2/org/springframework/amqp/spring-amqp/%{namedversion}/spring-amqp-%{namedversion}.pom
Source2:       http://repo1.maven.org/maven2/org/springframework/amqp/spring-erlang/%{namedversion}/spring-erlang-%{namedversion}.pom
Source3:       http://repo1.maven.org/maven2/org/springframework/amqp/spring-rabbit/%{namedversion}/spring-rabbit-%{namedversion}.pom
# rabbitmq-java-client 3.6.x support
Patch0:        springframework-amqp-1.3.9-amqp-client36.patch
# Security fix for CVE-2016-2173
Patch1:        springframework-amqp-1.3.9-CVE-2016-2173.patch

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
# Use rabbitmq-java-client:3.3.4
BuildRequires: mvn(com.rabbitmq:amqp-client)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
%if %{with jinterface}
BuildRequires: mvn(org.erlang.otp:jinterface)
%endif
BuildRequires: mvn(org.hamcrest:hamcrest-all)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-oxm)
BuildRequires: mvn(org.springframework:spring-test)
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(org.springframework.retry:spring-retry)

BuildArch:     noarch
Source44: import.info

%description
The Spring AMQP project applies core Spring concepts to the
development of AMQP-based messaging solutions. It provides
a "template" as a high-level abstraction for sending and
receiving messages. It also provides support for Message
driven POJOs with a "listener container". These libraries
facilitate management of AMQP resources while promoting the
use of dependency injection and declarative configuration.
In all of these cases, you will see similarities to the
JMS support in the Spring Framework.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}
find . -name "*.bat" -delete
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p1
%patch1 -p1

# This is a dummy POM added just to ease building in the RPM platforms
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <modelVersion>4.0.0</modelVersion>
  <groupId>org.springframework.amqp</groupId>
  <artifactId>spring-amqp-parent</artifactId>
  <packaging>pom</packaging>
  <name>Spring AMQP - Parent</name>
  <version>%{namedversion}</version>
  <description>Spring AMQP Parent</description>

  <modules>
    <module>spring-amqp</module>
    <module>spring-erlang</module>
    <module>spring-rabbit</module>
  </modules>
</project>
EOF

cp -p %{SOURCE1} %{oname}/pom.xml
%if %{with jinterface}
 cp -p %{SOURCE2} spring-erlang/pom.xml
%else
 %pom_disable_module spring-erlang
%endif
cp -p %{SOURCE3} spring-rabbit/pom.xml

%pom_add_dep cglib:cglib:3.1:test spring-amqp
%pom_add_dep junit:junit:4.11:test spring-amqp
%pom_add_dep log4j:log4j:1.2.17:test spring-amqp
%pom_add_dep org.hamcrest:hamcrest-all:1.3:test spring-amqp
%pom_add_dep org.mockito:mockito-core:1.9.5:test spring-amqp
%pom_add_dep org.springframework:spring-test:3.2.9.RELEASE:test spring-amqp

%if %{with jinterface}
%pom_add_dep commons-cli:commons-cli:1.2:test spring-rabbit
%pom_add_dep junit:junit:4.11:test spring-rabbit
%pom_add_dep org.hamcrest:hamcrest-all:1.3:test spring-rabbit
%pom_add_dep org.mockito:mockito-core:1.9.5:test spring-rabbit
%pom_add_dep org.springframework.amqp:spring-erlang:'${project.version}':test spring-rabbit
%pom_add_dep org.springframework:spring-test:3.2.9.RELEASE:test spring-rabbit
# unreported exception java.util.concurrent.TimeoutException; must be caught or declared to be thrown
rm -r spring-rabbit/src/test/java/org/springframework/amqp/rabbit/connection/CachingConnectionFactoryTests.java \
 spring-rabbit/src/test/java/org/springframework/amqp/rabbit/connection/AbstractConnectionFactoryTests.java \
 spring-rabbit/src/test/java/org/springframework/amqp/rabbit/connection/SingleConnectionFactoryTests.java
%else
rm -r spring-rabbit/src/test/java/*
%endif

for p in %{oname} \
%if %{with jinterface}
 spring-erlang \
%endif
 spring-rabbit; do
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>" ${p}
%pom_add_plugin org.apache.felix:maven-bundle-plugin ${p} '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Vendor>SpringSource</Bundle-Vendor>
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
done

%mvn_package :%{oname}-parent __noinstall

%build
%if %{without jinterface}
opts="-f"
%endif
# no test deps spring-erlang
%mvn_build $opts -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc src/dist/README.md
%doc src/dist/apache-license.txt src/dist/notice.txt

%files javadoc -f .mfiles-javadoc
%doc src/dist/apache-license.txt src/dist/notice.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1_5jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1_4jpp8
- new fc release

* Tue Feb 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1_1jpp8
- java 8 mass update

