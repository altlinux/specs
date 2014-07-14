BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           powermock
Version:        1.4.12
Release:        alt2_5jpp7
Summary:        A Java mocking framework
Group:          Development/Java

License:        ASL 2.0
URL:            http://code.google.com/p/powermock/
Source0:        powermock-%{version}.tar.xz
Source1:        make-powermock-sourcetarball.sh
# Disable broken tests.
Patch0:         powermock-disable-broken-tests.patch
# Disable modules that we cannot build (yet).
Patch1:         powermock-disable-modules.patch
# Fix cglib dependency of mockito
Patch2:         powermock-fix-cglib-mockito.patch
# Fix compatibility with JUnit3
Patch3:         powermock-fix-junit3-compat.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  objenesis
BuildRequires:  junit4
BuildRequires:  junit
BuildRequires:  mockito
BuildRequires:  easymock
BuildRequires:  javassist

Requires:       jpackage-utils
Source44: import.info

%description
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

%package common
Group: Development/Java
Summary:        Common files for PowerMock

%description common
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

This package contains common files for all PowerMock modules.

%package reflect
Group: Development/Java
Summary:        Reflection module of PowerMock
Requires:       objenesis
Requires:       powermock-common

%description reflect
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

This package contains the reflection module of PowerMock.

%package core
Group: Development/Java
Summary:        Core module of PowerMock
Requires:       powermock-reflect
Requires:       javassist
Requires:       powermock-common

%description core
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

This package contains the core module of PowerMock.

%package junit4
Group: Development/Java
Summary:        JUnit4 common module of PowerMock
Requires:       powermock-core
Requires:       junit4
Requires:       powermock-common

%description junit4
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

This package contains the JUnit4 module of PowerMock.

%package api-support
Group: Development/Java
Summary:        PowerMock API support module
Requires:       powermock-core
Requires:       powermock-common

%description api-support
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

This package contains support code for the PowerMock API extensions.

%package api-mockito
Group: Development/Java
Summary:        PowerMock Mockito API module
Requires:       powermock-api-support
Requires:       mockito
Requires:       cglib
Requires:       powermock-common

%description api-mockito
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

This package contains the PowerMock Mockito API extension.

%package javadoc
Summary:        JavaDocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
PowerMock is a framework that extend other mock libraries
such as EasyMock with more powerful capabilities. PowerMock uses a
custom classloader and bytecode manipulation to enable mocking of
static methods, constructors, final classes and methods, private
methods, removal of static initializers and more.

This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
mvn-rpmbuild -DargLine=-XX:-UseSplitVerifier install javadoc:aggregate

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
cp -p reflect/target/powermock-reflect-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-reflect.jar
cp -p core/target/powermock-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-core.jar
cp -p modules/module-impl/junit4-common/target/powermock-module-junit4-common-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit4-common.jar
cp -p modules/module-impl/junit4/target/powermock-module-junit4-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit4.jar
cp -p api/support/target/powermock-api-support-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-api-support.jar
cp -p api/mockito/target/powermock-api-mockito-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-api-mockito.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
install -pm 644 reflect/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-reflect.pom
install -pm 644 core/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
install -pm 644 modules//pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-modules.pom
install -pm 644 modules/module-impl/junit4-common/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-junit4-common.pom
install -pm 644 modules/module-impl/junit4/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-junit4.pom
install -pm 644 api/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-api.pom
install -pm 644 api/support/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-api-support.pom
install -pm 644 api/mockito/pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-api-mockito.pom

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%add_maven_depmap JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}-modules.pom
%add_maven_depmap JPP.%{name}-%{name}-api.pom
%add_maven_depmap JPP.%{name}-%{name}-reflect.pom %{name}/%{name}-reflect.jar -f "reflect"
%add_maven_depmap JPP.%{name}-%{name}-core.pom %{name}/%{name}-core.jar -f "core"
%add_maven_depmap JPP.%{name}-%{name}-junit4-common.pom %{name}/%{name}-junit4-common.jar -f "junit4"
%add_maven_depmap JPP.%{name}-%{name}-junit4.pom %{name}/%{name}-junit4.jar -f "junit4"
%add_maven_depmap JPP.%{name}-%{name}-api-support.pom %{name}/%{name}-api-support.jar -f "api-support"
%add_maven_depmap JPP.%{name}-%{name}-api-mockito.pom %{name}/%{name}-api-mockito.jar -f "api-mockito"

%files common
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-modules.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-api.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt

%files reflect
%{_javadir}/%{name}/%{name}-reflect.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-reflect.pom
%{_mavendepmapfragdir}/%{name}-reflect
%doc LICENSE.txt

%files core
%{_javadir}/%{name}/%{name}-core.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
%{_mavendepmapfragdir}/%{name}-core
%doc LICENSE.txt

%files junit4
%{_javadir}/%{name}/%{name}-junit4-common.jar
%{_javadir}/%{name}/%{name}-junit4.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-junit4-common.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-junit4.pom
%{_mavendepmapfragdir}/%{name}-junit4
%doc LICENSE.txt

%files api-support
%{_javadir}/%{name}/%{name}-api-support.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-api-support.pom
%{_mavendepmapfragdir}/%{name}-api-support
%doc LICENSE.txt

%files api-mockito
%{_javadir}/%{name}/%{name}-api-mockito.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-api-mockito.pom
%{_mavendepmapfragdir}/%{name}-api-mockito
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.12-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.12-alt1_5jpp7
- new version

