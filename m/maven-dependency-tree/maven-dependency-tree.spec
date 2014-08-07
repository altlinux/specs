# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          maven-dependency-tree
Version:       2.0
Release:       alt2_1jpp7
Summary:       Maven dependency tree artifact
Group:         Development/Java
License:       ASL 2.0
Url:           http://maven.apache.org/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires: jpackage-utils

BuildRequires: maven-local
BuildRequires: maven-artifact
BuildRequires: maven-project
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: plexus-containers-component-metadata
BuildRequires: plexus-containers-component-annotations

Requires:      maven
Requires:      maven-project
Requires:      maven-artifact
Requires:      plexus-containers-component-annotations
Requires:      jpackage-utils


BuildArch:     noarch

Provides: maven-shared-dependency-tree = %{version}-%{release}
Obsoletes: maven-shared-dependency-tree < %{version}-%{release}
Source44: import.info

%description
Apache Maven dependency tree artifact. Originally part of maven-shared

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_add_dep org.apache.maven:maven-compat:3.0.4
%pom_add_dep org.apache.maven:maven-artifact:2.2.1

%build
# we have no jmock yet
mvn-rpmbuild -Dproject.build.sourceEncoding=utf-8 \
             -Dmaven.test.skip=true \
             package javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_1jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp7
- update

