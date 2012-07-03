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

%define base_name poi
%define namedversion 3.2-FINAL

Name:           jakarta-%{base_name}
Version:        3.2
Release:        alt2_1jpp5
Epoch:          0
Summary:        Java API To Access Microsoft Format Files

Group:          Development/Java
License:        Apache Software License
URL:            http://jakarta.apache.org/poi/
Source0:        poi-src-3.2-FINAL-20081019.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi/3.2-FINAL/poi-3.2-FINAL.pom
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi-contrib/3.2-FINAL/poi-contrib-3.2-FINAL.pom
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/org/apache/poi/poi-scratchpad/3.2-FINAL/poi-scratchpad-3.2-FINAL.pom
BuildArch:      noarch

BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.1
BuildRequires: ant-trax
#BuildRequires:  jaxp_transform_impl
#BuildRequires:  ant-jdepend
#BuildRequires:  jdepend >= 0:2.6
#BuildRequires:  jakarta-commons-beanutils >= 0:1.6.1
#BuildRequires:  jakarta-commons-collections >= 0:2.1
#BuildRequires:  jakarta-commons-lang >= 0:2.0
BuildRequires: jakarta-commons-logging >= 0:1.1
BuildRequires: log4j >= 0:1.2.13
#BuildRequires:  xalan-j2 >= 0:2.5.2
#BuildRequires:  xerces-j2 >= 0:2.6.0
#Requires:  jakarta-commons-beanutils >= 0:1.6.1
#Requires:  jakarta-commons-collections >= 0:2.1
#Requires:  jakarta-commons-lang >= 0:2.0
Requires: jakarta-commons-logging >= 0:1.1
Requires: log4j >= 0:1.2.13
#Requires:  xalan-j2 >= 0:2.5.2
#Requires:  xerces-j2 >= 0:2.6.0

%description
The POI project consists of APIs for manipulating 
various file formats based upon Microsoft's OLE 2 
Compound Document format using pure Java. In short, 
you can read and write MS Excel files using Java. 
Soon, you'll be able to read and write Word files 
using Java. POI is your Java Excel solution as well 
as your Java Word solution. However, we have a 
complete API for porting other OLE 2 Compound 
Document formats and welcome others to participate. 
OLE 2 Compound Document Format based files include 
most Microsoft Office files such as XLS and DOC as 
well as MFC serialization API based file formats. 


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.


%prep
%setup -q -n poi-%{version}-FINAL
find . -name "*.jar" -exec mv {} {}.no \;

%build
export LANG=en_US.UTF-8
#export OPT_JAR_LIST="ant/ant-junit junit ant/ant-jdepend jdepend jaxp_transform_impl ant/ant-trax"
#export CLASSPATH=$(build-classpath \
#commons-beanutils \
#commons-collections \
#commons-lang \
#commons-logging \
#log4j \
#xalan-j2 \
#xerces-j2 \
#)
export CLASSPATH=$(build-classpath \
commons-logging \
log4j \
)
export ANT_OPTS="-Xmx356m -XX:MaxPermSize=256m -Djava.awt.headless=true -Dbuild.sysclasspath=first -Ddisconnected=true -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5"
ant -Dhalt.on.test.failure=false jar test

%install

install -dm 755 $RPM_BUILD_ROOT%{_javadir}
cp -p build/dist/%{base_name}-%{version}-FINAL-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
cp -p build/dist/%{base_name}-contrib-%{version}-FINAL-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-contrib-%{version}.jar
cp -p build/dist/%{base_name}-scratchpad-%{version}-FINAL-*.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-scratchpad-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in %{name}*-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.poi %{base_name} %{namedversion} JPP %{base_name}
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-contrib.pom
%add_to_maven_depmap org.apache.poi %{base_name}-contrib %{namedversion} JPP %{base_name}-contrib
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-scratchpad.pom
%add_to_maven_depmap org.apache.poi %{base_name}-scratchpad %{namedversion} JPP %{base_name}-scratchpad

#javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf docs/apidocs

#manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs # ghost symlink

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_1jpp5
- fixed build

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_1jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_2jpp5
- fixed repocop warnings

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

