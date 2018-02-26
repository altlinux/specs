# BEGIN SourceDeps(oneline):
BuildRequires: gcc-fortran
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with tests
%bcond_with tests


Summary: ANother Tool for Language Recognition
Name: antlr3
Version: 3.1.1
Release: alt1_10jpp6
URL: http://www.antlr.org/
Source0: http://www.antlr.org/download/antlr-%{version}.tar.gz
# Utility file, in conversation with upstream about this
Source1: antlr-clean-generated
Source2: antlr3
Source3: http://repo1.maven.org/maven2/org/antlr/antlr/%{version}/antlr-%{version}.pom
Source4: http://repo1.maven.org/maven2/org/antlr/antlr-runtime/%{version}/antlr-runtime-%{version}.pom
Patch0:  antlr3-build.patch
License: BSD
Group: Development/Java
BuildArch: noarch
## For cleaner script
BuildRequires: ant >= 0:1.7
BuildRequires: ant-antlr
BuildRequires: ant-apache-bcel
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: antlr
BuildRequires: bcel
BuildRequires: stringtemplate >= 3.2.1
# The build.xml uses this to version the jar
BuildRequires: bcel
BuildRequires: jpackage-utils >= 0:1.7.5
Requires: jpackage-utils >= 0:1.7.5
Requires: antlr
Requires: stringtemplate >= 3.2.1

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info

%description
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical 
descriptions containing actions in a variety of target languages.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%if 0
%package        python
Group:          Development/Java
Summary:        Python runtime support for ANTLR-generated parsers
BuildRequires:  python-devel
#BuildRequires:  python-setuptools-devel
BuildArch:      noarch

%description    python
Python runtime support for ANTLR-generated parsers
%endif

%prep
%setup -q -n antlr-%{version}
%patch0 -b .orig

%build
rm -f lib/*.jar
build-jar-repository -s -p lib stringtemplate antlr
# Clean out generated files upstream includes
%{__python} %{SOURCE1} .
# Build
export CLASSPATH=$(build-classpath bcel)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 build-all \
%if %with tests
test \
%endif
javadoc

%if 0
# Build the python runtime
cd runtime/Python
%{__python} setup.py build
cd ../..
%endif

%install
install -D build/antlr-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -D build/antlr-%{version}-runtime.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}-runtime-%{version}.jar
install -D -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/antlr3
pushd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`;
 done
popd
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.antlr antlr %{version} JPP %{name}
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-runtime.pom
%add_to_maven_depmap org.antlr antlr-runtime %{version} JPP %{name}-runtime

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if 0
cd runtime/Python
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
cd ../..
%endif

%files
%doc README.txt LICENSE.txt
%{_datadir}/java/*.jar
%{_bindir}/antlr3
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%if 0
%files python
%{python_sitelib}/antlr3/*
%{python_sitelib}/antlr_python_runtime-*
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_10jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_9jpp6
- new version

