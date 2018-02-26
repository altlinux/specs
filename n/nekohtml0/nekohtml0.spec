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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/nekohtml/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           nekohtml0
Version:        0.9.5
Release:        alt2_2jpp6
Epoch:          0
Summary:        HTML scanner and tag balancer
License:        Apache-like
Group:          Development/Java
URL:            http://sourceforge.net/projects/nekohtml/
Source0:        http://downloads.sourceforge.net/project/nekohtml/nekohtml/nekohtml-0.9.5/nekohtml-0.9.5.tar.gz
Source1:        nekohtml-filter.sh
Source2:        nekohtml-component-info.xml
# FIXME http://anonsvn.jboss.org/repos/repository.jboss.org/maven2/nekohtml/nekohtml/0.9.1/nekohtml-0.9.1.pom -> adjusted for 0.9.5
Source3:        nekohtml-0.9.5.pom
Patch0:         nekohtml-crosslink.patch
Patch1:         nekohtml-xerces.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jpackage-utils >= 0:1.5
Requires: xerces-j2 >= 0:2.4.0
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant
BuildRequires: java-javadoc
BuildRequires: xerces-j2 >= 0:2.4.0
BuildRequires: xerces-j2-javadoc-xni
BuildRequires: xerces-j2-javadoc-impl
BuildArch:      noarch
Source44: import.info

%description
NekoHTML is a simple HTML scanner and tag balancer that enables
application programmers to parse HTML documents and access the
information using standard XML interfaces. The parser can scan HTML
files and "fix up" many common mistakes that human (and computer)
authors make in writing HTML documents.  NekoHTML adds missing parent
elements; automatically closes elements with optional end tags; and
can handle mismatched inline element tags.

NekoHTML is written using the Xerces Native Interface (XNI) that is
the foundation of the Xerces2 implementation. This enables you to use
the NekoHTML parser with existing XNI tools without modification or
rewriting code.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n nekohtml-%{version}
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1

# Clean binary JARs
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
export LANG=en_US.ISO8859-1
export CLASSPATH=$(build-classpath xerces-j2)
export OPT_JAR_LIST=:
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build-html.xml \
    -Djarfile=%{name}-%{version}.jar \
    -DjarfileXni=%{name}-xni-%{version}.jar \
    -DjarfileSamples=%{name}-samples-%{version}.jar \
    -Dj2se.javadoc=%{_javadocdir}/java \
    -Dxni.javadoc=%{_javadocdir}/xerces-j2-xni \
    -Dxerces.javadoc=%{_javadocdir}/xerces-j2-impl \
    clean jar-xni package test

%install

# Jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p bin/package/nekohtml-%{version}/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p bin/package/nekohtml-%{version}/%{name}-xni-%{version}.jar %{buildroot}%{_javadir}/%{name}-xni-%{version}.jar
%{__cp} -p bin/package/nekohtml-%{version}/%{name}-samples-%{version}.jar %{buildroot}%{_javadir}/%{name}-samples-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap nekohtml nekohtml %{version} JPP %{name}

# Scripts
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}-filter

# Javadocs
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr bin/package/nekohtml-%{version}/doc/html/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# Avoid having javadocs in %doc.
%{__rm} -rf bin/package/nekohtml-%{version}/doc/html/javadoc

# Fix link between docs and javadoc.
pushd bin/package/nekohtml-%{version}/doc/html
%{__ln_s}f %{_javadocdir}/%{name}-%{version} javadoc
popd

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH1} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/nekohtml.jar
%{__cp} -p %{SOURCE3} %{buildroot}%{repodirlib}/nekohtml.pom
%endif

%files
%doc LICENSE* README* TODO* 
%attr(0755,root,root) %{_bindir}/%{name}-filter
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-xni-%{version}.jar
%{_javadir}/%{name}-xni.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_javadir}/%{name}-samples-%{version}.jar
%{_javadir}/%{name}-samples.jar

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_2jpp6
- fixed build with java 7

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_2jpp6
- new version

