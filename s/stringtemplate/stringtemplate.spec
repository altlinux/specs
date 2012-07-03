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

Name:           stringtemplate
Version:        3.2.1
Release:	alt1_3jpp6
Epoch:          0
Summary:        Java Template Engine
License:        BSD
Url:            http://www.stringtemplate.org/
Group:          Development/Java
Source0:        http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0:         stringtemplate-3.1-build-junit.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: antlr >= 0:2.7.2
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-antlr
BuildRequires: ant-junit
BuildRequires: antlr >= 0:2.7.2
BuildRequires: jpackage-utils
BuildRequires: junit
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
StringTemplate is a java template engine (with ports for C#
and Python) for generating source code, web pages, emails, 
or any other formatted text output. StringTemplate is 
particularly good at multi-targeted code generators, multiple 
site skins, and internationalization/localization. It evolved 
over years of effort developing jGuru.com. StringTemplate 
also generates this website and powers the ANTLR v3 code 
generator. Its distinguishing characteristic is that it 
strictly enforces model-view separation unlike other engines.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%if 0
%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q 
%patch0 -p0 -b .sav0
find . -name "*.jar" | xargs -t rm
ln -s $(build-classpath antlr) lib/

%build
export CLASSPATH=
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/{antlr,junit}`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 javadocs -Dpackages= -Djavadocs.additionalparam=

%install
# jars

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done
popd

# pom
install -p -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.antlr %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if 0
# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -p -m 644 LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -p -m 644 README.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif 

%files
%doc LICENSE.txt README.txt
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

%if 0
%files manual
%{_docdir}/%{name}-%{version}/doc
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.1-alt1_3jpp6
- new jpp release

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt4_2jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt3_2jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp5
- converted from JPackage by jppimport script

