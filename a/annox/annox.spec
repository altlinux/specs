Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          annox
Version:       0.5.0
Release:       alt2_11jpp8
Summary:       Java annotations in XML resources
License:       BSD
Url:           http://java.net/projects/annox
# svn export https://svn.java.net/svn/annox~svn/tags/0.5.0 annox-0.5.0
# tar czf annox-0.5.0-src-svn.tar.gz annox-0.5.0
Source0:       annox-0.5.0-src-svn.tar.gz
# from http://confluence.highsource.org/display/ANX/License
# annox package don't include the license file
# but annox developers allowed us to redistribute their
# work only if we include this notice. So we HAVE TO include these notices.
Source1:       annox-LICENSE

BuildRequires: ant
BuildRequires: apache-commons-lang
BuildRequires: glassfish-jaxb
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: sonatype-oss-parent

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
%setup -q
find \( -name '*.jar' -o -name '*.class' -o -name '*.bat' \) -exec rm -f '{}' \;

%pom_disable_module samples

%pom_xpath_remove "pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-antrun-plugin']/pom:dependencies/pom:dependency[pom:artifactId='ant-optional']"
%pom_xpath_inject "pom:project/pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId='maven-antrun-plugin']/pom:dependencies" "
<dependency>
  <groupId>org.apache.ant</groupId>
  <artifactId>ant</artifactId>
  <version>1.8.2</version>
</dependency>"

%pom_remove_dep org.hibernate:hibernate-search
%pom_remove_dep org.hibernate:hibernate-search core

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%mvn_file :%{name} %{name}

%build

# unavailable deps for run test: org.hibernate hibernate-search 3.0.0.GA
%mvn_build -f
  
%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
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

