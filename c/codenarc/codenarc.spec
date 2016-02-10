Group: Development/Java
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname CodeNarc
Name:          codenarc
Version:       0.17
Release:       alt1_15jpp8
Summary:       Groovy library that provides static analysis features for Groovy code
License:       ASL 2.0
Url:           http://codenarc.sourceforge.net/
Source0:       http://downloads.sourceforge.net/project/codenarc/codenarc/CodeNarc%%20Version%%20%{version}/CodeNarc-%{version}-bin.tar.gz
# use antrun-plugin instead of gmaven
# fix log4j version
Patch0:        codenarc-0.17-antrunplugin.patch
# remove @Override
# unavailable method in groovy 1.8.x (...)
Patch1:        codenarc-0.17-groovy18.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.codehaus.groovy:groovy-all:1.8)
BuildRequires: mvn(org.gmetrics:GMetrics)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
# groovy-all embedded libraries
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(asm:asm-all)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(org.slf4j:slf4j-nop)

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

%patch0 -p0
%patch1 -p1

%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_dep net.sourceforge.cobertura:cobertura
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin

chmod 644 README.txt
for d in CHANGELOG.txt LICENSE.txt NOTICE.txt README.txt ; do
  sed -i 's/\r//' $d
done

%mvn_file org.%{name}:%{oname} %{name} %{oname}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.txt README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_15jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_3jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2jpp7
- new version

