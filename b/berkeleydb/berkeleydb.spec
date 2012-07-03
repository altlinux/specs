BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define repodir %{_javadir}/repository.jboss.com/sleepycat/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           berkeleydb
Version:        3.0.12
Release:        alt2_1jpp6
Epoch:          0
Summary:        Berkeley DB Java Edition
Group:          Development/Java
License:        BSD-style Sleepycat Public License
URL:            http://www.oracle.com/technology/software/products/berkeley-db/index.html
Source0:        http://download.oracle.com/berkeley-db/je-3.0.12.tar.gz
Source1:        http://download.oracle.com/maven/com/sleepycat/je/3.0.12/je-3.0.12.pom
Source2:        berkeleydb-component-info.xml
Patch0:         berkeleydb-junit.patch
Requires: j2ee-connector
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: geronimo-j2ee-connector-1.5-api
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: junit
BuildArch:      noarch
Source44: import.info

%description
Berkeley DB Java Edition is a high performance, transactional
storage engine written entirely in Java. Like the highly
successful Berkeley DB product, Berkeley DB Java Edition
executes in the address space of the application, without
the overhead of client/server communication. It stores data
in the application's native format, so no runtime data
translation is required. Berkeley DB Java Edition supports
full ACID transactions and recovery. It provides an easy-to-use,
programmatic interface, allowing developers to store and
retrieve information quickly, simply and reliably.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
Javadoc for %{name}

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
Documents for %{name}

%package        demo
Summary:        Examples for %{name}
Group:          Development/Documentation

%description    demo
Examples for %{name}

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
%setup -q -n je-%{version}
%{__chmod} -Rf a+rX,u+w,g-w,o-w .
%patch0 -p1 -b .junit

%build
export CLASSPATH=
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/{junit,trax}`"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
        -Djmx.jarfile=$(build-classpath mx4j/mx4j) \
        -Dj2ee.jarfile=$(build-classpath geronimo-j2ee-connector-1.5-api) \
        jar javadoc-all
#	test-j2ee

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}

install -pm 644 lib/je.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/je-%{version}.jar
ln -s je-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/je.jar

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/java/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# FIXME: (dwalluck): This breaks rpmbuild -bi --short-circuit
rm -rf docs/java

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}

# demo
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/examples
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}/examples

# pom
%add_to_maven_depmap com.sleepycat je %{version} JPP %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/je.jar
%endif

%files
%doc LICENSE README
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/je-%{version}.jar
%{_javadir}/je.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}

%files demo
%{_datadir}/%{name}/examples

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.0.12-alt2_1jpp6
- fixed build

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.0.12-alt1_1jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.90-alt1_4jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.90-alt1_3jpp5
- converted from JPackage by jppimport script

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.90-alt1_1jpp1.7
- converted from JPackage by jppimport script

