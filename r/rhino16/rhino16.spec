# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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


%define cvs_version     1_6R7
%define archive_version 1_6R7
%define oname rhino

Name:           rhino16
Version:        1.6
Release:        alt1_1.r7.2jpp6
Epoch:          0
Summary:        JavaScript for Java
License:        MPL
Source0:        ftp://ftp.mozilla.org/pub/mozilla.org/js/rhino%{archive_version}.zip
Source1:        http://java.sun.com/products/jfc/tsc/articles/treetable2/downloads/src.zip
Source2:        rhino16.script
Source3:        rhino16-debugger.script
Source4:        rhino16-idswitch.script
Source5:        rhino16-jsc.script
Source6:        rhino16-js.pom
Source7:        rhino16.pom

URL:            http://www.mozilla.org/rhino/
Group:          Development/Java

Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

Requires:       stax_1_0_api
Requires:       xmlbeans
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  stax_1_0_api
BuildRequires:  xmlbeans
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

This version contains Dojo's JavaScript compression patch.

%package demo
Summary:        Examples for %{name}
Group:          Development/Java

%description demo
Examples for %{name}.

%package manual

Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{oname}%{archive_version}

# Fix build
%{__perl} -pi -e 's|.*<get.*src=.*>\n||' build.xml testsrc/build.xml toolsrc/org/mozilla/javascript/tools/debugger/build.xml xmlimplsrc/build.xml
%{__install} -D -m 644 %{SOURCE1} toolsrc/org/mozilla/javascript/tools/debugger/downloaded/swingExSrc.zip

# Fix manifest
%{__perl} -pi -e 's|^Class-Path:.*\n||g' src/manifest

# Add jpp release info to version
%{__perl} -pi -e 's|^implementation.version: Rhino .* release .* \${implementation.date}|implementation.version: Rhino %{version} release %{release} \${implementation.date}|' build.properties

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dxbean.jar=$(build-classpath xmlbeans/xbean) -Djsr173.jar=$(build-classpath stax_1_0_api) deepclean jar copy-all javadoc

pushd examples
export CLASSPATH=../build/%{oname}%{archive_version}/js.jar:$(build-classpath xmlbeans/xbean 2>/dev/null)
%{javac}  -target 1.5 -source 1.5 *.java
%{jar} cvf ../build/%{oname}%{archive_version}/%{oname}-examples-%{version}.jar *.class
popd

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -a build/%{oname}%{archive_version}/js.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -a build/%{oname}%{archive_version}/%{oname}-examples-%{version}.jar %{buildroot}%{_javadir}/%{name}-examples-%{version}.jar
(cd %{buildroot}%{_javadir} && %{__ln_s} %{name}-%{version}.jar js16-%{version}.jar)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `echo $jar| %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -a %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-js16.pom
%{__cp} -a %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{oname} %{oname} %{version} JPP %{name}
%add_to_maven_depmap %{oname} js %{version} JPP js16

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -a build/%{oname}%{archive_version}/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{_bindir}/find %{buildroot}%{_javadocdir}/%{name}-%{version} -type f -name '*.html' | %{_bindir}/xargs %{__perl} -pi -e 's/\r$//g'

# scripts
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
%{__install} -p -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-debugger
%{__install} -p -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}-idswitch
%{__install} -p -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/%{name}-jsc

# examples
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -a examples/* %{buildroot}%{_datadir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-debugger
%attr(0755,root,root) %{_bindir}/%{name}-idswitch
%attr(0755,root,root) %{_bindir}/%{name}-jsc

%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*
%endif
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*
%config(noreplace,missingok) /etc/%{name}.conf

%files demo
%{_datadir}/%{name}

%files manual
%if 0
%doc build/%{name}%{archive_version}/docs/*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_1.r7.2jpp6
- new jpp relase

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_1.r7.1jpp5
- compat build

