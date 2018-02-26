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

Name:           stringtemplate22
Version:        2.2
Release:        alt1_4jpp6
Epoch:          0
Summary:        StringTemplate Template Engine
License:        BSD
Url:            http://www.stringtemplate.org/
Group:          Development/Java
Source0:        http://www.stringtemplate.org/download/stringtemplate-2.2.tar.gz
Source1:        stringtemplate-2.2.pom
Source2:        stringtemplate-2.2-build.xml
Source3:        stringtemplate-2.2-LICENSE.txt
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: antlr >= 0:2.7.2
Requires: jpackage-utils
BuildRequires: jpackage-utils
BuildRequires: ant >= 0:1.7
BuildRequires: ant-antlr
BuildRequires: antlr >= 0:2.7.2
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
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n stringtemplate-%{version}
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
ln -s $(build-classpath antlr) lib/
cp -p %{SOURCE2} build.xml
cp -p %{SOURCE3} LICENSE.txt

%build
export CLASSPATH=
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/antlr`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dversion=%{version} '-Dbuild.packages=org.antlr.stringtemplate.*' -Djavadocs.additionalparam= release

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 build/stringtemplate.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
    for jar in *-%{version}*; do ln -s ${jar} `/bin/echo $jar | sed  "s|-%{version}||g"`; done
popd
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap antlr stringtemplate %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -p -m 644 LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif 

%files
%doc LICENSE.txt
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
%{_docdir}/%{name}-%{version}

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp6
- new jpp release

