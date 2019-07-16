Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           powermock
Version:        2.0.0
Release:        alt1_2jpp8
Summary:        A Java mocking framework

# Note: api-mockito subpackage is ASL 2.0 and MIT, the rest is ASL 2.0
License:        ASL 2.0
URL:            https://github.com/jayway/powermock
Source0:        https://github.com/jayway/%{name}/archive/%{name}-%{version}.tar.gz
# Script to fetch poms and generate the sources list below
Source1:        get-poms.sh
Source10:       https://repo1.maven.org/maven2/org/powermock/powermock-api-support/%{version}/powermock-api-support-%{version}.pom
Source11:       https://repo1.maven.org/maven2/org/powermock/powermock-api-easymock/%{version}/powermock-api-easymock-%{version}.pom
Source12:       https://repo1.maven.org/maven2/org/powermock/powermock-api-mockito2/%{version}/powermock-api-mockito2-%{version}.pom
Source13:       https://repo1.maven.org/maven2/org/powermock/powermock-classloading-base/%{version}/powermock-classloading-base-%{version}.pom
Source14:       https://repo1.maven.org/maven2/org/powermock/powermock-classloading-xstream/%{version}/powermock-classloading-xstream-%{version}.pom
Source15:       https://repo1.maven.org/maven2/org/powermock/powermock-classloading-objenesis/%{version}/powermock-classloading-objenesis-%{version}.pom
Source16:       https://repo1.maven.org/maven2/org/powermock/powermock-core/%{version}/powermock-core-%{version}.pom
Source17:       https://repo1.maven.org/maven2/org/powermock/powermock-module-junit4-legacy/%{version}/powermock-module-junit4-legacy-%{version}.pom
Source18:       https://repo1.maven.org/maven2/org/powermock/powermock-module-testng-common/%{version}/powermock-module-testng-common-%{version}.pom
Source19:       https://repo1.maven.org/maven2/org/powermock/powermock-module-javaagent/%{version}/powermock-module-javaagent-%{version}.pom
Source20:       https://repo1.maven.org/maven2/org/powermock/powermock-module-junit4-rule/%{version}/powermock-module-junit4-rule-%{version}.pom
Source21:       https://repo1.maven.org/maven2/org/powermock/powermock-module-testng-agent/%{version}/powermock-module-testng-agent-%{version}.pom
Source22:       https://repo1.maven.org/maven2/org/powermock/powermock-module-junit4-rule-agent/%{version}/powermock-module-junit4-rule-agent-%{version}.pom
Source23:       https://repo1.maven.org/maven2/org/powermock/powermock-module-junit4/%{version}/powermock-module-junit4-%{version}.pom
Source24:       https://repo1.maven.org/maven2/org/powermock/powermock-module-testng/%{version}/powermock-module-testng-%{version}.pom
Source25:       https://repo1.maven.org/maven2/org/powermock/powermock-module-junit4-common/%{version}/powermock-module-junit4-common-%{version}.pom
Source26:       https://repo1.maven.org/maven2/org/powermock/powermock-reflect/%{version}/powermock-reflect-%{version}.pom

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib-nodep)
BuildRequires:  mvn(com.thoughtworks.xstream:xstream) >= 1.4.10
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.mockito:mockito-core) >= 2.23.0
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.testng:testng)

%global desc \
PowerMock is a framework that extend other mock libraries\
such as EasyMock with more powerful capabilities. PowerMock uses a\
custom classloader and bytecode manipulation to enable mocking of\
static methods, constructors, final classes and methods, private\
methods, removal of static initializers and more.
Source44: import.info

%description
%{desc}

%package reflect
Group: Development/Java
Summary:        Reflection module of PowerMock

%description reflect
%{desc}

This package contains the reflection module of PowerMock.

%package javaagent
Group: Development/Java
Summary:        PowerMock Java agent support

%description javaagent
%{desc}

This package contains the Java agent support for PowerMock.

%package core
Group: Development/Java
Summary:        Core module of PowerMock
Obsoletes:      %{name}-common < %{version}-%{release}
Provides:       %{name}-common = %{version}-%{release}
Requires:       mvn(com.thoughtworks.xstream:xstream) >= 1.4.10

%description core
%{desc}

This package contains the core module of PowerMock.

%package junit4
Group: Development/Java
Summary:        JUnit4 common module of PowerMock

%description junit4
%{desc}

This package contains the JUnit4 module of PowerMock.

%package api-support
Group: Development/Java
Summary:        PowerMock API support module

%description api-support
%{desc}

This package contains support code for the PowerMock API extensions.

%package api-mockito
Group: Development/Java
Summary:        PowerMock Mockito API module
Requires:       mvn(org.mockito:mockito-core) >= 2.23.0

%description api-mockito
%{desc}

This package contains the PowerMock Mockito API extension.

%package api-easymock
Group: Development/Java
Summary:        PowerMock EasyMock API module

%description api-easymock
%{desc}

This package contains the PowerMock EasyMock API extension.

%package testng
Group: Development/Java
Summary:        PowerMock module for TestNG.

%description testng
%{desc}

This package contains the PowerMock TestNG extension.

%package javadoc
Group: Development/Java
Summary:        JavaDocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Inject pom files
modules=
for src in $(find powermock* -name src -type d) ; do
  dir=$(dirname $src)
  aid=$(basename $dir)
  cp %{_sourcedir}/$aid-%{version}.pom $dir/pom.xml
  modules="$modules<module>$dir</module>"
done

# Generate build aggregator pom
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.powermock</groupId>
  <artifactId>parent</artifactId>
  <packaging>pom</packaging>
  <version>%{version}</version>
  <modules>
    $modules
    <module>tests/utils</module>
  </modules>
</project>
EOF

# Generate test utils pom
cat > tests/utils/pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.powermock.tests</groupId>
  <artifactId>powermock-tests-utils</artifactId>
  <version>%{version}</version>
  <dependencies>
    <dependency>
      <groupId>org.powermock</groupId>
      <artifactId>powermock-core</artifactId>
      <version>%{version}</version>
    </dependency>
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>servlet-api</artifactId>
      <version>2.5</version>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>2.19.1</version>
          <configuration><skip>true</skip></configuration>
      </plugin>
    </plugins>
  </build>
</project>
EOF

# Fix references to ASM, which is not bundled by bytebuddy
sed -i -e 's/net\.bytebuddy\.jar\.asm/org.objectweb.asm/g;'  \
  $(find powermock-reflect/src/test/java/org/powermock/reflect/internal/proxy powermock-core/src/main/java/org/powermock/core/bytebuddy powermock-modules/powermock-module-javaagent/src/main/java/org/powermock/modules/agent -name '*.java')

# Inject test deps not present in published poms
%pom_add_dep "junit:junit:4.12:test" powermock-{core,reflect} \
  powermock-api/powermock-api-{support,easymock,mockito2} powermock-classloading/powermock-classloading-{objenesis,xstream}
%pom_add_dep "org.assertj:assertj-core:2.6.0:test" powermock-{core,reflect} \
  powermock-api/powermock-api-{support,easymock,mockito2} powermock-classloading/powermock-classloading-{objenesis,xstream} \
  powermock-modules/powermock-module-junit4{,-common,-rule,-rule-agent}
%pom_add_dep "org.hamcrest:hamcrest-core:1.3:test" powermock-{core,reflect} \
  powermock-api/powermock-api-{support,easymock,mockito2} powermock-classloading/powermock-classloading-{objenesis,xstream}
%pom_add_dep "cglib:cglib-nodep:3.2.9:test" powermock-reflect
%pom_add_dep "org.mockito:mockito-core:2.23.0:test" powermock-core
%pom_add_dep "org.powermock.tests:powermock-tests-utils:%{version}:test" powermock-api/powermock-api-mockito2
%pom_add_dep "org.easymock:easymock:4.0.1:test" powermock-modules/powermock-module-junit4

# Fix needed for using old easymock
sed -i -e 's/PowerMockTestNotifier, PowerMockTestNotifier/PowerMockTestNotifier/' \
  powermock-modules/powermock-module-junit4/src/test/java/org/powermock/modules/junit4/internal/impl/PowerMockRunNotifierTest.java

# Missing junit rules from com.github.stefanbirkner:system-rules
rm powermock-core/src/test/java/org/powermock/configuration/support/ConfigurationFactoryImplTest.java

# Junit4 in Fedora is too new, don't build legacy module
%pom_disable_module powermock-modules/powermock-module-junit4-legacy

%mvn_package ":powermock-core" core
%mvn_package ":powermock-classloading*" core
%mvn_package ":powermock-module-junit4*" junit4
%mvn_package ":powermock-module-testng*" testng
%mvn_package ":powermock-module-javaagent" javaagent
%mvn_package ":powermock-api-mockito2" api-mockito
%mvn_package ":powermock-api-support" api-support
%mvn_package ":powermock-api-easymock" api-easymock
%mvn_package ":powermock-reflect" reflect

# Compat alias for mockito support
%mvn_alias :powermock-api-mockito2 :powermock-api-mockito :powermock-api-mockito-common

# Don't install internal test stuff
%mvn_package org.powermock.tests: __noinstall

# No need to install the parent pom
%mvn_package :parent __noinstall

%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files core -f .mfiles-core
%doc README.md CONTRIBUTING.md
%doc --no-dereference LICENSE.txt
%files reflect -f .mfiles-reflect
%files junit4 -f .mfiles-junit4
%files api-support -f .mfiles-api-support
%files api-mockito -f .mfiles-api-mockito
%files api-easymock -f .mfiles-api-easymock
%files testng -f .mfiles-testng
%files javaagent -f .mfiles-javaagent
%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_2jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt1_4jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.12-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.12-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.12-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.12-alt1_5jpp7
- new version

