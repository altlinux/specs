# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          javaparser
Version:       1.0.8
Release:       alt2_1jpp7
Summary:       Java 1.5 Parser and AST
Group:         Development/Java
License:       GPLv3+ and LGPLv3+
URL:           http://code.google.com/p/javaparser/
Source0:       http://javaparser.googlecode.com/files/%{name}-%{version}-src.zip
Source1:       http://%{name}.googlecode.com/svn/maven2/com/google/code/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# remove org.jvnet.wagon-svn wagon-svn 1.9
Patch0:        %{name}-%{version}-remove-wagon-svn.patch

BuildRequires: jpackage-utils

# test deps
BuildRequires: junit

BuildRequires: javacc
BuildRequires: maven
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
# BuildRequires: maven-surefire-provider-junit4
BuildRequires: sonatype-oss-parent

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
A Java 1.5 Parser with AST generation and visitor support.
The AST records the source code structure, java doc and
comments. It is also possible to change the AST nodes or
create new ones to modify the source code.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

cp -p %{SOURCE1} pom.xml
%patch0 -p0

for s in $(find . -name "*.java");do
  native2ascii -encoding UTF8 ${s} ${s}
done

for d in COPYING readme.txt ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

sed -i 's/\r//' COPYING.LESSER

%build

(
  cd src/japa/parser
  rm JavaCharStream.java ParseException.java Token.java TokenMgrError.java
  javacc.sh java_1_5.jj
)

# test skip http://code.google.com/p/javaparser/issues/detail?id=43
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.skip=true install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc COPYING COPYING.LESSER readme.txt

%files javadoc
%{_javadocdir}/%{name}
%doc COPYING COPYING.LESSER readme.txt

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_1jpp7
- new version

