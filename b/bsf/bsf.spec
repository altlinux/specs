BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 2.4.0
%define name bsf
# Copyright (c) 2000-2011, JPackage Project
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-bsf/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           bsf
Version:        2.4.0
Release:        alt3_11jpp6
Epoch:          1
Summary:        Bean Scripting Framework
License:        ASL 2.0
Group:          Development/Java
URL:            http://jakarta.apache.org/bsf/
#Source0:       http://archive.apache.org/dist/jakarta/bsf/source/bsf-src-2.4.0.tar.gz
# <https://issues.apache.org/jira/browse/BSF-12>
# Also missing xdocs
# svn export http://svn.apache.org/repos/asf/jakarta/bsf/tags/bsf-2.4.0
Source0:        bsf-2.4.0.tar.bz2
Source1:        bsf-component-info.xml
Source2:        bsf-2.4.0.pom
Patch0:         bsf-javadoc-crosslink.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:       jakarta-commons-logging
Requires:       jpackage-utils
Requires:       jsp_2_1_api
Requires:       xalan-j2
Requires:       servlet_2_5_api
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-logging-javadoc
BuildRequires:  java-javadoc
BuildRequires:  jpackage-utils
BuildRequires:  jsp_2_1_api
BuildRequires:  jacl
BuildRequires:  jython
BuildRequires:  rhino
BuildRequires:  servlet_2_5_api
BuildRequires:  velocity14
BuildRequires:  xalan-j2
BuildArch:      noarch
Source44: import.info
%add_findreq_skiplist /usr/share/bsf-*

%description
Bean Scripting Framework (BSF) is a set of Java classes which provides
scripting language support within Java applications, and access to Java
objects and methods from scripting languages. BSF allows one to write
JSPs in languages other than Java while providing access to the Java
class library. In addition, BSF permits any Java application to be
implemented in part (or dynamically extended) by a language that is
embedded within it. This is achieved by providing an API that permits
calling scripting language engines from within Java, as well as an
object registry that exposes Java objects to these scripting language
engines.

BSF supports several scripting languages currently:
* Javascript (using Rhino ECMAScript, from the Mozilla project)
* Python (using either Jython or JPython)
* Tcl (using Jacl)
* NetRexx (an extension of the IBM REXX scripting language in Java)
* XSLT Stylesheets (as a component of Apache XML project's Xalan and
Xerces)

In addition, the following languages are supported with their own BSF
engines:
* Java (using BeanShell, from the BeanShell project)
* JRuby
* JudoScript

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
Manual for %{name}.

%prep
%setup -q
%patch0 -p1 -b .sav0
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__rm} -r docs/
%{__perl} -pi -e 's/\r$//g' samples/scriptedui/ui.{jacl,py}

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath commons-logging jacl jsp_2_1_api jython rhino servlet_2_5_api xalan-j2)
export CLASSPATH=${CLASSPATH}:$(build-classpath excalibur/avalon-logkit commons-collections commons-lang jdom velocity14)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Djava.javadoc=%{_javadocdir}/java -Dcommons.logging.javadoc=%{_javadocdir}/jakarta-commons-logging all \
%if 0
test
%endif

%install

# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -p -m 644 dist/bsf-%{version}/lib/bsf.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

# pom and depmap frag
%{__install} -d -m 755 %{buildroot}%{_datadir}/maven2/poms
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-bsf.pom
%add_to_maven_depmap bsf bsf %{version} JPP %{name}

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/bsf-%{version}/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -s %{name}-%{version} %{name})

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/bsf.jar %{buildroot}%{repodirlib}
%endif

%files
%doc dist/bsf-%{version}/{AUTHORS.txt,BUILDING.txt,CHANGES.txt,INSTALL.txt,LICENSE.txt,NOTICE.txt,README.txt,RELEASE-NOTE.txt,samples/,TODO.txt}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc docs/*

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Jan 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt3_11jpp6
- restored repolib

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt2_11jpp6
- new jpp relase

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt2_2jpp6
- fixed repolib

* Fri Jan 07 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.4.0-alt1_2jpp6
- new version

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 1:2.3.0-alt1_13jpp5
- downgrade to match 5.0; added repolib

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt4_1jpp1.7
branch 4.0 compatible build

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt3_1jpp1.7
- do disabled python findreq on jython code
- added commons-lang dependency

* Tue Nov 27 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt2_1jpp1.7
- disabled python findreq on jython code

* Sun Nov 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_1jpp1.7
- updated to new jpackage release

* Mon Oct 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_11jpp1.7
- resurrected from orphaned
- added obsolete jakarta-bsf

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_11jpp1.7
- converted from JPackage by jppimport script

