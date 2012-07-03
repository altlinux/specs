BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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
#

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


%define base_name standard
%define short_name taglibs-%{base_name}

Name:           apache-taglibs-standard
Version:        1.1.2
Release:        alt3_8jpp6
Epoch:          0
Summary:        Open-source implementation of the JSP Standard Tag Library
License:        ASL 2.0
Group:          Development/Java
URL:            http://tomcat.apache.org/taglibs/standard/
# svn -q export http://svn.apache.org/repos/asf/tomcat/taglibs/standard/tags/standard-112/ apache-taglibs-standard-1.1.2 && tar cjf apache-taglibs-standard-1.1.2.tar.bz2 apache-taglibs-standard-1.1.2
Source0:        apache-taglibs-standard-1.1.2.tar.bz2
# FIXME: in tarball, but not SVN
Source1:        common.properties
Source2:        LICENSE
Source3:        NOTICE
#
Patch0:         apache-taglibs-standard-build.patch
Patch1:         apache-taglibs-standard-jdbc4.patch
Provides:       jakarta-taglibs-standard = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-taglibs-standard < %{epoch}:%{version}-%{release}
Requires: jpackage-utils
Requires: jsp_2_1_api
Requires: servlet_2_5_api
Requires: xalan-j2 >= 2.6.0
BuildRequires: jpackage-utils >= 0:1.5.30
BuildRequires: ant
BuildRequires: jsp_2_1_api
BuildRequires: servlet_2_5_api
BuildRequires: xalan-j2 >= 2.6.0
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
This directory contains releases for the 1.1.x versions of the Standard
Tag Library, Jakarta Taglibs's open-source implementation of the JSP
Standard Tag Library (JSTL), version 1.1. JSTL is a standard under the
Java Community Process.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildRequires: java-javadoc
Provides:       jakarta-taglibs-standard-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-taglibs-standard-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%{__cp} -p %{SOURCE1} .
%{__cp} -p %{SOURCE2} .
%{__cp} -p %{SOURCE3} .
%{__cat} > build.properties << EOF
build.dir=build
dist.dir=dist
servlet24.jar=$(%{_bindir}/build-classpath servlet_2_5_api)
jsp20.jar=$(%{_bindir}/build-classpath jsp_2_1_api)
jaxp-api.jar=$(%{_bindir}/build-classpath xalan-j2)
EOF

# XXX: old jsp
%{__rm} src/org/apache/taglibs/standard/lang/jstl/test/PageContextImpl.java
%{__rm} src/org/apache/taglibs/standard/lang/jstl/test/EvaluationTest.java

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  dist

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/standard/lib/jstl.jar %{buildroot}%{_javadir}/apache-taglibs-core-%{version}.jar
%{__cp} -p dist/standard/lib/standard.jar %{buildroot}%{_javadir}/apache-taglibs-standard-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in apache*-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|apache-|jakarta-|g"`; done)
(cd %{buildroot}%{_javadir} && for jar in apache*-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|apache-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr dist/standard/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jakarta-taglibs-standard-%{version}
%{__ln_s} jakarta-taglibs-standard-%{version} %{buildroot}%{_javadocdir}/jakarta-taglibs-standard

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc README_src.txt README_bin.txt dist/doc/doc/standard-doc/*.html dist/standard/README
%{_javadir}/apache-taglibs-core-%{version}.jar
%{_javadir}/apache-taglibs-core.jar
%{_javadir}/jakarta-taglibs-core-%{version}.jar
%{_javadir}/jakarta-taglibs-core.jar
%{_javadir}/taglibs-core-%{version}.jar
%{_javadir}/taglibs-core.jar
%{_javadir}/apache-taglibs-standard-%{version}.jar
%{_javadir}/apache-taglibs-standard.jar
%{_javadir}/jakarta-taglibs-standard-%{version}.jar
%{_javadir}/jakarta-taglibs-standard.jar
%{_javadir}/taglibs-standard-%{version}.jar
%{_javadir}/taglibs-standard.jar
%if %{gcj_support} 
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/apache-taglibs-core-%{version}.jar.*
%{_libdir}/gcj/%{name}/apache-taglibs-standard-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/jakarta-taglibs-standard-%{version}
%{_javadocdir}/jakarta-taglibs-standard

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt3_8jpp6
- built with java 6 due to abstract getParentLogger

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_8jpp6
- renamed to apache-taglibs-standard

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_7jpp5
- selected java5 compiler explicitly

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_7jpp5
- fixed build with java 5

* Mon Jul 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt4_8jpp1.7
- converted from JPackage by jppimport script

* Fri May 04 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt4
- rebuild on x86_64 

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3
- added JPackage compat stuff

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1.1-alt2
- Fixed build with j2se1.5

* Wed Mar 30 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1.1-alt1
- Initial build for ALT Linux Sisyphus

