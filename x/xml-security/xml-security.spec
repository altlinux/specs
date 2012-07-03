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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/org/apache/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           xml-security
Version:        1.4.3
Release:	alt3_0jpp6
Epoch:          0
Summary:        Implementation of W3C security standards for XML
License:        ASL 2.0
URL:            http://santuario.apache.org/
Group:          Development/Java
Source0:        http://santuario.apache.org/dist/java-library/xml-security-src-1_4_3.zip
Source1:        xml-security-component-info.xml
Source2:        http://repository.jboss.org/maven2/org/apache/xmlsec/1.4.3/xmlsec-1.4.3.pom
Patch0:         xml-security-build_xml.patch
Patch1:         xml-security-disable-test-fail.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jakarta-commons-logging
Requires: log4j
Requires: xalan-j2 >= 0:2.7
Requires: xml-commons-jaxp-1.3-apis >= 0:1.3
Requires: xerces-j2 >= 0:2.7
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: ant-trax
BuildRequires: jakarta-commons-logging
BuildRequires: log4j
BuildRequires: xalan-j2 >= 0:2.7
BuildRequires: xml-commons-jaxp-1.3-apis
BuildRequires: xerces-j2 >= 0:2.7
BuildArch:      noarch

%description
The XML Security project is aimed at providing implementation 
of security standards for XML. Currently the focus is on the 
W3C standards :
- XML-Signature Syntax and Processing; and
- XML Encryption Syntax and Processing.
Once these are implemented, XML Key Management is likely to 
be the next focus for the project.
Two libraries are currently available.
A Java library, which includes a mature Digital Signature 
implementation. Encryption is currently under development.
A C++ library is also now available. Functionality is 
currently more basic than that provided by the Java library.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides: %name-repolib = 0:1.4.2

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
Javadoc for %{name}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation

%description demo
Samples for %{name}.

%prep
%setup -q -n xml-security-1_4_3
%patch0 -p0
%patch1 -p0

mkdir -p libs/endorsed
pushd libs
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath commons-logging-api)
ln -s $(build-classpath junit)
ln -s $(build-classpath log4j)
ln -s $(build-classpath xalan-j2)
ln -s $(build-classpath xalan-j2-serializer)
ln -s $(build-classpath xerces-j2)
ln -s $(build-classpath xml-commons-jaxp-1.3-apis)
popd

%build
export CLASSPATH=
export OPT_JAR_LIST="junit ant/ant-junit jaxp_transform_impl ant/ant-trax xalan-j2-serializer"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djava.endorsed.dirs=libs -Dlib.xalan.3=libs/xml-commons-jaxp-1.3-apis.jar build.src build.jar build.docs
# FIXME: (dwalluck) AES key size above 128 will fail with default Sun JCE provider policy
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djava.endorsed.dirs=libs -Dlib.xalan.3=libs/xml-commons-jaxp-1.3-apis.jar test

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/xmlsec-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xmlsec-%{version}.jar
install -m 644 build/xmlsecSamples-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-samples-%{version}.jar
ln -s %{name}-samples-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xmlsecSamples-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/html/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache xmlsec %{version} JPP %{name}
%add_to_maven_depmap org.apache.santuario xmlsec %{version} JPP %{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr src_samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/xmlsec.jar
%endif
%if %with repolib
%define compatrepodir %{_javadir}/repository.jboss.com/apache-xmlsec/%{version}-brew
install -d -m 755 $RPM_BUILD_ROOT%{compatrepodir}/
ln -s $(relative %{repodir}/lib %{compatrepodir}/lib) $RPM_BUILD_ROOT%{compatrepodir}/lib
ln -s $(relative %{repodir}/src %{compatrepodir}/src) $RPM_BUILD_ROOT%{compatrepodir}/src
cp -a $RPM_BUILD_ROOT%{repodir}/component-info.xml $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
sed -i s,org/apache,apache-xmlsec, $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
%endif


%files
%doc LICENSE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/xmlsec-%{version}.jar
%{_javadir}/xmlsec.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_javadir}/%{name}-samples-%{version}.jar
%{_javadir}/%{name}-samples.jar
%{_javadir}/xmlsecSamples-%{version}.jar
%{_javadir}/xmlsecSamples.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_0jpp6
- added depmap for org.apache.santuario:xmlsec:jar

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_0jpp6
- added jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_0jpp6
- new version (closes: #20786)

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_5jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_2jpp5
- jpp5 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

