Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jacorb
%define version 2.3.2
%global namedreltag _jboss-5
%global namedversion %(echo %{version}| tr . _)%{?namedreltag}

%global pomreltag -jbossorg-5
%global pomversion %{version}%{?pomreltag}

Name:          jacorb
Version:       2.3.2
Release:       alt1_1.jbossorg.5jpp8
Summary:       The Java implementation of the OMG's CORBA standard
License:       LGPLv2
URL:           http://www.jacorb.org/index.html
Source0:       https://github.com/JacORB/JacORB/archive/R_%{namedversion}/JacORB-R_%{namedversion}.tar.gz

# These methods are not implemented in the current
Patch0:        jacorb-2.3.1-Implement-a-few-methods-in-GSSUPContextSpi-to-make-i.patch

# Fix "error: unmappable character for encoding ASCII" JDK issues
Patch1:        jacorb-2.3.1-Set-encoding-to-UTF-8-when-generating-javadoc.patch

# Support for JDK 8
Patch2:        JDK8-support.patch

# jacorb use java_cup = 0.9e for generate java stuff
# Our java_cup (0.11b) generated wrong entries in the java code, e.g.
# import org.jacorb.idl.runtime.XMLElement;
# patch was generated using the following steps
# find . -name "*.jar" ! -name "java_cup.jar" -print -delete
# ln -s $(build-classpath avalon-logkit) lib/logkit-1.2.jar
# ant -f src/org/jacorb/idl/build.xml
# find . -name "*.jar" -print -delete
# find . -name "*.class" -print -delete
Patch3:        jacorb-2.3.2-java_cup.patch

BuildRequires: ant
BuildRequires: java-devel
BuildRequires: maven-local
BuildRequires: mvn(antlr:antlr)
BuildRequires: mvn(avalon-logkit:avalon-logkit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-apache-regexp)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)

BuildArch:     noarch
Source44: import.info

%description
This package contains the Java implementation of the OMG's CORBA standard.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JacORB-R_%{namedversion}
# Cleanup
find . -name "*.class" -print -delete
find . -name "*.dll" -print -delete
find . -name "*.jar" -print -delete
find . -name "*.zip" -print -delete

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%pom_disable_module maven/release
%pom_disable_module maven/resources

%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:scope"
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:systemPath"

%pom_remove_plugin -r org.commonjava.maven.plugins:build-migration-maven-plugin

%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :maven-source-plugin

%pom_add_dep avalon-logkit:avalon-logkit:1.2:compile maven/idl-compiler

# No xdoclet available
sed -i 's|,notification||' src/org/jacorb/build.xml

sed -i '/Class-Path/d' build.xml

%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"
%pom_xpath_inject "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>" maven/core maven/idl-compiler

sed -i 's|${IGNORED_TAGS}|${IGNORED_TAGS} -Xdoclint:none|' build.xml
sed -i 's|,org.jacorb.notification.\*||' build.xml
sed -i 's|org.jacorb.notification.filter.bsh|org.jacorb.notification.*|' build.xml

ln -s $(build-classpath antlr) lib/antlr-2.7.2.jar
ln -s $(build-classpath slf4j/api) lib/slf4j-api-1.5.6.jar
ln -s $(build-classpath avalon-logkit) lib/logkit-1.2.jar

%mvn_artifact org.jacorb:jacorb:jar:%{pomversion} lib/jacorb.jar
%mvn_artifact org.jacorb:jacorb-idl-compiler:jar:%{pomversion} lib/idl.jar
%mvn_alias "org.jacorb:" "jacorb:"

%build

# due to javadoc x86_64 out of memory
subst 's,maxmemory="256m",maxmemory="512m",' build.xml

%mvn_build -- -Dcompile=all -DskipTests=true -Djava-source-version=1.6 -Djavac-encoding=utf-8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc doc/REL_NOTES
%doc doc/LICENSE

%files javadoc -f .mfiles-javadoc
%doc doc/LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.2-alt1_1.jbossorg.5jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_9jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_5jpp7
- new release

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_3.20120215gitjpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_20jpp6
- built with java 6

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_20jpp6
- new jpp release

* Thu May 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_19jpp5
- jpp6 import

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_17jpp5
- new jpp release

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_11jpp5
- new version

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt3_3jpp1.7
- rebuild with backport-util-concurrent 3

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt2_3jpp1.7
branch 4.0 compatible build

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.4-alt1_3jpp1.7
- converted from JPackage by jppimport script

