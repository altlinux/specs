Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global site_name maven-bundle-plugin

Name:           maven-plugin-bundle
Version:        3.0.1
Release:        alt1_1jpp8
Summary:        Maven Bundle Plugin
License:        ASL 2.0
URL:            http://felix.apache.org
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/felix/%{site_name}-%{version}-source-release.tar.gz

# Needs polishing to be sent upstream
Patch0:         0001-Port-to-current-maven-dependency-tree.patch
# It doesn't really need new aqute-bnd
Patch1:         0002-Downgrade-aqute-bnd.patch

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.bundlerepository)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jdom:jdom)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires:  mvn(xpp3:xpp3)
Source44: import.info

%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}

%patch0 -p1
%patch1 -p1

find -name '*.jar' -delete

# Bundled class from old maven-dependency-tree
rm -r src/main/java/org/apache/maven/shared/dependency

# There is forked version of maven-osgi in
# src/{main,test}/java/org/apache/maven

%pom_add_dep org.apache.maven:maven-compat
%pom_add_dep xpp3:xpp3
%pom_add_dep net.sf.kxml:kxml2
%pom_add_dep org.apache.felix:org.apache.felix.framework
%pom_add_dep org.apache.maven.reporting:maven-reporting-impl

%build
# Tests depend on bundled JARs
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_1jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt1_1jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt3_10jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_4jpp7
- new version

* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_12jpp6
- fixed buildrequires

* Fri Oct 15 2010 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_4jpp6
- new version

