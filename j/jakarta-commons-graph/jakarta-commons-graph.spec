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

%define base_name commons-graph

Name:           jakarta-commons-graph
Version:        0.8.1
Release:        alt1_0.cvs20040118.5jpp6
Epoch:          1
Summary:        Commons Graph Package

Group:          Development/Java
License:        Apache Software License
URL:            http://cvs.apache.org/viewcvs/jakarta-commons-sandbox/graph2/
Source0:        graph2-%{version}.cvs20040118.tar.gz
Source1:        http://repo1.maven.org/maven2/commons-graph/commons-graph/0.8.1/commons-graph-0.8.1.pom
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  jdepend >= 0:2.6
BuildRequires:  apache-commons-collections >= 0:2.1
BuildRequires:  log4j >= 0:1.2.8
Requires:       jdepend >= 0:2.6
Requires:       apache-commons-collections >= 0:2.1
Requires:       log4j >= 0:1.2.8
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
Jakarta Graph is a toolkit for managing graphs and graph based data structures.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%prep
%setup -q -n graph2-%{version}.cvs20040118

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=$(build-classpath jdepend commons-collections log4j )
CLASSPATH=target/classes:target/test-classes:$CLASSPATH
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only dist

%install
install -Dm 644 dist/%{base_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}-%{version}.jar
ln -s %{base_name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{base_name}.jar
%add_to_maven_depmap %{base_name} %{base_name} %{version} JPP %{base_name}


# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_0.cvs20040118.5jpp6
- new jpp relase

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_0.cvs20040118.4jpp5
- new jpp release

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_0.cvs20040118.3jpp1.7
- updated to new jpackage release

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 1:0.8.1-alt1_0.cvs20040118.2jpp1.7
- converted from JPackage by jppimport script

* Tue May 03 2005 Vladimir Lettiev <crux@altlinux.ru> 0.8.1-alt0.1
- Rebuilt for ALT Linux Sisyphus
- spec cleanup

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:0.8.2.cvs20040118-4jpp
- Rebuild with ant-1.6.2

* Fri Aug 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.8.2.cvs20040118-3jpp
- Void change

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:0.8.2.cvs20040118-2jpp
- Upgrade to Ant 1.6.X

* Mon Jan 19 2004 Ralph Apel <r.apel at r-apel.de> - 0:0.8.2.cvs20040118-1jpp
- First JPackage release.
