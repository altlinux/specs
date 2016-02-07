Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm)
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Summary:        High-performance, full-featured text search engine
Name:           lucene
Version:        5.3.0
Release:        alt1_1jpp8
Epoch:          0
License:        ASL 2.0
URL:            http://lucene.apache.org/
Source0:        http://www.apache.org/dist/lucene/java/%{version}/lucene-%{version}-src.tgz
#svn export http://svn.apache.org/repos/asf/lucene/dev/tags/lucene_solr_5_3_0/dev-tools/
#tar caf dev-tools-5.3.0.tar.xz dev-tools/
Source4:        dev-tools-%{version}.tar.xz

Patch0:         0001-disable-ivy-settings.patch
Patch1:         0001-dependency-generation.patch

BuildRequires:  git
BuildRequires:  ant
BuildRequires:  ivy-local
BuildRequires:  icu4j
BuildRequires:  httpcomponents-client
BuildRequires:  jetty-continuation
BuildRequires:  jetty-http
BuildRequires:  jetty-io
BuildRequires:  jetty-server
BuildRequires:  jetty-servlet
BuildRequires:  jetty-util
BuildRequires:  morfologik-stemming
BuildRequires:  uimaj
BuildRequires:  uima-addons
BuildRequires:  spatial4j
BuildRequires:  nekohtml
BuildRequires:  xerces-j2
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  maven-local
BuildRequires:  apache-parent
BuildRequires:  forbidden-apis

# test-framework deps
BuildRequires:  junit
BuildRequires:  randomizedtesting-junit4-ant
BuildRequires:  randomizedtesting-runner

Provides:       %{name}-core = %{epoch}:%{version}-%{release}
# previously used by eclipse but no longer needed
Obsoletes:      %{name}-devel < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-demo  < %{epoch}:%{version}-%{release}
# previously distributed separately, but merged into main package
Provides:       %{name}-contrib = %{version}-%{release}
Obsoletes:      %{name}-contrib < %{version}-%{release}

BuildArch:      noarch
Source44: import.info

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

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

%package analysis
Group: Development/Java
Summary:      Lucene Common Analyzers

%description analysis
Lucene Common Analyzers.

%package sandbox
Group: Development/Java
Summary:      Lucene Sandbox Module

%description sandbox
Lucene Sandbox Module.

%package queries
Group: Development/Java
Summary:      Lucene Queries Module

%description queries
Lucene Queries Module.

%package spatial
Group: Development/Java
Summary:      Spatial Strategies for Apache Lucene

%description spatial
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


%package javadoc
Group: Development/Java
Summary:        Javadoc for Lucene
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

# dependency generator expects that the directory name is just lucene
mkdir %{name}
find -maxdepth 1 ! -name CHANGES.txt ! -name LICENSE.txt ! -name README.txt \
    ! -name NOTICE.txt ! -name MIGRATE.txt  ! -name ivy-settings.xml \
    ! -path %{name} -exec mv \{} %{name}/ \;

tar xf %{SOURCE4}
pushd dev-tools/maven
sed -i -e "s|/Export-Package>|/Export-Package><_nouses>true</_nouses>|g" pom.xml.template
popd

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%mvn_package ":%{name}-analysis-modules-aggregator" %{name}-analysis
%mvn_package ":%{name}-analyzers-common" %{name}-analysis
%mvn_package ":{*}-aggregator" @1

%build
pushd %{name}
# generate dependencies
ant filter-pom-templates -Divy.mode=local -Dversion=%{version}

# fix source dir + move to expected place
for pom in `find build/poms/%{name} -name pom.xml`; do
    sed 's/\${module-path}/${basedir}/g' "$pom" > "${pom##build/poms/%{name}/}"
done
%pom_remove_plugin :forbiddenapis
for module in test-framework; do
    %pom_remove_plugin :forbiddenapis ${module}
done

%pom_disable_module src/test core
%pom_disable_module src/test codecs

# test deps
%pom_add_dep org.ow2.asm:asm::test demo
%pom_add_dep org.ow2.asm:asm-commons::test demo
%pom_add_dep org.antlr:antlr-runtime::test demo

popd

mv lucene/build/poms/pom.xml .

%pom_disable_module solr
%pom_remove_plugin :gmaven-plugin
%pom_remove_plugin :forbiddenapis
%pom_remove_plugin :maven-enforcer-plugin

# For some reason TestHtmlParser.testTurkish fails when building inside SCLs
%mvn_build -s -f

%install
# suggest provides spellchecker
%mvn_alias :%{name}-suggest :%{name}-spellchecker

# compatibility with existing packages
%mvn_alias :%{name}-analyzers-common :%{name}-analyzers

%mvn_install

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

%files -f .mfiles-%{name}-core
%dir %{_javadir}/%{name}
%doc CHANGES.txt README.txt MIGRATE.txt
%doc LICENSE.txt NOTICE.txt

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
%files analysis -f .mfiles-%{name}-analysis
%files sandbox -f .mfiles-%{name}-sandbox
%files queries -f .mfiles-%{name}-queries
%files spatial -f .mfiles-%{name}-spatial
%files spatial3d -f .mfiles-%{name}-spatial3d
%files codecs -f .mfiles-%{name}-codecs
%files queryparser -f .mfiles-%{name}-queryparser
%files analyzers-smartcn -f .mfiles-%{name}-analyzers-smartcn
%files analyzers-phonetic -f .mfiles-%{name}-analyzers-phonetic
%files analyzers-icu -f .mfiles-%{name}-analyzers-icu
%files analyzers-morfologik -f .mfiles-%{name}-analyzers-morfologik
%files analyzers-uima -f .mfiles-%{name}-analyzers-uima
%files analyzers-kuromoji -f .mfiles-%{name}-analyzers-kuromoji
%files analyzers-stempel -f .mfiles-%{name}-analyzers-stempel

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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
