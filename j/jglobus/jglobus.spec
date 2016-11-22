Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
Name:		jglobus
Version:	2.1.0
Release:	alt1_4jpp8
Summary:	Globus Java client libraries

#		Everything is Apache 2.0 except for one file that is MIT:
#		ssl-proxies/src/main/java/org/globus/tools/GridCertRequest.java
License:	ASL 2.0 and MIT
URL:		http://github.com/%{name}/
Source0:	http://github.com/%{name}/JGlobus/archive/JGlobus-Release-%{version}.tar.gz
#		DERObjectIdentifier is obsolete
Patch0:		%{name}-DERObjectIdentifier-is-obsolete.patch
#		Don't force SSLv3
Patch1:		%{name}-dont-force-SSLv3.patch

BuildArch:	noarch

BuildRequires:	maven-local
%if %{?fedora}%{!?fedora:0}
BuildRequires:	mvn(axis:axis)
BuildRequires:	mvn(axis:axis-jaxrpc)
%endif
BuildRequires:	mvn(commons-codec:commons-codec)
BuildRequires:	mvn(commons-httpclient:commons-httpclient)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(javax.servlet:servlet-api)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(log4j:log4j)
BuildRequires:	mvn(org.apache.httpcomponents:httpclient)
BuildRequires:	mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:	mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:	mvn(org.apache.tomcat:tomcat-coyote)
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk15on)
Source44: import.info

%description
%{name} is a collection of Java client libraries for Globus Toolkit security,
GRAM, GridFTP and MyProxy.

%package parent
Group: Development/Java
Summary:	Globus Java - parent pom file
License:	ASL 2.0

%description parent
Globus Java libraries parent maven pom file

%package ssl-proxies
Group: Development/Java
Summary:	Globus Java - SSL and proxy certificate support
License:	ASL 2.0 and MIT

%description ssl-proxies
Globus Java library with SSL and proxy certificate support

%package jsse
Group: Development/Java
Summary:	Globus Java - SSL support
License:	ASL 2.0
Requires:	%{name}-ssl-proxies = %{version}

%description jsse
Globus Java library with SSL support

%package gss
Group: Development/Java
Summary:	Globus Java - GSS-API implementation for SSL with proxies
License:	ASL 2.0
Requires:	%{name}-jsse = %{version}

%description gss
Globus Java GSS-API implementation for SSL with proxies

%package gram
Group: Development/Java
Summary:	Globus Java - Grid Resource Allocation and Management (GRAM)
License:	ASL 2.0
Requires:	%{name}-gss = %{version}

%description gram
Globus Java library with GRAM support

%package gridftp
Group: Development/Java
Summary:	Globus Java - GridFTP
License:	ASL 2.0
Requires:	%{name}-gss = %{version}

%description gridftp
Globus Java library with GridFTP support

%package ssl-proxies-tomcat
Group: Development/Java
Summary:	Globus Java - SSL and proxy certificate support for Tomcat
License:	ASL 2.0
Requires:	%{name}-jsse = %{version}

%description ssl-proxies-tomcat
Globus Java library with SSL and proxy certificate support for Tomcat

%package io
Group: Development/Java
Summary:	Globus Java - IO
License:	ASL 2.0
Requires:	%{name}-gram = %{version}
Requires:	%{name}-gridftp = %{version}

%description io
Globus Java library with IO utilities

%package myproxy
Group: Development/Java
Summary:	Globus Java - MyProxy
License:	ASL 2.0
Requires:	%{name}-gss = %{version}

%description myproxy
Globus Java library with MyProxy support

%if %{?fedora}%{!?fedora:0}
%package axisg
Group: Development/Java
Summary:	Globus Java - Apache AXIS support
License:	ASL 2.0
Requires:	%{name}-gss = %{version}

%description axisg
Globus Java library with Apache AXIS support
%endif

%package javadoc
Group: Development/Java
Summary:	Javadocs for %{name}
License:	ASL 2.0 and MIT
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JGlobus-JGlobus-Release-%{version}
%patch0 -p1
%patch1 -p1

# Do not package test classes
%mvn_package org.jglobus:container-test-utils __noinstall
%mvn_package org.jglobus:test-utils __noinstall

# Avoid build dependency bloat
%pom_remove_parent

# Disable axis module for EPEL 7
%if %{?rhel}%{!?rhel:0} == 7
%pom_disable_module axis
%endif

%build
# Many tests requires network connections and a valid proxy certificate
%mvn_build -f -s -- -Ptomcat7 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files parent -f .mfiles-parent 
%doc LICENSE

%files ssl-proxies -f .mfiles-ssl-proxies
%dir %{_javadir}/%{name}
%doc README.textile
%doc LICENSE

%files jsse -f .mfiles-jsse

%files gss -f .mfiles-gss

%files gram -f .mfiles-gram

%files gridftp -f .mfiles-gridftp

%files ssl-proxies-tomcat -f .mfiles-ssl-proxies-tomcat

%files io -f .mfiles-io

%files myproxy -f .mfiles-myproxy

%if %{?fedora}%{!?fedora:0}
%files axisg -f .mfiles-axisg
%doc axis/src/main/java/org/globus/axis/example/README.txt
%endif

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_4jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_3jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.6-alt1_2jpp7
- new version

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_0.1.rc2jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_9.20121013git597e3acjpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_5jpp7
- new version

