Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:           maven-indexer
Version:        4.1.2
Release:        alt1_5jpp7
Summary:        Standard for producing indexes of Maven repositories

License:        ASL 2.0
URL:            http://maven.apache.org/maven-indexer/index.html

## jars need to be removed from tarball so that the srpm doesn't violate their
## licensing terms:
#
# wget http://central.maven.org/maven2/org/apache/maven/indexer/maven-indexer/4.1.2/maven-indexer-4.1.2-source-release.zip
# unzip maven-indexer-4.1.2-source-release.zip
# pushd maven-indexer-4.1.2/ && find -name *.jar -delete && popd
# zip -r maven-indexer-4.1.2-source-release.zip maven-indexer-4.1.2/
Source0:        %{name}-%{version}-source-release.zip

# Comment out unavailable test dependencies
Patch0:        %{name}-core-deps.patch

# Fix for lucene version for F17 (only applied to fedora versions <= f17)
Patch1:        %{name}-lucene-version-f17.patch

BuildArch:      noarch

BuildRequires:  aether
BuildRequires:  animal-sniffer
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-compress
BuildRequires:  atinject
BuildRequires:  bouncycastle
BuildRequires:  felix-osgi-compendium
BuildRequires:  felix-osgi-core
BuildRequires:  google-guice
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  lucene
BuildRequires:  lucene-contrib
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
BuildRequires:  sisu
BuildRequires:  slf4j
BuildRequires:  truezip-driver-zip
BuildRequires:  truezip-swing

Requires:       aether
Requires:       animal-sniffer
Requires:       apache-commons-cli
Requires:       apache-commons-compress
Requires:       atinject
Requires:       bouncycastle
Requires:       felix-osgi-compendium
Requires:       felix-osgi-core
Requires:       google-guice
Requires:       jpackage-utils
Requires:       junit
Requires:       lucene
Requires:       lucene-contrib
Requires:       maven
Requires:       maven-archetype-catalog
Requires:       maven-archetype-common
Requires:       maven-wagon
Requires:       plexus-cli
Requires:       plexus-utils
Requires:       port-allocator-maven-plugin
Requires:       sisu
Requires:       slf4j
Requires:       truezip-driver-zip
Requires:       truezip-swing
Source44: import.info

%description
Apache Maven Indexer (former Sonatype Nexus Indexer) is the defacto
standard for producing indexes of Maven repositories. The Indexes
are produced and consumed by all major tools in the ecosystem.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%patch0

%if %fedora <= 17
%patch1
%endif

%build
# skip tests because of unpackaged test deps
mvn-rpmbuild package javadoc:aggregate -Dmaven.test.skip=true

%install

# Jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
cp -p indexer-core/target/indexer-core-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-core.jar
cp -p indexer-artifact/target/indexer-artifact-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-artifact.jar

# Javadocs
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POMs
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -p -m 0644 indexer-artifact/pom.xml \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-artifact.pom
install -p -m 0644 indexer-core/pom.xml \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-core.pom

%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap JPP-%{name}-artifact.pom %{name}-artifact.jar
%add_maven_depmap JPP-%{name}-core.pom %{name}-core.jar


%files
%{_javadir}/*
%doc LICENSE
%doc NOTICE
%doc README.md
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE
%doc NOTICE
%doc README.md
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_5jpp7
- new release

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3jpp7
- new version

