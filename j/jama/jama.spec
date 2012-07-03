Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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


Name:           jama
Version:        1.0.2
Release:        alt1_1jpp5
Epoch:          0
Summary:        A Java Matrix Package.

Group:          Development/Java
License:        Public Domain
URL:            http://math.nist.gov/javanumerics/jama/
Source0:        http://math.nist.gov/javanumerics/jama/Jama-1.0.2.tar.gz
Source1:        jama-1.0.2.pom



BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
JAMA is a basic linear algebra package for Java. It provides
user-level classes for constructing and manipulating real, 
dense matrices.  It is meant to provide sufficient 
functionality for routine problems, packaged in a way that 
is natural and understandable to non-experts. 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
Javadoc for %{name}


%prep
%setup -T  -c
mkdir -p target/classes
mkdir -p target/site/apidocs
mkdir -p src
cd src
gzip -dc %{SOURCE0} | tar xf -

%build
export JAVA_HOME=%{_jvmdir}/java
$JAVA_HOME/bin/javac -d target/classes $(find src/ -name "*.java")
$JAVA_HOME/bin/javadoc -d target/site/apidocs -sourcepath src Jama Jama.examples Jama.test Jama.util


pushd target/classes
$JAVA_HOME/bin/jar cf ../%{name}-%{version}.jar *
popd


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_1jpp5
- new version

