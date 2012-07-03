Packager: Igor Vlasenko <viy@altlinux.ru>
%define oldname snmptrapappender
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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/snmptrapappender/1.2.8-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define _without_nonfree 1

# If you do not want wengsoft-SNMP support, give rpmbuild option '--without nonfree'
%define with_nonfree %{!?_without_nonfree:1}%{?_without_nonfree:0}
%define without_nonfree %{?_without_nonfree:1}%{!?_without_nonfree:0}


Name:		snmptrapappender-repolib
Version:	1.2.8
Release:	alt1_6jpp5
Epoch:		0
License:	ASL 1.1
Group:		Development/Java
Summary:	SNMP Trap Appender extension for log4j
URL:		http://www.m2technologies.net/asp/snmpTrapAppender.asp
Source0:	http://www.m2technologies.net/bin/snmpTrapAppender_1_2_8.zip
Source1:	snmpTrapAppender_build.xml
Source2:	snmptrapappender-component-info.xml
#Patch0:		snmpTrapAppender_1_2_8.patch
BuildArch:	noarch
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: ant >= 0:1.6.1
BuildRequires: joesnmp >= 0:0.3.2
BuildRequires: log4j >= 0:1.2.8
%if %{with_nonfree}
BuildRequires: wengsoftsnmp
%endif
Requires: jpackage-utils >= 0:1.5
Requires: joesnmp >= 0:0.3.2
Requires: log4j >= 0:1.2.8
%if %{with_nonfree}
Requires: wengsoftsnmp
%endif

%description
An appender to send formatted logging event strings to a 
specified managment host (typically, a MLM of some sort, 
but could also be an SNMP management console) in the form 
of an SNMP trap. 
This appender does not attempt to provide full access to the 
SNMP API. In particular, use of this appender does not make 
an SNMP agent out of the calling application. You cannot use 
this appender as an interface to do SNMP GET or SET calls -- 
all it does is pass on your logging event as a TRAP.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Summary:        Javadoc for %{oldname}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{oldname}.

%prep
%setup -q -c -n %{oldname}-%{version}
cp %{SOURCE1} build.xml
chmod -R go=u-w *
find . -name "*.jar" | xargs %{__rm}
%if %{without_nonfree}
  %{__rm} src/org/apache/log4j/ext/WengsoftSNMPTrapSender.java
%endif

# Fix package name
#%patch0

%if %{with_repolib}
tag=`echo %{oldname}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE2}
%endif

%build
%if %{without_nonfree}
export CLASSPATH=$(build-classpath \
joesnmp \
log4j \
)
%else
export CLASSPATH=$(build-classpath \
joesnmp \
log4j \
wengsoftsnmp \
)
%endif
export OPT_JAR_LIST=:
ant dist javadoc

%install

# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 dist/lib/snmpTrapAppender-1.2.8.jar \
                   $RPM_BUILD_ROOT%{_javadir}
ln -s snmpTrapAppender-1.2.8.jar \
                   $RPM_BUILD_ROOT%{_javadir}/%{oldname}-%{version}.jar
ln -s snmpTrapAppender-1.2.8.jar $RPM_BUILD_ROOT%{_javadir}/snmpTrapAppender.jar
ln -s %{oldname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}
ln -s %{oldname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/snmpTrapAppender.jar $RPM_BUILD_ROOT%{repodirlib}
%endif
%if %{with_repolib}

%files
%{repodir}
%endif

%changelog
* Fri Aug 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt1_6jpp5
- repolib

* Fri Jun 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.8-alt0.1jpp
bootstrap; see deps.notes for details

