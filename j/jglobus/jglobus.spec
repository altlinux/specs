Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		jglobus
Version:	2.0.6
Release:	alt1_3jpp7
Summary:	Globus Java client libraries

#		Everything is Apache 2.0 except for one file that is MIT:
#		ssl-proxies/src/main/java/org/globus/tools/GridCertRequest.java
License:	ASL 2.0 and MIT
URL:		http://github.com/%{name}/
Source0:	http://github.com/%{name}/JGlobus/archive/JGlobus-%{version}.tar.gz
#		Fixes from Bartek Palak (see pull request in github)
Patch0:		jglobus-final-static.patch
Patch1:		jglobus-semi.patch
Patch2:		jglobus-synch-disconnect.patch
Patch3:		jglobus-errors.patch
Patch4:		jglobus-impl-clonable.patch
Patch5:		jglobus-dont-hide-super.patch
#		Fix javadoc warnings
Patch6:		jglobus-doc.patch
#		Name parent parent
Patch7:		jglobus-parent.patch

BuildArch:	noarch

BuildRequires:	dos2unix
BuildRequires:	maven-local
BuildRequires:	mvn(axis:axis)
BuildRequires:	mvn(axis:axis-jaxrpc)
BuildRequires:	mvn(commons-codec:commons-codec)
BuildRequires:	mvn(commons-httpclient:commons-httpclient)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(javax.servlet:servlet-api)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(log4j:log4j)
BuildRequires:	mvn(org.apache.httpcomponents:httpclient)
BuildRequires:	mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-patch-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:	mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:	mvn(org.apache.tomcat:tomcat-coyote)
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk16)
BuildRequires:	mvn(org.sonatype.oss:oss-parent)
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

%package ssl-proxies-tomcat
Group: Development/Java
Summary:	Globus Java - SSL and proxy certificate support for Tomcat
License:	ASL 2.0
Requires:	%{name}-jsse = %{version}-%{release}

%description ssl-proxies-tomcat
Globus Java library with SSL and proxy certificate support for Tomcat

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

%package axisg
Group: Development/Java
Summary:	Globus Java - Apache AXIS support
License:	ASL 2.0
Requires:	%{name}-gss = %{version}-%{release}

%description axisg
Globus Java library with Apache AXIS support

%package javadoc
Group: Development/Java
Summary:	Javadocs for %{name}
License:	ASL 2.0 and MIT
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JGlobus-JGlobus-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

dos2unix axis/src/main/java/org/globus/axis/example/README.txt
chmod 644 axis/src/main/java/org/globus/axis/example/README.txt

# Move test classes to test directory
mkdir -p gram/src/test/java/org/globus/gram/util
mv gram/src/main/java/org/globus/gram/Gram15Test.java \
   gram/src/test/java/org/globus/gram/Gram15Test.java
mv gram/src/main/java/org/globus/gram/GramTest.java \
   gram/src/test/java/org/globus/gram/GramTest.java
mv gram/src/main/java/org/globus/gram/MultiUserGramTest.java \
   gram/src/test/java/org/globus/gram/MultiUserGramTest.java
mv gram/src/main/java/org/globus/gram/util/TestUtil.java \
   gram/src/test/java/org/globus/gram/util/TestUtil.java

# Move gram tests using io classes to io directory
mkdir -p io/src/test/java/org/globus/gram/tests
mkdir -p io/src/test/java/org/globus/gram/util
mkdir -p io/src/test/resources
mv gram/src/test/java/org/globus/gram/Gram15Test.java \
   io/src/test/java/org/globus/gram/Gram15Test.java
mv gram/src/test/java/org/globus/gram/tests/GramTest.java \
   io/src/test/java/org/globus/gram/tests/GramTest.java
mv gram/src/test/java/org/globus/gram/tests/test.sh \
   io/src/test/java/org/globus/gram/tests/test.sh
mv gram/src/test/java/org/globus/gram/util/TestUtil.java \
   io/src/test/java/org/globus/gram/util/TestUtil.java
mv gram/src/test/resources/test.properties \
   io/src/test/resources/test.properties

# Remove code duplication
mkdir -p gss/src/test/java/org/globus/net/test
mv gram/src/test/java/org/globus/net/test/GSIHttpURLConnectionTest.java \
   gss/src/test/java/org/globus/net/test/GSIHttpURLConnectionTest.java
rm gss/src/test/java/org/globus/net/GSIHttpURLConnectionTest.java
rm -rf gram/src/main/java/org/globus/net      # also in gss
rm -rf gram/src/main/java/org/globus/io/gass  # also in io

# Move test.properties files to resources directories
mkdir -p gridftp/src/test/resources/org/globus/ftp/test
mkdir -p myproxy/src/test/resources/org/globus/myproxy/test
rm gridftp/src/test/java/org/globus/ftp/test/test1.properties
rm gridftp/src/test/java/test.properties
mv gridftp/src/test/java/org/globus/ftp/test/test.properties \
   gridftp/src/test/resources/org/globus/ftp/test/test.properties
mv gridftp/src/test/java/org/globus/ftp/test/test.properties.in \
   gridftp/src/test/resources/org/globus/ftp/test/test.properties.in
mv myproxy/src/test/java/org/globus/myproxy/test/test.properties \
   myproxy/src/test/resources/org/globus/myproxy/test/test.properties

# Do not package test classes
%mvn_package org.jglobus:container-test-utils __noinstall
%mvn_package org.jglobus:test-utils __noinstall

%build
# Many tests requires network connections and a valid proxy certificate
%mvn_build -f -s -- -Ptomcat7 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files parent -f .mfiles-parent 
%doc LICENSE

%files ssl-proxies -f .mfiles-ssl-proxies
%dir %{_javadir}/%{name}
%doc LICENSE README.textile

%files jsse -f .mfiles-jsse

%files gss -f .mfiles-gss

%files gram -f .mfiles-gram

%files gridftp -f .mfiles-gridftp

%files ssl-proxies-tomcat -f .mfiles-ssl-proxies-tomcat

%files io -f .mfiles-io

%files myproxy -f .mfiles-myproxy

%files axisg -f .mfiles-axisg

%files javadoc -f .mfiles-javadoc

%changelog
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

