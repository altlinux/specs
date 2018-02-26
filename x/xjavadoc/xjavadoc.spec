BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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

#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define repodir %{_javadir}/repository.jboss.com/xjavadoc/1.1-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           xjavadoc
Version:        1.1
Release:        alt1_9jpp6
Epoch:          0
Summary:        XJavaDoc engine
License:        BSD
URL:            http://xdoclet.sourceforge.net/xjavadoc/
Group:          Development/Java
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xdoclet login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/xdoclet export -r XJAVADOC_1_1 xjavadoc
Source0:        %{name}-src-%{version}.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xjavadoc/xjavadoc/1.1/xjavadoc-1.1.pom
Source2:        xjavadoc-component-info.xml
Patch0:         %{name}-build_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       ant
Requires:       jakarta-commons-collections
Requires:       jakarta-commons-logging
Requires:       junit
Requires:       log4j
Requires:       xalan-j2
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  ant >= 0:1.5
BuildRequires:  ant-junit
BuildRequires:  ant-nodeps
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-collections
BuildRequires:  jpackage-utils
BuildRequires:  jrefactory
BuildRequires:  junit
BuildRequires:  javacc
BuildRequires:  log4j
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
The XJavaDoc engine is a complete rewrite of Sun's 
JavaDoc engine that is faster and more suited for 
XDoclet (although it is completely standalone). It 
scans java source code and makes information about 
a class available via special java beans that are 
part of the XJavaDoc core. These beans provide the 
same information about a class as Sun's JavaDoc API, 
and some nice extra features. 

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
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
%patch0 -p0 -b .sav
find . -name "*.zip" | xargs -t rm
find . -name "*.jar" | xargs -t rm

build-jar-repository lib \
xalan-j2 \
xalan-j2-serializer \
junit \
javacc \
log4j \
commons-logging \
commons-collections \
xml-commons-apis \
jrefactory \
ant

%build
#FIXME: Fix these binary deps
#BINCLASSPATH=$PWD/lib/ConfigLog4j.jar
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{nodeps,junit}`
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djavacchome=%{_javadir} javadoc

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p target/xjavadoc-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap xjavadoc xjavadoc %{version} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 %{buildroot}%{repodir}
install -d -m 755 %{buildroot}%{repodirlib}
install -m 755 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i 's/@TAG@/$tag/g' %{buildroot}%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' %{buildroot}%{repodir}/component-info.xml
install -d -m 755 %{buildroot}%{repodirsrc}
install -m 755 %{PATCH0} %{buildroot}%{repodirsrc}
install -m 755 %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/xjavadoc.jar %{buildroot}%{repodirlib}/xjavadoc.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/xjavadoc.pom
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt docs/architecture.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_9jpp6
- new jpp relase

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_7jpp6
- added pom

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_5jpp5
- converted from JPackage by jppimport script

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

