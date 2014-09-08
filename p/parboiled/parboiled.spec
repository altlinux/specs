Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          parboiled
Version:       1.0.2
Release:       alt2_6jpp7
Summary:       Java/Scala library providing parsing of input text based on PEGs
License:       ASL 2.0
URL:           http://parboiled.org/
Source0:       https://github.com/sirthias/parboiled/archive/%{version}.tar.gz
# for build see https://github.com/sirthias/parboiled/wiki/Building-parboiled
Source1:       http://repo1.maven.org/maven2/org/%{name}/%{name}-core/%{version}/%{name}-core-%{version}.pom
Source2:       http://repo1.maven.org/maven2/org/%{name}/%{name}-java/%{version}/%{name}-java-%{version}.pom
# customized aggregator pom
Source3:       %{name}-%{version}-pom.xml


BuildRequires: mvn(asm:asm)
BuildRequires: mvn(asm:asm-analysis)
BuildRequires: mvn(asm:asm-tree)
BuildRequires: mvn(asm:asm-util)

%if 0
# TODO 
BuildRequires: mvn(org.scala-lang:scala-library)
# test deps
BuildRequires: mvn(org.scalatest:scalatest_2.10)
BuildRequires: mvn(org.testng:testng)

# use https://github.com/davidB/scala-maven-plugin
BuildRequires: scala-maven-plugin
BuildRequires: maven-surefire-provider-testng
%endif

BuildRequires: maven-local


BuildArch:     noarch
Source44: import.info

%description
parboiled is a mixed Java/Scala library providing for lightweight and
easy-to-use, yet powerful and elegant parsing of arbitrary input text
based on Parsing expression grammars (PEGs). PEGs are an alternative to
context free grammars (CFGs) for formally specifying syntax, they
make a good replacement for regular expressions and generally have quite
a few advantages over the "traditional" way of building parsers via CFGs.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

find . -name "*.class" -delete
find . -name "*.jar" -delete

cp -p %{SOURCE1} %{name}-core/pom.xml
cp -p %{SOURCE2} %{name}-java/pom.xml
#cp -p %%{SOURCE?} %%{name}-scala/pom.xml
cp -p %{SOURCE3} pom.xml

%mvn_file :%{name}-core %{name}/core
%mvn_file :%{name}-java %{name}/java

%build

# test skipped unavailable dep org.scalatest scalatest_2.9.0 1.6.1
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8
 
%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc CHANGELOG LICENSE README.markdown

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- rebuild with maven-local

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new version

