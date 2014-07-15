BuildRequires: /proc
BuildRequires: jpackage-compat
%global site_name maven-bundle-plugin

Name:           maven-plugin-bundle
Version:        2.3.7
Release:        alt2_4jpp7
Summary:        Maven Bundle Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://apache.tradebit.com/pub/felix/%{site_name}-%{version}-source-release.tar.gz

Patch0:         %{site_name}-dependency.patch
Patch1:         %{site_name}-unreported-exception.patch

BuildRequires: aqute-bndlib >= 1.50.0
BuildRequires: plexus-utils >= 1.4.5
BuildRequires: felix-osgi-obr
BuildRequires: kxml2
BuildRequires: maven
BuildRequires: maven-shared-dependency-tree >= 1.1-3
BuildRequires: maven-wagon >= 1.0-0.2.b2
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin >= 2.3
BuildRequires: maven-surefire-provider-junit4 >= 2.3
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-shared-osgi
BuildRequires: maven-archiver
BuildRequires: plexus-archiver
BuildRequires: plexus-containers-container-default
BuildRequires: felix-parent
BuildRequires: felix-bundlerepository

Requires: aqute-bndlib >= 1.50.0
Requires: plexus-utils >= 1.4.5
Requires: felix-osgi-obr
Requires: kxml2
Requires: maven
Requires: maven-archiver
Requires: maven-shared-dependency-tree
Requires: maven-wagon
Requires: maven-shared-osgi
Requires: plexus-archiver
Requires: plexus-containers-container-default
Requires: felix-parent
Requires: felix-bundlerepository

BuildArch: noarch
Source44: import.info


%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}

%patch0 -p1
%patch1 -p1

# remove bundled stuff
#rm -rf src/main/java/org/apache/maven

%build
# tests can't be built (seems like a MavenProjectStub incompatibility with MavenProject)
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.skip=true

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/maven-bundle-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE NOTICE DEPENDENCIES
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_4jpp7
- new version

* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_12jpp6
- fixed buildrequires

* Fri Oct 15 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_4jpp6
- new version

