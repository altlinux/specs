Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm) rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with     jp_minimal

Summary:        High-performance, full-featured text search engine
Name:           lucene
Version:        6.1.0
Release:        alt1_4jpp8
Epoch:          0
License:        ASL 2.0
URL:            http://lucene.apache.org/
# solr source contains both lucene and dev-tools
Source0:        http://www.apache.org/dist/lucene/solr/%{version}/solr-%{version}-src.tgz

Patch0:         0001-Disable-ivy-settings.patch
Patch1:         0002-Dependency-generation.patch

BuildRequires:  ant
BuildRequires:  ivy-local
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(jakarta-regexp:jakarta-regexp)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%if %{without jp_minimal}
BuildRequires:  mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(com.spatial4j:spatial4j)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.uima:Tagger)
BuildRequires:  mvn(org.apache.uima:uimaj-core)
BuildRequires:  mvn(org.apache.uima:WhitespaceTokenizer)
BuildRequires:  mvn(org.carrot2:morfologik-fsa)
BuildRequires:  mvn(org.carrot2:morfologik-polish)
BuildRequires:  mvn(org.carrot2:morfologik-stemming)
BuildRequires:  mvn(org.eclipse.jetty:jetty-continuation)
BuildRequires:  mvn(org.eclipse.jetty:jetty-http)
BuildRequires:  mvn(org.eclipse.jetty:jetty-io)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(xerces:xercesImpl)
%endif

Provides:       %{name}-core = %{epoch}:%{version}-%{release}

BuildArch:      noarch
Source44: import.info

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package analysis
Group: Development/Java
Summary:      Lucene Common Analyzers

%description analysis
Lucene Common Analyzers.

%package queries
Group: Development/Java
Summary:      Lucene Queries Module

%description queries
Lucene Queries Module.

%package queryparser
Group: Development/Java
Summary:      Lucene QueryParsers Module

%description queryparser
Lucene QueryParsers Module.

%package analyzers-smartcn
Group: Development/Java
Summary:      Smart Chinese Analyzer

%description analyzers-smartcn
Lucene Smart Chinese Analyzer.

%package sandbox
Group: Development/Java
Summary:      Lucene Sandbox Module

%description sandbox
Lucene Sandbox Module.

%if %{without jp_minimal}
%package parent
Group: Development/Java
Summary:      Parent POM for Lucene

%description parent
Parent POM for Lucene.

%package solr-grandparent
Group: Development/Java
Summary:      Lucene Solr grandparent POM

%description solr-grandparent
Lucene Solr grandparent POM.

%package backward-codecs
Group: Development/Java
Summary:      Lucene Backward Codecs Module

%description backward-codecs
Codecs for older versions of Lucene.

%package benchmark
Group: Development/Java
Summary:      Lucene Benchmarking Module

%description benchmark
Lucene Benchmarking Module.

%package replicator
Group: Development/Java
Summary:      Lucene Replicator Module

%description replicator
Lucene Replicator Module.

%package grouping
Group: Development/Java
Summary:      Lucene Grouping Module

%description grouping
Lucene Grouping Module.

%package highlighter
Group: Development/Java
Summary:      Lucene Highlighter Module

%description highlighter
Lucene Highlighter Module.

%package misc
Group: Development/Java
Summary:      Miscellaneous Lucene extensions

%description misc
Miscellaneous Lucene extensions.

%package test-framework
Group: Development/Java
Summary:      Apache Lucene Java Test Framework

%description test-framework
Apache Lucene Java Test Framework.

%package memory
Group: Development/Java
Summary:      Lucene Memory Module

%description memory
High-performance single-document index to compare against Query.

%package expressions
Group: Development/Java
Summary:      Lucene Expressions Module

%description expressions
Dynamically computed values to sort/facet/search on based on a pluggable
grammar.

%package demo
Group: Development/Java
Summary:      Lucene Demo Module

%description demo
Demo for Apache Lucene Java.

%package classification
Group: Development/Java
Summary:      Lucene Classification Module

%description classification
Lucene Classification Module.

%package join
Group: Development/Java
Summary:      Lucene Join Module

%description join
Lucene Join Module.

%package suggest
Group: Development/Java
Summary:      Lucene Suggest Module

%description suggest
Lucene Suggest Module.

%package facet
Group: Development/Java
Summary:      Lucene Facets Module

%description facet
Package for Faceted Indexing and Search.

%package spatial
Group: Development/Java
Summary:      Geospatial indexing APIs for Apache Lucene

%description spatial
Geospatial indexing APIs for Apache Lucene.

%package spatial-extras
Group: Development/Java
Summary:      Spatial Strategies for Apache Lucene

%description spatial-extras
Spatial Strategies for Apache Lucene.

%package spatial3d
Group: Development/Java
Summary:      Lucene Spatial 3D

%description spatial3d
Spatial shapes implemented using 3D planar geometry

%package codecs
Group: Development/Java
Summary:      Codecs and postings formats for Apache Lucene

%description codecs
Codecs and postings formats for Apache Lucene.

%package analyzers-phonetic
Group: Development/Java
Summary:      Lucene Phonetic Filters

%description analyzers-phonetic
Provides phonetic encoding via Commons Codec.

%package analyzers-icu
Group: Development/Java
Summary:      Lucene ICU Analysis Components

%description analyzers-icu
Provides integration with ICU (International Components for Unicode) for
stronger Unicode and internationalization support.

%package analyzers-morfologik
Group: Development/Java
Summary:      Lucene Morfologik Polish Lemmatizer

%description analyzers-morfologik
A dictionary-driven lemmatizer for Polish (includes morphosyntactic
annotations).

%package analyzers-uima
Group: Development/Java
Summary:      Lucene UIMA Analysis Components

%description analyzers-uima
Lucene Integration with UIMA for extracting metadata from arbitrary (text)
fields and enrich document with features extracted from UIMA types (language,
sentences, concepts, named entities, etc.).

%package analyzers-kuromoji
Group: Development/Java
Summary:      Lucene Kuromoji Japanese Morphological Analyzer

%description analyzers-kuromoji
Lucene Kuromoji Japanese Morphological Analyzer.

%package analyzers-stempel
Group: Development/Java
Summary:      Lucene Stempel Analyzer

%description analyzers-stempel
Lucene Stempel Analyzer.

%endif # without jp_minimal

%package javadoc
Group: Development/Java
Summary:        Javadoc for Lucene
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n solr-%{version}

%patch0 -p1
%patch1 -p1

rm -rf solr

find -name "*.jar" -delete

mv lucene/*.txt .

sed -i -e "s|/Export-Package>|/Export-Package><_nouses>true</_nouses>|g" dev-tools/maven/pom.xml.template

# make the target public
sed -i 's/-filter-pom-templates/filter-pom-templates/' lucene/common-build.xml
# avoid descent to other modules to avoid unnecessary compilation of modules we
# will recompile with maven anyway
%pom_xpath_remove 'target[@name="compile-tools"]/modules-crawl' lucene/build.xml

# suggest provides spellchecker
%mvn_alias :%{name}-suggest :%{name}-spellchecker

# compatibility with existing packages
%mvn_alias :%{name}-analyzers-common :%{name}-analyzers

%mvn_package ":%{name}-analysis-modules-aggregator" %{name}-analysis
%mvn_package ":%{name}-analyzers-common" %{name}-analysis
%mvn_package ":{*}-aggregator" @1

%build
pushd %{name}
find -maxdepth 2 -type d -exec mkdir -p '{}/lib' \;
# generate dependencies
ant -f common-build.xml filter-pom-templates -Divy.mode=local -Dversion=%{version}

# fix source dir + move to expected place
for pom in `find build/poms/%{name} -name pom.xml`; do
    sed 's/\${module-path}/${basedir}/g' "$pom" > "${pom##build/poms/%{name}/}"
done
%pom_disable_module src/test core
%pom_disable_module src/test codecs

# unresolvable test dep
%pom_remove_dep org.locationtech.spatial4j:spatial4j::test spatial-extras

# fix dep on spatial4j
%pom_change_dep org.locationtech.spatial4j:spatial4j com.spatial4j:spatial4j spatial-extras
%pom_change_dep org.locationtech.spatial4j:spatial4j com.spatial4j:spatial4j benchmark
find benchmark spatial-extras -name *.java -exec sed -i \
  -e 's/org\.locationtech\.spatial4j/com.spatial4j.core/' {} \;

# test deps
%pom_add_dep org.antlr:antlr-runtime::test demo

popd

mv lucene/build/poms/pom.xml .

# deal with split packages in core/misc modules by adding additional metadata and
# require-bundling the core bundle from misc
%pom_xpath_set "pom:Export-Package" "*;version=\"%{version}\""
%pom_add_plugin org.apache.felix:maven-bundle-plugin lucene/misc \
"<configuration><instructions>
<Require-Bundle>org.apache.lucene.core;bundle-version=\"%{version}\"</Require-Bundle>
<Export-Package>
 org.apache.lucene.document;version=\"%{version}\";misc=split;mandatory:=misc,
 org.apache.lucene.index;version=\"%{version}\";misc=split;mandatory:=misc,
 org.apache.lucene.search;version=\"%{version}\";misc=split;mandatory:=misc,
 org.apache.lucene.store;version=\"%{version}\";misc=split;mandatory:=misc,
 org.apache.lucene.util.fst;version=\"%{version}\";misc=split;mandatory:=misc,
 *;version=\"%{version}\"</Export-Package>
</instructions></configuration>"

%pom_disable_module solr
%pom_remove_plugin -r :gmaven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :forbiddenapis
%pom_remove_plugin -r :buildnumber-maven-plugin

%if %{with jp_minimal}
pushd lucene
%pom_disable_module backward-codecs
%pom_disable_module codecs
%pom_disable_module test-framework
%pom_disable_module benchmark
%pom_disable_module classification
%pom_disable_module demo
%pom_disable_module expressions
%pom_disable_module facet
%pom_disable_module grouping
%pom_disable_module highlighter
%pom_disable_module join
%pom_disable_module memory
%pom_disable_module misc
%pom_disable_module replicator
%pom_disable_module spatial
%pom_disable_module spatial-extras
%pom_disable_module spatial3d
%pom_disable_module suggest

%pom_disable_module icu analysis
%pom_disable_module kuromoji analysis
%pom_disable_module morfologik analysis
%pom_disable_module phonetic analysis
%pom_disable_module stempel analysis
%pom_disable_module uima analysis

popd

%mvn_package :lucene-parent __noinstall
%mvn_package :lucene-solr-grandparent __noinstall
%endif


# For some reason TestHtmlParser.testTurkish fails when building inside SCLs
%mvn_build -s -f

%install
%mvn_install

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

%files -f .mfiles-%{name}-core
%doc CHANGES.txt README.txt MIGRATE.txt
%doc LICENSE.txt NOTICE.txt

%files analysis -f .mfiles-%{name}-analysis
%files queries -f .mfiles-%{name}-queries
%files queryparser -f .mfiles-%{name}-queryparser
%files analyzers-smartcn -f .mfiles-%{name}-analyzers-smartcn
%files sandbox -f .mfiles-%{name}-sandbox
%if %{without jp_minimal}
%files parent -f .mfiles-%{name}-parent
%files solr-grandparent -f .mfiles-%{name}-solr-grandparent
%files benchmark -f .mfiles-%{name}-benchmark
%files backward-codecs -f .mfiles-%{name}-backward-codecs
%files replicator -f .mfiles-%{name}-replicator
%files grouping -f .mfiles-%{name}-grouping
%files highlighter -f .mfiles-%{name}-highlighter
%files misc -f .mfiles-%{name}-misc
%files test-framework -f .mfiles-%{name}-test-framework
%files memory -f .mfiles-%{name}-memory
%files expressions -f .mfiles-%{name}-expressions
%files demo -f .mfiles-%{name}-demo
%files classification -f .mfiles-%{name}-classification
%files join -f .mfiles-%{name}-join
%files suggest -f .mfiles-%{name}-suggest
%files facet -f .mfiles-%{name}-facet
%files spatial -f .mfiles-%{name}-spatial
%files spatial-extras -f .mfiles-%{name}-spatial-extras
%files spatial3d -f .mfiles-%{name}-spatial3d
%files codecs -f .mfiles-%{name}-codecs
%files analyzers-phonetic -f .mfiles-%{name}-analyzers-phonetic
%files analyzers-icu -f .mfiles-%{name}-analyzers-icu
%files analyzers-morfologik -f .mfiles-%{name}-analyzers-morfologik
%files analyzers-uima -f .mfiles-%{name}-analyzers-uima
%files analyzers-kuromoji -f .mfiles-%{name}-analyzers-kuromoji
%files analyzers-stempel -f .mfiles-%{name}-analyzers-stempel
%endif

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.1.0-alt1_4jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.5.0-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.5.0-alt1_4jpp8
- new fc release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.5.0-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.3.0-alt1_1jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_2jpp7
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.6.0-alt1_11jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.6.0-alt1_6jpp7
- new version

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.6.0-alt1_5jpp7
- new version

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.9.4-alt1_7jpp6
- update to new release by jppimport

* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.9.4-alt1_6jpp6
- update to new release by jppimport

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt3_5jpp6
- rebuild without osgi provides

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_5jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_1jpp5
- added provides for lucene2-demo

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_1jpp5
- new version

* Tue Mar 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt2_jvm5
- added maven poms, added Provides: lucene23

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_jvm5
- Sisyphus upload; thanks to Alexey Morozov.

* Fri Jan 23 2009 Alexey Morozov <morozov@altlinux.org> 0:2.4.0-alt0.1
- updated to 2.4.0

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_3.4jpp5
- updated to 2.3.1; added provides lucene22

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt5jvm4.2
- renamed to lucene2 to avoid conflicts with lucene1

* Tue Nov 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt4jvm4.2
- enabled check, disabled devel, added contrib

* Mon Nov 05 2007 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt3jvm4.2
- NMU: added -devel subpackage

* Tue Jul 17 2007 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2
- NMU: partial jpackage compatibility added
- enabled demo (required for eclipse).
- demo is packaged according to jpackage.
- added source=1.4 and target=1.4

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.1.0-alt1
- Update to 2.1.0 release

* Thu Nov 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.0.0-alt1
- Update to 2.0.0 release

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.9.1-alt1
- Updated to 1.9.1
- Disabled tests (fail to build for some bogus reason)
- Disabled demo by default

* Wed Dec 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.3-alt1
- Updated to 1.4.3
- Spec cleanup for rpm-build-java

* Tue Jun 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.3-alt1
- New upstream release
- Disable debug for non-debug builds

* Tue Sep 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.2-alt1
- Released for ALT Linux
