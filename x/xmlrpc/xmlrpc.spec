Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xmlrpc
Version:        3.1.3
Release:        alt7_18jpp8
Epoch:          1
Summary:        Java XML-RPC implementation
License:        ASL 2.0
URL:            http://ws.apache.org/xmlrpc/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/ws/xmlrpc/sources/apache-xmlrpc-%{version}-src.tar.bz2
Patch0:         %{name}-client-addosgimanifest.patch
Patch1:         %{name}-common-addosgimanifest.patch
Patch2:         %{name}-javax-methods.patch
Patch3:         %{name}-server-addosgimanifest.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.ws.commons.util:ws-commons-util)
Source44: import.info


%description
Apache XML-RPC is a Java implementation of XML-RPC, a popular protocol
that uses XML over HTTP to implement remote procedure calls.
Apache XML-RPC was previously known as Helma XML-RPC. If you have code
using the Helma library, all you should have to do is change the import
statements in your code from helma.xmlrpc.* to org.apache.xmlrpc.*.

%package javadoc
Group: Development/Java
Summary:    Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package common
Group: Development/Java
Summary:    Common classes for XML-RPC client and server implementations
# Provide xmlrpc is not here because it would be useless due to different jar names
Obsoletes:  %{name} < 3.1.3
Obsoletes:  %{name}3-common < 3.1.3-13
Provides:   %{name}3-common = 3.1.3-13

%description common
%{summary}.

%package client
Group: Development/Java
Summary:    XML-RPC client implementation
Obsoletes:  %{name}3-client < 3.1.3-13
Provides:   %{name}3-client = 3.1.3-13

%description client
%{summary}.

%package server
Group: Development/Java
Summary:    XML-RPC server implementation
Obsoletes:  %{name}3-server < 3.1.3-13
Provides:   %{name}3-server = 3.1.3-13

%description server
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}-src
%patch2 -p1
pushd client
%patch0 -b .sav
popd
pushd common
%patch1 -b .sav
popd
pushd server
%patch3 -b .sav
popd

sed -i 's/\r//' LICENSE.txt

%pom_disable_module dist
%pom_remove_dep jaxme:jaxmeapi common
# This dep is no longer supplied by ws-commons-util
%pom_add_dep junit:junit:3.8.1:test

%mvn_file :{*} @1
%mvn_package :*-common %{name}

%build
# FIXME: ignore test failure because server part needs network
%mvn_build -s -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files common -f .mfiles-%{name}
%doc LICENSE.txt NOTICE.txt

%files client -f .mfiles-%{name}-client

%files server -f .mfiles-%{name}-server

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_18jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_16jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_5jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_2jpp7
- rebuild with maven-local

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt6_2jpp7
- fixed deps

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt5_2jpp7
- fc update

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt4_4jpp6
- moved xmlrpc:xmlrpc jppmap to xmlrpc2

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt3_4jpp6
- added xmlrpc:xmlrpc jppmap

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt2_4jpp6
- fixed pom names

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_4jpp6
- new jpp release

* Sat Feb 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_1jpp5
- fixed build

