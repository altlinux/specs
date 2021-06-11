Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jsch-agent-proxy
Version:        0.0.8
Release:        alt1_15jpp11
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
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

# SSHj is not longer available in Fedora
Obsoletes: %{name}-sshj <= 0.0.8-11
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

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Put parent POM together with core module
%mvn_package :jsch.agentproxy jsch.agentproxy.core

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"
%pom_remove_plugin ":maven-source-plugin"
%pom_xpath_remove pom:build/pom:extensions

# Remove hard-coded compiler configuration
%pom_remove_plugin ":maven-compiler-plugin"

# SSHj not available in Fedora
%pom_disable_module jsch-agent-proxy-sshj

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.release=8 -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

%files core -f .mfiles-jsch.agentproxy.core
%doc README README.md
%doc --no-dereference LICENSE.txt

%files connector-factory -f .mfiles-jsch.agentproxy.connector-factory
%files jsch -f .mfiles-jsch.agentproxy.jsch
%files pageant -f .mfiles-jsch.agentproxy.pageant
%files sshagent -f .mfiles-jsch.agentproxy.sshagent
%files trilead-ssh2 -f .mfiles-jsch.agentproxy.svnkit-trilead-ssh2
%files usocket-jna -f .mfiles-jsch.agentproxy.usocket-jna
%files usocket-nc -f .mfiles-jsch.agentproxy.usocket-nc

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0.0.8-alt1_15jpp11
- fc34 update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0.0.8-alt1_12jpp11
- sisyphus build

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

