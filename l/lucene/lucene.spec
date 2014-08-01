# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm)
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
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
Version:        3.6.2
Release:        alt1_2jpp7
Epoch:          0
License:        ASL 2.0
URL:            http://lucene.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/lucene/java/%{version}/%{name}-%{version}-src.tgz
Source1:        lucene-%{version}-core-OSGi-MANIFEST.MF
Source2:        lucene-%{version}-analysis-OSGi-MANIFEST.MF
Source3:        ivy-conf.xml
# DictionaryBasedBreakIterator was moved into the base RuleBasedBreakIterator
# in icu4j. v49 => v50
Patch0:         lucene_contrib_icu4j_v50.patch
#svn export http://svn.apache.org/repos/asf/lucene/dev/tags/lucene_solr_3_6_2/dev-tools@r1450168
#tar caf dev-tools.tar.xz dev-tools/
Source4:        dev-tools.tar.xz
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  junit
BuildRequires:  javacc
BuildRequires:  java-javadoc
BuildRequires:  jline
BuildRequires:  jtidy
BuildRequires:  regexp
BuildRequires:  apache-commons-digester
BuildRequires:  unzip
BuildRequires:  zip
BuildRequires:  apache-commons-compress
BuildRequires:  apache-ivy
BuildRequires:  lucene
# for tests
BuildRequires:  subversion
# BR for lucene-contrib
%if 0%{?fedora}
BuildRequires:  icu4j
%endif

Provides:       lucene-core = %{epoch}:%{version}-%{release}
# previously used by eclipse but no longer needed
Obsoletes:      lucene-devel < %{epoch}:%{version}-%{release}
Obsoletes:      lucene-demo < %{epoch}:%{version}-%{release}
BuildArch:      noarch

Requires:       jpackage-utils
Source44: import.info

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package javadoc
Summary:        Javadoc for Lucene
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if 0%{?fedora}
%package contrib
Summary:        Lucene contributed extensions
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description contrib
%{summary}.
%endif

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

tar xfs %{SOURCE4}
pushd dev-tools
find . -name "pom.xml.template" -exec sed -i "s/@version@/%{version}/g" '{}' \;
popd

iconv --from=ISO-8859-1 --to=UTF-8 CHANGES.txt > CHANGES.txt.new

# prepare pom files (replace @version@ with real version)
find . -name '*pom.xml.template' -exec \
              sed -i "s:@version@:%{version}:g" '{}' \;

cp %{SOURCE3} .

#modify artifactIds to make it easier to map to fedora
sed -i -e "s|ant-junit|ant/ant-junit|g" test-framework/ivy.xml
sed -i -e "s|xercesImpl|xerces-j2|g" contrib/benchmark/ivy.xml
sed -i -e "s|jakarta-regexp|regexp|g" contrib/queries/ivy.xml

# ICU4J v50 compatibility
%patch0 -p2

%build
mkdir -p docs
mkdir -p lib
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath jline jtidy regexp commons-digester apache-commons-compress ivy)


ant -Divy.settings.file=ivy-conf.xml -Dbuild.sysclasspath=first \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=file://%{_javadocdir}/java \
  -Dversion=%{version} \
  -Dfailonjavadocwarning=false \
  -Dmaven-tasks.uptodate=true \
  jar-lucene-core docs javadocs-core

%if 0%{?fedora}
export CLASSPATH=$(build-classpath jline jtidy regexp commons-digester apache-commons-compress icu4j ivy)
ant -Divy.settings.file=ivy-conf.xml -Dbuild.sysclasspath=first \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=file://%{_javadocdir}/java \
  -Dversion=%{version} \
  -Dfailonjavadocwarning=false \
  -Dmaven-tasks.uptodate=true \
  jar-test-framework javadocs build-contrib
%endif
    
# add missing OSGi metadata to manifests
mkdir META-INF
unzip -o build/core/lucene-core-%{version}.jar META-INF/MANIFEST.MF
cp %{SOURCE1} META-INF/MANIFEST.MF
sed -i '/^\r$/d' META-INF/MANIFEST.MF
zip -u build/core/lucene-core-%{version}.jar META-INF/MANIFEST.MF

%if 0%{?fedora}
unzip -o build/contrib/analyzers/common/lucene-analyzers-%{version}.jar META-INF/MANIFEST.MF
cp %{SOURCE2} META-INF/MANIFEST.MF
sed -i '/^\r$/d' META-INF/MANIFEST.MF
zip -u build/contrib/analyzers/common/lucene-analyzers-%{version}.jar META-INF/MANIFEST.MF

mv build/contrib/analyzers/common build/contrib/analyzers/analyzers
mv dev-tools/maven/lucene/contrib/analyzers/common dev-tools/maven/lucene/contrib/analyzers/analyzers
%endif

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 0644 build/core/%{name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core.jar

# core pom + parents
install -m 0644 dev-tools/maven/lucene/core/pom.xml.template \
           $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-lucene-core.pom
%add_maven_depmap JPP-lucene-core.pom %{name}-core.jar
install -m 0644 dev-tools/maven/lucene/pom.xml.template \
       $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-lucene-parent.pom
%add_maven_depmap JPP-lucene-parent.pom
install -m 0644 dev-tools/maven/pom.xml.template \
       $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-lucene-solr-grandparent.pom
%add_maven_depmap JPP-lucene-solr-grandparent.pom

%if 0%{?fedora}
# contrib jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib
for c in benchmark demo facet grouping highlighter \
         icu instantiated join memory misc pruning queries queryparser remote \
         spatial spellchecker xml-query-parser; do
    install -m 0644 build/contrib/$c/%{name}-${c}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib/%{name}-${c}.jar

    install -m 0644 dev-tools/maven/lucene/contrib/$c/pom.xml.template \
               $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.lucene-contrib-lucene-$c.pom
    %add_maven_depmap JPP.lucene-contrib-lucene-$c.pom %{name}-contrib/%{name}-${c}.jar
done

# contrib analyzers
for c in analyzers kuromoji phonetic smartcn stempel; do
    install -m 0644 build/contrib/analyzers/$c/%{name}-${c}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib/%{name}-${c}.jar

    install -m 0644 dev-tools/maven/lucene/contrib/analyzers/$c/pom.xml.template \
               $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.lucene-contrib-lucene-$c.pom
    %add_maven_depmap JPP.lucene-contrib-lucene-$c.pom %{name}-contrib/%{name}-${c}.jar
done

# contrib pom
install -m 0644 dev-tools/maven/lucene/contrib/pom.xml.template \
       $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-lucene-contrib.pom
%add_maven_depmap JPP-lucene-contrib.pom
%endif

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/docs/api/* \
  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc CHANGES.txt LICENSE.txt README.txt NOTICE.txt
%{_mavenpomdir}/JPP*pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-core.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%if 0%{?fedora}
%files contrib
%{_javadir}/%{name}-contrib
%doc contrib/CHANGES.txt
%endif

%changelog
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
