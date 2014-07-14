Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

%global checkForbiddenJARFiles F=`find -type f -iname '*.jar'`; [ ! -z "$F" ] && \
echo "ERROR: Sources should not contain JAR files:" && echo "$F" && exit 1

%global fm_compatible_ver 2.3
%global fm_ver %{fm_compatible_ver}.19

Name:           freemarker
Version:        %{fm_ver}
Release:        alt2_4jpp7
Summary:        A template engine

Group:          Development/Java
License:        BSD
URL:            http://freemarker.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        http://freemarker.sourceforge.net/maven2/org/%{name}/%{name}/%{version}/%{name}-%{version}.pom

# disabled functionality: ext/jdom, ext/jsp/FreeMarkerPageContext1, ext/xml/JdomNavigator
Patch0:         %{name}-%{version}-build.patch
#
Patch1:         %{name}-2.3.13~PyObject.__class__.patch
# http://netbeans.org/bugzilla/show_bug.cgi?id=156876
Patch2:         %{name}-%{version}-logging.patch
# illegal character in the javadoc comment
Patch3:         %{name}-2.3.13~encoding.patch
# do not depend on tomcat5
Patch4:         %{name}-%{version}-no-tomcat5.patch
# Disable JavaRebelIntegration
Patch5:         %{name}-%{version}-no-javarebel.patch
# enable jdom extension
Patch6:         %{name}-%{version}-enable-jdom.patch
# use system javacc and fix Token.java
Patch7:         %{name}-%{version}-javacc.patch

BuildArch:      noarch

BuildRequires: ant >= 1.6
BuildRequires: ant-nodeps >= 1.6
BuildRequires: apache-commons-logging
BuildRequires: avalon-logkit >= 1.2
BuildRequires: dom4j >= 1.6.1
BuildRequires: dos2unix
BuildRequires: emma >= 2.0
BuildRequires: javacc >= 4.0
BuildRequires: jaxen >= 1.1
BuildRequires: jdom >= 1.0
BuildRequires: jpackage-utils
BuildRequires: junit >= 3.8.2
BuildRequires: jython >= 2.2.1
BuildRequires: log4j >= 1.2
BuildRequires: rhino >= 1.6
BuildRequires: slf4j
BuildRequires: tomcat6-el-2.1-api
BuildRequires: tomcat6-lib >= 6.0.16
BuildRequires: tomcat6-servlet-2.5-api >= 6.0
BuildRequires: xalan-j2 >= 2.7.0

Requires: jpackage-utils
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
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

find -type f \( -iname '*.jar' -o -iname '*.class' \)  -exec rm -f '{}' \;

%patch0 -p0
#  % p atch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p0

# %{__rm} -rf src/freemarker/core/ParseException.java
%{__rm} -rf src/freemarker/core/FMParser.java
%{__rm} -rf src/freemarker/core/FMParserConstants.java
%{__rm} -rf src/freemarker/core/FMParserTokenManager.java
%{__rm} -rf src/freemarker/core/SimpleCharStream.java
%{__rm} -rf src/freemarker/core/Token.java
%{__rm} -rf src/freemarker/core/TokenMgrError.java

%{__ln_s} -f %{_javadir}/ant.jar           lib/ant.jar
%{__ln_s} -f %{_javadir}/commons-logging.jar    lib/commons-logging.jar
%{__ln_s} -f %{_javadir}/dom4j.jar         lib/dom4j.jar
%{__ln_s} -f %{_javadir}/emma_ant.jar      lib/emma_ant.jar
%{__ln_s} -f %{_javadir}/emma.jar          lib/emma.jar
#%{__ln_s} -f %{_javadir}/javacc.jar        lib/javacc.jar
%{__ln_s} -f %{_javadir}/jaxen.jar         lib/jaxen.jar
%{__ln_s} -f %{_javadir}/jdom.jar          lib/jdom.jar
# js.jsr provided by rhino package
%{__ln_s} -f %{_javadir}/js.jar            lib/js.jar

# The JavaServer Pages 1.2 technology isn't provided in Fedora 10
#%{__ln_s} -f %{_javadir}/jsp-api-1.2.jar   lib/jsp-api-1.2.jar

%{__ln_s} -f %{_javadir}/tomcat5-jsp-2.0-api.jar  lib/jsp-api-2.0.jar

%{__ln_s} -f %{_javadir}/tomcat6-jsp-2.1-api.jar  lib/jsp-api-2.1.jar

%{__ln_s} -f %{_javadir}/junit.jar         lib/junit.jar
%{__ln_s} -f %{_javadir}/jython.jar        lib/jython.jar
%{__ln_s} -f %{_javadir}/log4j.jar         lib/log4j.jar
%{__ln_s} -f %{_javadir}/avalon-logkit.jar lib/logkit.jar
%{__ln_s} -f %{_javadir}/slf4j/api.jar lib/slf4j-api.jar

# It doesn't required due to OpenJDK 6 is used
#%{__ln_s} -f %{_javadir}/rt122.jar         lib/rt122.jar

# SAXPath has been merged into the Jaxen codebase and is 
# no longer being maintained separately. See jaxen-1.1.jar
#%{__ln_s} -f %{_javadir}/saxpath.jar       lib/saxpath.jar

# The package javax.el isn't included in:
%{__ln_s} -f %{_javadir}/tomcat6-servlet-2.5-api.jar lib/servlet.jar
# so, el-api.jar is additionally used.
%{__ln_s} -f %{_javadir}/tomcat6-el-2.1-api.jar lib/el-api.jar

%{__ln_s} -f %{_javadir}/struts.jar        lib/struts.jar
%{__ln_s} -f %{_javadir}/xalan-j2.jar      lib/xalan.jar

dos2unix -k docs/docs/api/stylesheet.css
dos2unix -k docs/docs/api/package-list

%checkForbiddenJARFiles

%build
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 

%install
# jars
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr docs/docs/api/* %{buildroot}%{_javadocdir}/%{name}

# pom
%{__install} -d -m 755 %{buildroot}%{_mavenpomdir}
%{__install} -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

# depmap
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*.jar
%doc LICENSE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
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

