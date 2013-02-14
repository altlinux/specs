Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		jglobus
Version:	2.0.5
Release:	alt1_0.1.rc2jpp7
Summary:	Globus Java client libraries

#		Everything is Apache 2.0 except for one file that is MIT:
#		ssl-proxies/src/main/java/org/globus/tools/GridCertRequest.java
License:	ASL 2.0 and MIT
URL:		http://github.com/%{name}/
Source0:	http://github.com/%{name}/JGlobus/archive/%{name}-all-%{version}-rc2.tar.gz

BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	dos2unix
BuildRequires:	maven
BuildRequires:	maven-compiler-plugin
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-install-plugin
BuildRequires:	maven-jar-plugin
BuildRequires:	maven-javadoc-plugin
BuildRequires:	maven-patch-plugin
BuildRequires:	maven-release-plugin
BuildRequires:	maven-resources-plugin

BuildRequires:	apache-commons-codec
BuildRequires:	apache-commons-io
BuildRequires:	apache-commons-logging
BuildRequires:	bouncycastle
BuildRequires:	log4j
BuildRequires:	tomcat-lib >= 7.0.28
BuildRequires:	axis
BuildRequires:	servlet
Source44: import.info

%description
%%{name} is a collection of Java client libraries for Globus Toolkit security,
GRAM, GridFTP and MyProxy.

%package parent
Group: Development/Java
Summary:	Globus Java - parent pom file
License:	ASL 2.0
Requires:	jpackage-utils

%description parent
Globus Java libraries parent maven pom file

%package ssl-proxies
Group: Development/Java
Summary:	Globus Java - SSL and proxy certificate support
License:	ASL 2.0 and MIT
Requires:	jpackage-utils
Requires:	%{name}-parent = %{version}-%{release}
Requires:	apache-commons-codec
Requires:	apache-commons-io
Requires:	apache-commons-logging
Requires:	bouncycastle
Requires:	log4j

%description ssl-proxies
Globus Java library with SSL and proxy certificate support

%package jsse
Group: Development/Java
Summary:	Globus Java - SSL support
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-ssl-proxies = %{version}-%{release}

%description jsse
Globus Java library with SSL support

%package gss
Group: Development/Java
Summary:	Globus Java - GSS-API implementation for SSL with proxies
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-jsse = %{version}-%{release}

%description gss
Globus Java GSS-API implementation for SSL with proxies

%package gram
Group: Development/Java
Summary:	Globus Java - Grid Resource Allocation and Management (GRAM)
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-gss = %{version}-%{release}

%description gram
Globus Java library with GRAM support

%package gridftp
Group: Development/Java
Summary:	Globus Java - GridFTP
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-gss = %{version}-%{release}

%description gridftp
Globus Java library with GridFTP support

%package ssl-proxies-tomcat
Group: Development/Java
Summary:	Globus Java - SSL and proxy certificate support for Tomcat
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-jsse = %{version}-%{release}
Requires:	tomcat-lib >= 7

%description ssl-proxies-tomcat
Globus Java library with SSL and proxy certificate support for Tomcat

%package io
Group: Development/Java
Summary:	Globus Java - IO
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-gram = %{version}-%{release}
Requires:	%{name}-gridftp = %{version}-%{release}

%description io
Globus Java library with IO utilities

%package myproxy
Group: Development/Java
Summary:	Globus Java - MyProxy
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-gss = %{version}-%{release}

%description myproxy
Globus Java library with MyProxy support

%package axisg
Group: Development/Java
Summary:	Globus Java - Apache AXIS support
License:	ASL 2.0
Requires:	jpackage-utils
Requires:	%{name}-gss = %{version}-%{release}
Requires:	axis
Requires:	servlet

%description axisg
Globus Java library with Apache AXIS support

%package javadoc
Group: Development/Java
Summary:	Javadocs for %{name}
License:	ASL 2.0 and MIT
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q -n JGlobus-%{name}-all-%{version}-rc2
dos2unix axis/src/main/java/org/globus/axis/example/README.txt
chmod 644 axis/src/main/java/org/globus/axis/example/README.txt

%build
# Many tests requires network connections and a valid proxy certificate
mvn-rpmbuild -Ptomcat7 -Dproject.build.sourceEncoding=UTF-8 \
	     -Dmaven.test.skip=true install javadoc:aggregate

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
install -p -m 644 ssl-proxies/target/ssl-proxies-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/ssl-proxies.jar
install -p -m 644 jsse/target/jsse-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/jsse.jar
install -p -m 644 gss/target/gss-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/gss.jar
install -p -m 644 gram/target/gram-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/gram.jar
install -p -m 644 gridftp/target/gridftp-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/gridftp.jar
install -p -m 644 ssl-proxies-tomcat/target/ssl-proxies-tomcat-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/ssl-proxies-tomcat.jar
install -p -m 644 io/target/io-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/io.jar
install -p -m 644 myproxy/target/myproxy-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/myproxy.jar
install -p -m 644 axis/target/axisg-%{version}-rc2.jar \
    %{buildroot}%{_javadir}/%{name}/axisg.jar

mkdir -p %{buildroot}%{_javadocdir}
cp -pr target/site/apidocs %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
install -p -m 644 ssl-proxies/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-ssl-proxies.pom
install -p -m 644 jsse/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-jsse.pom
install -p -m 644 gss/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-gss.pom
install -p -m 644 gram/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-gram.pom
install -p -m 644 gridftp/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-gridftp.pom
install -p -m 644 ssl-proxies-tomcat/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-ssl-proxies-tomcat.pom
install -p -m 644 io/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-io.pom
install -p -m 644 myproxy/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-myproxy.pom
install -p -m 644 axis/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-axisg.pom

%add_maven_depmap -f parent JPP.%{name}-parent.pom
%add_maven_depmap -f ssl-proxies JPP.%{name}-ssl-proxies.pom %{name}/ssl-proxies.jar
%add_maven_depmap -f jsse JPP.%{name}-jsse.pom %{name}/jsse.jar
%add_maven_depmap -f gss JPP.%{name}-gss.pom %{name}/gss.jar
%add_maven_depmap -f gram JPP.%{name}-gram.pom %{name}/gram.jar
%add_maven_depmap -f gridftp JPP.%{name}-gridftp.pom %{name}/gridftp.jar
%add_maven_depmap -f ssl-proxies-tomcat JPP.%{name}-ssl-proxies-tomcat.pom %{name}/ssl-proxies-tomcat.jar
%add_maven_depmap -f io JPP.%{name}-io.pom %{name}/io.jar
%add_maven_depmap -f myproxy JPP.%{name}-myproxy.pom %{name}/myproxy.jar
%add_maven_depmap -f axisg JPP.%{name}-axisg.pom %{name}/axisg.jar

%files parent
%{_mavenpomdir}/JPP.%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}-parent

%files ssl-proxies
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/ssl-proxies.jar
%{_mavenpomdir}/JPP.%{name}-ssl-proxies.pom
%{_mavendepmapfragdir}/%{name}-ssl-proxies

%files jsse
%{_javadir}/%{name}/jsse.jar
%{_mavenpomdir}/JPP.%{name}-jsse.pom
%{_mavendepmapfragdir}/%{name}-jsse

%files gss
%{_javadir}/%{name}/gss.jar
%{_mavenpomdir}/JPP.%{name}-gss.pom
%{_mavendepmapfragdir}/%{name}-gss

%files gram
%{_javadir}/%{name}/gram.jar
%{_mavenpomdir}/JPP.%{name}-gram.pom
%{_mavendepmapfragdir}/%{name}-gram

%files gridftp
%{_javadir}/%{name}/gridftp.jar
%{_mavenpomdir}/JPP.%{name}-gridftp.pom
%{_mavendepmapfragdir}/%{name}-gridftp

%files ssl-proxies-tomcat
%{_javadir}/%{name}/ssl-proxies-tomcat.jar
%{_mavenpomdir}/JPP.%{name}-ssl-proxies-tomcat.pom
%{_mavendepmapfragdir}/%{name}-ssl-proxies-tomcat

%files io
%{_javadir}/%{name}/io.jar
%{_mavenpomdir}/JPP.%{name}-io.pom
%{_mavendepmapfragdir}/%{name}-io

%files myproxy
%{_javadir}/%{name}/myproxy.jar
%{_mavenpomdir}/JPP.%{name}-myproxy.pom
%{_mavendepmapfragdir}/%{name}-myproxy

%files axisg
%{_javadir}/%{name}/axisg.jar
%{_mavenpomdir}/JPP.%{name}-axisg.pom
%{_mavendepmapfragdir}/%{name}-axisg
%doc axis/src/main/java/org/globus/axis/example/README.txt

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_0.1.rc2jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_9.20121013git597e3acjpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_5jpp7
- new version

