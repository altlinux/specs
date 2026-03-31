%define _unpackaged_files_terminate_build 1

Name: freemarker
Version: 2.3.32
Release: alt1

Summary: The Apache FreeMarker Template Engine
Group: Development/Java
License: Apache-2.0
Url: https://freemarker.apache.org
Vcs: https://github.com/apache/freemarker
BuildArch: noarch

Source0: %name-%version.tar.gz

# enable jdom extension
Patch0: enable-jdom.patch
Patch1: javacc-7.patch
# disable JSP extension
# Support for the modern JSP 3.0+ will be made in the next version 2.3.33,
# which we cannot build yet due to the inability to build .kt plugins by gradle
Patch2: disable-jsp.patch

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: ant
BuildRequires: gnupg2
BuildRequires: ivy-local
BuildRequires: java-1.8.0-openjdk
BuildRequires: java-11-openjdk-devel
BuildRequires: mvn(biz.aQute:bnd)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(jaxen:jaxen)
BuildRequires: mvn(jdom:jdom)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.java.dev.javacc:javacc)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:log4j-over-slf4j)
BuildRequires: mvn(rhino:js)
BuildRequires: mvn(xalan:xalan)
BuildRequires: mvn(saxpath:saxpath)
BuildRequires: mvn(avalon-logkit:avalon-logkit)

%description
Apache FreeMarker is a template engine: a Java library to generate text output
(HTML web pages, e-mails, configuration files, source code, etc.) based on
templates and changing data. Templates are written in the FreeMarker Template
Language (FTL), which is a simple, specialized language (not a full-blown
programming language like PHP).

%prep
%setup
%autopatch -p1

find -type f '(' -name '*.jar' -o -iname '*.class' ')' -print -delete

# Use system ivy settings
rm ivysettings.xml

# Remove javarebel-sdk
%pom_remove_dep org.zeroturnaround:javarebel-sdk
rm src/main/java/freemarker/ext/beans/JRebelClassChangeNotifier.java
 
# Disable JSP deps
%pom_remove_dep javax.servlet.jsp:jsp-api
%pom_remove_dep javax.servlet:servlet-api

# Remove jython:jython
%pom_remove_dep jython:jython
rm src/main/java/freemarker/ext/ant/UnlinkedJythonOperationsImpl.java
rm src/main/java/freemarker/ext/jython/JythonHashModel.java
rm src/main/java/freemarker/ext/jython/JythonModel.java
rm src/main/java/freemarker/ext/jython/JythonModelCache.java
rm src/main/java/freemarker/ext/jython/JythonNumberModel.java
rm src/main/java/freemarker/ext/jython/JythonSequenceModel.java
rm src/main/java/freemarker/ext/jython/JythonVersionAdapter.java
rm src/main/java/freemarker/ext/jython/JythonVersionAdapterHolder.java
rm src/main/java/freemarker/ext/jython/JythonWrapper.java
rm src/main/java/freemarker/ext/jython/_Jython20And21VersionAdapter.java
rm src/main/java/freemarker/template/utility/JythonRuntime.java

# Remove org.python:jython
%pom_remove_dep org.python:jython
rm src/main/java/freemarker/ext/jython/_Jython22VersionAdapter.java
rm src/main/java/freemarker/ext/jython/_Jython25VersionAdapter.java

%mvn_file : %{name}

%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Divy.mode=local -Dsun.boot.class.path=%{_jvmdir}/jre-1.8.0/lib/rt.jar jar maven-pom

%install
%mvn_artifact build/pom.xml build/freemarker.jar
%mvn_install

%files -f .mfiles
%doc README.md RELEASE-NOTES
%doc --no-dereference LICENSE NOTICE

%changelog
* Mon Mar 30 2026 Arseniy Kostevich <faux@altlinux.org> 2.3.32-alt1
- new version
- fix FTBFS:
  + disable JSP extension
  + fix javacc-7.patch

* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 0:2.3.31-alt1_4jpp11
- new version

* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 0:2.3.30-alt5_3jpp8
- build without jython

* Sat May 28 2022 Igor Vlasenko <viy@altlinux.org> 0:2.3.30-alt4_3jpp8
- build with aqute-bnd4

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
