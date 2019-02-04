Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with     jp_minimal

Name:           jsch-agent-proxy
Version:        0.0.8
Release:        alt1_9jpp8
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
%if %{without jp_minimal}
BuildRequires:  mvn(net.schmizz:sshj)
%endif
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
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

%if %{without jp_minimal}
%package sshj
Group: Development/Java
Summary:        sshj connector for jsch-agent-proxy

%description sshj
%{summary}.
%endif

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

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"
%pom_remove_plugin ":maven-source-plugin"
%pom_xpath_remove pom:build/pom:extensions

%if %{with jp_minimal}
%pom_disable_module jsch-agent-proxy-sshj
%endif

%build
%mvn_build -s

%install
%mvn_install

%files core -f .mfiles-jsch.agentproxy.core
%doc README README.md
%doc --no-dereference LICENSE.txt

%files connector-factory -f .mfiles-jsch.agentproxy.connector-factory
%files jsch -f .mfiles-jsch.agentproxy.jsch
%files pageant -f .mfiles-jsch.agentproxy.pageant
%files sshagent -f .mfiles-jsch.agentproxy.sshagent
%if %{without jp_minimal}
%files sshj -f .mfiles-jsch.agentproxy.sshj
%endif
%files trilead-ssh2 -f .mfiles-jsch.agentproxy.svnkit-trilead-ssh2
%files usocket-jna -f .mfiles-jsch.agentproxy.usocket-jna
%files usocket-nc -f .mfiles-jsch.agentproxy.usocket-nc

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_9jpp8
- java update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_8jpp8
- java fc28+ update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_3jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_2jpp8
- unbootsrap build

