Name:    lucene
Version: 10.4.0
Release: alt1
Summary: High-performance, full-featured text search engine
License: Apache-2.0 AND MIT AND BSD-3-Clause AND BSD-2-Clause
Group: Development/Java
URL: http://lucene.apache.org/

Source0: %name-%version-src.tgz
Source1: aggregator.pom
Source2: aggregator-analysis.pom

Source3:  https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-common/%{version}/lucene-analysis-common-%{version}.pom
Source4:  https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-icu/%{version}/lucene-analysis-icu-%{version}.pom
Source5:  https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-kuromoji/%{version}/lucene-analysis-kuromoji-%{version}.pom
Source6:  https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-morfologik/%{version}/lucene-analysis-morfologik-%{version}.pom
Source7:  https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-nori/%{version}/lucene-analysis-nori-%{version}.pom
Source8:  https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-opennlp/%{version}/lucene-analysis-opennlp-%{version}.pom
Source9:  https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-phonetic/%{version}/lucene-analysis-phonetic-%{version}.pom
Source10: https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-smartcn/%{version}/lucene-analysis-smartcn-%{version}.pom
Source11: https://repo1.maven.org/maven2/org/apache/lucene/lucene-analysis-stempel/%{version}/lucene-analysis-stempel-%{version}.pom

Source12: https://repo1.maven.org/maven2/org/apache/lucene/lucene-backward-codecs/%{version}/lucene-backward-codecs-%{version}.pom
Source13: https://repo1.maven.org/maven2/org/apache/lucene/lucene-benchmark/%{version}/lucene-benchmark-%{version}.pom
Source14: https://repo1.maven.org/maven2/org/apache/lucene/lucene-classification/%{version}/lucene-classification-%{version}.pom
Source15: https://repo1.maven.org/maven2/org/apache/lucene/lucene-codecs/%{version}/lucene-codecs-%{version}.pom
Source16: https://repo1.maven.org/maven2/org/apache/lucene/lucene-core/%{version}/lucene-core-%{version}.pom
Source17: https://repo1.maven.org/maven2/org/apache/lucene/lucene-demo/%{version}/lucene-demo-%{version}.pom
Source18: https://repo1.maven.org/maven2/org/apache/lucene/lucene-expressions/%{version}/lucene-expressions-%{version}.pom
Source19: https://repo1.maven.org/maven2/org/apache/lucene/lucene-facet/%{version}/lucene-facet-%{version}.pom
Source20: https://repo1.maven.org/maven2/org/apache/lucene/lucene-grouping/%{version}/lucene-grouping-%{version}.pom
Source21: https://repo1.maven.org/maven2/org/apache/lucene/lucene-highlighter/%{version}/lucene-highlighter-%{version}.pom
Source22: https://repo1.maven.org/maven2/org/apache/lucene/lucene-join/%{version}/lucene-join-%{version}.pom
Source23: https://repo1.maven.org/maven2/org/apache/lucene/lucene-luke/%{version}/lucene-luke-%{version}.pom
Source24: https://repo1.maven.org/maven2/org/apache/lucene/lucene-memory/%{version}/lucene-memory-%{version}.pom
Source25: https://repo1.maven.org/maven2/org/apache/lucene/lucene-misc/%{version}/lucene-misc-%{version}.pom
Source26: https://repo1.maven.org/maven2/org/apache/lucene/lucene-monitor/%{version}/lucene-monitor-%{version}.pom
Source27: https://repo1.maven.org/maven2/org/apache/lucene/lucene-queries/%{version}/lucene-queries-%{version}.pom
Source28: https://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/%{version}/lucene-queryparser-%{version}.pom
Source29: https://repo1.maven.org/maven2/org/apache/lucene/lucene-replicator/%{version}/lucene-replicator-%{version}.pom
Source30: https://repo1.maven.org/maven2/org/apache/lucene/lucene-sandbox/%{version}/lucene-sandbox-%{version}.pom
Source31: https://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial3d/%{version}/lucene-spatial3d-%{version}.pom
Source32: https://repo1.maven.org/maven2/org/apache/lucene/lucene-suggest/%{version}/lucene-suggest-%{version}.pom

ExcludeArch: %ix86 armh

BuildRequires(pre): rpm-build-java
BuildRequires(pre): maven-local
BuildRequires: /proc java-devel
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(org.antlr:antlr4-runtime)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)

AutoReq: yes,noosgi

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package analysis-common
Summary: Lucene module: analysis-common
Group: Development/Java
Obsoletes: %{name}-analysis < %EVR
Provides: %{name}-analysis = %EVR

%description analysis-common
%{summary}.

%package analysis-icu
Summary: Lucene module: analysis-icu
Group: Development/Java
Obsoletes: %{name}-analyzers-icu < %EVR
Provides: %{name}-analyzers-icu = %EVR

%description analysis-icu
%{summary}.

%package analysis-kuromoji
Summary: Lucene module: analysis-kuromoji
Group: Development/Java
Obsoletes: %{name}-analyzers-kuromoji < %EVR
Provides: %{name}-analyzers-kuromoji = %EVR

%description analysis-kuromoji
%{summary}.

%package analysis-nori
Summary: Lucene module: analysis-nori
Group: Development/Java
Obsoletes: %{name}-analyzers-nori < %EVR
Provides: %{name}-analyzers-nori = %EVR

%description analysis-nori
%{summary}.

%package analysis-phonetic
Summary: Lucene module: analysis-phonetic
Group: Development/Java
Obsoletes: %{name}-analyzers-phonetic < %EVR
Provides: %{name}-analyzers-phonetic = %EVR

%description analysis-phonetic
%{summary}.

%package analysis-smartcn
Summary: Lucene module: analysis-smartcn
Group: Development/Java
Obsoletes: %{name}-analyzers-smartcn < %EVR
Provides: %{name}-analyzers-smartcn = %EVR

%description analysis-smartcn
%{summary}.

%package analysis-stempel
Summary: Lucene module: analysis-stempel
Group: Development/Java
Obsoletes: %{name}-analyzers-stempel < %EVR
Provides: %{name}-analyzers-stempel = %EVR

%description analysis-stempel
%{summary}.

%package backward-codecs
Summary: Lucene module: backward-codecs
Group: Development/Java

%description backward-codecs
%{summary}.

%package classification
Summary: Lucene module: classification
Group: Development/Java

%description classification
%{summary}.

%package codecs
Summary: Lucene module: codecs
Group: Development/Java

%description codecs
%{summary}.

%package core
Summary: Lucene module: core
Group: Development/Java
Provides: lucene = %EVR
Obsoletes: lucene < %EVR

%description core
%{summary}.

%package expressions
Summary: Lucene module: expressions
Group: Development/Java

%description expressions
%{summary}.

%package facet
Summary: Lucene module: facet
Group: Development/Java

%description facet
%{summary}.

%package grouping
Summary: Lucene module: grouping
Group: Development/Java

%description grouping
%{summary}.

%package highlighter
Summary: Lucene module: highlighter
Group: Development/Java

%description highlighter
%{summary}.

%package join
Summary: Lucene module: join
Group: Development/Java

%description join
%{summary}.

%package memory
Summary: Lucene module: memory
Group: Development/Java

%description memory
%{summary}.

%package misc
Summary: Lucene module: misc
Group: Development/Java

%description misc
%{summary}.

%package monitor
Summary: Lucene module: monitor
Group: Development/Java

%description monitor
%{summary}.

%package queries
Summary: Lucene module: queries
Group: Development/Java

%description queries
%{summary}.

%package queryparser
Summary: Lucene module: queryparser
Group: Development/Java

%description queryparser
%{summary}.

%package sandbox
Summary: Lucene module: sandbox
Group: Development/Java

%description sandbox
%{summary}.

%package spatial3d
Summary: Lucene module: spatial3d
Group: Development/Java

%description spatial3d
%{summary}.

%package suggest
Summary: Lucene module: suggest
Group: Development/Java

%description suggest
%{summary}.

%prep
%setup
find -mindepth 1 -maxdepth 1 ! -name lucene ! -name LICENSE.txt ! -name NOTICE.txt ! -name README.md -exec rm -rf {} +
mv -t . lucene/*
rmdir lucene

cp %SOURCE1 pom.xml
for source in $(ls -1 %_sourcedir/lucene-*.pom | grep -v 'lucene-analysis-.*\.pom'); do
  module=${source##*/lucene-}
  module=${module%%%%-%{version}.pom}
  cp ${source} ${module}/pom.xml
  %pom_add_parent org.fedoraproject.xmvn.lucene:aggregator:any ${module}
  %pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" "compile" ${module}
done

pushd analysis
cp %SOURCE2 pom.xml
%pom_add_parent org.fedoraproject.xmvn.lucene:aggregator:any

for source in %_sourcedir/lucene-analysis-*.pom; do
  module=${source##*/lucene-analysis-}
  module=${module%%%%-%{version}.pom}
  cp ${source} ${module}/pom.xml
  %pom_add_parent org.fedoraproject.xmvn.lucene:aggregator-analysis:any ${module}
done
popd

%pom_disable_module benchmark
%pom_disable_module demo
%pom_disable_module luke
%pom_disable_module replicator
%pom_disable_module test-framework

%pom_disable_module morfologik analysis
%pom_disable_module opennlp analysis

%mvn_package :aggregator __noinstall
%mvn_package :aggregator-analysis __noinstall

%build
%mvn_build -s -f -j

%install
%mvn_install

%files analysis-common -f .mfiles-lucene-analysis-common
%files analysis-icu -f .mfiles-lucene-analysis-icu
%files analysis-kuromoji -f .mfiles-lucene-analysis-kuromoji
%files analysis-nori -f .mfiles-lucene-analysis-nori
%files analysis-phonetic -f .mfiles-lucene-analysis-phonetic
%files analysis-smartcn -f .mfiles-lucene-analysis-smartcn
%files analysis-stempel -f .mfiles-lucene-analysis-stempel
%files backward-codecs -f .mfiles-lucene-backward-codecs
%files classification -f .mfiles-lucene-classification
%files codecs -f .mfiles-lucene-codecs

# core is a common dependency of all other modules
%files core -f .mfiles-lucene-core
%doc LICENSE.txt NOTICE.txt README.md

%files expressions -f .mfiles-lucene-expressions
%files facet -f .mfiles-lucene-facet
%files grouping -f .mfiles-lucene-grouping
%files highlighter -f .mfiles-lucene-highlighter
%files join -f .mfiles-lucene-join
%files memory -f .mfiles-lucene-memory
%files misc -f .mfiles-lucene-misc
%files monitor -f .mfiles-lucene-monitor
%files queries -f .mfiles-lucene-queries
%files queryparser -f .mfiles-lucene-queryparser
%files sandbox -f .mfiles-lucene-sandbox
%files spatial3d -f .mfiles-lucene-spatial3d
%files suggest -f .mfiles-lucene-suggest

%changelog
* Mon Mar 30 2026 Andrey Cherepanov <cas@altlinux.org> 10.4.0-alt1
- New version (fixes: CVE-2024-43383, CVE-2024-45772).

* Sat Jul 19 2025 Andrey Cherepanov <cas@altlinux.org> 10.2.2-alt1
- New version

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
