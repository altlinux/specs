BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 1.0
%define name aopalliance
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/%{name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           aopalliance
Version:        1.0
Release:        alt2_7jpp6
Epoch:          0
Summary:        Java/J2EE AOP standards
Group:          Development/Java
License:        Public Domain
URL:            http://aopalliance.sourceforge.net/
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/aopalliance login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        aopalliance-src.tar.gz
Source1:        http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
Source2:        aopalliance-component-info.xml
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.6.5
BuildArch:      noarch
Source44: import.info

%description
Java/J2EE AOP standards

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n aopalliance

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc

%install
install -dm 755 %{buildroot}%{_javadir}

install -pm 644 build/aopalliance.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
install -dm 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap aopalliance aopalliance %{version} JPP %{name}

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/aopalliance.jar
%endif

%files
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_7jpp6
- new jpp relase

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp6
- new jpp release

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_6jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp5
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

