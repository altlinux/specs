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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/com/sun/facelets/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           facelets
Version:        1.1.15
Release:        alt1_0.b1.1jpp6
Epoch:          0
Summary:        JavaServer Faces View Definition Framework
License:        ASL 2.0
Group:          Development/Java
URL:            https://facelets.dev.java.net/
# cvs -Q -d :pserver:guest@cvs.dev.java.net:/cvs export -d facelets-1.1.15 -r milestone_1-1-15-beta facelets && tar cjf facelets-1.1.15.tar.bz2 facelets-1.1.15
Source0:        facelets-%{version}.tar.bz2
Source1:        facelets-component-info.xml
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: el_1_0_api
Requires: el-impl
Requires: jsf_1_2_api
Requires: servlet_2_4_api
BuildRequires: ant
BuildRequires: jpackage-utils
BuildRequires: el_1_0_api
BuildRequires: el-impl
BuildRequires: jsf_1_2_api
BuildRequires: servlet_2_4_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
The web community is eagerly seeking a framework like 
Tapestry, backed by JavaServer Faces as the industry 
standard. While JavaServer Faces and JSP are meant to 
be aligned,Facelets steps outside of the JSP spec and 
provides a highly performant, JSF-centric view technology. 
Anyone who has created a JSP page will be able to do the 
same with Facelets. The difference is under the hood where 
all the burden of the JSP Vendor API is removed to more 
greatly enhance JSF performance and provide easy plug-and-go 
development. Even though Facelets is being developed open 
source under Sun's guidance, it can work with any JSF 1.2 
compliant implementation or MyFaces. 

%package manual

Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t %{__rm}

mkdir lib
ln -sf $(build-classpath jsf_1_2_api) lib/jsf-api-1.2_04-p02.jar
ln -sf $(build-classpath servlet_2_4_api) lib/servlet-api-2.4.jar
ln -sf $(build-classpath el_1_0_api) lib/el-api-1.0.jar
ln -sf $(build-classpath el-impl) lib/el-impl-1.0.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} 

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/jsf-facelets.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p dist/jsf-facelets.jar %{buildroot}%{_javadir}/jsf-facelets-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `echo $jar| %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__sed} -i -e 's/@VERSION@/%{version}/' jsf-%{name}.pom
%{__cp} -a jsf-%{name}.pom $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.sun.facelets jsf-%{name} %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a build/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jsf-facelets-%{version}
%{__ln_s} jsf-facelets-%{version} %{buildroot}%{_javadocdir}/jsf-facelets

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/jsf-facelets.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_datadir}/maven2/*
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jsf-facelets-%{version}.jar
%{_javadir}/jsf-facelets.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif
%{_mavendepmapfragdir}/*

%files manual
%if 0
%doc build/%{name}%{archive_version}/docs/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/jsf-facelets-%{version}
%{_javadocdir}/jsf-facelets

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Jan 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.15-alt1_0.b1.1jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.14-alt1_2jpp5
- first build

