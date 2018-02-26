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


Name:           gnu-regexp
Version:        1.1.4
Release:        alt1_14jpp6
Epoch:          0
Summary:        Java NFA regular expression engine implementation
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.cacas.org/java/gnu/regexp/
Source0:        ftp://ftp.tralfamadore.com/pub/java/gnu.regexp-1.1.4.tar.gz
Source1:        %{name}.build.xml
Source2:        http://repo2.maven.org/maven2/gnu-regexp/gnu-regexp/1.1.4/gnu-regexp-1.1.4.pom
BuildRequires: ant >= 0:1.7.1
BuildRequires: gnu-getopt
BuildRequires: jpackage-utils >= 0:1.7.5
BuildArch:      noarch
Provides:       gnu.regexp = %{epoch}:%{version}-%{release}
Obsoletes:      gnu.regexp < %{epoch}:%{version}-%{release}
Requires: jpackage-utils >= 0:1.7.5
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
The gnu.regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep. For
a relatively complete list of supported and non-supported syntax, refer
to the syntax and usage notes.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: gnu-getopt
Provides:       gnu.regexp-demo = %{epoch}:%{version}-%{release}
Obsoletes:      gnu.regexp-demo < %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       gnu.regexp-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      gnu.regexp-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n gnu.regexp-%{version}
%__cp -a %{SOURCE1} build.xml
# remove all binary libs
find . -name "*.jar" | xargs %{__rm}

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath gnu.getopt)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc

%install
%__rm -rf %{buildroot}

# jars
%__mkdir_p %{buildroot}%{_javadir}
%__cp -a build/lib/gnu.regexp.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%__ln_s %{name}-%{version}.jar %{buildroot}%{_javadir}/gnu.regexp-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %__ln_s ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
%__mkdir_p %{buildroot}%{_datadir}/maven2/poms
%__cp -a %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# demo
%__mkdir_p %{buildroot}%{_datadir}/%{name}/gnu/regexp/util
%__cp -a build/classes/gnu/regexp/util/*.class \
  %{buildroot}%{_datadir}/%{name}/gnu/regexp/util
%__ln_s %{name} %{buildroot}%{_datadir}/gnu.regexp

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/gnu.regexp-%{version}
%__ln_s gnu.regexp-%{version} %{buildroot}%{_javadocdir}/gnu.regexp

%files
%doc COPYING COPYING.LIB README TODO docs/*.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/gnu.regexp-%{version}.jar
%{_javadir}/gnu.regexp.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files demo
%{_datadir}/%{name}
%{_datadir}/gnu.regexp

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/gnu.regexp-%{version}
%{_javadocdir}/gnu.regexp

%changelog
* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_14jpp6
- new jpp release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_13jpp5
- new jpackage release

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.4-alt1_10jpp1.7
- converted from JPackage by jppimport script

* Sat Apr 23 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus

