BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with eclipse
%bcond_with eclipse

%define reltag GA
%define namedversion %{version}.%{reltag}


Name:           hibernate3-tools
Version:        3.2.4
Release:        alt1_1jpp6
Epoch:          0
Summary:        Hibernate tools
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.hibernate.org/
# svn -q export http://anonsvn.jboss.org/repos/hibernate/tags/TOOLS_3_2_4_GA/tools/ hibernate-tools-3.2.4 && tar cjf hibernate-tools-3.2.4.tar.bz2 hibernate-tools-3.2.4
Source0:       hibernate-tools-3.2.4.tar.bz2
Source1:       http://anonsvn.jboss.org/repos/hibernate/tags/TOOLS_3_2_4_GA/common/common-build.xml
Source2:       http://anonsvn.jboss.org/repos/hibernate/tags/TOOLS_3_2_4_GA/common/checkstyle_checks.xml
Source3:       http://anonsvn.jboss.org/repos/hibernate/tags/TOOLS_3_2_4_GA/jpa-api/etc/jdstyle.css
Source4:       http://repository.jboss.org/maven2/org/hibernate/hibernate-tools/3.2.4.GA/hibernate-tools-3.2.4.GA.pom
Patch0:        hibernate3-tools-build.patch
Patch1:        hibernate3-tools-common-build.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: bsh2
Requires: freemarker
Requires: jtidy
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: antlr
BuildRequires: cglib
BuildRequires: dom4j
%if %with eclipse
BuildRequires: eclipse-jdt
BuildRequires: eclipse-platform
BuildRequires: eclipse-rcp
%endif
BuildRequires: freemarker
BuildRequires: hibernate3
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-logging
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: jtidy
BuildArch:      noarch
Source44: import.info

%description
Working with Hibernate is very easy and developers enjoy 
using the APIs and the query language. Even creating mapping 
metadata is not an overly complex task once you've mastered 
the basics. Hibernate Tools makes working with Hibernate or 
EJB 3.0 persistence even more pleasant.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n hibernate-tools-%{version}
find . -name "*.jar" | xargs -t %{__rm}
mkdir common
cp -p %{SOURCE1} common/common-build.xml
cp -p %{SOURCE2} common/checkstyle_checks.xml
mkdir -p hibernate-3.2/doc/api
cp -p %{SOURCE3} hibernate-3.2/doc/api/jdstyle.css
%patch0 -b .sav0
%patch1 -b .sav1
mkdir -p hibernate-3.2/build
ln -sf $(build-classpath hibernate3-core) hibernate-3.2/build/hibernate3.jar
mkdir -p hibernate-3.2/lib
ln -sf $(build-classpath cglib) hibernate-3.2/lib
ln -sf $(build-classpath freemarker) lib
%if %with eclipse
ln -sf %{_datadir}/eclipse/plugins/org.eclipse.core.runtime_*.jar lib
ln -sf %{_datadir}/eclipse/plugins/org.eclipse.equinox.common_*.jar lib
ln -sf %{_datadir}/eclipse/plugins/org.eclipse.jdt.core_*.jar lib
ln -sf %{_datadir}/eclipse/plugins/org.eclipse.text_*.jar lib
%else
rm src/java/org/hibernate/tool/ide/formatting/JavaFormatter.java
rm src/java/org/hibernate/tool/ant/JavaFormatterTask.java
rm -r src/test/*
%endif
ln -sf $(build-classpath ant) lib
ln -sf $(build-classpath antlr) lib
ln -sf $(build-classpath commons-collections) lib
ln -sf $(build-classpath commons-logging) lib
ln -sf $(build-classpath dom4j) lib
ln -sf $(build-classpath jtidy) lib

%build
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -p -m 644 target/hibernate-tools/hibernate-tools.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 644 target/hibernate-tools/hibernate-tools-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-tests-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests.jar

%add_to_maven_depmap org.hibernate hibernate-tools %{namedversion} JPP %{name}
cp -p %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}.pom

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/hibernate-tools/doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc *.txt
%{_javadir}/%{name}*.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.4-alt1_1jpp6
- new version

* Tue Aug 25 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt4_1jpp5
- fixed build

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt3_1jpp5
- fixed build with new eclipse

* Fri Sep 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt2_1jpp5
- fixed build

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_1jpp5
- converted from JPackage by jppimport script

