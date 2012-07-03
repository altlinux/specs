Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#


Name:           jspwiki
Version:        2.8.4
Release:	alt1_1jpp6
Epoch:          0
Summary:        JSP based WikiWiki engine
Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://www.jspwiki.org
Source0:        http://www.ecyrd.com/~jalkanen/JSPWiki/2.8.4/JSPWiki-2.8.4-src.zip
Patch0:         jspwiki-UserManager.patch
BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: ecs
BuildRequires: freshcookies-security
BuildRequires: jakarta-taglibs-standard
BuildRequires: jaf_1_0_2_api
BuildRequires: jaxen
BuildRequires: jdom
BuildRequires: jrcs
BuildRequires: json-rpc
BuildRequires: jsp_2_0_api
BuildRequires: log4j
BuildRequires: lucene1
BuildRequires: lucene1-contrib
BuildRequires: glassfish-javamail
BuildRequires: nekohtml
BuildRequires: oro
BuildRequires: oscache
BuildRequires: sandler
BuildRequires: servlet_2_4_api
BuildRequires: xmlrpc2
BuildRequires: hsqldb
BuildRequires: tomcat5-jasper
BuildRequires: tomcat5-server-lib
BuildRequires: jetty5
BuildRequires: junit
BuildRequires: openqa-selenium-rc-java-client-driver
BuildRequires: openqa-selenium-rc-server
BuildRequires: stripes
BuildRequires: xerces-j2

Requires: jakarta-commons-codec
Requires: jakarta-commons-fileupload
Requires: jakarta-commons-lang
Requires: ecs
Requires: freshcookies-security
Requires: jaf_1_0_2_api
Requires: jakarta-oro
Requires: javamail
Requires: jdom
Requires: jrcs
Requires: json-rpc
Requires: jsp_2_0_api
Requires: log4j
Requires: lucene1
Requires: lucene1-contrib
Requires: sandler
Requires: servlet_2_4_api
Requires: stripes
Requires: tomcat5-server-lib
Requires: xmlrpc2

BuildArch:      noarch
Source44: import.info

%description
JSPWiki is a feature-rich and extensible WikiWiki engine 
built around the standard J2EE components (Java, servlets,
JSP). 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        webapp
Summary:        Exploded Webapp for %{name}
Group:          Development/Java

%description    webapp
%{summary}.

%prep 
%setup -q -c
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
rm src/com/ecyrd/jspwiki/filters/SpamFilter.java # akismet is not free
%patch0 -b .sav0
ln -s $(build-classpath jaf_1_0_2_api) lib/activation.jar
#lib/akismet-java-1.02.jar
ln -s $(build-classpath commons-codec) lib/commons-codec-1.3.jar
ln -s $(build-classpath commons-fileupload) lib/commons-fileupload-1.2.1.jar
ln -s $(build-classpath commons-httpclient) lib/commons-httpclient-3.0.1.jar
ln -s $(build-classpath commons-io) lib/commons-io-1.4.jar
ln -s $(build-classpath commons-lang) lib/commons-lang-2.3.jar
ln -s $(build-classpath commons-logging-api) lib/commons-logging-api.jar
ln -s $(build-classpath ecs) lib/ecs.jar
ln -s $(build-classpath freshcookies-security) lib/freshcookies-security-0.60.jar
ln -s $(build-classpath taglibs-standard) lib/jakarta-tablibs-standard-1.1.2.jar
ln -s $(build-classpath jstl) lib/jakarta-taglibs-jstl-1.1.2.jar
ln -s $(build-classpath jaxen) lib/jaxen.jar
ln -s $(build-classpath jdom) lib/jdom.jar
ln -s $(build-classpath jrcs) lib/jrcs-diff.jar
ln -s $(build-classpath json-rpc) lib/jsonrpc-1.0.jar
ln -s $(build-classpath jsp_2_0_api) lib/jsp-api.jar
ln -s $(build-classpath log4j) lib/log4j-1.2.14.jar
ln -s $(build-classpath lucene1-contrib/lucene-highlighter) lib/lucene-highlighter.jar
ln -s $(build-classpath lucene1) lib/lucene.jar
ln -s $(build-classpath glassfish-javamail-monolithic) lib/mail.jar
ln -s $(build-classpath nekohtml) lib/nekohtml.jar
ln -s $(build-classpath oro) lib/oro.jar
ln -s $(build-classpath oscache) lib/oscache.jar
ln -s $(build-classpath sandler) lib/sandler.jar
ln -s $(build-classpath servlet_2_4_api) lib/servlet-api.jar
ln -s $(build-classpath xmlrpc2) lib/xmlrpc.jar

ln -s $(build-classpath hsqldb) tests/lib/hsqldb.jar
ln -s $(build-classpath jasper5-compiler) tests/lib/jasper-compiler-5.5.25.jar
ln -s $(build-classpath jasper5-runtime) tests/lib/jasper-runtime-5.5.25.jar
ln -s $(build-classpath jetty5/jetty5-jmx) tests/lib/jetty-jmx-5.1.14.jar
ln -s $(build-classpath maven2/empty-dep) tests/lib/jetty-plus-5.1.14.jar
ln -s $(build-classpath jetty5/jetty5-servlet) tests/lib/jetty-servlet-5.1.14.jar
ln -s $(build-classpath junit) tests/lib/junit.jar
ln -s $(build-classpath selenium-java-client-driver) tests/lib/selenium-java-client-driver-1.0-beta1.jar
ln -s $(build-classpath selenium-server) tests/lib/selenium-server-1.0-beta1.jar
ln -s $(build-classpath stripes) tests/lib/stripes-1.5.jar
ln -s $(build-classpath xerces-j2) tests/lib/xercesImpl-2.6.2.jar
ln -s $(build-classpath maven2/empty-dep) tests/lib/xml-apis-1.0.b2.jar
#tests/lib/yuicompressor-2.4.2.jar


%build
ant jar javadoc opened-war

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -m 644 build/JSPWiki.jar \
           %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
ln -s ${jar} ${jar/-%{version}/}; done)

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# webapp
install -dm 755 %{buildroot}%{_datadir}/%{name}/webapp
cp -pr build/JSPWiki/* %{buildroot}%{_datadir}/%{name}/webapp

%files
%{_javadir}/%{name}*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files webapp
%{_datadir}/%{name}


%changelog
* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.8.4-alt1_1jpp6
- new version

