%define oldname junit
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: javapackages-local
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
#

Name:           junit3
Version:        3.8.2
Release:	alt12_10jpp6
Epoch:          1
Summary:        Java regression test package
License:        CPL
Url:            http://www.junit.org/
Group:          Development/Java
#http://osdn.dl.sourceforge.net/junit/junit3.8.2.zip
Source0:        junit3.8.2.zip
Source1:        junit3.8.2-build.xml
Source2:        junit-component-info.xml
Source3:        http://repo1.maven.org/maven2/junit/junit/3.8.2/junit-3.8.2.pom
BuildRequires:  ant
Buildarch:      noarch
Source44: import.info
Conflicts: junit < 3.8.3

%description
JUnit is a regression testing framework written by Erich Gamma and Kent
Beck. It is used by the developer who implements unit tests in Java.
JUnit is Open Source Software, released under the IBM Public License and
hosted on SourceForge.

%package manual
Group:          Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
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
%setup -q -n %{oldname}%{version}
%{jar} xf src.jar
rm src.jar
cp -p %{SOURCE1} build.xml
rm -r javadoc

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6  dist

%mvn_artifact %{SOURCE3} %{oldname}%{version}/%{oldname}.jar
%mvn_compat_version : 3 %{version}

%install
%mvn_install -J %{oldname}%{version}/javadoc

# demo
# Not using %%name for last part because it is part of package name
mkdir -p %{buildroot}%{_datadir}/%{name}/demo/junit
cp -pr %{oldname}%{version}/%{oldname}/* %{buildroot}%{_datadir}/%{name}/demo/junit

%files -f .mfiles
%doc cpl-v10.html README.html

%files javadoc -f .mfiles-javadoc

%files manual
# FIXME: (dwalluck) Manuals are usually stored in an absolute location inside %%{_docdir}
%doc %{oldname}%{version}/doc/*

%files demo
%{_datadir}/%{name}

%changelog
* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 1:3.8.2-alt12_10jpp6
- java11 build

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt11_10jpp6
- fixed conflict

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt10_10jpp6
- disabled old maven support

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt9_10jpp6
- dropped junit-junit3 virtual provider - no more needed

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt8_10jpp6
- renamed to junit3; added junit-junit3 virtual provider

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt7_10jpp6
- target 5 build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt6_10jpp6
- added junit3 provides

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt6_9jpp6
- target 4

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt5_9jpp6
- fixed ant target

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt4_9jpp6
- new jpp relase

* Mon Jul 27 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt4_7jpp5
- target 1.4 to be compatible with java 1.4

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt3_7jpp5
- added repolib

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt3_4jpp1.7
- fixed major bug: the old package was not even built from sources, just unpacked :(
- resolved conflict with junit4.

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 1:3.8.2-alt3
- added JPackage stuff (required to build ant-contrib):
  Provides: junit = 0:3.8.2
  symlink to junit-3.8.2.jar

* Sun Mar 25 2007 Denis Smirnov <mithraen@altlinux.ru> 1:3.8.2-alt2
- downgrade to 3.8

* Tue Mar 20 2007 Denis Smirnov <mithraen@altlinux.ru> 4.1-alt2
- add symlink junit.jar -> junit-1.4.jar (#11160, damir@)

* Mon Mar 12 2007 Denis Smirnov <mithraen@altlinux.ru> 4.1-alt1
- 4.1

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.8.2-alt1
- 3.8.2
- Don't build as the source archive has lost build files
- Use macros from rpm-build-java
- Split off manual and demo

* Sun Aug 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 3.8.1-alt2
- Added unzip to BuildRequires

* Tue Sep 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 3.8.1-alt1
- New version
- Split out the javadoc package
- BuildRequires

* Mon May 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 3.7-alt1
- Initial package created
