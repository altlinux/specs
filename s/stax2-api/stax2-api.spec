BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             stax2-api
Version:          3.1.1
Release:          alt2_4jpp7
Summary:          Experimental API extending basic StAX implementation
License:          BSD
Group:            Development/Java

URL:              http://docs.codehaus.org/display/WSTX/StAX2

Source0:          http://repository.codehaus.org/org/codehaus/woodstox/%{name}/%{version}/%{name}-%{version}-sources.jar
Source1:          http://repository.codehaus.org/org/codehaus/woodstox/%{name}/%{version}/%{name}-%{version}.pom

BuildArch:        noarch

BuildRequires:    maven-surefire-provider-junit
BuildRequires:    bea-stax-api
BuildRequires:    maven
BuildRequires:    jpackage-utils

Requires:         bea-stax-api
Requires:         jpackage-utils
Source44: import.info

%description
StAX2 is an experimental API that is intended to extend
basic StAX specifications in a way that allows implementations
to experiment with features before they end up in the actual
StAX specification (if they do). As such, it is intended
to be freely implementable by all StAX implementations same way
as StAX, but without going through a formal JCP process.


%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c %{name}
# fixing incomplete source directory structure
mkdir -p src/main/java
mv -f org src/main/java/

cp %{SOURCE1} pom.xml

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_4jpp7
- new version

