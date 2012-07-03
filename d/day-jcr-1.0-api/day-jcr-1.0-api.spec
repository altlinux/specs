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


Name:           day-jcr-1.0-api
Version:        1.0
Release:        alt4_2jpp6
Epoch:          0
Summary:        Content Repository for Java Technology (JSR-170) API

Group:          Development/Java
License:        Freely distributable source
URL:            http://www.jcp.org/en/jsr/detail?id=170
Source0:        http://repo1.maven.org/maven2/javax/jcr/jcr/1.0/jcr-1.0-sources.jar
Source1:        http://repo1.maven.org/maven2/javax/jcr/jcr/1.0/jcr-1.0.pom
Source2:        http://www.day.com/maven/jsr170/jars/LICENSE.txt


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7

Provides:  jcr_1_0_api = %{epoch}:%{version}-%{release}

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Specifies a standard API to access content repositories in 
JavaTM 2 independently of implementation.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}


%prep
%setup -q  -c
mkdir -p target/site/apidocs/
mkdir -p target/classes/
mkdir -p src/main/java
mv javax src/main/java
mv META-INF target/classes
cp %{SOURCE2} target/classes/META-INF/additional-LICENSE.txt


%build
#export LANG=en_US.utf8
export LANG=en_US.ISO8859-1
unset CLASSPATH

%{java_home}/bin/javac  -target 1.5 -source 1.5 -d target/classes $(find src/main/java -name "*.java")
%{java_home}/bin/javadoc -d target/site/apidocs -sourcepath src/main/java javax.jcr javax.jcr.lock javax.jcr.nodetype javax.jcr.observation javax.jcr.query javax.jcr.util javax.jcr.version

pushd target/classes
%{java_home}/bin/jar cf ../%{name}-%{version}.jar *
popd


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.jcr jcr %{version} JPP %{name}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jcr_1_0_api_day-jcr-1.0-api<<EOF
%{_javadir}/jcr_1_0_api.jar	%{_javadir}/%{name}-%{version}.jar	10000
EOF

%files
%_altdir/jcr_1_0_api_day-jcr-1.0-api
%{_javadir}/*.jar
%doc target/classes/META-INF/*LICENSE.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp6
- fixed build with java 7

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- new jpp release

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_1jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- converted from JPackage by jppimport script

