# HOW???
%filter_from_provides /.usr.bin.jar/d
%def_with manualreq
%define oldname lucene
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm) unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        High-performance, full-featured text search engine
Name:           lucene5
Version:        5.5.0
Release:        alt1_0jpp8
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
BuildRequires:  mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(com.spatial4j:spatial4j)
BuildRequires:  mvn(jakarta-regexp:jakarta-regexp)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sourceforge.nekohtml:nekohtml)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
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

Provides:       %{oldname}-core = %{epoch}:%{version}-%{release}

BuildArch:      noarch
Source44: import.info

%if_with manualreq
AutoReq: yes,nomaven
#Requires: 
%endif

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package parent
Group: Development/Java
Summary:      Parent POM for Lucene

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-solr-grandparent = %EVR
%endif

%description parent
Parent POM for Lucene.

%package solr-grandparent
Group: Development/Java
Summary:      Lucene Solr grandparent POM

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(org.apache.felix:maven-bundle-plugin)  
Requires: mvn(org.apache.maven.plugins:maven-jar-plugin)  
Requires: mvn(org.apache:apache:pom:)  
Requires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)  
%endif

%description solr-grandparent
Lucene Solr grandparent POM.

%package backward-codecs
Group: Development/Java
Summary:      Lucene Backward Codecs Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %name = %EVR
%endif

%description backward-codecs
Codecs for older versions of Lucene.

%package benchmark
Group: Development/Java
Summary:      Lucene Benchmarking Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(com.ibm.icu:icu4j)
Requires: mvn(net.sourceforge.nekohtml:nekohtml)
Requires: mvn(org.apache.commons:commons-compress)
Requires: mvn(xerces:xercesImpl)
Requires: %{name}-highlighter = %EVR
Requires: %{name}-facet = %EVR
Requires: %{name}-spatial = %EVR
Requires: %{name}-codecs = %EVR
Requires: %{name}-queryparser = %EVR
%endif

%description benchmark
Lucene Benchmarking Module.

%package replicator
Group: Development/Java
Summary:      Lucene Replicator Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(commons-logging:commons-logging)  
Requires: mvn(javax.servlet:javax.servlet-api)  
Requires: mvn(org.apache.httpcomponents:httpclient)  
Requires: mvn(org.apache.httpcomponents:httpcore)  
Requires: mvn(org.eclipse.jetty:jetty-continuation)  
Requires: mvn(org.eclipse.jetty:jetty-http)  
Requires: mvn(org.eclipse.jetty:jetty-io)  
Requires: mvn(org.eclipse.jetty:jetty-server)  
Requires: mvn(org.eclipse.jetty:jetty-servlet)  
Requires: mvn(org.eclipse.jetty:jetty-util)  
Requires: %{name}-facet = %EVR
%endif

%description replicator
Lucene Replicator Module.

%package grouping
Group: Development/Java
Summary:      Lucene Grouping Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-queries = %EVR
%endif

%description grouping
Lucene Grouping Module.

%package highlighter
Group: Development/Java
Summary:      Lucene Highlighter Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-memory = %EVR
Requires: %{name}-join = %EVR
Requires: %{name}-analysis = %EVR
%endif

%description highlighter
Lucene Highlighter Module.

%package misc
Group: Development/Java
Summary:      Miscellaneous Lucene extensions

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name} = %EVR
%endif

%description misc
Miscellaneous Lucene extensions.

%package test-framework
Group: Development/Java
Summary:      Apache Lucene Java Test Framework

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(com.carrotsearch.randomizedtesting:junit4-ant)  
Requires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)  
Requires: mvn(junit:junit)  
Requires: mvn(org.apache.ant:ant)  
Requires: %{name}-codecs = %EVR
%endif

%description test-framework
Apache Lucene Java Test Framework.

%package memory
Group: Development/Java
Summary:      Lucene Memory Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name} = %EVR
%endif

%description memory
High-performance single-document index to compare against Query.

%package expressions
Group: Development/Java
Summary:      Lucene Expressions Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(org.antlr:antlr-runtime)  
Requires: mvn(org.ow2.asm:asm)  
Requires: mvn(org.ow2.asm:asm-commons)  
Requires: %{name}-queries = %EVR
%endif

%description expressions
Dynamically computed values to sort/facet/search on based on a pluggable
grammar.

%package demo
Group: Development/Java
Summary:      Lucene Demo Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(javax.servlet:servlet-api)
Requires: %{name}-expressions = %EVR
Requires: %{name}-facet = %EVR
Requires: %{name}-analysis = %EVR
Requires: %{name}-queryparser = %EVR
%endif

%description demo
Demo for Apache Lucene Java.

%package classification
Group: Development/Java
Summary:      Lucene Classification Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-queries = %EVR
%endif

%description classification
Lucene Classification Module.

%package join
Group: Development/Java
Summary:      Lucene Join Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-grouping = %EVR
%endif

%description join
Lucene Join Module.

%package suggest
Group: Development/Java
Summary:      Lucene Suggest Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-misc = %EVR
Requires: %{name}-analysis = %EVR
Requires: %{name}-queries = %EVR
%endif

%description suggest
Lucene Suggest Module.

%package facet
Group: Development/Java
Summary:      Lucene Facets Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-queries = %EVR
%endif

%description facet
Package for Faceted Indexing and Search.

%package analysis
Group: Development/Java
Summary:      Lucene Common Analyzers

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name} = %EVR
%endif

%description analysis
Lucene Common Analyzers.

%package sandbox
Group: Development/Java
Summary:      Lucene Sandbox Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(jakarta-regexp:jakarta-regexp)
Requires: %{name} = %EVR
%endif

%description sandbox
Lucene Sandbox Module.

%package queries
Group: Development/Java
Summary:      Lucene Queries Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name} = %EVR
%endif

%description queries
Lucene Queries Module.

%package spatial
Group: Development/Java
Summary:      Spatial Strategies for Apache Lucene

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(com.spatial4j:spatial4j)  
Requires: %{name}-misc = %EVR
Requires: %{name}-queries = %EVR
Requires: %{name}-spatial3d = %EVR
%endif

%description spatial
Spatial Strategies for Apache Lucene.

%package spatial3d
Group: Development/Java
Summary:      Lucene Spatial 3D

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name} = %EVR
%endif

%description spatial3d
Spatial shapes implemented using 3D planar geometry

%package codecs
Group: Development/Java
Summary:      Codecs and postings formats for Apache Lucene

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name} = %EVR
%endif

%description codecs
Codecs and postings formats for Apache Lucene.

%package queryparser
Group: Development/Java
Summary:      Lucene QueryParsers Module

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-sandbox = %EVR
Requires: %{name}-queries = %EVR
%endif

%description queryparser
Lucene QueryParsers Module.

%package analyzers-smartcn
Group: Development/Java
Summary:      Smart Chinese Analyzer

%if_with manualreq
AutoReq: yes,nomaven 
Requires: %{name}-analysis = %EVR
%endif

%description analyzers-smartcn
Lucene Smart Chinese Analyzer.

%package analyzers-phonetic
Group: Development/Java
Summary:      Lucene Phonetic Filters

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(commons-codec:commons-codec)
Requires: %{name}-analysis = %EVR
%endif

%description analyzers-phonetic
Provides phonetic encoding via Commons Codec.

%package analyzers-icu
Group: Development/Java
Summary:      Lucene ICU Analysis Components

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(com.ibm.icu:icu4j)  
Requires: %{name}-analysis = %EVR
%endif

%description analyzers-icu
Provides integration with ICU (International Components for Unicode) for
stronger Unicode and internationalization support.

%package analyzers-morfologik
Group: Development/Java
Summary:      Lucene Morfologik Polish Lemmatizer

%if_with manualreq
AutoReq: yes,nomaven 
Requires: mvn(org.carrot2:morfologik-fsa)  
Requires: mvn(org.carrot2:morfologik-polish)  
Requires: mvn(org.carrot2:morfologik-stemming)  
Requires: %{name}-analysis = %EVR
%endif

%description analyzers-morfologik
A dictionary-driven lemmatizer for Polish (includes morphosyntactic
annotations).

%package analyzers-uima
Group: Development/Java
Summary:      Lucene UIMA Analysis Components

%if_with manualreq
AutoReq: yes,nomaven
Requires: mvn(org.apache.uima:Tagger)  
Requires: mvn(org.apache.uima:WhitespaceTokenizer)  
Requires: mvn(org.apache.uima:uimaj-core)  
Requires: %{name}-analysis = %EVR
%endif

%description analyzers-uima
Lucene Integration with UIMA for extracting metadata from arbitrary (text)
fields and enrich document with features extracted from UIMA types (language,
sentences, concepts, named entities, etc.).

%package analyzers-kuromoji
Group: Development/Java
Summary:      Lucene Kuromoji Japanese Morphological Analyzer

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-analysis = %EVR
%endif

%description analyzers-kuromoji
Lucene Kuromoji Japanese Morphological Analyzer.

%package analyzers-stempel
Group: Development/Java
Summary:      Lucene Stempel Analyzer

%if_with manualreq
AutoReq: yes,nomaven
Requires: %{name}-analysis = %EVR
%endif

%description analyzers-stempel
Lucene Stempel Analyzer.


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

# unresolvable test dep
%pom_remove_dep com.spatial4j:spatial4j::test lucene/spatial

# suggest provides spellchecker
%mvn_alias :%{oldname}-suggest :%{oldname}-spellchecker

# compatibility with existing packages
%mvn_alias :%{oldname}-analyzers-common :%{oldname}-analyzers

%mvn_package ":%{oldname}-analysis-modules-aggregator" %{oldname}-analysis
%mvn_package ":%{oldname}-analyzers-common" %{oldname}-analysis
%mvn_package ":{*}-aggregator" @1

%mvn_compat_version : 5 %{version}

%build
pushd %{oldname}
# generate dependencies
ant generate-maven-artifacts -Divy.mode=local -Dversion=%{version}

# fix source dir + move to expected place
for pom in `find build/poms/%{oldname} -name pom.xml`; do
    sed 's/\${module-path}/${basedir}/g' "$pom" > "${pom##build/poms/%{oldname}/}"
done
%pom_disable_module src/test core
%pom_disable_module src/test codecs

# test deps
%pom_add_dep org.antlr:antlr-runtime::test demo

popd

mv lucene/build/poms/pom.xml .

%pom_disable_module solr
%pom_remove_plugin -r :gmaven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :forbiddenapis
%pom_remove_plugin -r :buildnumber-maven-plugin


# For some reason TestHtmlParser.testTurkish fails when building inside SCLs
%mvn_build -s -f

# Fix OSGi metadata in misc module
pushd lucene/misc/target
unzip lucene-misc-%{version}.jar META-INF/MANIFEST.MF
sed -i -e '1aRequire-Bundle: org.apache.lucene.core
' META-INF/MANIFEST.MF
jar ufm lucene-misc-%{version}.jar META-INF/MANIFEST.MF 2>&1 > /dev/null
popd

# analyzers-common needs versioned requires on package from core
# maven-bundle-plugin doesn't seem to recognize this case on F24
%if 0%{?fedora} == 24
pushd lucene/analysis/common/target
unzip lucene-analyzers-common-%{version}.jar META-INF/MANIFEST.MF
sed -i -e 's/org.apache.lucene.analysis,/org.apache.lucene.analysis;version="[5.5,6)",/' META-INF/MANIFEST.MF
jar ufm lucene-analyzers-common-%{version}.jar META-INF/MANIFEST.MF 2>&1 > /dev/null
popd
%endif

%install
%mvn_install



# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{oldname}

%files -f .mfiles-%{oldname}-core
%doc CHANGES.txt README.txt MIGRATE.txt
%doc LICENSE.txt NOTICE.txt

%files parent -f .mfiles-%{oldname}-parent
%files solr-grandparent -f .mfiles-%{oldname}-solr-grandparent
%files benchmark -f .mfiles-%{oldname}-benchmark
%files backward-codecs -f .mfiles-%{oldname}-backward-codecs
%files replicator -f .mfiles-%{oldname}-replicator
%files grouping -f .mfiles-%{oldname}-grouping
%files highlighter -f .mfiles-%{oldname}-highlighter
%files misc -f .mfiles-%{oldname}-misc
%files test-framework -f .mfiles-%{oldname}-test-framework
%files memory -f .mfiles-%{oldname}-memory
%files expressions -f .mfiles-%{oldname}-expressions
%files demo -f .mfiles-%{oldname}-demo
%files classification -f .mfiles-%{oldname}-classification
%files join -f .mfiles-%{oldname}-join
%files suggest -f .mfiles-%{oldname}-suggest
%files facet -f .mfiles-%{oldname}-facet
%files analysis -f .mfiles-%{oldname}-analysis
%files sandbox -f .mfiles-%{oldname}-sandbox
%files queries -f .mfiles-%{oldname}-queries
%files spatial -f .mfiles-%{oldname}-spatial
%files spatial3d -f .mfiles-%{oldname}-spatial3d
%files codecs -f .mfiles-%{oldname}-codecs
%files queryparser -f .mfiles-%{oldname}-queryparser
%files analyzers-smartcn -f .mfiles-%{oldname}-analyzers-smartcn
%files analyzers-phonetic -f .mfiles-%{oldname}-analyzers-phonetic
%files analyzers-icu -f .mfiles-%{oldname}-analyzers-icu
%files analyzers-morfologik -f .mfiles-%{oldname}-analyzers-morfologik
%files analyzers-uima -f .mfiles-%{oldname}-analyzers-uima
%files analyzers-kuromoji -f .mfiles-%{oldname}-analyzers-kuromoji
%files analyzers-stempel -f .mfiles-%{oldname}-analyzers-stempel

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Apr 20 2018 Igor Vlasenko <viy@altlinux.ru> 0:5.5.0-alt1_0jpp8
- compat package lucene5 for hibernate-search

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
