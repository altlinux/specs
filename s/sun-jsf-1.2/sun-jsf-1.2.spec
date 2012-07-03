BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0

%define bname jsf
%define namedversion 1.2_04

Name:           sun-jsf-1.2
Version:        1.2.04
Release:        alt4_2jpp6
Epoch:          0
Summary:        Java Server Pages
License:        CDDL
Url:            https://javaserverfaces.dev.java.net/
Source0:        sun-jsf-1.2.04-src.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r JSF_1_2_04_BRANCH javaserverfaces-sources
#Source1:        sun-jsf-glassfish-appserv-rt.jar
Source2:        jsf-api-1.2_04.pom
Source3:        jsf-impl-1.2_04.pom

Patch0:         sun-jsf-common-ant-dependencies.patch
Patch1:         sun-jsf-common-ant-common.patch
Patch2:         sun-jsf-api-build.patch
Patch3:         sun-jsf-ri-build.patch  
Patch99:        sun-jsf-1.2-Jetty6InjectionProvider.patch

Group:          Development/Java
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-nodeps
BuildRequires:  ant-trax
BuildRequires:  ant-contrib
BuildRequires:  htmlunit
BuildRequires:  junit

BuildRequires:  annotation_1_0_api
BuildRequires:  el_1_0_api
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-logging
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  jetty6
BuildRequires:  jetty6-annotations
BuildRequires:  jetty6-plus
BuildRequires:  jsp_2_1_api
BuildRequires:  portlet-1.0-api
BuildRequires:  servlet_2_5_api
BuildRequires:  tlddoc
BuildRequires:  tomcat6-lib

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Source44: import.info

%description
JavaServer(TM) Faces technology simplifies building user 
interfaces for JavaServer applications. Developers of 
various skill levels can quickly build web applications by: 
assembling reusable UI components in a page; connecting 
these components to an application data source; and wiring 
client-generated events to server-side event handlers.

%package api
Summary:        JSF 1.2 API from %{name}
Group:          Development/Java
Provides:       jsf_1_2_api

%description api
%{summary}.

%package impl
Summary:        JSF 1.2 Implementation from %{name}
Group:          Development/Java
Requires:       %{name}-api = %{epoch}:%{version}-%{release}

%description impl
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n javaserverfaces-sources
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
for j in $(find . -name "*.java" -exec grep -l 'com\.sun\.org\.apache\.commons\.' {} \;); do
    sed -i -e 's:com\.sun\.org\.apache\.commons\.:org\.apache\.commons\.:g' $j
done

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch99 -b .sav99

ln -sf $(build-classpath ant-contrib) common/lib/
ln -sf $(build-classpath commons-beanutils) common/lib/com-sun-commons-beanutils.jar
ln -sf $(build-classpath commons-digester) common/lib/com-sun-commons-digester.jar
ln -sf $(build-classpath commons-collections) common/lib/com-sun-commons-collections.jar
ln -sf $(build-classpath commons-logging-api) common/lib/com-sun-commons-logging-api.jar

mkdir -p dependencies/jars/
ln -sf $(build-classpath tlddoc) dependencies/jars/tlddoc-1.3.jar
ln -sf $(build-classpath junit) dependencies/jars/junit-3.8.1.jar
ln -sf $(build-classpath htmlunit) dependencies/jars/htmlunit-1.10.jar
ln -sf $(build-classpath servlet_2_5_api) dependencies/jars/servlet-api-2.5.jar
ln -sf $(build-classpath jsp_2_1_api) dependencies/jars/jsp-api-2.1.jar
ln -sf $(build-classpath el_1_0_api) dependencies/jars/el-api-1.0.jar
ln -sf $(build-classpath taglibs-core) dependencies/jars/jstl-1.2.jar
ln -sf $(build-classpath annotation_1_0_api) dependencies/jars/jsr250-api-1.0.jar
ln -sf $(build-classpath portlet-1.0-api) dependencies/jars/portlet-api-1.0.jar

mkdir -p dependencies/apache-tomcat-6.0.10/lib/
ln -sf $(build-classpath tomcat6/catalina) dependencies/apache-tomcat-6.0.10/lib/

mkdir -p dependencies/jetty-6.1.2rc0/lib/annotations
ln -sf $(build-classpath jetty6/annotations/jetty6-annotations) dependencies/jetty-6.1.2rc0/lib/annotations/jetty-annotations-6.1.2rc0.jar
ln -sf $(build-classpath jetty6/jetty6) dependencies/jetty-6.1.2rc0/lib/annotations/jetty-6.1.2rc0.jar
mkdir -p dependencies/jetty-6.1.2rc0/lib/plus
ln -sf $(build-classpath jetty6/plus/jetty6-plus) dependencies/jetty-6.1.2rc0/lib/plus/jetty-plus-6.1.2rc0.jar

# TODO: bring in glassfish-appserv-rt.jar dependency
#mkdir -p dependencies/glassfish/lib/
#cp %{SOURCE1} dependencies/glassfish/lib/appserv-rt.jar
rm jsf-ri/src/com/sun/faces/vendor/GlassFishInjectionProvider.java

%build
export OPT_JAR_LIST="ant-launcher ant/ant-trax"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djsf.build.home=$(pwd) -Dcontainer.name=template main
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f jsf-api/build.xml -Djsf.build.home=$(pwd) -Dcontainer.name=template javadocs
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f jsf-ri/build.xml -Djsf.build.home=$(pwd) -Dcontainer.name=template javadocs

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 jsf-api/build/lib/%{bname}-api.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version}.jar
install -m 644 jsf-ri/build/lib/%{bname}-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-impl-%{version}.jar
%add_to_maven_depmap javax.faces jsf-api %{namedversion} JPP %{name}-api
%add_to_maven_depmap javax.faces jsf-impl %{namedversion} JPP %{name}-impl

(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-api.pom
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-impl.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
cp -pr jsf-api/build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr jsf-ri/build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/impl
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jsf_1_2_api_sun-jsf-1.2-api<<EOF
%{_javadir}/jsf_1_2_api.jar	%{_javadir}/%{name}-api.jar	10200
EOF

%files api
%_altdir/jsf_1_2_api_sun-jsf-1.2-api
%doc legal/jsf-cddl/*
%{_javadir}/%{name}-api*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-api-%{version}.jar.*
%endif

%files impl
%doc legal/jsf-cddl/*
%{_javadir}/%{name}-impl*.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-impl-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.04-alt4_2jpp6
- new jpp relase

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.04-alt4_1jpp5
- explicit selection of java5 compiler

* Mon Jul 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.04-alt3_1jpp5
- fixed build

* Thu Mar 19 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.04-alt2_1jpp5
- fixed alternatives

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.04-alt1_1jpp5
- converted from JPackage by jppimport script

