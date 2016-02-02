Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          javaparser
Version:       1.0.8
Release:       alt2_10jpp8
Summary:       Java 1.5 Parser and AST
License:       GPLv3+ and LGPLv3+
URL:           http://javaparser.github.io/javaparser/
Source0:       http://javaparser.googlecode.com/files/%{name}-%{version}-src.zip
Source1:       http://%{name}.googlecode.com/svn/maven2/com/google/code/%{name}/%{name}/%{version}/%{name}-%{version}.pom

# test deps
BuildRequires: junit

BuildRequires: javacc
BuildRequires: maven-local
BuildRequires: sonatype-oss-parent

BuildArch:     noarch
Source44: import.info

%description
A Java 1.5 Parser with AST generation and visitor support.
The AST records the source code structure, java doc and
comments. It is also possible to change the AST nodes or
create new ones to modify the source code.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

cp -p %{SOURCE1} pom.xml
# remove org.jvnet.wagon-svn wagon-svn 1.9
%pom_xpath_remove "pom:project/pom:build/pom:extensions"

for s in $(find . -name "*.java");do
  native2ascii -encoding UTF8 ${s} ${s}
done

for d in COPYING readme.txt ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

sed -i 's/\r//' COPYING.LESSER

%mvn_file :%{name} %{name}

%build

(
  cd src/japa/parser
  rm JavaCharStream.java ParseException.java Token.java TokenMgrError.java
  javacc.sh java_1_5.jj
)

# test skip http://code.google.com/p/javaparser/issues/detail?id=43
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc readme.txt
%doc COPYING COPYING.LESSER

%files javadoc -f .mfiles-javadoc
%doc readme.txt
%doc COPYING COPYING.LESSER

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_1jpp7
- new version

