BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-resources-plugin
Version:        2.5
Release:        alt1_5jpp7
Summary:        Maven Resources Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-resources-plugin
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-resources-plugin-2.5 maven-resources-plugin-2.5
#tar zcf maven-resources-plugin-2.5.tar.gz maven-resources-plugin-2.5/
Source0:        %{name}-%{version}.tar.gz

# Relocation of plexus-container-default is necessary as sisu gets to the
# classpath first and uses an old version of a class from container-default
Patch0:         %{name}-plexus-dep.patch

BuildArch: noarch

BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-shared-reporting-impl
BuildRequires: plexus-interpolation
BuildRequires: plexus-digest
BuildRequires: maven-project
BuildRequires: maven-monitor
BuildRequires: maven-filtering

Requires: plexus-build-api
Requires: plexus-containers-container-default
Requires: plexus-utils
Requires: plexus-interpolation
Requires: maven-plugin-testing-harness
Requires: maven-filtering
Requires: maven
Requires: maven-project
Requires: maven-monitor
Requires:       jpackage-utils

Provides:       maven2-plugin-resources = %{version}-%{release}
Obsoletes:      maven2-plugin-resources <= 0:2.0.8
Source44: import.info

%description
The Resources Plugin handles the copying of project resources
to the output directory.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

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
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

