Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           powermock
Version:        1.6.5
Release:        alt1_4jpp8
Summary:        A Java mocking framework

License:        ASL 2.0
URL:            https://github.com/jayway/powermock
Source0:        https://github.com/jayway/%{name}/archive/%{name}-%{version}.tar.gz

Patch1:         0001-Fix-junit3-compat.patch
# powermock contains forked version of mockito
# this is the same patch as in mockito to fix incompatibility with our cglib
Patch2:         0002-Setting-naming-policy.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib-nodep)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
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

%package common
Group: Development/Java
Summary:        Common files for PowerMock

%description common
%{desc}

This package contains common files for all PowerMock modules.

%package reflect
Group: Development/Java
Summary:        Reflection module of PowerMock
Requires:       %{name}-common = %{version}

%description reflect
%{desc}

This package contains the reflection module of PowerMock.

%package core
Group: Development/Java
Summary:        Core module of PowerMock
Requires:       %{name}-common = %{version}

%description core
%{desc}

This package contains the core module of PowerMock.

%package junit4
Group: Development/Java
Summary:        JUnit4 common module of PowerMock
Requires:       %{name}-common = %{version}

%description junit4
%{desc}

This package contains the JUnit4 module of PowerMock.

%package api-support
Group: Development/Java
Summary:        PowerMock API support module
Requires:       %{name}-common = %{version}

%description api-support
%{desc}

This package contains support code for the PowerMock API extensions.

%package api-mockito
Group: Development/Java
Summary:        PowerMock Mockito API module
Requires:       %{name}-common = %{version}

%description api-mockito
%{desc}

This package contains the PowerMock Mockito API extension.

%package api-easymock
Group: Development/Java
Summary:        PowerMock EasyMock API module
Requires:       %{name}-common = %{version}

%description api-easymock
%{desc}

This package contains the PowerMock EasyMock API extension.

%package testng
Group: Development/Java
Summary:        PowerMock module for TestNG.
Requires:       %{name}-common = %{version}

%description testng
%{desc}

This package contains the PowerMock TestNG extension.


%package javadoc
Group: Development/Java
Summary:        JavaDocs for %{name}
BuildArch: noarch

%description javadoc
%{desc}

This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch1 -p1
%patch2 -p1

# bundled sources of various libraries
rm -r modules/module-impl/agent
# there is forked mockito, which contains bundled cglib and asm
rm -r api/mockito2/src/main/java/org/powermock/api/mockito/repackaged/{cglib,asm}

find -name '*.java' | xargs sed -i 's/org\.mockito\.cglib/net.sf.cglib/g;
                                    s/org\.powermock\.api\.mockito\.repackaged\.cglib/net.cf.cglib/g;
                                    s/org\.powermock\.api\.mockito\.repackaged\.asm/org.objectweb.asm/g'

# Assumes different JUnit version
rm modules/module-impl/junit4-common/src/test/java/org/powermock/modules/junit4/common/internal/impl/JUnitVersionTest.java

# StackOverflow in koji
sed -i '/shouldLoadClassAndOverrideMethodGreaterThanJvmLimit/i@org.junit.Ignore' \
    core/src/test/java/org/powermock/core/transformers/impl/ClassMockTransformerTest.java

# Disable modules that we cannot build (yet).
%pom_disable_module module-test modules
%pom_disable_module junit4-legacy modules/module-impl
%pom_disable_module junit4-rule-agent modules/module-impl
%pom_disable_module junit3 modules/module-impl
%pom_disable_module testng-agent modules/module-impl
%pom_disable_module agent modules/module-impl
%pom_disable_module examples
%pom_disable_module release
%pom_disable_module classloading-xstream classloading
%pom_disable_module mockito2 api

%pom_remove_plugin :rat-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

%mvn_package :powermock-core core
%mvn_package :powermock-classloading-base core
%mvn_package :powermock-classloading-objenesis core
%mvn_package :powermock-module-junit4 junit4
%mvn_package :powermock-module-junit4-rule junit4
%mvn_package :powermock-module-junit4-common junit4
%mvn_package :powermock-api-mockito api-mockito
%mvn_package :powermock-api-mockito-common api-mockito
%mvn_package :powermock-api-support api-support
%mvn_package :powermock-api-easymock api-easymock
%mvn_package :powermock-reflect reflect
%mvn_package :powermock-module-testng testng
%mvn_package :powermock-module-testng-common testng

%mvn_package org.powermock.tests: __noinstall

# poms are not needed by anything
%mvn_package ::pom: __noinstall

%build
%mvn_build

%install
%mvn_install

%files common
%dir %{_javadir}/%{name}
%doc LICENSE.txt
%files reflect -f .mfiles-reflect
%files core -f .mfiles-core
%files junit4 -f .mfiles-junit4
%files api-support -f .mfiles-api-support
%files api-mockito -f .mfiles-api-mockito
%files api-easymock -f .mfiles-api-easymock
%files testng -f .mfiles-testng

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
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

