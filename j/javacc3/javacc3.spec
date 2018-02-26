BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 3.2
%define name javacc3
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

%define _with_repolib 1

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/sun-javacc/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define _basename javacc

Name:           javacc3
Version:        3.2
Release:        alt3_7jpp6
Epoch:          0
Summary:        A parser/scanner generator for java
License:        BSD
Source0:        javacc-3.2-src.tar.gz
Source1:        javacc
Source2:        jjdoc
Source3:        jjtree
Source4:        javacc-component-info.xml
Source5:        http://repo2.maven.org/maven2/net/java/dev/javacc/3.2/javacc-3.2.pom
Patch0:         javacc3-build.patch
URL:            https://javacc.dev.java.net/
Group:          Development/Java
BuildArch:      noarch
Requires:       jpackage-utils >= 0:1.7.5
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info

%description 
Java Compiler Compiler (JavaCC) is the most popular parser generator for use
with Java applications. A parser generator is a tool that reads a grammar
specification and converts it to a Java program that can recognize matches to
the grammar. In addition to the parser generator itself, JavaCC provides other
standard capabilities related to parser generation such as tree building (via
a tool called JJTree included with JavaCC), actions, debugging, etc.

%if %{with_repolib}
%package        repolib
Summary:        Artifacts to be uploaded to a repository library
Group:  Development/Java

%description    repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package manual
Summary:        Manual for %{_basename}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%package demo
Summary:        Examples for %{_basename}
Group:          Development/Documentation

%description demo
%{summary}.

%package javadoc
Summary:        Javadocs for %{_basename}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{_basename}-%{version}
%patch0 -b .sav0
cp -p %{SOURCE1} javacc3
cp -p %{SOURCE2} jjdoc3
cp -p %{SOURCE3} jjtree3
mv www/doc .

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant \
  -Dant.build.javac.source=1.4 \
  -Dversion=%{version} \
  jar javadoc

%install
rm -fr $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 bin/lib/%{_basename}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap %{_basename} %{_basename} %{version} JPP %{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms/
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-javacc3.pom

install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -m 755 javacc3 jjdoc3 jjtree3 $RPM_BUILD_ROOT/usr/bin
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr examples $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/javacc.jar
%endif

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%doc LICENSE README
#%defattr(0755,root,root,0755)
%{_bindir}/*

%files manual
%doc doc/*

%files javadoc
%{_javadocdir}/%{name}*

%files demo
%{_datadir}/%{name}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_7jpp6
- new jpp relase

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt3_6jpp6
- restored depmap fragment

* Sat Feb 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_6jpp6
- added depmap for net.java.dev.javacc:javacc

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_6jpp6
- new jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_5jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_3jpp5
- converted from JPackage by jppimport script

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

