# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:       xmlrpc
Version:    3.1.3
Release:    alt7_2jpp7
Epoch:      1
Summary:    Java XML-RPC implementation
License:    ASL 2.0
Group:      Development/Java
URL:        http://ws.apache.org/xmlrpc/
Source0:    http://www.apache.org/dist/ws/xmlrpc/sources/apache-xmlrpc-%{version}-src.tar.bz2
Source1:    %{name}-jpp-depmap.xml
# Add OSGi MANIFEST information
Patch0:     %{name}-client-addosgimanifest.patch
Patch1:     %{name}-common-addosgimanifest.patch
Patch2:     %{name}-javax-methods.patch

BuildRequires:  maven-local
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  ws-jaxme
BuildRequires:  ws-commons-util
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  tomcat-servlet-3.0-api
BuildRequires:  junit
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  apache-commons-logging

BuildArch:    noarch
Source44: import.info

%description
Apache XML-RPC is a Java implementation of XML-RPC, a popular protocol
that uses XML over HTTP to implement remote procedure calls.
Apache XML-RPC was previously known as Helma XML-RPC. If you have code
using the Helma library, all you should have to do is change the import
statements in your code from helma.xmlrpc.* to org.apache.xmlrpc.*.

%package javadoc
Summary:    Javadoc for %{name}
Group:      Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package common
Summary:    Common classes for XML-RPC client and server implementations
Group:      Development/Java
# Provide xmlrpc is not here because it would be useless due to different jar names
Obsoletes:  %{name} < 3.1.3
Obsoletes:  %{name}3-common < 3.1.3-13
Provides:   %{name}3-common = 3.1.3-13
Requires:   ws-jaxme
Requires:   ws-commons-util
Requires:   jpackage-utils >= 0:1.6
Requires:   apache-commons-logging

%description common
%{summary}.

%package client
Summary:    XML-RPC client implementation
Group:      Development/Java
Requires:   %{name}-common
Requires:   jakarta-commons-httpclient
Obsoletes:  %{name}3-client < 3.1.3-13
Provides:  %{name}3-client = 3.1.3-13

%description client
%{summary}.

%package server
Summary:    XML-RPC server implementation
Group:      Development/Java
Requires:   %{name}-client
Requires:   junit
Requires:   tomcat-servlet-3.0-api
Obsoletes:  %{name}3-server < 3.1.3-13
Provides:  %{name}3-server = 3.1.3-13

%description server
%{summary}.

%prep
%setup -q -n apache-%{name}-%{version}-src
%patch2 -b .sav
pushd client
%patch0 -b .sav
popd
pushd common
%patch1 -b .sav
popd

sed -i 's/\r//' LICENSE.txt

%build
# ignore test failure because server part needs network
mvn-rpmbuild \
  -e \
  -Dmaven.local.depmap.file=%{SOURCE1} \
  -Dmaven.test.failure.ignore=true \
  install javadoc:aggregate

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 client/target/%{name}-client-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-client.jar
install -m 644 server/target/%{name}-server-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-server.jar
install -m 644 common/target/%{name}-common-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-common.jar

#compat symlinks remove in F-20
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-client.jar %{name}3-client.jar
ln -s %{name}-server.jar %{name}3-server.jar
ln -s %{name}-common.jar %{name}3-common.jar
popd

# install maven pom files
install -Dm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
install -Dm 644 common/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-common.pom
install -Dm 644 client/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-client.pom
install -Dm 644 server/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-server.pom

# ... and maven depmaps
%add_maven_depmap JPP-%{name}.pom
%add_maven_depmap JPP-%{name}-common.pom %{name}-common.jar
%add_maven_depmap JPP-%{name}-client.pom %{name}-client.jar
%add_maven_depmap JPP-%{name}-server.pom %{name}-server.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/*

%files common
%doc LICENSE.txt NOTICE.txt
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavenpomdir}/JPP-%{name}-common.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}-common.jar
%{_javadir}/%{name}3-common.jar

%files client
%{_mavenpomdir}/JPP-%{name}-client.pom
%{_javadir}/%{name}-client.jar
%{_javadir}/%{name}3-client.jar

%files server
%{_mavenpomdir}/JPP-%{name}-server.pom
%{_javadir}/%{name}-server.jar
%{_javadir}/%{name}3-server.jar

%changelog
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

