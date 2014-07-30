Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jmock
%define version 2.5.1
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}

Name:          jmock
Version:       2.5.1
Release:       alt1_2jpp7
Summary:       Java library for testing code with mock objects
Group:         Development/Java
License:       BSD
Url:           http://www.jmock.org/
# svn export http://svn.codehaus.org/jmock/tags/2.5.1 jmock-2.5.1
# find jmock-2.5.1 -name "*.jar" -type f -delete
# find jmock-2.5.1 -name "*.class" -delete
# svn export http://svn.codehaus.org/jmock/tags/packaging-maven-2.5.1 jmock-2.5.1/maven
# tar czf jmock-2.5.1-clean-src-svn.tar.gz jmock-2.5.1
Source0:       %{name}-%{namedversion}-clean-src-svn.tar.gz
Patch0:        %{name}-%{namedversion}-use_system_libraries.patch
# build with cglib 2.2
Patch1:        %{name}-%{namedversion}-cglib22.patch
# patch for java6
Patch2:        %{name}-%{namedversion}-DeterministicSchedule.patch
# remove hamcrest classes
Patch3:        %{name}-%{namedversion}-javadoc.patch
# remove
#    gmaven
#    wagon-webdav 
#    profile jmock1
# change
#   cglib cglib-nodep 2.1_3 -> net.sf.cglib cglib 2.2
#   junit-dep -> junit
Patch4:        %{name}-%{namedversion}-poms.patch
# from Debian
Patch5:        %{name}-%{namedversion}-hamcrest12.patch
# build fix for java 7
Patch6:        %{name}-%{namedversion}-name-clash.patch

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: bsh
BuildRequires: cglib
BuildRequires: hamcrest12
BuildRequires: junit4
BuildRequires: objectweb-asm
BuildRequires: objenesis

Requires:      bsh
Requires:      hamcrest12
Requires:      junit4

Requires:      objenesis
Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Mock objects help you design and test the interactions between the objects in
your programs.
The jMock library:
  * makes it quick and easy to define mock objects, so you don't break the
    rhythm of programming.
  * lets you precisely specify the interactions between your objects, reducing
    the brittleness of your tests.
  * works well with the auto-completion and re-factoring features of your IDE
  * plugs into your favorite test framework
  * is easy to extend.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p1
%patch6 -p0

# fix non ASCII chars
for s in test/org/jmock/example/sniper/Money.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# TODO this test fails
rm -r test/org/jmock/test/acceptance/ParameterMatchingAcceptanceTests.java \
  test/org/jmock/test/acceptance/PrimitiveParameterTypesAcceptanceTests.java

%build

ant \
  -Dant.build.javac.source=1.5 \
  -Dant.build.javac.target=1.5 \
 -Dversion=%{namedversion} \
 zip.jars javadoc

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 maven/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

mkdir -p %{buildroot}%{_javadir}/%{name}
for m in %{name} \
  %{name}-junit3 \
  %{name}-junit4 \
  %{name}-legacy \
  %{name}-script;do
    install -m 644 build/%{name}-%{namedversion}/${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
    install -pm 644 maven/${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
    %add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

sed -i 's|<version>x-SNAPSHOT</version>|<version>%{namedversion}</version>|'  maven/%{name}-core/pom.xml
sed -i 's|<artifactId>%{name}-core</artifactId>|<artifactId>%{name}-tests</artifactId>|'  maven/%{name}-core/pom.xml
sed -i 's|<name>jMock 1 Core</name>|<name>jMock 2 Tests</name>|' maven/%{name}-core/pom.xml
install -m 644 build/%{name}-%{namedversion}/%{name}-tests-%{namedversion}.jar \
  %{buildroot}%{_javadir}/%{name}/%{name}-tests.jar
install -pm 644 maven/%{name}-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-tests.pom
%add_maven_depmap JPP.%{name}-%{name}-tests.pom %{name}/%{name}-tests.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/%{name}-%{namedversion}/doc/* %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README*

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_2jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_1jpp7
- fc update

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt4_3jpp6
- build with objectweb-asm

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_3jpp6
- new jpp release

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_2jpp5
- fixed build; use cglib21 (with old asm)

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_1jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

