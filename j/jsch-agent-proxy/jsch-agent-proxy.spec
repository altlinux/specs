Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jsch-agent-proxy
Version:        0.0.8
Release:        alt1_3jpp8
Summary:        Proxy to ssh-agent and Pageant in Java
License:        BSD
URL:            http://www.jcraft.com/jsch-agent-proxy/
BuildArch:      noarch

Source0:        https://github.com/ymnk/jsch-agent-proxy/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.trilead:trilead-ssh2)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:platform)
BuildRequires:  mvn(net.schmizz:sshj)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-ssh-external)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
jsch-agent-proxy is a proxy program to OpenSSH ssh-agent and Pageant
included Putty.  It will be easily integrated into JSch, and users
will be allowed to use those programs in authentications.  This
software has been developed for JSch, but it will be easily applicable
to other ssh2 implementations in Java.  This software is licensed
under BSD style license.

%package connector-factory
Group: Development/Java
Summary:        Connector factory for jsch-agent-proxy

%description connector-factory
%{summary}.

%package core
Group: Development/Java
Summary:        jsch-agent-proxy core module

%description core
%{summary}.

%package jsch
Group: Development/Java
Summary:        JSch connector for jsch-agent-proxy

%description jsch
%{summary}.

%package pageant
Group: Development/Java
Summary:        Pageant connector for jsch-agent-proxy

%description pageant
%{summary}.

%package sshagent
Group: Development/Java
Summary:        ssh-agent connector for jsch-agent-proxy

%description sshagent
%{summary}.

%package sshj
Group: Development/Java
Summary:        sshj connector for jsch-agent-proxy

%description sshj
%{summary}.

%package trilead-ssh2
Group: Development/Java
Summary:        trilead-ssh2 connector for jsch-agent-proxy

%description trilead-ssh2
%{summary}.

%package usocket-jna
Group: Development/Java
Summary:        USocketFactory implementation using JNA

%description usocket-jna
%{summary}.

%package usocket-nc
Group: Development/Java
Summary:        USocketFactory implementation using Netcat

%description usocket-nc
%{summary}.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q

# Put parent POM together with core module
%mvn_package :jsch.agentproxy jsch.agentproxy.core

%build
%mvn_build -s

%install
%mvn_install

%files core -f .mfiles-jsch.agentproxy.core
%dir %{_javadir}/%{name}
%doc README README.md
%doc LICENSE.txt

%files connector-factory -f .mfiles-jsch.agentproxy.connector-factory
%files jsch -f .mfiles-jsch.agentproxy.jsch
%files pageant -f .mfiles-jsch.agentproxy.pageant
%files sshagent -f .mfiles-jsch.agentproxy.sshagent
%files sshj -f .mfiles-jsch.agentproxy.sshj
%files trilead-ssh2 -f .mfiles-jsch.agentproxy.svnkit-trilead-ssh2
%files usocket-jna -f .mfiles-jsch.agentproxy.usocket-jna
%files usocket-nc -f .mfiles-jsch.agentproxy.usocket-nc

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_2jpp8
- unbootsrap build

