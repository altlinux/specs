Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ perl(LWP/UserAgent.pm) unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
%global majorversion 3

Summary:        High-performance, full-featured text search engine
Name:           lucene3
Version:        3.6.2
Release:        alt1_8jpp8
Epoch:          0
License:        ASL 2.0 and BSD
URL:            http://lucene.apache.org/
Source0:        https://archive.apache.org/dist/lucene/java/%{version}/lucene-%{version}-src.tgz
Source1:        lucene-%{version}-core-OSGi-MANIFEST.MF
Source2:        lucene-%{version}-analysis-OSGi-MANIFEST.MF
Source3:        ivy-conf.xml
# DictionaryBasedBreakIterator was moved into the base RuleBasedBreakIterator
# in icu4j. v49 => v50
Patch0:         lucene_contrib_icu4j_v50.patch
# Add hamcrest-core in classpath
# Disable doclint in javadoc task
Patch1:         lucene-3.6.2-hamcrest-core.patch
#svn export http://svn.apache.org/repos/asf/lucene/dev/tags/lucene_solr_3_6_2/dev-tools@r1450168
#tar caf dev-tools.tar.xz dev-tools/
Source4:        dev-tools.tar.xz

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  junit
BuildRequires:  javacc
BuildRequires:  java-javadoc
BuildRequires:  jtidy
BuildRequires:  regexp
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-compress
BuildRequires:  apache-ivy
BuildRequires:  lucene
BuildRequires:  apache-commons-codec

# for tests
BuildRequires: subversion subversion-server-common
BuildRequires:  hamcrest-core

%if 0%{?fedora}
BuildRequires:  icu4j
%endif

BuildArch:      noarch

Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
Apache Lucene is a high-performance, full-featured text search
engine library written entirely in Java. It is a technology suitable
for nearly any application that requires full-text search, especially
cross-platform.

%if 0%{?fedora}
%package contrib
Group: Development/Java
Summary:        Lucene contributed extensions
Requires:       %{name} = %{epoch}:%{version}

%description contrib
%{summary}.
%endif

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

cp %{SOURCE3} .

#modify artifactIds to make it easier to map to fedora
sed -i -e "s|ant-junit|ant/ant-junit|g" test-framework/ivy.xml
sed -i -e "s|xercesImpl|xerces-j2|g" contrib/benchmark/ivy.xml
sed -i -e "s|jakarta-regexp|regexp|g" contrib/queries/ivy.xml
sed -i -e "s|lucene-core|lucene/lucene-core|g" backwards/ivy.xml
sed -i -e "s|icu4j|icu4j/icu4j|g" contrib/icu/ivy.xml

# ICU4J v50 compatibility
%patch0 -p2
%patch1 -p1

%build
mkdir -p docs
mkdir -p lib
export OPT_JAR_LIST="ant/ant-junit junit hamcrest/core"
export CLASSPATH=$(build-classpath jtidy regexp commons-digester apache-commons-compress ivy)

ant -Divy.settings.file=ivy-conf.xml -Dbuild.sysclasspath=first \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=file://%{_javadocdir}/java \
  -Dversion=%{version} \
  -Dfailonjavadocwarning=false \
  -Dmaven-tasks.uptodate=true \
  -Djavac.source=1.6 \
  -Djavac.target=1.6 \
  jar-lucene-core docs javadocs-core

%if 0%{?fedora}
export CLASSPATH=$(build-classpath jtidy regexp commons-digester apache-commons-compress icu4j ivy)
ant -Divy.settings.file=ivy-conf.xml -Dbuild.sysclasspath=first \
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
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 0644 build/core/lucene-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/lucene-core.jar

install -pm 0644 dev-tools/maven/lucene/core/pom.xml.template $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-lucene-core.pom
%add_maven_depmap JPP.%{name}-lucene-core.pom %{name}/lucene-core.jar -v "%{majorversion},%{version}"

install -pm 0644 dev-tools/maven/lucene/pom.xml.template $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-lucene-parent.pom
%add_maven_depmap JPP.%{name}-lucene-parent.pom -v "%{majorversion},%{version}"

install -pm 0644 dev-tools/maven/pom.xml.template $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-solr-grandparent.pom
%add_maven_depmap JPP.%{name}-solr-grandparent.pom -v "%{majorversion},%{version}"

%if 0%{?fedora}
# contrib jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib

for c in benchmark demo facet grouping highlighter \
         icu instantiated join memory misc pruning queries queryparser remote \
         spatial spellchecker xml-query-parser; do
    install -pm 0644 build/contrib/$c/lucene-${c}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib/lucene-${c}.jar
    install -pm 0644 dev-tools/maven/lucene/contrib/$c/pom.xml.template $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-contrib-lucene-$c.pom
    %add_maven_depmap JPP.%{name}-contrib-lucene-$c.pom %{name}-contrib/lucene-${c}.jar -v "%{majorversion},%{version}"
done

# contrib analyzers
for c in analyzers kuromoji phonetic smartcn stempel; do
    install -pm 0644 build/contrib/analyzers/$c/lucene-${c}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib/lucene-${c}.jar

    install -pm 0644 dev-tools/maven/lucene/contrib/analyzers/$c/pom.xml.template $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-contrib-lucene-$c.pom
    %add_maven_depmap JPP.%{name}-contrib-lucene-$c.pom %{name}-contrib/lucene-${c}.jar -v "%{majorversion},%{version}"
done

# contrib pom
install -pm 0644 dev-tools/maven/lucene/contrib/pom.xml.template $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-lucene-contrib.pom
%add_maven_depmap JPP.%{name}-lucene-contrib.pom -v "%{majorversion},%{version}"
%endif

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc CHANGES.txt LICENSE.txt README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%if 0%{?fedora}
%files contrib
%{_javadir}/%{name}-contrib
%doc contrib/CHANGES.txt
%doc LICENSE.txt NOTICE.txt
%endif

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_8jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt1_7jpp8
- unbootsrap build

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.6.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

