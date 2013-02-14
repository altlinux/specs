# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          maven-common-artifact-filters
Version:       1.4
Release:       alt2_3jpp7
Summary:       Maven Common Artifact Filters
Group:         Development/Java
License:       ASL 2.0
Url:           http://maven.apache.org/shared/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:        %{name}-%{version}-pom.patch
BuildRequires: jpackage-utils

BuildRequires: easymock
BuildRequires: junit

BuildRequires: maven

BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-resources-plugin
BuildRequires: maven-shared
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-test-tools
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-utils

# test deps
BuildRequires: aopalliance
BuildRequires: cglib

Requires:      junit
Requires:      maven
Requires:      maven-shared
Requires:      maven-test-tools
Requires:      plexus-containers-container-default
Requires:      plexus-utils

Requires:      jpackage-utils
BuildArch:     noarch

Provides: maven-shared-common-artifact-filters = %{version}-%{release}
Obsoletes: maven-shared-common-artifact-filters < %{version}-%{release}
Source44: import.info

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %%{name}.

%prep
%setup -q
# replace maven-project with maven-core and maven-compat 3.0.3
%patch0 -p0

rm -rf DEPENDENCIES

%pom_xpath_inject "pom:project/pom:dependencies" "
  <dependency>
    <groupId>aopalliance</groupId>
    <artifactId>aopalliance</artifactId>
    <scope>test</scope>
  </dependency>
  <dependency>
    <groupId>net.sf.cglib</groupId>
    <artifactId>cglib</artifactId>
    <scope>test</scope>
  </dependency>"


%build

mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

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
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

