Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Prevent brp-java-repack-jars from being run.
%global __jar_repack %{nil}

%global checkForbiddenJARFiles F=`find -type f -iname '*.jar'`; [ ! -z "$F" ] && \
echo "ERROR: Sources should not contain JAR files:" && echo "$F" && exit 1

%global fm_compatible_ver 2.3
%global fm_ver %{fm_compatible_ver}.19

Name:           freemarker
Version:        %{fm_ver}
Release:        alt2_11jpp8
Summary:        A template engine
License:        BSD
URL:            http://freemarker.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

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
# generate pom file
Patch8:         %{name}-%{version}-pom.patch
# fix javadoc classpath and doclint issues
Patch9:         %{name}-%{version}-javadoc.patch

BuildArch:      noarch

BuildRequires: ant >= 1.6
BuildRequires: apache-commons-logging
BuildRequires: avalon-logkit >= 1.2
BuildRequires: dom4j >= 1.6.1
BuildRequires: emma >= 2.0
BuildRequires: javacc >= 4.0
BuildRequires: javapackages-local
BuildRequires: jaxen >= 1.1
BuildRequires: jdom >= 1.0
BuildRequires: junit >= 3.8.2
BuildRequires: jython >= 2.2.1
BuildRequires: log4j >= 1.2
BuildRequires: rhino >= 1.6
BuildRequires: slf4j
BuildRequires: tomcat-el-3.0-api
BuildRequires: tomcat-lib >= 6.0.16
BuildRequires: tomcat-jsp-2.3-api
BuildRequires: tomcat-servlet-3.1-api >= 6.0
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
%setup -q -n %{name}-%{version}

find . -name "*.jar" -delete
find . -name "*.class" -delete
rm -rf docs/docs/api

%patch0 -p0
#  %% p atch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p0
%patch9 -p0

# %%{__rm} -rf src/freemarker/core/ParseException.java
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
#%%{__ln_s} -f %%{_javadir}/javacc.jar        lib/javacc.jar
%{__ln_s} -f %{_javadir}/jaxen.jar         lib/jaxen.jar
%{__ln_s} -f %{_javadir}/jdom.jar          lib/jdom.jar
# js.jsr provided by rhino package
%{__ln_s} -f %{_javadir}/js.jar            lib/js.jar

# The JavaServer Pages 1.2 technology isn't provided in Fedora 10
#%%{__ln_s} -f %%{_javadir}/jsp-api-1.2.jar   lib/jsp-api-1.2.jar

%{__ln_s} -f %{_javadir}/tomcat-jsp-api.jar  lib/jsp-api-2.0.jar

%{__ln_s} -f %{_javadir}/tomcat-jsp-api.jar  lib/jsp-api-2.1.jar

%{__ln_s} -f %{_javadir}/junit.jar         lib/junit.jar
%{__ln_s} -f %{_javadir}/jython/jython.jar        lib/jython.jar
%{__ln_s} -f %{_javadir}/log4j.jar         lib/log4j.jar
%{__ln_s} -f %{_javadir}/avalon-logkit.jar lib/logkit.jar
%{__ln_s} -f %{_javadir}/slf4j/api.jar lib/slf4j-api.jar

# It doesn't required due to OpenJDK 6 is used
#%%{__ln_s} -f %%{_javadir}/rt122.jar         lib/rt122.jar

# SAXPath has been merged into the Jaxen codebase and is
# no longer being maintained separately. See jaxen-1.1.jar
#%%{__ln_s} -f %%{_javadir}/saxpath.jar       lib/saxpath.jar

# The package javax.el isn't included in:
%{__ln_s} -f %{_javadir}/tomcat-servlet-api.jar lib/servlet.jar
# so, el-api.jar is additionally used.
%{__ln_s} -f %{_javadir}/tomcat-el-api.jar lib/el-api.jar

%{__ln_s} -f %{_javadir}/struts.jar        lib/struts.jar
%{__ln_s} -f %{_javadir}/xalan-j2.jar      lib/xalan.jar

%checkForbiddenJARFiles

%mvn_file org.%{name}:%{name} %{name}

%build

%{ant} jar javadoc maven-upload

%install
%mvn_artifact build/pom.xml lib/%{name}.jar
%mvn_install -J build/api

%files -f .mfiles
%doc README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

