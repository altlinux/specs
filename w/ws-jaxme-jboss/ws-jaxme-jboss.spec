Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%bcond_without jdk6
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-jaxme/%{version}-cvs-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define base_name jaxme

Name:           ws-%{base_name}-jboss
Version:        0.2
Release:	alt3_3jpp6
Epoch:          0
Summary:        Open source implementation of JAXB
Group:          Development/Java
License:        ASL 1.1
URL:            http://ws.apache.org/jaxme/
# svn export -r231719 http://svn.apache.org/repos/asf/webservices/jaxme/trunk ws-jaxme-0.2
# tar cjf ws-jaxme-0.2.tar.bz2 ws-jaxme-0.2
Source0:        ws-jaxme-%{version}.tar.bz2
Source1:        http://repository.jboss.org/maven2/apache-jaxme/jaxmexs/0.2-cvs/jaxmexs-0.2-cvs.pom
Source2:        ws-jaxme-component-info.xml
Patch0:         ws-jaxme-jdk16.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-apache-resolver
BuildRequires: ant-trax
BuildRequires: docbook-style-xsl
BuildRequires: hsqldb
BuildRequires: jaxp_transform_impl
BuildRequires: junit >= 0:3.8.1
BuildRequires: log4j
BuildRequires: servlet
BuildRequires: xalan-j2
BuildRequires: xmldb-api
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xml-commons-resolver12
BuildArch:      noarch

%description
A Java/XML binding compiler takes as input a schema 
description (in most cases an XML schema, but it may 
be a DTD, a RelaxNG schema, a Java class inspected 
via reflection, or a database schema). The output is 
a set of Java classes:
* A Java bean class matching the schema description. 
  (If the schema was obtained via Java reflection, 
  the original Java bean class.)
* Read a conforming XML document and convert it into 
  the equivalent Java bean.
* Vice versa, marshal the Java bean back into the 
  original XML document.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n ws-%{base_name}-%{version}
%if %with jdk6
%patch0 -p1 -b .orig
%endif
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__perl} -pi -e 's/\r$//g' prerequisites/README

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/trax`
export CLASSPATH=$(%{_bindir}/build-classpath hsqldb log4j servlet xalan-j2 xmldb-api xerces-j2 xml-commons-jaxp-1.3-apis xml-commons-resolver12 junit)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all javadoc \
  -Dbuild.sysclasspath=first \
  -Ddocbook.home=%{_datadir}/sgml/docbook \
  -Ddocbookxsl.home=%{_datadir}/sgml/docbook/xsl-stylesheets

%install

%{__mkdir_p} %{buildroot}%{_javadir}/%{base_name}-jboss

for jar in dist/*.jar; do
   jbs=`/bin/basename ${jar}`
   jnm=`/bin/echo ${jbs} | %{__sed} -e 's|\.jar||'`
   %{__cp} -p ${jar} %{buildroot}%{_javadir}/%{base_name}-jboss/ws-${jnm}-%{version}.jar
done
(cd %{buildroot}%{_javadir}/%{base_name}-jboss && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)
(cd %{buildroot}%{_javadir}/%{base_name}-jboss && for jar in ws-*.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|ws-||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{base_name}-jboss-jaxmexs.pom
%add_to_maven_depmap apache-jaxme jaxmexs %{version}-cvs JPP/%{base_name}-jboss jaxmexs

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/docs/src/documentation/content/apidocs %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if 0
# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr build/docs/src/documentation/content/manual %{buildroot}%{_docdir}/%{name}-%{version}
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-cvs-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{base_name}-jboss/jaxmexs.jar %{buildroot}%{repodirlib}/jaxmexs.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{base_name}-jboss-jaxmexs.pom %{buildroot}%{repodirlib}/jaxmexs.pom
%endif

%files
%doc LICENSE prerequisites/README
%dir %{_javadir}/%{base_name}-jboss
%{_javadir}/%{base_name}-jboss/jaxme2-%{version}.jar
%{_javadir}/%{base_name}-jboss/jaxme2-rt-%{version}.jar
%{_javadir}/%{base_name}-jboss/jaxme2-rt.jar
%{_javadir}/%{base_name}-jboss/jaxme2.jar
%{_javadir}/%{base_name}-jboss/jaxmeapi-%{version}.jar
%{_javadir}/%{base_name}-jboss/jaxmeapi.jar
%{_javadir}/%{base_name}-jboss/jaxmejs-%{version}.jar
%{_javadir}/%{base_name}-jboss/jaxmejs.jar
%{_javadir}/%{base_name}-jboss/jaxmepm-%{version}.jar
%{_javadir}/%{base_name}-jboss/jaxmepm.jar
%{_javadir}/%{base_name}-jboss/jaxmexs-%{version}.jar
%{_javadir}/%{base_name}-jboss/jaxmexs.jar
%{_javadir}/%{base_name}-jboss/ws-jaxme2-%{version}.jar
%{_javadir}/%{base_name}-jboss/ws-jaxme2-rt-%{version}.jar
%{_javadir}/%{base_name}-jboss/ws-jaxme2-rt.jar
%{_javadir}/%{base_name}-jboss/ws-jaxme2.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmeapi-%{version}.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmeapi.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmejs-%{version}.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmejs.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmepm-%{version}.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmepm.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmexs-%{version}.jar
%{_javadir}/%{base_name}-jboss/ws-jaxmexs.jar
%{_datadir}/maven2/poms/JPP.%{base_name}-jboss-jaxmexs.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

# FIXME: (dwalluck): manual requires apache forrest
%if 0
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt3_3jpp6
- new jpackage release

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt3_1jpp5
- explicitly selected java5 as default

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_1jpp5
- converted from JPackage by jppimport script

