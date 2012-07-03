BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 3.2.76
%define name berkeleydb-je32
# Copyright (c) 2000-2010, JPackage Project
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

#def_with repolib
%bcond_with repolib

%define repodir %{_javadir}/repository.jboss.com/sleepycat/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           berkeleydb-je32
Version:        3.2.76
Release:        alt1_2jpp6
Epoch:          0
Summary:        Berkeley DB Java Edition
Group:          Development/Java
License:        BSD-style License
URL:            http://www.oracle.com/technology/products/berkeley-db/index.html
Source0:        http://download.oracle.com/berkeley-db/je-3.2.76.tar.gz
Source1:        http://download.oracle.com/maven/com/sleepycat/je/3.2.76/je-3.2.76.pom
Source2:        berkeleydb-je3-component-info.xml
Patch0:         berkeleydb-je3-build_xml.patch
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Requires:       j2ee_connector_1_5_api
BuildRequires:  jpackage-utils >= 0:5.0.0
BuildRequires:  ant >= 0:1.7
BuildRequires:  ant-junit
BuildRequires:  ant-trax
BuildRequires:  junit
BuildRequires:  j2ee_connector_1_5_api
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
Javadoc for %{name}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
Documents for %{name}.

%package        demo
Summary:        Examples for %{name}
Group:          Development/Documentation

%description    demo
Examples for %{name}.

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
%patch0 -b .sav0
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
export CLASSPATH=
export OPT_JAR_LIST="ant/ant-trax ant/ant-junit junit j2ee_connector_1_5_api"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dj2ee.jarfile=$(build-classpath j2ee_connector_1_5_api) \
  jar javadoc-all 
# jar javadoc-all test-j2ee

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/lib/je.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/je32-%{version}.jar
ln -s je32-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/je32.jar

# pom
mkdir -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap com.sleepycat je JPP %{name}

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/java/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/je32-%{version}
ln -s je32-%{version} $RPM_BUILD_ROOT%{_javadocdir}/je32
# FIXME: (dwalluck): This breaks rpmbuild -bi --short-circuit
rm -rf docs/java

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -pr docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}

# demo
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/examples
cp -pr examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}/examples

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}.%{reltag}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{repodirlib}/je.jar
%endif

%files
%doc LICENSE README
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/je32-%{version}.jar
%{_javadir}/je32.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/je32-%{version}
%{_javadocdir}/je32

%files manual
%doc %{_docdir}/%{name}

%files demo
%{_datadir}/%{name}/examples

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.2.76-alt1_2jpp6
- new jpp relase

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.76-alt1_1jpp6
- new version

