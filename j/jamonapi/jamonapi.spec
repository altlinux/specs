Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname jamon

Name:          jamonapi
Version:       2.74
Release:       alt1_9jpp8
Summary:       A Java monitoring API
License:       BSD
URL:           http://jamonapi.sourceforge.net/
# Newer release available @ https://github.com/stevensouza/jamonapi/
# cvs -d:pserver:anonymous@jamonapi.cvs.sourceforge.net:/cvsroot/jamonapi login
# cvs -z3 -d:pserver:anonymous@jamonapi.cvs.sourceforge.net:/cvsroot/jamonapi co -P -r v2_74 jamonapi/src
# Remove pregenerated javadoc files in the source tree
# rm -rf jamonapi/src/JAMonUsersGuide/javadoc/*
# Remove zip file which contains a proprietary binary
# rm -rf jamonapi/src/JAMonUsersGuide/JAMon_PB.zip
# rm -rf $(find -name "CVS")
# tar cJf jamonapi-2.74.tar.xz jamonapi
Source0:       %{name}-%{version}.tar.xz
# This POM is completely Fedora-specific
Source1:       %{name}-%{version}.pom

Patch0:        %{name}-buildxml.patch
Patch1:        %{name}-jetty8.patch
Patch2:        %{name}-log4j12.patch
Patch3:        %{name}-jetty93.patch

BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: tomcat-lib
BuildRequires: tomcat-servlet-3.1-api
BuildRequires: tomcat-el-3.0-api
BuildRequires: jetty
BuildRequires: geronimo-interceptor
BuildRequires: log4j12
BuildRequires: dos2unix

Requires:      geronimo-interceptor
Requires:      log4j12

BuildArch:     noarch
Source44: import.info

%description
JAMon API is a free, simple, high performance, thread safe,
Java API that allows developers to easily monitor the
performance and scalability of production applications. JAMon
tracks hits, execution times (total, avg, min, max, std dev),
and more.

%package javadoc
Group: Development/Java
Summary:         API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for Java monitoring API.

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i "s|tomcat-el-2.2-api.jar|tomcat-el-api.jar|" src/ant/build.xml
sed -i "s|tomcat-servlet-3.0-api.jar|tomcat-servlet-api.jar|" src/ant/build.xml

sed -i 's|target="1.5" source="1.5"|target="1.6" source="1.6"|' src/ant/build.xml
sed -i 's|"source" value="1.5"|"source" value="1.6"|' src/ant/build.xml
sed -i 's|"vm" value="1.5"|"vm" value="1.6"|' src/ant/build.xml

sed -i 's|packagenames="${package}"|packagenames="${package}" additionalparam="-Xdoclint:none"|' src/ant/build.xml

mkdir dist
mkdir lib

%build
pushd src/ant
ant JAR
ant javadoc
popd

# Remove spurious executable permissions
find src/JAMonUsersGuide -type f | xargs chmod -x
find src/JAMonUsersGuide -regex '.*\(xml\|css\|js\)' -o -name package-list | xargs dos2unix

# There should be a shorter way to do an iconv task, but I do not know of one
pushd src/JAMonUsersGuide/presentation/jamon_files/
mv master04_stylesheet.css master04_stylesheet.css.iso8859-1
iconv -f ISO-8859-1 -t UTF-8 master04_stylesheet.css.iso8859-1 > master04_stylesheet.css
rm master04_stylesheet.css.iso8859-1
popd

cp -p src/JAMonUsersGuide/JAMonLicense.html .

%install
%mvn_artifact %{SOURCE1} dist/%{oname}-%{version}.jar
%mvn_file com.jamonapi:jamon %{oname} %{name}
%mvn_install -J src/doc/javadoc

%files -f .mfiles
%doc src/JAMonUsersGuide
%doc JAMonLicense.html

%files javadoc -f .mfiles-javadoc
%doc JAMonLicense.html

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.74-alt1_9jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.74-alt1_8jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.73-alt2_7jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.73-alt2_6jpp7
- use fc geronimo

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.73-alt1_6jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt3_2jpp6
- built with java 6 due to abstract getParentLogger

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt2_2jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt2_1jpp5
- selected java5 compiler explicitly

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7-alt1_1jpp5
- new jpp5.0 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

