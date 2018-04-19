Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          junit-addons
Version:       1.4
Release:       alt3_16jpp8
Summary:       JUnitX helper classes for JUnit
License:       ASL 1.1
Url:           http://sourceforge.net/projects/junit-addons/
Source0:       http://sourceforge.net/projects/%{name}/files/JUnit-addons/JUnit-addons%%20%{version}/%{name}-%{version}.zip
# from http://junit-addons.cvs.sourceforge.net/viewvc/junit-addons/junit-addons/build.xml?view=markup&pathrev=release_1_4
Source1:       %{name}-build.xml
Source2:       http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Patch0:        junit-addons-1.4-enum.patch

BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: apache-commons-logging
BuildRequires: jaxen
BuildRequires: jdom
BuildRequires: junit
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

Requires:      ant
Requires:      jaxen
Requires:      jdom
Requires:      junit
Requires:      xerces-j2

BuildArch:     noarch
Source44: import.info

%description
JUnit-addons is a collection of helper classes for JUnit. 

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%jar xf src.jar
find . -name "*.class" -delete
find . -type f -name "*.jar" -delete
find . -type f -name "*.zip" -delete

%patch0 -p0

rm -r api
cp -p %{SOURCE1} build.xml

# fix non ASCII chars
for s in src/main/junitx/framework/TestSuite.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# disable test
# some tests fails with the regenerate test resource
# tests.jar
# tests.zip
sed -i "s| test, ||" build.xml

%build
# regenerate test resource
#(
#  cd src/example
#  mkdir test
#  javac -d test -source 1.4 -target 1.4 $(find . -name "*.java") -cp $(build-classpath junit4)
#  rm test/junitx/example/*.class
#  cp -p junitx/example/packageA/SampleA.txt test/junitx/example/packageA/
#  cp -p junitx/example/packageA/packageB/SampleB.txt test/junitx/example/packageA/packageB/
#  (
#    cd test
#    jar -cf ../tests.jar *
##    zip -r ../tests.zip *
#  )
#  cp -p tests.jar tests.zip
#  rm -r test
#)

export CLASSPATH=
export OPT_JAR_LIST=:
%ant \
  -Dant.build.javac.source=1.6 \
  -Djdom.jar=$(build-classpath jdom) \
  -Djaxen.jar=$(build-classpath jaxen) \
  -Dsaxpath.jar=$(build-classpath jaxen) \
  -Dant.jar=$(build-classpath ant.jar) \
  -Djunit.jar=$(build-classpath junit) \
  -Dxerces.jar=$(build-classpath xerces-j2) \
  -Dxml-apis.jar=$(build-classpath xml-commons-apis) \
  -Dcommons-logging.jar=$(build-classpath commons-logging) \
  -Dproject.name=%{name} \
  -Dproject.version=%{version} \
  release

%install
%mvn_file : %{name}
%mvn_artifact %{SOURCE2} dist/%{name}-%{version}.jar

%mvn_install -J build/api

%files -f .mfiles
%doc README WHATSNEW
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_15jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_12jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_11jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_4jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_3jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_7jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp5
- new version

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_2jpp5
- fixed build with java 5

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp1.7
- converted from JPackage by jppimport script

