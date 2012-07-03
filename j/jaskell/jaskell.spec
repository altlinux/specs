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


Name:           jaskell
Version:        1.0
Release:        alt1_1jpp5
Epoch:          0
Summary:        Java Haskell pure functional programming language.

Group:          Development/Java
License:        BSD
URL:            http://jaskell.codehaus.org/
Source0:        http://dist.codehaus.org/jaskell/distributions/jaskell-1.0.zip
Source1:        %{name}-%{version}.pom
Patch0:         jaskell-build.patch


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit

BuildRequires: bsf
BuildRequires: jakarta-commons-lang
BuildRequires: jfunutil
BuildRequires: jparsec

Requires: jakarta-commons-lang
Requires: jfunutil
Requires: jparsec

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
There are already many cool scripting languages in jvm. 
Jython, JRuby, Groovy etc. They are all excellent and very 
practical scripting languages. Why yet another scripting 
language?
Well. Jaskell is designed not to be a better language, but 
a different one.
1. Most of the current scripting languages are Object-Oriented.
   Though they more or less have functional tastes (Ruby's 
   sexy closure, for example), the heart of them are still 
   Object-Oriented. One of the most important essenses of 
   functional programming (combinators) is yet to be brought
   into Java.
2. Jaskell brings with it higher order function, function 
   currying, pattern match and monadic combinator support.
3. Monadic combinator is ideal for designing Domain Specifi
   Language. It is relatively easy to tailor Jaskell runtime
   to make domain specific syntax look like simple atomic 
   statements. See Neptune for a real example.
4. Jaskell bridges nicely between functional interpreter and
   Java. In fact, Jaskell is nothing but a Java library that
   passes Java objects in and out of the interpreter.

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
unzip -q ../jaskell_src-1.0.zip
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath commons-lang) lib/commons-lang-2.1.jar
ln -sf $(build-classpath bsf) lib/bsf.jar
ln -sf $(build-classpath jfunutil) lib/jfunutil.jar
ln -sf $(build-classpath jparsec) lib/jparsec.jar
ln -sf $(build-classpath jparsec) lib/junit.jar

#mv lib/jparsec_old2.jar.no lib/jparsec_old2.jar
#mv lib/jparsec_old.jar.no lib/jparsec_old.jar

%patch0 -p1 -b .sav0
popd
mkdir doc
pushd doc
unzip -q ../jaskell_doc-1.0.zip
popd


%build
pushd src
ant buildlib test doc
popd

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 src/bin/jaskell.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr src/docs/jaskell/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf doc/docs/jaskell/api
cp -pr doc/docs/jaskell/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

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
* Tue Mar 17 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- first build

