BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.0.2
%define name hibernate3-ejb-persistence-3.0-api
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           hibernate3-ejb-persistence-3.0-api
Version:        1.0.2
Release:        alt1_6jpp6
Epoch:          1
Summary:        EJB3 persistence API
License:        LGPLv2+
Group:          Databases
URL:            http://www.hibernate.org/
# svn -q export https://svn.jboss.org/repos/hibernate/jpa-api/tags/v1_0_2_GA hibernate3-ejb-persistence-3.0-api-1.0.2 && tar cjf hibernate3-ejb-persistence-3.0-api-1.0.2.tar.bz2 hibernate3-ejb-persistence-3.0-api-1.0.2
Source0:        hibernate3-ejb-persistence-3.0-api-1.0.2.tar.bz2
Source1:        hibernate3-ext-lgpl.txt
Source2:        http://repository.jboss.org/maven2/org/hibernate/ejb3-persistence/1.0.2.GA/ejb3-persistence-1.0.2.GA.pom
Patch0:         hibernate3-ejb-persistence-3.0-api-ivy.patch
Provides:       jpa_1_0_api = %{epoch}:%{version}-%{release}
Provides:       jpa_api = 0:1.0
Requires(post): jpackage-utils
Requires(post): alternatives
Requires(postun): jpackage-utils
Requires(preun): alternatives
Requires:       jpackage-utils
BuildRequires:  ant
BuildRequires:  apache-ivy
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  maven2 >= 0:2.0.8
BuildRequires:  maven-ant-tasks
BuildArch:      noarch
Source44: import.info

%description
JSR-220 EJB 3.0 (persistence) API 1.0.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__cp} -p %{SOURCE1} lgpl.txt

%{_bindir}/build-jar-repository -s -p ivy apache-ivy maven-ant-tasks

%{__mv} etc/license.txt etc/license.txt.orig
%{_bindir}/iconv -f iso88591 -t utf8 etc/license.txt.orig > etc/license.txt

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Doffline.repository.jboss.org=$(pwd)/build deploy javadoc

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/ejb3-persistence.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p build/src.jar %{buildroot}%{_javadir}/%{name}-sources-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}.jar|.jar|g"`; done)
/bin/touch %{buildroot}%{_javadir}/jpa_api.jar
/bin/touch %{buildroot}%{_javadir}/jpa_1_0_api.jar

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.hibernate ejb3-persistence %{namedversion} JPP %{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_api_hibernate3-ejb-persistence-3.0-api<<EOF
%{_javadir}/jpa_api.jar	%{_javadir}/%{name}.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_1_0_api_hibernate3-ejb-persistence-3.0-api<<EOF
%{_javadir}/jpa_1_0_api.jar	%{_javadir}/%{name}.jar	10000
EOF

%files
%_altdir/jpa_1_0_api_hibernate3-ejb-persistence-3.0-api
%_altdir/jpa_api_hibernate3-ejb-persistence-3.0-api
%doc etc/license.txt lgpl.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-sources-%{version}.jar
%{_javadir}/%{name}-sources.jar
%exclude %{_javadir}/jpa_api.jar
%exclude %{_javadir}/jpa_1_0_api.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_6jpp6
- new jpp release

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp6
- jpp 6 release

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_4jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_2jpp5
- converted from JPackage by jppimport script

* Wed Jan 23 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_2jpp5.0
nobootstrap build

