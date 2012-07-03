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

%define gcj_support 0


Summary:        JSR-175 Backport
Name:           backport175
Version:        1.0
Release:        alt2_1jpp5
Epoch:          0
License:        Apache Software License 2.0
URL:            http://backport175.codehaus.org/
Group:          Development/Java
Source0:        http://dist.codehaus.org/backport175/distributions/backport175-1.0.zip
Source1:        http://repo1.maven.org/maven2/backport175/backport175/1.0/backport175-1.0.pom

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
BuildRequires: asm2
BuildRequires: jarjar
BuildRequires: qdox
Requires: asm2
Requires: qdox
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
Backport175 is backport of the Java 5 annotations (JSR-175)
specification. Making strongly typed annotation available 
or Java 1.3/1.4 platforms. They are bytecode compatible with 
Java 5 annotations making them available for use by tools etc.
It has two separate modules:
* Compiler - which compiles the backport175 annotations and
  puts them into the bytecode of the class (compatible with
  regular Java 5 RuntimeVisible annotations).
* Reader - which allows you to read the backport175 
  annotations as well as regular Java 5 annotation through 
  one single uniformed API. The reader also has an API for 
  runtime management, which allows you to update the bytecode 
  at runtime and have your changes propagated.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}
for j in $(find . -name "*.jar"); do
      mv $j $j.no
done
ln -sf $(build-classpath asm2/asm2) lib/asm-2.0.jar
ln -sf $(build-classpath qdox) lib/qdox-1.6-SNAPSHOT.jar
ln -sf $(build-classpath jarjar) lib/jarjar-0.3.jar
ln -sf $(build-classpath junit) lib/junit-3.8.1.jar

%build
export LANG=en_US.ISO8859-1
mkdir -p target/testcompiler-classes
mkdir -p target/testclassloader-classes
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist test doc

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

# jars
install -m 644 target/%{name}-%{version}.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-backport175.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- fixed build with java 7

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- first build

