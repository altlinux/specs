# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          maven-common-artifact-filters
Version:       1.4
Release:       alt1_2jpp7
Summary:       Maven Common Artifact Filters
Group:         Development/Java
License:       ASL 2.0
Url:           http://maven.apache.org/shared/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/1.4/maven-common-artifact-filters-1.4-source-release.zip
Patch0:        maven-common-artifact-filters-1.4-pom.patch
BuildRequires: jpackage-utils

BuildRequires: easymock
BuildRequires: junit4

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

Requires:      junit4
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
This package contains javadoc for %{name}.

%prep
%setup -q -n maven-common-artifact-filters-%{version}
# replace maven-project with maven-core and maven-compat 3.0.3
%patch0 -p0

rm -rf DEPENDENCIES

%build

mvn-rpmbuild install javadoc:aggregate

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
%doc LICENSE

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

