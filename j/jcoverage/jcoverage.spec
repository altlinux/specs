Packager: Igor Vlasenko <viy@altlinux.ru>
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


Summary:	Java code coverage tool
URL:		http://www.jcoverage.org/
Source0:	http://www.jcoverage.org/download/jcoverage-1.0.5-src.zip
Source1:	jcoverage.pdf
# from http://www.jcoverage.org/download/jcoverage-1.0.5-bin.zip
Source2:	http://mirrors.ibiblio.org/pub/mirrors/maven2/jcoverage/jcoverage/1.0.5/jcoverage-1.0.5.pom
Patch0:		jcoverage-build.patch

Name:		jcoverage
Version:	1.0.5
Release:	alt1_4jpp5
Epoch:		0
License:	GPL
Group:		Development/Java
BuildArch:	noarch
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: bcel5.3
BuildRequires: gnu-getopt
BuildRequires: junit
BuildRequires: log4j
BuildRequires: oro
Requires: jpackage-utils >= 0:1.7.3
Requires: bcel5.3
Requires: gnu-getopt
Requires: log4j
Requires: oro
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3


%description
Everybody wants to make the practice of coding more efficient. 
However, the reality is that your productivity is inextricably 
linked with how efficiently each step of the development cycle 
is performed. Beyond just productivity in coding, there are the 
knotty tasks of running tests, gathering results, diagnosing 
failures. Each step has the potential to eat into your 
development time.
Working with jcoverage makes your job of testing software a lot 
easier. jcoverage tools allow you to run isolated tests, get 
your result quicker, diagnose where the relevant problem in an 
all-in-one solution, saving your software projects time, money 
and effort. jcoverage modifies your Java? classes at the 
bytecode level, something no other industry tool offers. 


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;
cp build.xml build.xml.sav
cp build.properties build.properties.sav

%patch0

%build
export CLASSPATH=$(build-classpath \
bcel5.3 \
gnu-getopt \
junit \
log4j \
oro
)
ant -Dbuild.sysclasspath=only

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -p -m 0644 build/eclipse/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/eclipse-%{name}-%{version}.jar
install -p -m 0644 build/eclipse/%{name}-main.jar $RPM_BUILD_ROOT%{_javadir}/eclipse-%{name}-main-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp %{SOURCE1}   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp CHANGELOG   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp CONTRIBUTORS   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp COPYING   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp COPYRIGHT   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp README   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/*
%{_docdir}/%{name}-%{version}/CHANGELOG
%{_docdir}/%{name}-%{version}/CONTRIBUTORS
%{_docdir}/%{name}-%{version}/COPYING
%{_docdir}/%{name}-%{version}/COPYRIGHT
%{_docdir}/%{name}-%{version}/README
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}/%{name}.pdf
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_4jpp5
- new jpp release

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_3jpp1.7
- converted from JPackage by jppimport script

