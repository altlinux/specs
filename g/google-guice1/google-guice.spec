%define oldname google-guice
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat cglib
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

%define gcj_support 0


Summary:        Dependency Injection Framework
Name:           google-guice1
Version:        1.0
Release:        alt4_0.RC2.1jpp5
Epoch:          0
Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://code.google.com/p/google-guice/
Source0:        http://google-guice.googlecode.com/files/guice-1.0-src.zip

Source1:        %{oldname}-jpp-depmap.xml
Source2:        %{oldname}-settings.xml

Patch0:         google-guice-pom.patch

#Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:%{_vendor}}
#Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin

BuildRequires: aopalliance
BuildRequires: objectweb-asm >= 0:3.0

Requires: aopalliance
Requires: objectweb-asm >= 0:3.0

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
Put simply, Guice alleviates the need for factories and the
use of new in your Java code. Think of Guice's @Inject as 
the new new. You will still need to write factories in some
cases, but your code will not depend directly on them. Your
code will be easier to change, unit test and reuse in other
contexts.
Guice embraces Java's type safe nature, especially when it 
comes to features introduced in Java 5 such as generics and
annotations. You might think of Guice as filling in missing
features for core Java. Ideally, the language itself would 
provide most of the same features, but until such a 
language comes along, we have Guice.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
#Requires(post):   /bin/rm,/bin/ln
#Requires(postun): /bin/rm
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q  -c
mkdir -p src/main/java
mv src/com src/main/java

%patch0 -b .sav0

%build
cp %{SOURCE2} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

#export JAVA_HOME=%{_jvmdir}/java-1.5.0


export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.google.inject guice %{version} JPP %{name}

install -m 644 target/guice-1.0-RC2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.RC2.1jpp5
- compat build

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.RC2.1jpp5
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.RC2.1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.RC2.1jpp5
- converted from JPackage by jppimport script

