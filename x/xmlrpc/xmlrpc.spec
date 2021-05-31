Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xmlrpc
Version:        3.1.3
Release:        alt7_27jpp11
Epoch:          1
Summary:        Java XML-RPC implementation
License:        ASL 2.0
URL:            https://ws.apache.org/xmlrpc/
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/ws/xmlrpc/sources/apache-xmlrpc-%{version}-src.tar.bz2

# Fix build against modern servlet API by implementing missing interfaces
Patch0: 0001-Javax-Servlet-API.patch
# Add OSGi metadata so that xmlrpc can be used in OSGi runtimes
Patch1: 0002-Add-OSGi-metadata.patch
# CVE-2016-5003 - Disallow deserialization of <ex:serializable> tags by default
Patch2: 0003-disallow-deserialization-of-ex-serializable-tags.patch
# CVE-2016-5002 - isallow loading of external DTD
Patch3: 0004-disallow-loading-external-dtd.patch
# Jakarta Commons HttpClient is obsolete and should not be used, one of the other
# provider implementations should by used instead by clients of xmlrpc
Patch4: 0005-Remove-dep-on-ancient-commons-httpclient.patch
# CVE-2019-17570 - Deserialization of server-side exception from faultCause in XMLRPC error response
Patch5: 0006-Fix-for-CVE-2019-17570.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.ws.commons.util:ws-commons-util)
Source44: import.info

%description
Apache XML-RPC is a Java implementation of XML-RPC, a popular protocol
that uses XML over HTTP to implement remote procedure calls.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package common
Group: Development/Java
Summary: Common classes for XML-RPC client and server implementations

%description common
%{summary}.

%package client
Group: Development/Java
Summary: XML-RPC client implementation

%description client
%{summary}.

%package server
Group: Development/Java
Summary: XML-RPC server implementation

%description server
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}-src

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i 's/\r//' LICENSE.txt

%pom_disable_module dist
%pom_remove_dep jaxme:jaxmeapi common
%pom_add_dep junit:junit:3.8.1:test

%pom_remove_plugin :maven-javadoc-plugin

# Add missing dep when building against Java 11
%pom_add_dep javax.xml.bind:jaxb-api:2.2.12

# don't hard code source and target levels
sed -i -e '/<source>/d' \
       -e '/<target>/d' pom.xml

%mvn_file :{*} @1
%mvn_package :*-common %{name}

%build
# ignore test failure because server part needs network
%mvn_build -s -- -Dmaven.test.failure.ignore=true \
  -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files common -f .mfiles-%{name}
%doc --no-dereference LICENSE.txt NOTICE.txt

%files client -f .mfiles-%{name}-client

%files server -f .mfiles-%{name}-server

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:3.1.3-alt7_27jpp11
- update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 1:3.1.3-alt7_24jpp8
- fc update

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_23jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_22jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_20jpp8
- java fc28+ update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.1.3-alt7_19jpp8
- java update

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

