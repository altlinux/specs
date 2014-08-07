# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          parboiled
Version:       1.0.2
Release:       alt2_3jpp7
Summary:       Java/Scala library providing parsing of input text based on PEGs
Group:         Development/Java
License:       ASL 2.0
URL:           http://parboiled.org/
# git clone git://github.com/sirthias/parboiled.git parboiled-1.0.2
# cd parboiled-1.0.2/ && git archive --format=tar --prefix=parboiled-1.0.2/ 1.0.2 | xz > ../parboiled-1.0.2-src-git.tar.xz
Source0:       %{name}-%{version}-src-git.tar.xz
# for build see https://github.com/sirthias/parboiled/wiki/Building-parboiled
Source1:       http://repo1.maven.org/maven2/org/%{name}/%{name}-core/%{version}/%{name}-core-%{version}.pom
Source2:       http://repo1.maven.org/maven2/org/%{name}/%{name}-java/%{version}/%{name}-java-%{version}.pom
# customized aggregator pom
Source3:       %{name}-%{version}-pom.xml

BuildRequires: jpackage-utils

BuildRequires: objectweb-asm

# TODO parboiled-scala require org.scala-lang scala-library 2.9.1
# use https://github.com/davidB/scala-maven-plugin v3.0.2
# BuildRequires: scala
# BuildRequires: scala-maven-plugin

# test deps
#BuildRequires: mvn(org.scalatest:scalatest_2.10.0-RC1)
#BuildRequires: testng

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
#BuildRequires: maven-surefire-provider-testng

Requires:      objectweb-asm

Requires:      jpackage-utils
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
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
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

%build

# test skipped unavailable dep org.scalatest scalatest_2.9.0 1.6.1
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.skip=true install javadoc:aggregate
 
%install

mkdir -p %{buildroot}%{_mavenpomdir}
mkdir -p %{buildroot}%{_javadir}/%{name}
# scala
for m in \
  core \
  java;do
    install -m 644 %{name}-${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
    install -pm 644 %{name}-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
    %add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGELOG LICENSE README.markdown

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- rebuild with maven-local

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new version

