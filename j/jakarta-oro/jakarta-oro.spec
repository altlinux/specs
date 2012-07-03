AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

%define base_name oro

Name:           jakarta-oro
Version:        2.0.8
Release:	alt2_6jpp6
Epoch:          0
Summary:        Full regular expressions API
License:        ASL 1.1
Group:          Development/Java
URL:            http://jakarta.apache.org/oro/
Source0:        http://archive.apache.org/dist/jakarta/oro/jakarta-oro-2.0.8.tar.gz
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/oro/oro/2.0.8/oro-2.0.8.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
Provides:       oro = %{epoch}:%{version}-%{release}
Obsoletes:      oro < %{epoch}:%{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info
Source45: jakarta-oro-2.0.8.jar-OSGi-MANIFEST.MF

%description
The Jakarta-ORO Java classes are a set of text-processing Java classes
that provide Perl5 compatible regular expressions, AWK-like regular
expressions, glob expressions, and utility classes for performing
substitutions, splits, filtering filenames, etc. This library is the
successor to the OROMatcher, AwkTools, PerlTools, and TextTools
libraries from ORO, Inc. (www.oroinc.com). They have been donated to the
Jakarta Project by Daniel Savarese (www.savarese.org), the copyright
holder of the ORO libraries. Daniel will continue to participate in
their development under the Jakarta Project.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Provides:       oro-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      oro-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dfinal.name=%{base_name} jar javadocs

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p %{base_name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && %{__ln_s} %{name}-%{version}.jar %{base_name}-%{version}.jar)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{base_name}-%{version}
%{__ln_s} %{base_name}-%{version} %{buildroot}%{_javadocdir}/%{base_name}

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap oro oro %{version} JPP %{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

# inject OSGi manifest jakarta-oro-2.0.8.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
zip -u %buildroot/usr/share/java/jakarta-oro.jar META-INF/MANIFEST.MF
# end inject OSGi manifest jakarta-oro-2.0.8.jar-OSGi-MANIFEST.MF

%files
%doc COMPILE ISSUES README TODO CHANGES CONTRIBUTORS LICENSE STYLE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{base_name}-%{version}.jar
%{_javadir}/%{base_name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/jakarta-oro-2.0.8.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/%{base_name}-%{version}
%{_javadocdir}/%{base_name}

%changelog
* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt2_6jpp6
- added osgi manifest

* Thu Feb 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_6.3jpp5
- build for new eclipse version

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.8-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.8-alt1
- New upstream release

* Tue Sep 16 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.0.7-alt1
- Adapted for Sisyphus from JPackage project.
