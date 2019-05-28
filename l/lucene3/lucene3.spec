Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm) rpm-build-java unzip zip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:        High-performance, full-featured text search engine
Name:           lucene3
Version:        3.6.2
Release:        alt2_16jpp8
Epoch:          0
License:        ASL 2.0 and BSD
URL:            http://lucene.apache.org/
Source0:        https://archive.apache.org/dist/lucene/java/%{version}/lucene-%{version}-src.tgz
Source1:        lucene-%{version}-core-OSGi-MANIFEST.MF
Source2:        lucene-%{version}-analysis-OSGi-MANIFEST.MF

# DictionaryBasedBreakIterator was moved into the base RuleBasedBreakIterator
# in icu4j. v49 => v50
Patch0:         lucene_contrib_icu4j_v50.patch
# Add hamcrest-core in classpath
# Disable doclint in javadoc task
Patch1:         lucene-3.6.2-hamcrest-core.patch
# javascript not allowed in javadoc
Patch2:         lucene-3.6.2-javascript.patch
# Fix build errors in test-framework
Patch3:         test-framework.patch
#svn export http://svn.apache.org/repos/asf/lucene/dev/tags/lucene_solr_3_6_2/dev-tools@r1450168
#tar caf dev-tools.tar.xz dev-tools/
Source4:        dev-tools.tar.xz

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-digester
BuildRequires:  apache-ivy
BuildRequires:  apache-parent
BuildRequires:  hamcrest-core
BuildRequires:  icu4j
BuildRequires:  ivy-local
BuildRequires:  javacc
BuildRequires:  java-javadoc
BuildRequires:  jtidy
BuildRequires:  junit
BuildRequires:  lucene3
BuildRequires:  regexp
BuildRequires:  xerces-j2

# for tests
BuildRequires:  subversion subversion-server-common

BuildArch:      noarch
Source44: import.info

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%package contrib
Group: Development/Java
Summary:        Lucene contributed extensions
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description contrib
%{summary}.

%package javadoc
Group: Development/Java
Summary:        Javadoc for Lucene
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n lucene-%{version}
# remove all binary libs
find . -name "*.jar" -delete

tar xfs %{SOURCE4}
pushd dev-tools
find . -name "pom.xml.template" -exec sed -i "s/@version@/%{version}/g" '{}' \;
popd

iconv --from=ISO-8859-1 --to=UTF-8 CHANGES.txt > CHANGES.txt.new

# prepare pom files (replace @version@ with real version)
find . -name '*pom.xml.template' -exec \
              sed -i "s:@version@:%{version}:g" '{}' \;

# must specify exact version for compat package deps
sed -i -e "s|3.5.0|3.6.2|g" backwards/ivy.xml

%patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
mkdir -p docs
mkdir -p lib
export OPT_JAR_LIST="ant/ant-junit junit hamcrest/core"

export CLASSPATH=$(build-classpath jtidy regexp commons-codec commons-digester commons-compress icu4j ivy xmvn)
ant -Divy.mode=local -Dbuild.sysclasspath=first \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=file://%{_javadocdir}/java \
  -Dversion=%{version} \
  -Dfailonjavadocwarning=false \
  -Dmaven-tasks.uptodate=true \
  -Djavac.source=1.6 \
  -Djavac.target=1.6 \
  -Djavac.source.backwards=1.6 \
  -Djavac.target.backwards=1.6 \
  jar-lucene-core jar-test-framework docs javadocs build-contrib

# add missing OSGi metadata to manifests
mkdir META-INF
unzip -o build/core/lucene-core-%{version}.jar META-INF/MANIFEST.MF
cp %{SOURCE1} META-INF/MANIFEST.MF
sed -i '/^\r$/d' META-INF/MANIFEST.MF
zip build/core/lucene-core-%{version}.jar META-INF/MANIFEST.MF

unzip -o build/contrib/analyzers/common/lucene-analyzers-%{version}.jar META-INF/MANIFEST.MF
cp %{SOURCE2} META-INF/MANIFEST.MF
sed -i '/^\r$/d' META-INF/MANIFEST.MF
zip build/contrib/analyzers/common/lucene-analyzers-%{version}.jar META-INF/MANIFEST.MF

mv build/contrib/analyzers/common build/contrib/analyzers/analyzers
mv dev-tools/maven/lucene/contrib/analyzers/common dev-tools/maven/lucene/contrib/analyzers/analyzers

# Core
sed -i -e '/relativePath/d' dev-tools/maven/pom.xml.template
%mvn_artifact dev-tools/maven/pom.xml.template
%mvn_artifact dev-tools/maven/lucene/pom.xml.template
%mvn_artifact dev-tools/maven/lucene/core/pom.xml.template build/core/lucene-core-%{version}.jar

# Contrib
%mvn_artifact dev-tools/maven/lucene/contrib/pom.xml.template
%mvn_package :lucene-contrib-aggregator contrib
for c in benchmark demo facet grouping highlighter icu instantiated join \
         memory misc pruning queries queryparser remote spatial spellchecker xml-query-parser ; do
  %mvn_artifact dev-tools/maven/lucene/contrib/$c/pom.xml.template build/contrib/$c/lucene-${c}-%{version}.jar
  %mvn_package :lucene-${c} contrib
done
for c in analyzers kuromoji phonetic smartcn stempel ; do
  %mvn_artifact dev-tools/maven/lucene/contrib/analyzers/$c/pom.xml.template build/contrib/analyzers/$c/lucene-${c}-%{version}.jar
  %mvn_package :lucene-${c} contrib
done

# Compat versions
%mvn_compat_version : 3 3.6.2

%install
%mvn_install -J build/docs/api

%files -f .mfiles
%doc CHANGES.txt README.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%files contrib -f .mfiles-contrib
%doc contrib/CHANGES.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt2_16jpp8
- new version

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt2_13jpp8
- fixed build with new ant

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_12jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_8jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_7jpp8
- unbootsrap build

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

