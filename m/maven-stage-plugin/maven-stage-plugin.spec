BuildRequires: /proc
BuildRequires: jpackage-compat
%global project_version 1.0-alpha-2
Name:           maven-stage-plugin
Version:        1.0
Release:        alt2_0.6.alpha2jpp7
Summary:        Plugin to copy artifacts from one repository to another

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-stage-plugin/
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-stage-plugin-1.0-alpha-2/
# tar jcf maven-stage-plugin-1.0-alpha-2.tar.bz2 maven-stage-plugin-1.0-alpha-2/
Source0:        %{name}-%{project_version}.tar.bz2

# Migrating from plexus-maven-plugin to plexus-containers-component-metadata
Patch0:         %{name}-plexus-maven-plugin.patch

BuildArch: noarch

BuildRequires: plexus-containers-component-metadata
BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: plexus-utils
Requires: ant
Requires: maven
Requires: jpackage-utils

Obsoletes: maven2-plugin-stage <= 0:2.0.8
Provides: maven2-plugin-stage = 1:%{version}-%{release}
Source44: import.info

%description
The Maven Stage Plugin copies artifacts from one repository to another. 
Its main use is for copying artifacts from a staging repository to 
the real repository.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{project_version}
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{project_version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.6.alpha2jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.6.alpha2jpp7
- new version

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.alpha2jpp7
- new version

