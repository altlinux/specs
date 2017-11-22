Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Use 5.1.2 snapshot there was no release tagged by upstream,
# but this is what is available in maven central
%global git_tag e0570bff5c60604115ab7ad0d5498055a60fc772

Name:           maven-indexer
Version:        5.1.2
Release:        alt1_0.4.gite0570bfjpp8
Summary:        Standard for producing indexes of Maven repositories

License:        ASL 2.0
URL:            http://maven.apache.org/maven-indexer/index.html

Source0:        https://github.com/apache/maven-indexer/archive/%{git_tag}/maven-indexer-%{version}.tar.gz

# Port to latest lucene
Patch0:         0001-Port-to-Lucene-5.patch
Patch1:         0002-Port-to-Lucene-6.patch

# Drop dep on truezip
Patch2:         maven-indexer-truezip.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.lucene:lucene-analyzers-common)
BuildRequires:  mvn(org.apache.lucene:lucene-core)
BuildRequires:  mvn(org.apache.lucene:lucene-highlighter)
BuildRequires:  mvn(org.apache.lucene:lucene-queryparser)
BuildRequires:  mvn(org.apache.maven.archetype:archetype-common)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
Source44: import.info

%description
Apache Maven Indexer (former Sonatype Nexus Indexer) is the defacto
standard for producing indexes of Maven repositories. The Indexes
are produced and consumed by all major tools in the ecosystem.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{git_tag}
%patch0 -p1
%patch1 -p1
%patch2

find -name '*.jar' -delete
find -name '*.zip' -delete
find -name '*.class' -delete

# Tests need porting to a modern jetty
%pom_remove_dep -r org.mortbay.jetty:jetty

# Switch from sonatype aether to eclipse aether
%pom_remove_dep org.sonatype.aether:aether-api indexer-core
%pom_remove_dep org.sonatype.aether:aether-util indexer-core
%pom_add_dep org.eclipse.aether:aether-api indexer-core
%pom_add_dep org.eclipse.aether:aether-util indexer-core
find -name *.java -exec sed -i -e "s/org.sonatype.aether/org.eclipse.aether/g" {} \;

# Switch from sonatype to codehaus plexus
%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus indexer-cli
%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus indexer-core
%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus indexer-artifact
%pom_add_dep org.codehaus.plexus:plexus-container-default indexer-cli
%pom_add_dep org.codehaus.plexus:plexus-container-default indexer-core
%pom_add_dep org.codehaus.plexus:plexus-container-default indexer-artifact

# Remove unnecessary plugins
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :apache-rat-plugin

# Disable CLI module because of how it bundles stuff
%pom_disable_module indexer-cli

# Drop unneeded dep on truezip
%pom_remove_dep -r de.schlichtherle.truezip:
rm indexer-core/src/main/java/org/apache/maven/index/util/zip/TrueZipZipFileHandle.java

%build
# Skip tests because they need porting to modern jetty
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc NOTICE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc NOTICE

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_0.4.gite0570bfjpp8
- fixed build with new lucene

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.2-alt1_0.1.gite0570bfjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_9jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_8jpp8
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version

