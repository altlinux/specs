# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 3.8.2
%define name junit
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/junit/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           junit
Version:        3.8.2
Release:	alt6_9jpp6
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
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires:  ant
BuildRequires:  jpackage-utils
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
Buildarch:      noarch
%endif
Source44: import.info
Provides: junit = 0:%{version}

%description
JUnit is a regression testing framework written by Erich Gamma and Kent
Beck. It is used by the developer who implements unit tests in Java.
JUnit is Open Source Software, released under the IBM Public License and
hosted on SourceForge.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

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
%setup -q -n %{name}%{version}
%{jar} xf src.jar
%{__rm} src.jar
%{__cp} -p %{SOURCE1} build.xml
%{__rm} -r javadoc

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 dist

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p %{name}%{version}/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr %{name}%{version}/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap junit junit JPP %{name}

# demo
# Not using %%name for last part because it is part of package name
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}/demo/junit
%{__cp} -pr %{name}%{version}/%{name}/* %{buildroot}%{_datadir}/%{name}/demo/junit

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/junit.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/junit.pom
%endif

%files
%doc cpl-v10.html README.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/junit-3.8.2.jar.*
%endif

%files manual
# FIXME: (dwalluck) Manuals are usually stored in an absolute location inside %%{_docdir}
%doc %{name}%{version}/doc/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}
%if %{gcj_support}
%{_libdir}/gcj/%{name}/demo.*
%endif

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
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
