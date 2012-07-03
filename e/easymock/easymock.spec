BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 1.2
%define name easymock
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

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/%{name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           easymock
Version:        1.2
Release:        alt1_8jpp6
Epoch:          0
Summary:        Easy mock objects
Group:          Development/Java
License:        MIT
URL:            http://www.easymock.org/
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/easymock login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/easymock export -r EasyMock1_2_Java1_3 easymock
Source0:        easymock-1.2-src.tar.gz
Source1:        http://repo1.maven.org/maven2/easymock/easymock/1.2_Java1.5/easymock-1.2_Java1.5.pom
Source2:        easymock-component-info.xml
Patch0:		easymock-1.2-build_xml.patch
Requires(post): jpackage-utils >= 1.7.2
Requires(postun): jpackage-utils >= 1.7.2
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
%if %with repolib
BuildRequires: easymock-classextension
%endif
BuildRequires: junit >= 0:3.8.1
BuildArch:      noarch
Source44: import.info

%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style
of recording expectations, most refactorings will not affect the Mock Objects.
So EasyMock is a perfect fit for Test-Driven Development.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

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
%setup -q -n %{name}
%patch0 -p0
mkdir lib
pushd lib
ln -sf $(build-classpath junit) .
popd

# We no longer ship a 1.3/1.4 VM, Set it to generic javahome
rm easymockbuild.properties
echo "java\ 1.3=%{java}" >> easymockbuild.properties
echo "java\ 1.4=%{java}" >> easymockbuild.properties
echo "java\ 1.5=%{java}" >> easymockbuild.properties
echo "java\ compiler=%{javac}" >> easymockbuild.properties

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first

%install

unzip -qq %{name}%{version}_Java1.3.zip
install -dm 755 $RPM_BUILD_ROOT%{_javadir}

install -pm 644 %{name}%{version}_Java1.3/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr %{name}%{version}_Java1.3/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/
%add_to_maven_depmap easymock easymock %{version}_Java1.5 JPP easymock

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{name}.jar
%{__cp} -p %{_javadir}/easymock-classextension.jar %{buildroot}%{repodirlib}/easymockclassextension.jar
%endif

%files
%doc %{name}%{version}_Java1.3/{Documentation,License}.html
%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_8jpp6
- jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp5
- new jpackage release

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

