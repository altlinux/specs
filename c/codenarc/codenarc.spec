Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global oname CodeNarc
Name:          codenarc
Version:       0.24.1
Release:       alt1_4jpp8
Summary:       Groovy library that provides static analysis features for Groovy code
License:       ASL 2.0
Url:           http://codenarc.sourceforge.net/
Source0:       https://github.com/CodeNarc/CodeNarc/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires: mvn(org.codehaus.groovy:groovy)
BuildRequires: mvn(org.codehaus.groovy:groovy-ant)
BuildRequires: mvn(org.codehaus.groovy:groovy-xml)
BuildRequires: mvn(org.gmetrics:GMetrics)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
CodeNarc is a static analysis tool for Groovy source code,
enabling monitoring and enforcement of many coding standards
and best practices. CodeNarc applies a set of Rules
(predefined and/or custom) that are applied to each Groovy
file, and generates an HTML report of the results, including
a list of rules violated for each source file, and a count
of the number of violations per package and for the whole
project.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{version}

find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/*

cp -p site-pom.xml pom.xml

mkdir -p src/main/java/org/codenarc/analyzer
cp -p src/main/groovy/org/codenarc/analyzer/SuppressionAnalyzer.java \
 src/main/java/org/codenarc/analyzer/

# Set encoding
%pom_xpath_inject pom:project/pom:properties '
  <antVersion>1.9.6</antVersion>
  <gmetricsVersion>0.7</gmetricsVersion>
  <junitVersion>4.12</junitVersion>
  <log4jVersion>1.2.17</log4jVersion>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>'

%pom_xpath_set pom:properties/pom:targetJdk 1.6
%pom_xpath_set pom:properties/pom:groovyVersion 2.4.5

%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.5.1 . "
<configuration>
    <source>\${targetJdk}</source>
    <target>\${targetJdk}</target>
</configuration>"

%pom_add_plugin org.codehaus.gmavenplus:gmavenplus-plugin:1.5 . "
 <executions>
  <execution>
   <goals>
    <goal>generateStubs</goal>
    <!--goal>testCompile</goal-->
    <goal>testGenerateStubs</goal>
   </goals>
  </execution>
 </executions>"

%pom_add_dep org.apache.ant:ant:'${antVersion}' . "<optional>true</optional>"
%pom_add_dep org.codehaus.groovy:groovy:'${groovyVersion}'
%pom_add_dep org.codehaus.groovy:groovy-ant:'${groovyVersion}'
%pom_add_dep org.codehaus.groovy:groovy-xml:'${groovyVersion}'
%pom_add_dep org.gmetrics:GMetrics:'${gmetricsVersion}'
%pom_add_dep junit:junit:'${junitVersion}'
%pom_add_dep log4j:log4j:'${log4jVersion}'

# Convert from dos to unix line ending
for file in CHANGELOG.txt LICENSE.txt NOTICE.txt README.md ; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%mvn_file org.%{name}:%{oname} %{name} %{oname}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.txt README.md
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.24.1-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.24.1-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.24.1-alt1_2jpp8
- new jpp release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_15jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_3jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2jpp7
- new version

