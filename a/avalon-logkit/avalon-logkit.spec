Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'
%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/apache-avalon-logkit/1.2-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
%define short_name      logkit
%define short_Name      LogKit
%define name            avalon-%{short_name}
%define version         1.2
%define release         2jpp.el4ep1.2

Name:           avalon-logkit
Version:        1.2
Release:        alt2_4jpp5
Epoch:          0
Summary:        Java logging toolkit
License:        ASL 2.0
Group:          Development/Java
#Distribution:  JPackage
#Vendor:                JPackage Project
Url:            http://avalon.apache.org/%{short_name}/
Source0:        http://jakarta.apache.org/builds/jakarta-avalon/release/logkit/latest/LogKit-1.2-src.tar.gz
Patch0:         %{name}-build.patch
Source1:        avalon-logkit-component-info.xml
Requires: avalon-framework >= 0:4.1.4
Requires: servlet
Requires: jms
Requires: jdbc-stdext
Requires(post): jpackage-utils >= 0:1.5
Requires(postun): jpackage-utils >= 0:1.5
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant
BuildRequires: javamail
BuildRequires: junit
BuildRequires: log4j
BuildRequires: avalon-framework >= 0:4.1.4
BuildRequires: servlet
BuildRequires: jms
BuildRequires: jdbc-stdext
BuildArch:      noarch

%description
LogKit is a logging toolkit designed for secure performance orientated
logging in applications. To get started using LogKit, it is recomended
that you read the whitepaper and browse the API docs.

%if %{with_repolib}
%package         repolib
Summary:         Artifacts to be uploaded to a repository library
Group:  Development/Java

%description     repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_Name}-%{version}
%patch
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;


tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}

%build
export CLASSPATH=%(build-classpath log4j javamail/mailapi jms servlet jdbc-stdext avalon-framework junit):$PWD/build/classes
ant clean jar javadocs

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/lib/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%if %{with_repolib}
        install -d -m 755 $RPM_BUILD_ROOT%{repodir}
        install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
        install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
        install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
        install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
        cp build/lib/%{short_name}.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%doc KEYS LICENSE
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp5
- selected java5 compiler explicitly

* Sat Jan 24 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp5
- restored in separate package due to repolib

