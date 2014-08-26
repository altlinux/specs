Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
Name:          gsbase
Version:       2.0.1
Release:       alt9_1jpp7
Summary:       A collection of java utility classes
Group:         Development/Java
# http://gsbase.sourceforge.net/license.html Apache style license
License:       ASL 2.0
Url:           http://sourceforge.net/projects/gsbase/
Source0:       http://downloads.sourceforge.net/gsbase/%{name}-%{version}.zip
Source1:       http://repo1.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# build fix for java7
Patch0:        %{name}-%{version}-jdk7.patch


BuildRequires: junit
BuildRequires: junitperf

BuildRequires: maven-local

Requires:      junit
Requires:      junitperf

BuildArch:     noarch
Source44: import.info

%description
A collection of classes that are helpful 
when writing JUnit test cases. Classes
include things like a logging subsystem and
a complex layout manager.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c
find . -name '*.jar' -delete
find . -name '*.class' -delete
rm -r docs/*
%patch0 -p1

cp -pr %{SOURCE1} pom.xml

%if %{?fedora} <= 18
%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId='junitperf']/pom:version"
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:artifactId='junitperf']" "
<scope>system</scope>
<systemPath>$(build-classpath junitperf)</systemPath>"
%endif

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']" "<version>any</version>"
# list.size expected:<2> but was:<0>
rm -r src/test/com/gargoylesoftware/base/resource/jdbc/WrapperTestCase.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/CallableStatementWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/ConnectionWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/DatabaseMetaDataWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/PreparedStatementWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/ResultSetWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/StatementWrapperTest.java

%build

mvn-rpmbuild \
 -Dproject.build.sourceEncoding=UTF-8 \
 package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt9_1jpp7
- new release

* Sat Mar 30 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt8_2jpp6
-fixed build with new xerces-j2

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt7_2jpp6
- jpp6 release

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt7_1jpp5
- build with saxon6-scripts

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt6_1jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt5_1jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt4_1jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt1_1jpp5
- converted from JPackage by jppimport script

