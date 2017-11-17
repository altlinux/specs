BuildRequires: ecj
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

%global checkForbiddenJARFiles F=`find -type f -iname '*.jar'`; [ ! -z "$F" ] && \
echo "ERROR: Sources should not contain JAR files:" && echo "$F" && exit 1

%global fm_compatible_ver 2.3
%global fm_ver %{fm_compatible_ver}.23

Name:           freemarker
Version:        %{fm_ver}
Release:        alt2_5jpp8
Summary:        A template engine
License:        BSD
URL:            http://freemarker.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# Remove JSP 1.x and 2.0 API usage
Patch1:         jsp-api.patch
# Compile only the classes compatible with the version of jython
Patch2:         jython-compatibility.patch
# illegal character in the javadoc comment
Patch3:         fix-javadoc-encoding.patch
# Fix ivy configuration
Patch4:         ivy-configuration.patch
# Disable JavaRebelIntegration
Patch5:         no-javarebel.patch
# enable jdom extension
Patch6:         enable-jdom.patch
# use system javacc and fix Token.java
Patch7:         javacc.patch
# Fix compatibility with javacc 7
Patch8:         javacc-7.patch

BuildArch:      noarch

BuildRequires: ant >= 1.6
BuildRequires: apache-parent
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-io
BuildRequires: aqute-bnd
BuildRequires: avalon-logkit >= 1.2
BuildRequires: dom4j >= 1.6.1
BuildRequires: emma >= 2.0
BuildRequires: findbugs
BuildRequires: hamcrest
BuildRequires: ivy-local
BuildRequires: java-devel >= 1.6.0
BuildRequires: javacc >= 4.0
BuildRequires: javapackages-local
BuildRequires: jaxen >= 1.1
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jcl-over-slf4j
BuildRequires: jdom >= 1.0
BuildRequires: jetty-jsp
BuildRequires: jetty-webapp
BuildRequires: junit >= 3.8.2
BuildRequires: jython >= 2.2.1
BuildRequires: log4j >= 1.2
BuildRequires: log4j-over-slf4j
BuildRequires: logback
BuildRequires: rhino >= 1.6
BuildRequires: sonatype-oss-parent
BuildRequires: saxpath
BuildRequires: slf4j
BuildRequires: xalan-j2 >= 2.7.0
Source44: import.info

%description
FreeMarker is a Java tool to generate text output based on templates.
It is designed to be practical as a template engine to generate web
pages and particularly for servlet-based page production that follows
the MVC (Model View Controller) pattern. That is, you can separate the
work of Java programmers and website designers - Java programmers
needn't know how to design nice websites, and website designers needn't
know Java programming.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version} -c


find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf documentation/_html/api/

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# javacc generated sources are not Java 4 compatible, set source and target levels to Java 8
sed -i 's/"1\.4"/"1.8"/g' source/build.xml

rm -rf source/ivysettings.xml

# %%{__rm} -rf src/freemarker/core/ParseException.java
rm -rf source/src/freemarker/core/FMParser.java
rm -rf source/src/freemarker/core/FMParserConstants.java
rm -rf source/src/freemarker/core/FMParserTokenManager.java
rm -rf source/src/freemarker/core/SimpleCharStream.java
rm -rf source/src/freemarker/core/Token.java
rm -rf source/src/freemarker/core/TokenMgrError.java

%checkForbiddenJARFiles

%mvn_file org.%{name}:%{name} %{name}

%build
cd source
ant -Divy.mode=local javacc jar javadoc maven-pom

%install
%mvn_artifact source/build/pom.xml source/build/%{name}.jar
%mvn_install -J source/build/api

%files -f .mfiles
%doc README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.3.23-alt2_5jpp8
- fixed build with new tomcat

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.3.23-alt1_5jpp8
- fc27 update

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.23-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.19-alt2_11jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.19-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.19-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.19-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.19-alt1_4jpp7
- new version

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.16-alt1_2jpp6
- new version

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.15-alt3_1jpp5
- fedora compat maven2 mapping added

* Wed Apr 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.15-alt2_1jpp5
- fedora compat symlink added

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.15-alt1_1jpp5
- new jpp release

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.13-alt2_4jpp5
- raised epoch: to 0 (alt rpm quirk)

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 2.3.13-alt1_4jpp5
- converted from JPackage by jppimport script

* Sat Nov 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.6-alt1_2jpp1.7
- converted from JPackage by jppimport script

