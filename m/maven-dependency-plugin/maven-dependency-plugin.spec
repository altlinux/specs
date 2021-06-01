Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-dependency-plugin
Version:        3.1.2
Release:        alt1_4jpp11
Summary:        Plugin to manipulate, copy and unpack local and remote artifacts
License:        ASL 2.0

URL:            http://maven.apache.org/plugins/%{name}
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(classworlds:classworlds)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer) >= 0.11.0
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-analyzer)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
The dependency plugin provides the capability to manipulate
artifacts. It can copy and/or unpack artifacts from local or remote
repositories to a specified location.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q

%pom_remove_plugin :maven-enforcer-plugin

# We don't want to support legacy Maven versions (older than 3.1)
%pom_remove_dep org.sonatype.aether:

# trivial port to commons-lang3
%pom_change_dep :commons-lang org.apache.commons:commons-lang3:3.8.1

sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    src/main/java/org/apache/maven/plugins/dependency/analyze/AbstractAnalyzeMojo.java
sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    src/main/java/org/apache/maven/plugins/dependency/resolvers/ResolveDependencySourcesMojo.java
sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    src/main/java/org/apache/maven/plugins/dependency/DisplayAncestorsMojo.java
sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" \
    src/test/java/org/apache/maven/plugins/dependency/fromConfiguration/TestUnpackMojo.java

%build
# Tests require legacy Maven
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.1.2-alt1_4jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 3.1.1-alt1_5jpp11
- update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_2jpp8
- new version

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_1jpp8
- new version

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_0.3.20160119svn1722372jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_2jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt4_2jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_2jpp7
- new release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

