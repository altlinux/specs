AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/MD5.pm)
# END SourceDeps(oneline)
%define oldname junit
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

Name:           junit4
Version:        4.10
Release:        alt5_6jpp7
Epoch:          1
Summary:        Java regression test package
License:        CPL
URL:            http://www.junit.org/
Group:          Development/Java
BuildArch:      noarch

# git clone --bare git://github.com/KentBeck/junit.git junit.git 
# mkdir junit-4.10
# git --git-dir=junit.git --work-tree=junit-4.10 checkout r4.10
# tar cjf junit-4.10.tar.xz junit-4.10/
Source0:        %{oldname}-%{version}.tar.xz
Source1:        http://search.maven.org/remotecontent?filepath=%{oldname}/%{oldname}/%{version}/%{oldname}-%{version}.pom
Source2:        junit-OSGi-MANIFEST.MF
Patch0:         %{oldname}-removed-test.patch

BuildRequires:  ant
BuildRequires:  ant-contrib
BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  hamcrest

Requires:       hamcrest

Source44: import.info

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck. 
It is used by the developer who implements unit tests in Java. JUnit is Open
Source Software, released under the Common Public License Version 1.0 and 
JUnit is Open Source Software, released under the IBM Public License and
hosted on SourceForge.

%package -n junit-junit4
Group:          Development/Java
Summary:        %{oldname} provider
BuildArch: noarch
Requires: %name = %epoch:%{version}-%{release}
Provides: junit = 0:%{version}
Provides: junit = %{epoch}:%{version}-%{release}
Provides: %_javadir/junit.jar

%description -n junit-junit4
Virtual junit package based on %{name}.

%package manual
Group:          Development/Java
Summary:        Manual for %{oldname}
BuildArch: noarch

%description manual
Documentation for %{oldname}.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{oldname}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{oldname}.

%package demo
Group:          Development/Java
Summary:        Demos for %{oldname}
Requires:       junit4 = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{oldname}.

%prep
%setup -q -n %{oldname}-%{version} 
%patch0 -p1
cp %{SOURCE1} pom.xml
find -iname '*.class' -o -iname '*.jar' -delete
ln -s $(build-classpath hamcrest/core) lib/hamcrest-core-1.1.jar

%build
ant dist

# inject OSGi manifest
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{oldname}%{version}/%{oldname}-%{version}.jar META-INF/MANIFEST.MF

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 %{oldname}%{version}/%{oldname}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# Many packages still use the junit4.jar directly
ln -s %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/%{oldname}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr %{oldname}%{version}/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/demo/%{name} 

cp -pr %{oldname}%{version}/%{oldname}/* %{buildroot}%{_datadir}/%{name}/demo/%{name}


mkdir -p %buildroot%_altdir
cat >>%buildroot%_altdir/%{name}<<EOF
%{_javadir}/junit.jar	%{_javadir}/%{name}.jar	4100
EOF

%files
%doc cpl-v10.html README.html
#%{_javadir}/%{oldname}.jar
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files demo
%doc cpl-v10.html
%{_datadir}/%{name}

%files javadoc
%doc cpl-v10.html
%doc %{_javadocdir}/%{name}

%files manual
%doc cpl-v10.html
%doc junit%{version}/doc/*

%files -n junit-junit4
%_altdir/%{name}

%changelog
* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.10-alt5_6jpp7
- bumped epoch for junit-junit4

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt4_6jpp7
- made junit-junit4 provider default

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt3_6jpp7
- added junit-junit4 provider

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt2_6jpp7
- added OSGi manifest

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt1_6jpp7
- new version

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
