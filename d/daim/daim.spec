Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 0.9.2
%define name daim
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without menus

%define appdir          %{_datadir}/%{name}

Name:           daim
Version:        0.9.2
Release:        alt1_15jpp6
Epoch:          0
Summary:        Instant Messaging Client and Library supporting AIM and ICQ
License:        LGPLv2+
URL:            http://daim.dev.java.net/
Group:          Networking/Instant messaging
Source0:        daim.tar.bz2
Source1:        %{name}-script
Source2:        %{name}-icon-16.png
Source3:        %{name}-icon-32.png
Source4:        %{name}-icon-48.png
Source5:        %{name}.desktop
Requires: bouncycastle >= 0:1.42
Requires: bsf
Requires: log4j
Requires: jpackage-utils >= 0:1.5
Requires: xerces-j2
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: antlr
BuildRequires: bouncycastle-javadoc >= 0:1.42
BuildRequires: bouncycastle >= 0:1.42
BuildRequires: bsf
BuildRequires: checkstyle
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-logging
BuildRequires: java-javadoc >= 0:1.5
BuildRequires: jpackage-utils >= 0:1.5
BuildRequires: junit
BuildRequires: junit-javadoc
BuildRequires: log4j
BuildRequires: regexp
BuildRequires: xerces-j2
BuildArch:      noarch

%description
daim already supports many features, including Add-Ins, AIM Proxy, Buddy
Icon, Chat, Direct IM, File Transfer, File Sharing, Send Buddy List and
Trillian SecureIM. daim also supports retrieving News and Stocks. daim
tries to support as many features as possible from WinAIM 5.2.

daim supports scripting through Apache BSF. Sample Jython scripts can be
found in the script directory in CVS, but any language supported by BSF
is supported by daim, including JavaScript and Tcl (among others).

You may log in using your ICQ UIN and password using daim. daim has full
support for the non-TCP portion of the ICQ protocol up to ICQ 2003a.

In addition to ICQ, daim can emulate Apple's iChat client, and daim
supports iChat available messages as well.

%package scripts
Summary:        Scripts for %{name}
Group:          Networking/Instant messaging
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: jython
AutoReq: yes,nopython

%description scripts
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=$(build-classpath antlr bcmail bcprov bsf checkstyle jakarta-commons-beanutils jakarta-commons-collections jakarta-commons-logging log4j regexp xerces-j2)
%{ant} jar test javadocs

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__install} -p -m 0644 build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# data
%{__mkdir_p} %{buildroot}%{appdir}
%{__install} -p -m 0644 script/*.py %{buildroot}%{appdir}

# scripts
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/daim

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with menus
# freedesktop.org menu entry
%{__install} -D -p -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/applications/jpackage-%{name}.desktop
%{__install} -D -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{__install} -D -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{__install} -D -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{__install} -D -p -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%endif

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files
%doc AUTHORS BUGS ChangeLog COPYING CREDITS HACKING INSTALL README STYLE
%doc THANKS TODO VERSION lib/README.JARS
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%dir %{appdir}
%if %with menus
%{_datadir}/applications/*-%{name}.desktop
%{_datadir}/icons/*/*/apps/*
%{_datadir}/pixmaps/%{name}.png
%endif
%config(noreplace,missingok) /etc/%{name}.conf

%files scripts
%doc script/README.SCRIPTING
%{appdir}/*.py

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Sep 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.2-alt1_15jpp6
- new version

