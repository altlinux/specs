Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash b8565e1faa39c4eb8841902cf65a1615f5a933d7
Name:          annox
Version:       1.0.1
Release:       alt1_2jpp8
Summary:       Java annotations in XML resources
License:       BSD
Url:           http://java.net/projects/annox
# https://svn.java.net/svn/annox~svn/tags/
Source0:       https://github.com/highsource/annox/archive/%{githash}/%{name}-%{githash}.tar.gz
# from http://confluence.highsource.org/display/ANX/License
# annox package don't include the license file
# but annox developers allowed us to redistribute their
# work only if we include this notice. So we HAVE TO include these notices.
# https://github.com/highsource/annox/issues/3
Source1:       annox-LICENSE

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.javaparser:javaparser)
BuildRequires: mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.hibernate:hibernate-search-engine)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Annox is an open source project which allows you to
read arbitrary Java annotations from XML resources.
JAXB users may be interested in Annox annotation
reader for JAXB RI which allows you to define JAXB 
Java/XML mappings in XML resources (instead of
annotations).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}
# Cleanup
find -name "*.bat" -print -delete
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

%pom_disable_module samples

%pom_remove_plugin :maven-deploy-plugin

%pom_change_dep :ant-optional org.apache.ant:ant

%pom_xpath_set "pom:dependency[pom:artifactId = 'tools' ]/pom:groupId" com.sun
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools' ]/pom:scope"
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools' ]/pom:systemPath"

%pom_change_dep -r :hibernate-search :hibernate-search-engine
sed -i "s|org.hibernate.search.annotations.Field(index=TOKENIZED, store=NO|org.hibernate.search.annotations.Field(store=NO|" \
 core/src/test/java/org/jvnet/annox/parser/tests/XAnnotationParserTest.java
sed -i '/TOKENIZED/d' core/src/test/resources/org/jvnet/annox/parser/tests/field.xml

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%mvn_file :%{name} %{name}

%build

# unavailable deps for run test: org.hibernate hibernate-search 3.0.0.GA
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_3jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_2jpp7
- fc build

