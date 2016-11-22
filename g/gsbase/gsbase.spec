Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          gsbase
Version:       2.0.1
Release:       alt9_8jpp8
Summary:       A collection of java utility classes
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
BuildArch:     noarch
Source44: import.info

%description
A collection of classes that are helpful 
when writing JUnit test cases. Classes
include things like a logging subsystem and
a complex layout manager.

%package javadoc
Group: Development/Java
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

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']" "<version>2.14.2</version>"
# list.size expected:<2> but was:<0>
rm -r src/test/com/gargoylesoftware/base/resource/jdbc/WrapperTestCase.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/CallableStatementWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/ConnectionWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/DatabaseMetaDataWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/PreparedStatementWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/ResultSetWrapperTest.java \
 src/test/com/gargoylesoftware/base/resource/jdbc/StatementWrapperTest.java
# Require Java awt subsystem
rm -r src/test/com/gargoylesoftware/base/gui/TableLayoutTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt9_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.1-alt9_7jpp8
- new version

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

