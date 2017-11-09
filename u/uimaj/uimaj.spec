Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          uimaj
Version:       2.8.1
Release:       alt1_5jpp8
Summary:       Apache UIMA is an implementation of the OASIS-UIMA specifications
License:       ASL 2.0
URL:           http://uima.apache.org/
Source0:       http://www.apache.org/dist/uima/%{name}-%{version}/%{name}-%{version}-source-release.zip
Patch0:        uimaj-2.8.1-jackson2.7.patch

BuildRequires: maven-local
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(axis:axis)
BuildRequires: mvn(axis:axis-jaxrpc)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.commons:commons-logging)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.ant:ant-apache-regexp)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.uima:parent-pom:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires: mvn(xmlunit:xmlunit)

BuildArch:     noarch
Source44: import.info

%description
Apache UIMA is an implementation of the OASIS-UIMA specifications.

OASIS UIMA Committee: <http://www.oasis-open.org/committees/uima/>.

Unstructured Information Management applications are software systems
that analyze large volumes of unstructured information in order to
discover knowledge that is relevant to an end user.

An example UIM application might ingest plain text and identify
entities, such as persons, places, organizations; or relations,
such as works-for or located-at.

%package -n jcasgen-maven-plugin
Group: Development/Java
Summary:       Apache UIMA Maven JCasGen Plugin

%description -n jcasgen-maven-plugin
A Maven Plugin for using JCasGen to generate Java classes from
XML type system descriptions.

%package -n uima-pear-maven-plugin
Group: Development/Java
Summary:       Apache UIMA Maven Pear Plugin

%description -n uima-pear-maven-plugin
This is a maven plugin that produces a pear artifact.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# Cleanup
find .  -name "*.jar" -delete
find .  -name "*.bat" -delete
find .  -name "*.class" -delete
find .  -name "*.cmd" -delete

%patch0 -p1

# Build @ random fails
%pom_remove_plugin -r :apache-rat-plugin
# org.semver:enforcer-rule:0.9.33
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Remove eclipse stuff (dont provides pom or depmap file)
%pom_disable_module ../aggregate-%{name}-eclipse-plugins aggregate-%{name}
%pom_remove_dep org.apache.uima:%{name}-ep-cas-editor
%pom_remove_dep org.apache.uima:%{name}-ep-configurator
%pom_remove_dep org.apache.uima:%{name}-ep-debug
%pom_remove_dep org.apache.uima:%{name}-ep-jcasgen
%pom_remove_dep org.apache.uima:%{name}-ep-pear-packager
%pom_remove_dep org.apache.uima:%{name}-ep-runtime
%pom_remove_dep org.apache.uima:%{name}-ep-cas-editor-ide
%pom_remove_dep org.apache.uima:%{name}-ep-launcher
%pom_remove_dep org.apache.uima:%{name}-examples
%pom_disable_module ../%{name}-examples aggregate-%{name}

# [ERROR] uimaj-adapter-soap/src/main/java/org/apache/uima/adapter/soap/BinaryDeserializer.java
# cannot access org.apache.commons.logging.Log
%pom_add_dep org.apache.commons:commons-logging %{name}-adapter-soap

# Use system jvm apis
%pom_remove_dep org.apache.geronimo.specs:geronimo-activation_1.0.2_spec %{name}-adapter-soap

# Unavailable deps org.apache.uima:uima-docbook-olink:zip:olink:1-SNAPSHOT
%pom_disable_module ../aggregate-%{name}-docbooks aggregate-%{name}

# These tests @ random fails
rm -r %{name}-core/src/test/java/org/apache/uima/internal/util/UIMAClassLoaderTest.java \
  %{name}-core/src/test/java/org/apache/uima/cas/test/SofaTest.java \
  %{name}-core/src/test/java/org/apache/uima/analysis_engine/impl/AnalysisEngine_implTest.java \
  %{name}-core/src/test/java/org/apache/uima/util/impl/JSR47Logger_implTest.java \
  jcasgen-maven-plugin/src/test/java/org/apache/uima/tools/jcasgen/maven/JCasGenMojoTest.java
# These tests fails with java8
rm -r %{name}-tools/src/test/java/org/apache/uima/tools/viewer/CasAnnotationViewerTest.java

# Unavailable test:crossref2:1.0.0-SNAPSHOT
%pom_remove_plugin :maven-invoker-plugin jcasgen-maven-plugin
 
sed -i 's/\r//' NOTICE README

%pom_xpath_set "pom:dependency[pom:artifactId = 'log4j']/pom:version" 1.2.17 %{name}-core

%mvn_package :PearPackagingMavenPlugin uima-pear-maven-plugin
%mvn_package :jcasgen-maven-plugin jcasgen-maven-plugin

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README RELEASE_NOTES.html
%doc LICENSE NOTICE

%files -n jcasgen-maven-plugin -f .mfiles-jcasgen-maven-plugin
%doc LICENSE NOTICE

%files -n uima-pear-maven-plugin -f .mfiles-uima-pear-maven-plugin
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_5jpp8
- java 8 mass update

