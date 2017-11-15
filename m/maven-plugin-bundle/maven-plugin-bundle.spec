Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{?fedora}
%bcond_without obr
%bcond_without reporting
%endif

%global site_name maven-bundle-plugin

Name:           maven-plugin-bundle
Version:        3.3.0
Release:        alt1_2jpp8
Summary:        Maven Bundle Plugin
License:        ASL 2.0
URL:            http://felix.apache.org
BuildArch:      noarch

Source0:        http://archive.apache.org/dist/felix/%{site_name}-%{version}-source-release.tar.gz

# Needs polishing to be sent upstream
Patch0:         0001-Port-to-current-maven-dependency-tree.patch
# New maven-archiver removed some deprecated methods we were using
Patch1:         0002-Fix-for-new-maven-archiver.patch
# Port to newer Plexus utils
Patch2:         0003-Port-to-plexus-utils-3.0.24.patch
# Port to newer Maven
Patch3:         0004-Use-Maven-3-APIs.patch

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%if %{with obr}
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.bundlerepository)
BuildRequires:  mvn(xpp3:xpp3)
%endif
%if %{with reporting}
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
%endif
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
%patch2 -p1
%patch3 -p1

find -name '*.jar' -delete

%pom_change_dep :org.osgi.core :osgi.core

# Bundled class from old maven-dependency-tree
rm -r src/main/java/org/apache/maven/shared/dependency

# Bundled classes from old maven
rm -r src/main/java/org/apache/felix/bundleplugin/pom

# There is forked version of maven-osgi in
# src/{main,test}/java/org/apache/maven

%if %{with obr}
# Deps unbundled from felix-bundlerepository
%pom_add_dep xpp3:xpp3
%pom_add_dep net.sf.kxml:kxml2
%else
rm -rf src/main/java/org/apache/felix/obrplugin/
%pom_remove_dep :org.apache.felix.bundlerepository
%endif

%if %{without reporting}
rm -f src/main/java/org/apache/felix/bundleplugin/baseline/BaselineReport.java
%pom_remove_dep :doxia-sink-api
%pom_remove_dep :doxia-site-renderer
%pom_remove_dep :maven-reporting-impl
%endif

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
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_2jpp8
- new version

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.0-alt1_4jpp8
- new version

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

