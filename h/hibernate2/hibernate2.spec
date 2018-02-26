Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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

%define base_version 2.1
%define oname hibernate

Summary:        Relational persistence and query service
Name:           hibernate2
Version:        2.1.8
Release:        alt2_1jpp5
Epoch:          0
License:        LGPL
URL:            http://www.hibernate.org/
Group:          Databases
Source0:        http://downloads.sourceforge.net/hibernate/hibernate-2.1.8.tar.gz
Source1:        http://repo1.maven.org/maven2/net/sf/hibernate/hibernate/2.1.8/hibernate-2.1.8.pom
Patch0:         hibernate-build_xml.patch
Patch1:         hibernate-FumTest.patch
Patch2:         hibernate2-EhCache.patch


BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: junit
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-swing
BuildRequires: ant-trax

BuildRequires: asm
BuildRequires: c3p0
BuildRequires: cglib >= 0:2.0
BuildRequires: jakarta-commons-collections >= 0:2.1
BuildRequires: jakarta-commons-dbcp >= 0:1.2.1
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-pool
BuildRequires: odmg = 0:3.0
BuildRequires: hsqldb >= 0:1.72
BuildRequires: dom4j
BuildRequires: j2ee_connector_1_5_api
BuildRequires: jta_1_0_1B_api
BuildRequires: log4j
BuildRequires: ehcache >= 0:1.3.0
BuildRequires: oscache
BuildRequires: proxool
BuildRequires: swarmcache
BuildRequires: jakarta-jcs
BuildRequires: jboss-cache
BuildRequires: jboss4-system >= 0:4.0.0
BuildRequires: xalan-j2
Requires: hibernate_jdbc_cache
Requires: hibernate_in_process_cache
Requires: cglib >= 0:2.0
Requires: jakarta-commons-collections >= 0:2.1
Requires: jakarta-commons-logging
Requires: odmg = 0:3.0
Requires: dom4j
Requires: jta_1_0_1B_api
Requires: xalan-j2
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
Hibernate is a powerful, ultra-high performance 
object/relational persistence and query service 
for Java. Hibernate lets you develop persistent 
objects following common Java idiom - including 
association, inheritance, polymorphism, composition 
and the Java collections framework. Extremely 
fine-grained, richly typed object models are 
possible. The Hibernate Query Language, designed 
as a "minimal" object-oriented extension to SQL, 
provides an elegant bridge between the object and 
relational worlds. Hibernate is now the most 
popular ORM solution for Java.


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

%prep
%setup -q -n %{oname}-%{base_version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

%build
(cd lib
ln -s $(build-classpath hsqldb) hsqldb.jar
)
export CLASSPATH=$(build-classpath \
c3p0 \
cglib \
commons-collections \
commons-dbcp \
commons-logging \
commons-pool \
dom4j \
ehcache \
j2ee_connector_1_5_api \
jboss-cache \
jboss4/jboss4-system \
jcs \
jta_1_0_1B_api \
odmg \
oscache \
proxool \
swarmcache \
xalan-j2 \
xalan-j2-serializer \
hsqldb \
asm/asm \
)
CLASSPATH=$CLASSPATH:build/classes:build/testclasses:etc
export OPT_JAR_LIST="ant/ant-trax xalan-j2-serializer ant/ant-swing ant/ant-junit junit"
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Dbuild.sysclasspath=only jar extras junitreport javadoc 

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp -p dist/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap net.sf.hibernate %{oname} %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc
cp -p etc/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/etc

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf doc/api

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p lgpl.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%doc %{_docdir}/%{name}-%{version}/lgpl.txt
%{_javadir}/*.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2
%{_mavendepmapfragdir}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.8-alt2_1jpp5
- selected java5 compiler explicitly

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.8-alt1_1jpp5
- new version

