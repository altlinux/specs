Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2012, JPackage Project
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

Name:           jsap
Version:        2.1
Release:        alt2_18.3jpp11
Summary:        A Java-based Simple Argument Parser
License:        LGPLv3+
Source0:        http://prdownloads.sourceforge.net/jsap/JSAP-2.1-src.tar.gz
Source1:        http://central.maven.org/maven2/com/martiansoftware/jsap/2.1/jsap-2.1.pom
Patch0:         jsap-javadoc.patch
Patch1:         jsap-javac.patch
URL:            http://www.martiansoftware.com/jsap/
BuildArch:      noarch

BuildRequires:  javapackages-local
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  xstream
BuildRequires:  rundoc
BuildRequires:  snip
BuildRequires:  xmlto

# /usr/share/maven-metadata needs an owner:
Requires:       javapackages-tools
Source44: import.info

%description 
JSAP not only syntactically validates your program's command line
arguments, but it converts those arguments into objects you specify. If you
tell JSAP that one of your parameters is an Integer, for example, and the
user does not provide a String that can be converted to an Integer when
invoking the program, JSAP will throw a ParseException when you have it
parse the command line. If no exception is thrown, you are guaranteed an
Integer when you request that parameter's value from your program. There's
a pretty big (and growing) list of return types supported by JSAP, including
Integers, Floats, Dates, URLs, and even java.awt.Colors; you can also add
your own in a matter of minutes.


%package javadoc
Group: Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package doc
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description doc
Manual for %{name}.

%prep
%setup -q -c

rm JSAP-%{version}/lib/ant.jar
rm JSAP-%{version}/lib/JSAP-2.1.jar
rm JSAP-%{version}/lib/junit.jar
rm JSAP-%{version}/lib/rundoc-0.11.jar
rm JSAP-%{version}/lib/snip-0.11.jar
rm JSAP-%{version}/lib/xstream-1.1.2.jar

%patch0 
%patch1 

cp %{SOURCE1} %{name}.pom

%build
mv JSAP-%{version}/* .
export CLASSPATH=%(build-classpath xstream snip rundoc junit)
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  -Dxstream.apiurl=%{_javadocdir}/xstream/core \
  jar javadoc manual
mv doc/javadoc .

# Tell XMvn which artifact belongs to which POM
%mvn_artifact %{name}.pom dist/JSAP-%{version}.jar


%install
%mvn_install -J javadoc/


%files -f .mfiles
%doc LICENSE.TXT CHANGELOG.TXT
%dir %{_datadir}/maven-poms/%{name}/
%dir %{_javadir}/%{name}/

%files javadoc -f .mfiles-javadoc
%doc LICENSE.TXT

%files doc
%doc doc/*
%doc LICENSE.TXT

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0:2.1-alt2_18.3jpp11
- new version

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_3jpp5
- explicitly use junit3

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_3jpp5
- new jpackage release

* Fri Dec 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

