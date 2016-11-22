Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-indexer
Version:        5.1.1
Release:        alt1_9jpp8
Summary:        Standard for producing indexes of Maven repositories

License:        ASL 2.0
URL:            http://maven.apache.org/maven-indexer/index.html

## jars need to be removed from tarball so that the srpm doesn't violate their
## licensing terms:
#
# wget http://central.maven.org/maven2/org/apache/maven/indexer/maven-indexer/5.1.1/maven-indexer-5.1.1-source-release.zip
# unzip maven-indexer-5.1.1-source-release.zip
# pushd maven-indexer-5.1.1/ && find -name *.jar -delete && popd
# zip -r maven-indexer-5.1.1-source-release-CLEAN.zip maven-indexer-5.1.1/
Source0:        %{name}-%{version}-source-release-CLEAN.zip

BuildArch:      noarch

BuildRequires:  aether-api
BuildRequires:  aether-util
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-compress
BuildRequires:  atinject
BuildRequires:  bouncycastle
BuildRequires:  felix-osgi-compendium
BuildRequires:  felix-osgi-core
BuildRequires:  google-guice
BuildRequires:  jetty-start
BuildRequires:  jmock
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  junit
BuildRequires:  lucene3
BuildRequires:  lucene3-contrib
BuildRequires:  maven-local
BuildRequires:  maven-archetype-catalog
BuildRequires:  maven-archetype-common
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-failsafe-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-shade-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-wagon
BuildRequires:  plexus-cli
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-utils
BuildRequires:  port-allocator-maven-plugin
BuildRequires:  regexp
BuildRequires:  slf4j
BuildRequires:  truezip-driver-zip
BuildRequires:  truezip-file
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
%setup -q

find -name '*.jar' -delete
find -name '*.zip' -delete
find -name '*.class' -delete

%pom_remove_dep org.mortbay.jetty:jetty indexer-cli
%pom_remove_dep org.mortbay.jetty:jetty indexer-core

%pom_remove_dep org.sonatype.aether:aether-api indexer-core
%pom_remove_dep org.sonatype.aether:aether-util indexer-core
%pom_add_dep org.eclipse.aether:aether-api indexer-core
%pom_add_dep org.eclipse.aether:aether-util indexer-core

%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus indexer-cli
%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus indexer-core
%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus indexer-artifact
%pom_add_dep org.codehaus.plexus:plexus-container-default indexer-cli
%pom_add_dep org.codehaus.plexus:plexus-container-default indexer-core
%pom_add_dep org.codehaus.plexus:plexus-container-default indexer-artifact

%pom_remove_plugin org.apache.rat:apache-rat-plugin
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_disable_module indexer-cli

find -name *.java -exec sed -i -e "s/org.sonatype.aether/org.eclipse.aether/g" {} \;

%build
# skip tests because of unpackaged test deps
%mvn_build --skip-tests

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_9jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_8jpp8
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version

