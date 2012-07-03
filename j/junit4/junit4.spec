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

Name:           junit4
Version:        4.8.2
Release:        alt1_5jpp6
Epoch:          0
Summary:        Java regression test package
License:        CPL
URL:            http://www.junit.org/
Group:          Development/Java
# git clone --bare git://github.com/KentBeck/junit.git junit.git
# mkdir junit-4.8.2
# git --git-dir=junit.git --work-tree=junit-4.8.2 checkout r4.8.2
# tar cjf junit-4.8.2.tar.bz2 junit-4.8.2/
Source0:        junit-%{version}.tar.bz2
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       hamcrest
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  hamcrest
BuildArch:      noarch
Source44: import.info

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck. 
It is used by the developer who implements unit tests in Java. JUnit is Open
Source Software, released under the Common Public License Version 1.0 and 
JUnit is Open Source Software, released under the IBM Public License and
hosted on SourceForge.

%package manual
Group:          Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Group:          Development/Java
Summary:        Demos for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n junit-%{version}
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
ln -s $(build-classpath hamcrest/core) lib/hamcrest-core-1.1.jar
perl -pi -e 's/\r$//g' stylesheet.css

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dant.build.javac.source=1.5 dist

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 junit%{version}/junit-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir} 
ln -s %{name}-%{version}.jar %{name}.jar
ln -s %{name}-%{version}.jar junit-%{version}.jar
popd

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap junit junit %{version} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr junit%{version}/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/demo/junit # Not using %%name for last part because it is 
                                                                # part of package name
cp -pr junit%{version}/junit/* %{buildroot}%{_datadir}/%{name}/demo/junit

%files
%doc cpl-v10.html README.html
%{_javadir}*/%{name}.jar
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/junit-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files demo
%{_datadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc junit%{version}/doc/*

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.8.2-alt1_5jpp6
- new jpp relase

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.8.2-alt1_4jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_4jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1_1.1jpp1.7
- new version
- resolved conflict with junit3.

* Sun Mar 25 2007 Denis Smirnov <mithraen@altlinux.ru> 4.1-alt2
- Update from upstream
- Add conflict with junit 3.8

* Sun Jul 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 4.1-alt1
- New package for JUnit 4.x
- Patch0: ignore a test relying on Java VM exit code that fails
- Relocated samples to /usr/share/junit4
