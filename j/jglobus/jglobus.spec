Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 29
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# The gaxis module requires axis version 1.x
%if %{?fedora}%{!?fedora:0} >= 28 || %{?rhel}%{!?rhel:0} >= 7
%define gaxismodule 0
%else
%global gaxismodule 1
%endif

# The tomcat module is not compatible with tomcat 8.5 or later
%if %{?fedora}%{!?fedora:0} >= 28 || %{?rhel}%{!?rhel:0} >= 8
%define tomcatmodule 0
%else
%global tomcatmodule 1
%endif

Name:		jglobus
Version:	2.1.0
Release:	alt1_13jpp8
Summary:	Globus Java client libraries

#		Everything is Apache 2.0 except for one file that is MIT:
#		ssl-proxies/src/main/java/org/globus/tools/GridCertRequest.java
License:	ASL 2.0 and MIT
URL:		http://github.com/%{name}/
Source0:	http://github.com/%{name}/JGlobus/archive/JGlobus-Release-%{version}.tar.gz
#		DERObjectIdentifier is obsolete
#		https://github.com/jglobus/JGlobus/pull/149
Patch0:		%{name}-DERObjectIdentifier-is-obsolete.patch
#		Don't force SSLv3 in myproxy, allow TLS
#		Backport from git (trunk)
Patch1:		%{name}-dont-force-SSLv3.patch
#		Relax proxy validation to be RFC-3820 compliant
#		https://github.com/jglobus/JGlobus/issues/160
#		https://github.com/jglobus/JGlobus/pull/165
Patch2:		%{name}-key-usage.patch
#		Fix javadoc
#		https://github.com/jglobus/JGlobus/pull/162
Patch3:		%{name}-javadoc.patch
#		Do not accumulate matches in
#		GlobusPathMatchingResourcePatternResolver
#		https://github.com/jglobus/JGlobus/pull/157
Patch4:		%{name}-do-not-accumulate-matches-in-GlobusPathMatchingResou.patch
#		Compatibility with clients that request minimum TLS version 1.2
#		https://github.com/jglobus/JGlobus/pull/166
Patch5:		%{name}-do-not-force-SSLv3-TLSv1-allow-TLSv1.1-TLSv1.2.patch
#		Remove synchronization on CRL in CRLChecker
#		Drop workaround for race condition in BouncyCastle < 1.46
#		Reduced lock contention leads to higher request throughput
#		Backport from git (trunk and 2.1 branch)
Patch6:		%{name}-remove-synchronization-on-CRL-in-CRLChecker.patch
#		Fix "no key" error for PKCS#8 encoded keys
#		https://github.com/jglobus/JGlobus/issues/118
#		https://github.com/jglobus/JGlobus/issues/146
#		https://github.com/jglobus/JGlobus/pull/164
Patch7:		%{name}-support-PKCS8-key-format.patch
#		Only allow TLSv1 and TLSv1.2 (not TLSv1.1)
#		https://github.com/jglobus/JGlobus/pull/166
Patch8:		%{name}-only-allow-TLSv1-and-TLSv1.2-not-TLSv1.1.patch
#		Remove unused FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES_FOR_GRAM
#		https://github.com/jglobus/JGlobus/pull/166
Patch9:		%{name}-remove-unused-FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES.patch
#		Adapt to changes in bouncycastle 1.61
#		https://github.com/jglobus/JGlobus/pull/168
Patch10:	%{name}-adapt-to-changes-in-PrivateKeyInfo-class.patch

BuildArch:	noarch

BuildRequires:	maven-local
%if %{gaxismodule}
BuildRequires:	mvn(axis:axis)
BuildRequires:	mvn(axis:axis-jaxrpc)
BuildRequires:	mvn(commons-httpclient:commons-httpclient)
BuildRequires:	mvn(javax.servlet:servlet-api)
%endif
BuildRequires:	mvn(commons-codec:commons-codec)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(log4j:log4j)
BuildRequires:	mvn(org.apache.httpcomponents:httpclient)
BuildRequires:	mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-surefire-plugin)
%if %{tomcatmodule}
BuildRequires:	mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:	mvn(org.apache.tomcat:tomcat-coyote)
%endif
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
%if ! %{gaxismodule}
Obsoletes:	%{name}-axisg < %{version}-%{release}
%endif
%if ! %{tomcatmodule}
Obsoletes:	%{name}-ssl-proxies-tomcat < %{version}-%{release}
%endif

%description ssl-proxies
Globus Java library with SSL and proxy certificate support

%package jsse
Group: Development/Java
Summary:	Globus Java - SSL support
License:	ASL 2.0
Requires:	%{name}-ssl-proxies = %{version}-%{release}

%description jsse
Globus Java library with SSL support

%package gss
Group: Development/Java
Summary:	Globus Java - GSS-API implementation for SSL with proxies
License:	ASL 2.0
Requires:	%{name}-jsse = %{version}-%{release}

%description gss
Globus Java GSS-API implementation for SSL with proxies

%package gram
Group: Development/Java
Summary:	Globus Java - Grid Resource Allocation and Management (GRAM)
License:	ASL 2.0
Requires:	%{name}-gss = %{version}-%{release}

%description gram
Globus Java library with GRAM support

%package gridftp
Group: Development/Java
Summary:	Globus Java - GridFTP
License:	ASL 2.0
Requires:	%{name}-gss = %{version}-%{release}

%description gridftp
Globus Java library with GridFTP support

%if %{tomcatmodule}
%package ssl-proxies-tomcat
Group: Development/Java
Summary:	Globus Java - SSL and proxy certificate support for Tomcat
License:	ASL 2.0
Requires:	%{name}-jsse = %{version}-%{release}

%description ssl-proxies-tomcat
Globus Java library with SSL and proxy certificate support for Tomcat
%endif

%package io
Group: Development/Java
Summary:	Globus Java - IO
License:	ASL 2.0
Requires:	%{name}-gram = %{version}-%{release}
Requires:	%{name}-gridftp = %{version}-%{release}

%description io
Globus Java library with IO utilities

%package myproxy
Group: Development/Java
Summary:	Globus Java - MyProxy
License:	ASL 2.0
Requires:	%{name}-gss = %{version}-%{release}

%description myproxy
Globus Java library with MyProxy support

%if %{gaxismodule}
%package axisg
Group: Development/Java
Summary:	Globus Java - Apache AXIS support
License:	ASL 2.0
Requires:	%{name}-gss = %{version}-%{release}

%description axisg
Globus Java library with Apache AXIS support
%endif

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
License:	ASL 2.0 and MIT
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JGlobus-JGlobus-Release-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# Do not package test classes
%mvn_package org.jglobus:container-test-utils __noinstall
%mvn_package org.jglobus:test-utils __noinstall

# Avoid build dependency bloat
%pom_remove_parent

%if ! %{gaxismodule}
%pom_disable_module axis
%endif

%if ! %{tomcatmodule}
%pom_disable_module ssl-proxies-tomcat
%endif

%build
# Many tests requires network connections and a valid proxy certificate
%mvn_build -f -s -- -Ptomcat7 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files parent -f .mfiles-parent 
%doc --no-dereference LICENSE

%files ssl-proxies -f .mfiles-ssl-proxies
%dir %{_javadir}/%{name}
%doc README.textile
%doc --no-dereference LICENSE

%files jsse -f .mfiles-jsse

%files gss -f .mfiles-gss

%files gram -f .mfiles-gram

%files gridftp -f .mfiles-gridftp

%if %{tomcatmodule}
%files ssl-proxies-tomcat -f .mfiles-ssl-proxies-tomcat
%endif

%files io -f .mfiles-io

%files myproxy -f .mfiles-myproxy

%if %{gaxismodule}
%files axisg -f .mfiles-axisg
%doc axis/src/main/java/org/globus/axis/example/README.txt
%endif

%files javadoc -f .mfiles-javadoc

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_13jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_10jpp8
- fc29 update

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_9jpp8
- fixed build with new tomcat

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_5jpp8
- new jpp release

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

