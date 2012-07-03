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


Name:           multithreadedtc
Version:        1.01
Release:        alt3_2jpp6
Epoch:          0
Summary:        Multithreaded TC

Group:          Development/Java
License:        BSD
URL:            http://code.google.com/p/multithreadedtc/
Source0:        http://multithreadedtc.googlecode.com/files/MultithreadedTC-1.01-source.zip
Source1:        http://repo1.maven.org/maven2/com/googlecode/multithreadedtc/multithreadedtc/1.01/multithreadedtc-1.01.pom


BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  junit

Requires:  junit

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
The MultithreadedTC framework was created to make it easier
to test small concurrent abstractions. It enables test 
designers to guarantee a specific interleaving of two or 
more threads, even in the presence of blocking and timing 
issues.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}


%prep
%setup -q  -n MultithreadedTC-%{version}-source
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
mkdir bin
export CLASSPATH=$(build-classpath junit)
%{_jvmdir}/java/bin/javac  -target 1.5 -source 1.5 -d bin $(find src -name "*.java")
%{_jvmdir}/java/bin/javadoc -d apidocs -sourcepath src edu.umd.cs.mtc

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 distjar

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 MultithreadedTC-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.googlecode.multithreadedtc %{name} %{version} JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_2jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt3_1jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.01-alt1_1jpp5
- converted from JPackage by jppimport script

