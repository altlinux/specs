Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionally build with a minimal dependency set
%bcond_with jp_minimal

Name:           freemarker
Version:        2.3.30
Release:        alt3_3jpp8
Summary:        The Apache FreeMarker Template Engine
License:        ASL 2.0
URL:            https://freemarker.apache.org/
Source0:        https://github.com/apache/freemarker/archive/v%{version}/%{name}-%{version}.tar.gz

# Remove JSP 2.0 API usage
Patch1:         jsp-api.patch
# Compile only the classes compatible with the version of jython
Patch2:         jython-compatibility.patch
# illegal character in the javadoc comment
Patch3:         fix-javadoc-encoding.patch
# Disable JRebel integration, it is not free software and not in Fedora
Patch5:         no-javarebel.patch
# enable jdom extension
Patch6:         enable-jdom.patch
# Fix compatibility with javacc 7
Patch7:         javacc-7.patch
Patch8:		freemarker-2.3.30-use-jakarta-el.patch

BuildArch:      noarch

BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: ant
BuildRequires: apache-parent
BuildRequires: apache-commons-logging
BuildRequires: aqute-bnd
BuildRequires: hamcrest
BuildRequires: ivy-local
BuildRequires: glassfish-jsp-api
BuildRequires: glassfish-servlet-api
BuildRequires: javacc >= 7.0
BuildRequires: jaxen >= 1.1
BuildRequires: jcl-over-slf4j
BuildRequires: jdom >= 1.0
BuildRequires: junit
BuildRequires: log4j-over-slf4j
BuildRequires: slf4j
BuildRequires: xalan-j2 >= 2.7.0

%if %{without jp_minimal}
BuildRequires: dom4j
BuildRequires: saxpath
BuildRequires: jython
BuildRequires: rhino >= 1.6
%endif
BuildRequires: jakarta-el-api
Source44: import.info

%description
Apache FreeMarker is a template engine: a Java library to generate text output
(HTML web pages, e-mails, configuration files, source code, etc.) based on
templates and changing data. Templates are written in the FreeMarker Template
Language (FTL), which is a simple, specialized language (not a full-blown
programming language like PHP).

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

find -type f -name "*.jar" -delete
find -type f -name "*.class" -delete

%patch1
%patch2
%patch3
%patch5
%patch6
%patch7 -p1
%patch8 -p1

# Use system ivy settings
rm ivysettings.xml

# Correct classpath for Javadoc generation
sed -i 's/cachepath conf="IDE"/cachepath conf="javadoc"/' build.xml
sed -i '/conf name="IDE"/i<conf name="javadoc" extends="build.jython2.5,build.jsp2.1" />' ivy.xml

# Disable Java 8 javadoc linting
sed -i '/<javadoc/a\ additionalparam="-Xdoclint:none" encoding="UTF-8"' build.xml

# Drop unnecessary dep on avalon
sed -i -e '/avalon-logkit/d' ivy.xml
rm src/main/java/freemarker/log/_AvalonLoggerFactory.java

%if %{with jp_minimal}
# Drop dep on optional extra deps for minimal build
sed -i -e '/"rhino"/d' -e '/"jython"/d' ivy.xml
rm -rf src/main/java/freemarker/ext/{rhino,jython,ant}
rm src/main/java/freemarker/template/utility/JythonRuntime.java
# Drop dep on additional xml backends for minimal build
sed -i -e '/dom4j/d' -e '/saxpath/d' ivy.xml
rm src/main/java/freemarker/ext/xml/_Dom4jNavigator.java
%endif

# Don't import all the logger implementations in the OSGi metadata
sed -i -e '/^Import-Package/s/:/: !org.apache.log4j, /' osgi.bnd

%mvn_file org.%{name}:%{name} %{name}

%build
export LANG=C.UTF-8
export JAVA_HOME=%{_jvmdir}/java-1.8.0
ant -Divy.mode=local -Ddeps.available=true javacc jar javadoc maven-pom

%install
export LANG=C.UTF-8
%mvn_artifact build/pom.xml build/%{name}.jar
%mvn_install -J build/api

%files -f .mfiles
%doc README.md RELEASE-NOTES
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed May 25 2022 Igor Vlasenko <viy@altlinux.org> 0:2.3.30-alt3_3jpp8
- fix for new cdi-api

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.3.30-alt2_3jpp8
- fc update

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 0:2.3.30-alt2_2jpp8
- fixed build

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 0:2.3.30-alt1_2jpp8
- new version, use jvm8

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:2.3.29-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.3.28-alt1_4jpp8
- update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.3.28-alt1_2jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.3.27-alt1_2jpp8
- java update

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

