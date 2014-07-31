# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-script-interpreter
Version:        1.0
Release:        alt2_3jpp7
Summary:        Maven Script Interpreter
Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}
Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Plexus-maven-plugin no longer used
Patch0:         %{name}-plexus.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  groovy
BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  plexus-containers-component-metadata

Requires:       jpackage-utils
Requires:       bsh
Requires:       groovy
Requires:       maven
Requires:       plexus-utils
Source44: import.info

%description
This component provides some utilities to interpret/execute some scripts for
various implementations: Groovy or BeanShell.


%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate -Dproject.build.sourceEncoding=UTF-8

%install
# JAR
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# JavaDoc
install -Ddm 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc DEPENDENCIES LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1jpp7
- new version

