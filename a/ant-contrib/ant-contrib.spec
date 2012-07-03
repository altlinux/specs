BuildRequires: ant-junit
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

#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           ant-contrib
Version:        1.0
Release:        alt4_1.b3.2jpp6
Epoch:          0
Summary:        Collection of tasks for Ant
License:        ASL 2.0
URL:            http://ant-contrib.sourceforge.net/
Group:          Development/Java
Source0:        http://prdownloads.sourceforge.net/ant-contrib/ant-contrib-1.0b3-src.tar.gz
Source1:        ant-contrib-1.0b3.pom
Patch0:         ant-contrib-build_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: ant >=  1.6.5
Requires: bcel >= 0:5.1
Requires: ivy >= 0:1.3.1
Requires: jakarta-commons-cli
Requires: jakarta-commons-codec
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-logging
Requires: junit >= 3.8.2
Requires: oro
Requires: xerces-j2
BuildRequires: ant >=  1.6.5
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: bcel >= 0:5.1
BuildRequires: ivy >= 0:1.3.1
BuildRequires: jakarta-commons-cli
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-logging
BuildRequires: jpackage-utils
BuildRequires: junit >= 3.8.2
BuildRequires: oro
BuildRequires: xerces-j2
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
The Ant-Contrib project is a collection of tasks 
(and at one point maybe types and other tools) 
for Apache Ant.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Docs for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n %{name}
%patch0 -p0 -b .sav0

%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%{__ln_s} $(build-classpath ant) lib/ant/jars/ant-1.6.5.jar
%{__ln_s} $(build-classpath bcel) lib/bcel/jars/bcel-5.1.jar
%{__ln_s} $(build-classpath commons-cli) lib/commons-cli/jars/commons-cli-1.0.jar
%{__ln_s} $(build-classpath commons-codec) lib/commons-codec/jars/commons-codec-1.3.jar
%{__ln_s} $(build-classpath commons-httpclient) lib/commons-httpclient/jars/commons-httpclient-3.0.1.jar
%{__ln_s} $(build-classpath commons-logging) lib/commons-logging/jars/commons-logging-1.0.4.jar
%{__ln_s} $(build-classpath ivy) lib/ivy/jars/ivy-1.3.1.jar
%{__ln_s} $(build-classpath junit) lib/junit/jars/junit-3.8.1.jar
%{__ln_s} $(build-classpath oro) lib/oro/jars/oro-2.0.8.jar
%{__ln_s} $(build-classpath xerces-j2) lib/xercesImpl/jars/xercesImpl-2.6.2.jar

%build
export CLASSPATH=$(build-classpath bcel)
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/{junit,nodeps}`"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first test

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/ant-contrib.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap ant-contrib ant-contrib 1.0b3 JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr target/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr target/docs/* %{buildroot}%{_docdir}/%{name}-%{version}
%{__rm} -r %{buildroot}%{_docdir}/%{name}-%{version}/api

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc docs/LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif


%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_1.b3.2jpp6
- new jpp release

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_1.b3.1jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.b3.1jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b3.1jpp5
- converted from JPackage by jppimport script

* Wed Aug 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b2.2jpp1.7
- converted from JPackage by jppimport script

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b2.1jpp1.7
- converted from JPackage by jppimport script

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b2.1jpp1.7
- converted from JPackage by jppimport script

* Thu Jul 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b2.1jpp1.7
- converted from JPackage by jppimport script

