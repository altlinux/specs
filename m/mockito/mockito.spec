Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           mockito
Version:        3.12.4
Release:        alt1_5jpp11
Summary:        Tasty mocking framework for unit tests in Java
License:        MIT
URL:            https://site.mockito.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        generate-tarball.sh

# A custom build script to allow building with maven instead of gradle
Source2:        mockito-core.pom

# Maven central POMs for subprojects
Source3:        https://repo1.maven.org/maven2/org/mockito/mockito-inline/%{version}/mockito-inline-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/mockito/mockito-junit-jupiter/%{version}/mockito-junit-jupiter-%{version}.pom

# Mockito expects byte-buddy to have a shaded/bundled version of ASM, but
# we don't bundle in Fedora, so this patch makes mockito use ASM explicitly
Patch0:         use-unbundled-asm.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bnd)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.opentest4j:opentest4j)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
Source44: import.info

%description
Mockito is a mocking framework that tastes really good. It lets you write
beautiful tests with clean & simple API. Mockito doesn't give you hangover
because the tests are very readable and they produce clean verification
errors.

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package inline
Group: Development/Java
Summary:        Mockito preconfigured inline mock maker
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description inline
Mockito preconfigured inline mock maker (intermediate and to be
superseded by automatic usage in a future version).

%if %{without bootstrap}
%package junit-jupiter
Group: Development/Java
Summary:        Mockito JUnit 5 support
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description junit-jupiter
Mockito JUnit 5 support.
%endif

%prep
%setup -q
%patch0 -p1


# Disable failing test
# TODO check status: https://github.com/mockito/mockito/issues/2162
sed -i '/add_listeners_concurrently_sanity_check/i @org.junit.Ignore' src/test/java/org/mockitousage/debugging/StubbingLookupListenerCallbackTest.java

# Use our custom build script
sed -e 's/@VERSION@/%{version}/' %{SOURCE2} > pom.xml

# Workaround easymock incompatibility with Java 17 that should be fixed
# in easymock 4.4: https://github.com/easymock/easymock/issues/274
%pom_add_plugin :maven-surefire-plugin . "<configuration>
    <argLine>--add-opens=java.base/sun.reflect.generics.reflectiveObjects=ALL-UNNAMED</argLine></configuration>"

# OSGi metadata configuration
cat > osgi.bnd <<EOF
Automatic-Module-Name: org.mockito
Bundle-SymbolicName: org.mockito
Bundle-Name: Mockito Mock Library for Java.
Import-Package: junit.*;resolution:=optional,org.junit.*;resolution:=optional,org.hamcrest;resolution:=optional,org.mockito*;version="%{version}",*
Private-Package: org.mockito.*
-removeheaders: Bnd-LastModified,Include-Resource,Private-Package
EOF

# OSGi metadata configuration for the junit-jupiter jar
cat > osgi-junit-jupiter.bnd <<EOF
Automatic-Module-Name: org.mockito.junit.jupiter
Bundle-SymbolicName: org.mockito.junit-jupiter
Bundle-Name: Mockito Extension Library for JUnit 5.
Import-Package: org.junit.jupiter.api.extension;version="[5.7,6)",org.junit.platform.commons.support;version="[1.7,2)",org.mockito*;version="%{version}",*
-removeheaders: Bnd-LastModified,Include-Resource
Export-Package: org.mockito.junit.jupiter;version="%{version}";uses:="org.junit.jupiter.api.extension,org.mockito.quality"
EOF

# Compatibility alias
%mvn_alias org.%{name}:%{name}-core org.%{name}:%{name}-all

%build
# See the usage of exec-maven-plugin in the pom
mkdir -p target/classes/
javac  -target 1.8 -source 1.8 -d target/classes/ src/main/java/org/mockito/internal/creation/bytebuddy/inject/MockMethodDispatcher.java
mv target/classes/org/mockito/internal/creation/bytebuddy/inject/MockMethodDispatcher.{class,raw}

%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

# Build the inline subproject
cd subprojects/inline/src/main/resources
jar cf ../../../../../target/mockito-inline.jar mockito-extensions
cd -
%mvn_artifact %{SOURCE3} target/mockito-inline.jar
%mvn_package org.mockito:mockito-inline inline

%if %{without bootstrap}
# Build the junit-jupiter subproject
cd subprojects/junit-jupiter
mkdir -p target/classes/
CLASSPATH=$(build-classpath apiguardian junit5/junit-jupiter-api junit5/junit-platform-commons)
javac  -target 1.8 -source 1.8 -d target/classes/ \
      -cp ../../target/mockito-core-%{version}.jar:$CLASSPATH \
      src/main/java/org/mockito/junit/jupiter/*.java
jar -cf ../../target/mockito-junit-jupiter.unwrapped.jar -C target/classes org
cd -
bnd wrap --properties osgi-junit-jupiter.bnd --version %{version} \
    --output target/mockito-junit-jupiter.jar \
    target/mockito-junit-jupiter.unwrapped.jar
%mvn_artifact %{SOURCE4} target/mockito-junit-jupiter.jar
%mvn_package org.mockito:mockito-junit-jupiter junit-jupiter
%endif

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md doc/design-docs/custom-argument-matching.md

%files inline -f .mfiles-inline

%if %{without bootstrap}
%files junit-jupiter -f .mfiles-junit-jupiter
%endif

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:3.12.4-alt1_5jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:3.12.4-alt1_3jpp11
- new version

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 0:3.7.13-alt1_3jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.13-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.28.2-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.23.9-alt1_6jpp8
- fc update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.23.9-alt1_4jpp8
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_17jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_13jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_10jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt1_4jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt1_9jpp7
- new version

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt5_0.1jpp6
- fixed build

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt4_0.1jpp6
- fixed build with new testng and xbean

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt3_0.1jpp6
- fixed build

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt2_0.1jpp6
- fixed build

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt1_0.1jpp6
- new version

