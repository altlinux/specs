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


Name:           jawk
Version:        1.02
Release:        alt1_1jpp5
Epoch:          0
Summary:        AWK in Java.

Group:          Development/Java
License:        GPL
URL:            http://jawk.sourceforge.net/
Source0:        http://downloads.sourceforge.net/jawk/jawk_src.1_02.jar
Source1:        jawk-1.02.pom
Source2:        jawk-jrt-1.02.pom



BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: bcel

Requires: bcel

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Jawk  is the implementation of AWK in Java. Jawk  parses, 
analyzes, and interprets and/or compiles AWK scripts. 
Compilation is targetted for the JVM.

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
unzip %{SOURCE0}

%build
export CLASSPATH=$(build-classpath bcel)
export JAVA_HOME=%{_jvmdir}/java
$JAVA_HOME/bin/javac -d target/classes $(find src/ -name "*.java")
for c in $(find target/classes/ -name "*.class" | grep -v '\$'); do
    d=$(dirname $c)
    s=$(echo $d | sed -e 's/\/classes\//\/apisrc\//')
    mkdir -p $s
    f=$(basename $c)
    j=$(echo $f | sed -e 's/\.class/\.java/')
    [ -f src/$j ] && cp src/$j $s
done
$JAVA_HOME/bin/javadoc -d target/site/apidocs -sourcepath target/apisrc org.jawk org.jawk.backend org.jawk.ext org.jawk.frontend org.jawk.intermediate org.jawk.jrt org.jawk.util


pushd target/classes
$JAVA_HOME/bin/jar cf ../%{name}-%{version}.jar *
$JAVA_HOME/bin/jar cf ../%{name}-jrt-%{version}.jar org/jawk/ext/* org/jawk/jrt/* org/jawk/util/AwkParameters.class
popd


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/
install -pm 644 target/%{name}-jrt-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
%add_to_maven_depmap %{name} jrt %{version} JPP %{name}-jrt
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -sf %{name}-jrt-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-jrt.jar


# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-jrt.pom

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
* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.02-alt1_1jpp5
- new version

