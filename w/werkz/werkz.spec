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


Name:           werkz
Version:        1.0
Release:        alt1_0.b10.8jpp6
Epoch:          0
Summary:        Goal-oriented process framework

Group:          Development/Java
License:        Open Source
URL:            http://werkz.codehaus.org/
Source0:        werkz-maven-1.0.tar.gz
# cvs -d :pserver:anonymous@cvs.werkz.codehaus.org:/home/projects/werkz/scm login
# cvs -z3 -d :pserver:anonymous@cvs.werkz.codehaus.org:/home/projects/werkz/scm export -r WERKZ_MAVEN_1_0-BRANCH werkz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/werkz/werkz/1.0-beta-10/werkz-1.0-beta-10.pom

BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: ant-junit
BuildRequires: junit >= 0:3.8.2
BuildRequires: apache-commons-logging
BuildRequires: jakarta-commons-jelly >= 0:1.0
BuildRequires: jakarta-commons-jelly-tags-ant >= 0:1.0
Requires: apache-commons-logging
Requires: jakarta-commons-jelly >= 0:1.0
Requires: jakarta-commons-jelly-tags-ant >= 0:1.0
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Werkz is a light-weight goal-oriented process framework.
Certain tasks, such as organizing the build-chain of a 
complex development project, can be easily modelled as a
graph of goals.  werkz is a framework that allows modelling 
of a complex graph of goals and an engine that efficiently 
and correctly attempts to satisfy requests. 
As an abstract framework, werkz imposes no particular domain
semantics or execution model. It simply manages the 
dependencies between goals and invokes application-specific 
code in the correct order. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: jakarta-commons-logging-javadoc
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-maven-%{version}
cp build.xml build.xml.sav

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath \
commons-logging \
jakarta-commons-jelly \
jakarta-commons-jelly-tags-ant)
CLASSPATH=target/classes:target/test-classes:$CLASSPATH
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only dist

%install
install -Dm 644 dist/%{name}-%{version}-beta-4.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap %{name} %{name} %{version}-beta-10 JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b10.8jpp6
- jpp 6 release

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b10.7jpp5
- new version

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b10.6jpp1.7
- converted from JPackage by jppimport script

* Sun Dec 11 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1.b10
- Rebuild for ALTLinux Sisyphus
- Spec cleanup

* Mon Aug 30 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b10.5jpp
- Build with ant-1.6.2

* Mon Aug 16 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b10.4jpp
- Restore MAVEN-branch as source

* Fri Aug 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b10.3jpp
- Void change

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:1.0-0.b10.2jpp
- Upgrade to Ant 1.6.X

* Fri Feb 13 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.b10.1jpp
- Go to a defined beta release

* Tue Jan 27 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.20040126dev.1jpp
- First JPackage release

