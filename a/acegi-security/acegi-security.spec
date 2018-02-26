BuildRequires: aspectj jmock
BuildRequires: servletapi4 backport-util-concurrent
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

%define gcj_support 0
%define _full_build 0
%define full_build %{?_with_full_build:1}%{!?_with_full_build:%{?_without_full_build:0}%{!?_without_full_build:%{?_full_build:%{_full_build}}%{!?_full_build:0}}}


Summary:        ACEGI spring security
Name:           acegi-security
Version:        1.0.7
Release:        alt8_2jpp5
Epoch:          0
Group:          Development/Java
License:        Apache License 2.0
URL:            http://www.acegisecurity.org/
Source0:        acegi-security-1.0.7.tar.gz
# svn export http://acegisecurity.svn.sourceforge.net/svnroot/acegisecurity/spring-security/tags/acegi-security-parent-1.0.7/ acegi-security-1.0.7


Source1:        %{name}-jpp-depmap.xml
Source2:        %{name}-settings.xml

Patch0:         acegisecurity-core-pom.patch
Patch1:         acegisecurity-adapters-cas-pom.patch
Patch2:         acegisecurity-nojetty.patch
Patch3:         acegisecurity-adapters-jboss-pom.patch
Patch4:         acegisecurity-noresin.patch
Patch5:         acegisecurity-nocas.patch
Patch6:         acegisecurity-nosamples.patch
Patch7:         acegisecurity-nospringldap.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-clean
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-deploy
BuildRequires: maven2-plugin-eclipse
BuildRequires: maven2-plugin-help
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven2-plugin-war
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin
BuildRequires: docbkx

BuildRequires: apacheds10-core
BuildRequires: apacheds-shared-ldap
BuildRequires: cas-client
BuildRequires: ehcache
BuildRequires: hsqldb
BuildRequires: jakarta-commons-modeler
BuildRequires: jakarta-taglibs-standard
#BuildRequires: jboss4-common
#BuildRequires: jboss4-security
BuildRequires: slf4j
BuildRequires: spring-aop
BuildRequires: spring-core
BuildRequires: spring-jdbc
BuildRequires: spring-ldap
BuildRequires: spring-mock
BuildRequires: spring-remoting
BuildRequires: spring-web
BuildRequires: tomcat5


Requires: ehcache
Requires: jakarta-taglibs-standard
Requires: slf4j
Requires: spring-aop
Requires: spring-core
Requires: spring-jdbc
Requires: spring-mock
Requires: spring-remoting
Requires: spring-web

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
Acegi Security is an open source project that provides 
comprehensive authentication and authorisation services for 
enterprise applications based on The Spring Framework. Acegi 
Security can authenticate using a variety of pluggable 
providers, and can authorise both web requests and method 
invocations. Acegi Security provides an integrated security 
approach across these various targets, and also offers 
access control list (ACL) capabilities to enable individual 
domain object instances to be secured. At an implementation 
level, Acegi Security is managed through Spring's inversion 
of control and lifecycle services, and actually enforces 
security using interception through servlet Filters and Java 
AOP frameworks. In terms of AOP framework support, Acegi 
Security currently supports AOP Alliance (which is what the 
Spring IoC container uses internally) and AspectJ, although 
additional frameworks can be easily supported.

%package adapter-catalina
Group:          Development/Java
Summary:        Catalina adapter for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jakarta-commons-modeler
Requires: tomcat5-server-lib

%description adapter-catalina
%{summary}.

%package adapter-jboss
Group:          Development/Java
Summary:        JBoss adapter for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jboss4-common
Requires: jboss4-security

%description adapter-jboss
%{summary}.

%if %{full_build}
%package adapter-cas
Group:          Development/Java
Summary:        CAS adapter for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: cas-client

%description adapter-cas
%{summary}.

%endif

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
#for j in $(find . -name "*.jar"); do
#    mv $j $j.no
#done

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
#%patch3 -b .sav3
%patch4 -b .sav4
%if ! %{full_build}
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%endif

# alt; aspectj 1.5.4
sed -i 's,<groupId>aspectj</groupId>,<groupId>org.aspectj</groupId>,' core/pom.xml

#find . -name site.xml -delete
sed -i 's,target="_blank",,' src/site/site.xml
sed -i 's, type="footer",,' src/site/site.xml
sed -i 's, img="[^"]*",,' src/site/site.xml

sed -i 's,<targetPath>/</targetPath>,,' core/pom.xml
#find . -name 'messages_*.properties' -delete

%build
export LANG=en_US.ISO8859-1

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
	-Dmaven.test.skip=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -N antrun:run

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
	-Dmaven.test.skip=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.test.failure.ignore=true \
        install

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Daggregate=true \
	-Dmaven.test.skip=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
%add_to_maven_depmap org.acegisecurity acegi-security-parent %{version} JPP/%{name} parent

install -m 644 core/target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/core-%{version}.jar
install -m 644 core/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%add_to_maven_depmap org.acegisecurity acegi-security %{version} JPP/%{name} core

install -m 644 core-tiger/target/%{name}-tiger-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/tiger-%{version}.jar
install -m 644 core-tiger/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tiger.pom
%add_to_maven_depmap org.acegisecurity acegi-security-tiger %{version} JPP/%{name} tiger

install -m 644 adapters/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-adapters.pom
%add_to_maven_depmap org.acegisecurity acegi-security-adapters %{version} JPP/%{name} adapters

install -m 644 adapters/catalina/target/%{name}-catalina-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/catalina-%{version}.jar
install -m 644 adapters/catalina/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-catalina.pom
%add_to_maven_depmap org.acegisecurity acegi-security-catalina %{version} JPP/%{name} catalina

#install -m 644 adapters/jboss/target/%{name}-jboss-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jboss-%{version}.jar
#install -m 644 adapters/jboss/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jboss.pom
#%add_to_maven_depmap org.acegisecurity acegi-security-jboss %{version} JPP/%{name} jboss

%if %{full_build}
install -m 644 adapters/cas/target/%{name}-cas-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/cas-%{version}.jar
install -m 644 adapters/cas/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-cas.pom
%add_to_maven_depmap org.acegisecurity acegi-security-cas %{version} JPP/%{name} cas
%endif

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/core*.jar
%{_javadir}/%{name}/tiger*.jar
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/core-%{version}.jar.*
%{_libdir}/gcj/%{name}/tiger-%{version}.jar.*
%endif

%files adapter-catalina
%{_javadir}/%{name}/catalina*.jar

#%files adapter-jboss
#%{_javadir}/%{name}/jboss*.jar


%if %{full_build}
%files adapter-cas
%{_javadir}/%{name}/cas*.jar

%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Fri May 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt8_2jpp5
- fixed build

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt7_2jpp5
- fixed build

* Thu Feb 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt6_2jpp5
- build w/o jboss4

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt5_2jpp5
- adapted for new aspectj

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt4_2jpp5
- fixed build

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt3_2jpp5
- build with velocity 15

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt2_2jpp5
- fixes for java6 support

* Sat Mar 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.7-alt1_2jpp5
- first build

