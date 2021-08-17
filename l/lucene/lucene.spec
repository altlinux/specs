Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm)
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
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
Version:        8.8.2
Release:        alt1_1jpp11
Epoch:          0
License:        ASL 2.0
URL:            http://lucene.apache.org/
# solr source contains both lucene and dev-tools
Source0:        https://archive.apache.org/dist/lucene/solr/%{version}/solr-%{version}-src.tgz

Patch0:         0001-Disable-ivy-settings.patch
Patch1:         0002-Dependency-generation.patch

BuildRequires:  ant
BuildRequires:  ivy-local
BuildRequires:  maven-local
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%if %{without jp_minimal}
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.commons:commons-compress)
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

# Obsolete since F32
# Required deps were removed from fedora
Obsoletes: %{name}-benchmark < 8.1.1-3
Obsoletes: %{name}-demo < 8.1.1-3
Obsoletes: %{name}-facet < 8.1.1-3
Obsoletes: %{name}-replicator < 8.1.1-3
Obsoletes: %{name}-spatial-extras < 8.1.1-3
Obsoletes: %{name}-spatial3d < 8.1.1-3
Obsoletes: %{name}-test-framework < 8.4.1-4

# Obsolete since F32
# Module was removed upstream
Obsoletes: %{name}-spatial < 8.1.1-3

%if %{with jp_minimal}
# Remove left-over packages that would have broken deps when built in minimal mode
Obsoletes: %{name}-parent < %{version}-%{release}
Obsoletes: %{name}-solr-grandparent < %{version}-%{release}
Obsoletes: %{name}-expressions < %{version}-%{release}
Obsoletes: %{name}-analyzers-phonetic < %{version}-%{release}
Obsoletes: %{name}-analyzers-icu < %{version}-%{release}
Obsoletes: %{name}-analyzers-nori < %{version}-%{release}
Obsoletes: %{name}-analyzers-kuromoji < %{version}-%{release}
Obsoletes: %{name}-analyzers-stempel < %{version}-%{release}
%endif

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
# Obsoletes since F30
# This module was removed upstream and no replacement exists
Obsoletes: %{name}-analyzers-uima < 8.1.1-3
# Obsolete since F32
# Required deps were removed from fedora
Obsoletes: %{name}-analyzers-morfologik < 8.1.1-3

%description analysis
Lucene Common Analyzers.

%package analyzers-smartcn
Group: Development/Java
Summary:      Smart Chinese Analyzer

%description analyzers-smartcn
Lucene Smart Chinese Analyzer.

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

%package join
Group: Development/Java
Summary:      Lucene Join Module

%description join
Lucene Join Module.

%package memory
Group: Development/Java
Summary:      Lucene Memory Module

%description memory
High-performance single-document index to compare against Query.

%package misc
Group: Development/Java
Summary:      Miscellaneous Lucene extensions

%description misc
Miscellaneous Lucene extensions.

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

%package sandbox
Group: Development/Java
Summary:      Lucene Sandbox Module

%description sandbox
Lucene Sandbox Module.

%package backward-codecs
Group: Development/Java
Summary:      Lucene Backward Codecs Module

%description backward-codecs
Codecs for older versions of Lucene.

%package codecs
Group: Development/Java
Summary:      Codecs and postings formats for Apache Lucene

%description codecs
Codecs and postings formats for Apache Lucene.

%package classification
Group: Development/Java
Summary:      Lucene Classification Module

%description classification
Lucene Classification Module.

%package suggest
Group: Development/Java
Summary:      Lucene Suggest Module

%description suggest
Lucene Suggest Module.

%package monitor
Group: Development/Java
Summary:      Lucene Monitor Module

%description monitor
Lucene Monitor Module.

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

%package expressions
Group: Development/Java
Summary:      Lucene Expressions Module

%description expressions
Dynamically computed values to sort/facet/search on based on a pluggable
grammar.

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

%package analyzers-nori
Group: Development/Java
Summary:      An analyzer with morphological analysis for Korean

%description analyzers-nori
An analyzer with morphological analysis for Korean.

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

%endif

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

mkdir -p lucene/build/analysis/{kuromoji,nori}

# don't generate uses clauses in osgi metadata
sed -i -e "/<Export-Package>/a<_nouses>true</_nouses>" dev-tools/maven/pom.xml.template

# optional on internal APIs that might not be present
sed -i -e "/<Export-Package>/a<Import-Package>com.sun.management;resolution:=\"optional\",sun.misc;resolution:=\"optional\",*</Import-Package>" dev-tools/maven/pom.xml.template

# compatibility with existing packages
%mvn_alias :%{name}-analyzers-common :%{name}-analyzers

%mvn_package ":%{name}-analysis-modules-aggregator" %{name}-analysis
%mvn_package ":%{name}-analyzers-common" %{name}-analysis
%mvn_package ":{*}-aggregator" @1

%build
pushd %{name}
find -maxdepth 2 -type d -exec mkdir -p '{}/lib' \;

# generate maven dependencies
ant -f build.xml generate-maven-artifacts -Divy.mode=local -Dversion=%{version} -Divy.available=true

# fix source dir + move to expected place
for pom in `find build/poms/%{name} -name pom.xml`; do
    sed 's/\${module-path}/${basedir}/g' "$pom" > "${pom##build/poms/%{name}/}"
done
%pom_disable_module src/test core
%pom_disable_module src/test codecs

popd

mv lucene/build/poms/pom.xml .

# deal with split packages in core/misc/analysis modules by adding additional metadata and
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
%pom_add_plugin org.apache.felix:maven-bundle-plugin lucene/analysis/common \
"<configuration><instructions>
<Require-Bundle>org.apache.lucene.core;bundle-version=\"%{version}\"</Require-Bundle>
<Export-Package>
 org.apache.lucene.analysis.standard;version=\"%{version}\";analysis=split;mandatory:=analysis,
 *;version=\"%{version}\"</Export-Package>
</instructions></configuration>"

%pom_disable_module solr
%pom_remove_plugin -r :gmaven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :forbiddenapis
%pom_remove_plugin -r :buildnumber-maven-plugin

# don't build modules for which deps are not in fedora or not new enough in fedora
pushd lucene
%pom_disable_module benchmark
%pom_disable_module demo
%pom_disable_module test-framework
%pom_disable_module facet
%pom_disable_module replicator
%pom_disable_module spatial-extras
%pom_disable_module spatial3d

%pom_disable_module opennlp analysis
%pom_disable_module morfologik analysis
popd

%if %{with jp_minimal}
pushd lucene
%pom_disable_module expressions
%pom_disable_module icu analysis
%pom_disable_module kuromoji analysis
%pom_disable_module phonetic analysis
%pom_disable_module stempel analysis
%pom_disable_module nori analysis
popd

%mvn_package :lucene-parent __noinstall
%mvn_package :lucene-solr-grandparent __noinstall
%endif

# Use compiler release flag when building on JDK >8 for correct cross-compiling
%pom_xpath_inject pom:profiles "
    <profile>
      <id>jdk-release-flag</id>
      <activation>
        <jdk>[9,)</jdk>
      </activation>
      <properties>
        <maven.compiler.release>\${java.compat.version}</maven.compiler.release>
      </properties>
    </profile>"

# For some reason TestHtmlParser.testTurkish fails when building inside SCLs
%mvn_build -s -f -- -Dcheckoutid=%{version}

%install
%mvn_install

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

%files -f .mfiles-%{name}-core
%doc lucene/CHANGES.txt lucene/README.txt
%doc lucene/MIGRATE.txt lucene/JRE_VERSION_MIGRATION.txt
%doc --no-dereference lucene/LICENSE.txt lucene/NOTICE.txt

%files analysis -f .mfiles-%{name}-analysis
%files analyzers-smartcn -f .mfiles-%{name}-analyzers-smartcn
%files grouping -f .mfiles-%{name}-grouping
%files highlighter -f .mfiles-%{name}-highlighter
%files join -f .mfiles-%{name}-join
%files memory -f .mfiles-%{name}-memory
%files misc -f .mfiles-%{name}-misc
%files queries -f .mfiles-%{name}-queries
%files queryparser -f .mfiles-%{name}-queryparser
%files sandbox -f .mfiles-%{name}-sandbox
%files backward-codecs -f .mfiles-%{name}-backward-codecs
%files codecs -f .mfiles-%{name}-codecs
%files classification -f .mfiles-%{name}-classification
%files suggest -f .mfiles-%{name}-suggest
%files monitor -f .mfiles-%{name}-monitor
%if %{without jp_minimal}
%files parent -f .mfiles-%{name}-parent
%files solr-grandparent -f .mfiles-%{name}-solr-grandparent
%files expressions -f .mfiles-%{name}-expressions
%files analyzers-phonetic -f .mfiles-%{name}-analyzers-phonetic
%files analyzers-icu -f .mfiles-%{name}-analyzers-icu
%files analyzers-nori -f .mfiles-%{name}-analyzers-nori
%files analyzers-kuromoji -f .mfiles-%{name}-analyzers-kuromoji
%files analyzers-stempel -f .mfiles-%{name}-analyzers-stempel
%endif

%files javadoc -f .mfiles-javadoc
%doc --no-dereference lucene/LICENSE.txt lucene/NOTICE.txt

%changelog
* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 0:8.8.2-alt1_1jpp11
- new version

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0:8.6.3-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:8.4.1-alt1_9jpp8
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:8.1.1-alt1_4jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0:7.7.0-alt1_1jpp8
- new version

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 0:7.1.0-alt1_3jpp8
- new version

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 0:6.1.0-alt3_7jpp8
- build with spatial4j0.5.0

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:6.1.0-alt2_7jpp8
- Build with randomizedtesting2.3.1-runner

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.1.0-alt1_7jpp8
- java update

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
