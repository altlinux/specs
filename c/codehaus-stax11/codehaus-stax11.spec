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

%bcond_without          repolib

%define repodir_api     %{_javadir}/repository.jboss.com/stax-api/1.0-brew
%define repodir_ri      %{_javadir}/repository.jboss.com/codehaus-stax/%{version}-brew
%define repodirlib      %{repodir}/lib
%define repodirsrc      %{repodir}/src


Name:           codehaus-stax11
Version:        1.1.2
Release:        alt1_3jpp6
Epoch:          0
Summary:        Streaming API for XML
# http://www.xmlpull.org/impls.shtml
License:        ASL 2.0
Group:          Development/Java
URL:            http://stax.codehaus.org/
# svn export https://svn.codehaus.org/stax/branches/STAX_1_1_2/dev/ codehaus-stax-1.1.2 && tar cjf codehaus-stax-1.1.2.tar.bz2 codehaus-stax-1.1.2
Source0:        codehaus-stax-%{version}.tar.bz2
Source1:        codehaus-stax-component-info.xml
Source2:        codehaus-stax-api-component-info.xml
Requires: %{name}-api = %{epoch}:%{version}-%{release}
Requires: dtdparser
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: ant-trax
BuildRequires: dtdparser
BuildRequires: jpackage-utils >= 0:1.6
BuildArch:      noarch
Source44: import.info

%description
The Streaming API for XML (StAX) is a groundbreaking 
new Java API for parsing and writing XML easily and 
efficiently. 

%package api
Summary:        The StAX API
Group:          Development/Java

%description api
%{summary}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java

%description demo
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n codehaus-stax-%{version}
find -type f -name '*.jar' | xargs -t %{__rm}
%{__rm} -r src/com/wutka

%build
export CLASSPATH=$(build-classpath dtdparser)
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{junit,trax}`
%{ant} all javadoc test

export CLASSPATH=`pwd`/build/{stax-api-1.0.jar,stax-%{version}-dev.jar}
pushd src
%{javac} samples/*.java
popd

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/stax-api-1.0.jar %{buildroot}%{_javadir}/%{name}-api-%{version}.jar
%{__cp} -p build/stax-%{version}-dev.jar %{buildroot}%{_javadir}/%{name}-ri-%{version}.jar
%{__ln_s} %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
%{__ln_s} %{name}-ri-%{version}.jar %{buildroot}%{_javadir}/%{name}-ri.jar

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}
%{__cp} -pr src/samples/ %{buildroot}%{_datadir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_datadir}/%{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
%if 0
%define repodir %{repodir_ri}
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -a %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/@VERSION@/%{version}-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -a %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-ri-%{version}.jar %{buildroot}%{repodirlib}/stax.jar
%endif

%define repodir %{repodir_api}
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i 's/@VERSION@/1.0-brew/g' %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-api-%{version}.jar %{buildroot}%{repodirlib}/stax-api.jar
%endif

%files
%{_javadir}/%{name}-ri-%{version}.jar
%{_javadir}/%{name}-ri.jar

%files api
%{_javadir}/%{name}-api-%{version}.jar
%{_javadir}/%{name}-api.jar

%files demo
%{_datadir}/%{name}-%{version}
%{_datadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_3jpp6
- new jpp release

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_1jpp5
- first build

