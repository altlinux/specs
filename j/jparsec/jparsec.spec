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


Name:           jparsec
Version:        1.2
Release:        alt1_1jpp5
Epoch:          0
Summary:        Java Haskell Parsec parser combinator.

Group:          Development/Java
License:        BSD
URL:            http://jparsec.codehaus.org/
Source0:        http://dist.codehaus.org/jparsec/distributions/jparsec-1.2.zip
Source1:        jparsec-1.2.pom


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Jparsec is a recursive-desent parser combinator framework 
written for Java. It constructs parsers in native Java 
language only.
Jparsec stands out for its combinator nature. It is no 
parser generator like YACC or ANTLR. No extra grammar file 
is required. Grammar is written in native Java /C# 
language, which also means you can utilize all the utilities
in the Java/.Net community to get your parser fancy.
Jparsec is an implementation of Haskell Parsec on the Java 
platform.  Feature highlights:
* operator precendence grammar.
* accurate error location and customizable error message.
* rich set of pre-defined reusable combinator functions.
* declarative API that resembles BNF.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description    manual
%{summary}.


%prep
%setup -q  -c
mkdir src
pushd src
unzip -q ../jparsec_src-1.2.zip
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath jfunutil) lib/jfunutil.jar
ln -sf $(build-classpath junit) lib/junit.jar
popd
mkdir doc
pushd doc
unzip -q ../jparsec_doc-1.2.zip
popd

%build
pushd src
mkdir bin
ant buildlib test doc
popd

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 src/bin/jparsec.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr src/docs/parsec/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf doc/api
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/*.jar
%doc src/LICENSE.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp5
- new version

