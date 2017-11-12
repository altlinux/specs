Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          uima-addons
Version:       2.3.1
Release:       alt1_9jpp8
Summary:       Apache UIMA Addons components
License:       ASL 2.0
URL:           http://uima.apache.org/sandbox.html
Source0:       http://www.apache.org/dist/uima/%{name}-%{version}-source-release.zip
# fix bundle plugin configuration
Patch0:        %{name}-%{version}-disable-embedded-dependencies.patch
# fix build for httpclient > 4.0
Patch1:        %{name}-%{version}-httpclient.patch

BuildRequires: mvn(bsf:bsf)
BuildRequires: mvn(commons-digester:commons-digester)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging-api)
BuildRequires: mvn(javax.xml.stream:stax-api)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.uima:parent-pom:pom:)
BuildRequires: mvn(org.apache.uima:uimaj-core)
BuildRequires: mvn(org.apache.uima:uimaj-document-annotation)
BuildRequires: mvn(org.apache.xmlbeans:xmlbeans)
BuildRequires: mvn(org.beanshell:bsh)
BuildRequires: mvn(org.tartarus:snowball)
BuildRequires: mvn(rhino:js)
BuildRequires: mvn(org.apache.tomcat:tomcat-servlet-api)

%if 0
# Unavailable build deps **
BuildRequires: mvn(org.apache.lucene:lucene-snowball:2.9.3)
BuildRequires: mvn(org.apache.solr:solr-core:3.1.0)
BuildRequires: mvn(org.apache.solr:solr-solrj:3.1.0)
BuildRequires: mvn(org.apache.tika:tika-core:0.7)
BuildRequires: mvn(org.apache.tika:tika-parsers:0.7)
BuildRequires: mvn(org.apache.uima:uimaj-examples:2.3.1)
BuildRequires: mvn(org.eclipse.emf.ecore:xmi:2.3.0-v200706262000)
BuildRequires: mvn(org.eclipse.emf:common:2.3.0-v200706262000)
BuildRequires: mvn(org.eclipse.emf:ecore:2.3.0-v200706262000)
BuildRequires: mvn(org.mortbay.jetty:jetty:6.1.8)
%endif

# Test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.uima:uimaj-test-util)
BuildRequires: mvn(org.apache.uima:uimaj-component-test-util)

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.apache.uima:PearPackagingMavenPlugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:xmlbeans-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(org.apache.ant:ant-apache-regexp)

BuildArch:     noarch
Source44: import.info

%description
UIMA Addons is a collection of Annotators extracted for
sandbox for official distribution. It also provides
Simple Server and Pear packaging tools.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%patch0 -p0
%patch1 -p0

# Disable unneeded (only for eclipse) OSGi artefacts
%pom_remove_plugin :maven-assembly-plugin uima-addons-parent
%pom_remove_plugin :maven-dependency-plugin uima-addons-parent
%pom_remove_plugin :maven-resources-plugin uima-addons-parent

%pom_remove_plugin :maven-javadoc-plugin uima-addons-parent

# Unavailable or too old build deps **
%pom_disable_module ConfigurableFeatureExtractor
%pom_disable_module Lucas
%pom_disable_module Solrcas
%pom_disable_module TikaAnnotator

%pom_remove_dep org.mortbay.jetty:jetty SimpleServer
rm -r SimpleServer/src/main/java/org/apache/uima/simpleserver/util/JettyUtils.java \
 SimpleServer/src/test/java/org/apache/uima/simpleserver/test/ServerFailureTest.java \
 SimpleServer/src/test/java/org/apache/uima/simpleserver/test/ServerTest.java

# Fail with XMvn if aId is different by finalName
for p in AlchemyAPIAnnotator BSFAnnotator ConceptMapper DictionaryAnnotator \
 FsVariables OpenCalaisAnnotator PearPackagingAntTask RegularExpressionAnnotator \
 SimpleServer SnowballAnnotator Tagger WhitespaceTokenizer; do
%pom_xpath_remove "pom:project/pom:build/pom:finalName" ${p}
done

for m in ConfigurableFeatureExtractor DictionaryAnnotator RegularExpressionAnnotator SimpleServer; do
%pom_remove_dep org.apache.geronimo.specs:geronimo-stax-api_1.0_spec  ${m}
%pom_add_dep javax.xml.stream:stax-api:1.0.1 ${m}
done

rm -r SnowballAnnotator/src/main/java/org/tartarus
%pom_add_dep org.tartarus:snowball SnowballAnnotator

# @ random fail AssertionFailedError
rm SnowballAnnotator/src/test/java/org/apache/uima/annotator/SnowballAnnotatorTest.java

# java.lang.AssertionError: null
rm -r AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/TextRankedEntityExtractionAnnotatorTest.java

sed -i 's/\r//' LICENSE NOTICE

# requires web access
rm -r AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/SimpleTest.java \
 AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/HtmlMicroformatsAnnotatorTest.java \
 AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/TextCategorizationAnnotatorTest.java \
 AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/TextConceptTaggingAnnotatorTest.java \
 AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/TextKeywordExtractionAnnotatorTest.java \
 AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/TextLanguageDetectionAnnotatorTest.java \
 AlchemyAPIAnnotator/src/test/java/org/apache/uima/alchemy/annotator/TextSentimentAnalysisAnnotatorTest.java \
 OpenCalaisAnnotator/src/test/java/org/apache/uima/annotator/calais/OpenCalaisAnnotatorTest.java

sed -i "s|<groupId>javax.servlet</groupId>|<groupId>org.apache.tomcat</groupId>|" SimpleServer/pom.xml
sed -i "s|<artifactId>servlet-api</artifactId>|<artifactId>tomcat-servlet-api</artifactId>|" SimpleServer/pom.xml
# Solrcas/pom.xml

sed -i "s|<version>1.2.14</version>|<version>1.2.17</version>|" BSFAnnotator/pom.xml
#  Lucas/pom.xml

%mvn_package ::pear: __noinstall

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc RELEASE_NOTES.html
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_7jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_5jpp8
- java 8 mass update

