BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

%define repodir %{_javadir}/repository.jboss.com/com/sun/xml/stream/%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

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

%define base_name sjsxp
%define api_version 1.0

Name:           sun-sjsxp
Version:        1.0
Release:        alt1_1jpp6
Epoch:          0
Summary:        SJSXP is an efficient implementation of the StAX API 
Group:          Development/Java
License:        CDDL v1.0 and GPL v2
URL:            https://sjsxp.dev.java.net/
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r sjsxp-1_0-FCS -d sun-sjsxp-1.0 sjsxp/zephyr && tar cjf sun-sjsxp-1.0.tar.bz2 sun-sjsxp-1.0
Source0:        sun-sjsxp-1.0.tar.bz2
Source1:        sjsxp.pom
Source5:	sun-sjsxp-component-info.xml
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: junit >= 0:3.8.1
BuildRequires: stax_1_0_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
The Sun Java Streaming XML Parser (SJSXP) is an efficient implementation of the
StAX API which is fully compliant with the XML 1.0 and Namespace 1.0
specifications.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

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
rm -r lib/*
ln -s $(build-classpath stax_1_0_api) lib/jsr173_1.0_api.jar
ln -s $(build-classpath stax_1_0_api) lib/jsr173_api.jar
ln -s $(build-classpath junit) lib/junit.jar

%build
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
%{ant} jar javadocs

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build/sjsxp.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{base_name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `/bin/echo ${jar} | sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
%if 0
install -p -m 644 etc/poms/sjsxp.pom %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%{__sed} -i "s/@VERSION@/%{version}/g" %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%{__sed} -i "s/@API_VERSION@/%{api_version}/g" %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%else
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%endif
%add_to_maven_depmap com.sun.xml.stream sjsxp %{version} JPP %{name}

%if %with repolib
install -d -m 755 %{buildroot}%{repodir}
install -d -m 755 %{buildroot}%{repodirlib}
install -p -m 644 %{SOURCE5} %{buildroot}%{repodir}/component-info.xml
tag=`echo %{version}-brew`
sed -i "s/@VERSION@/$tag/g" %{buildroot}%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
install -d -m 755 %{buildroot}%{repodirsrc}
install -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
cp -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/sjsxp.jar
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/sjsxp.pom
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc README
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{base_name}-%{version}.jar
%{_javadir}/%{base_name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.db
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.so
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp6
- new version

