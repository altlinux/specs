Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc subversion geronimo-el-1.0-api
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


Name:           stripes
Version:        1.5.3
Release:	alt2_1jpp6
Epoch:          0
Summary:        JSON-RPC Implementation
Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://www.stripesframework.org/
Source0:        http://sourceforge.net/projects/stripes/files/stripes/Stripes%%201.5.3/stripes-1.5.3-src.zip

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant
BuildRequires: tlddoc
BuildRequires: testng
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-io
BuildRequires: jakarta-commons-logging
BuildRequires: el_1_0_api
BuildRequires: glassfish-jstl
BuildRequires: jakarta-taglibs-standard
BuildRequires: javamail_1_4_api
BuildRequires: jsp_2_1_api
BuildRequires: log4j
BuildRequires: servlet_2_5_api
BuildRequires: spring2-all
Requires: jakarta-commons-fileupload
Requires: jakarta-commons-io
Requires: jakarta-commons-logging
Requires: el_1_0_api
Requires: glassfish-jstl
Requires: jakarta-taglibs-standard
Requires: javamail_1_4_api
Requires: jsp_2_1_api
Requires: log4j
Requires: servlet_2_5_api
BuildArch:      noarch
Source44: import.info

%description
Stripes is a presentation framework for building web
applications using the latest Java technologies. The main
driver behind Stripes is that web application development
in Java is just too much work! It seems like every existing
framework requires gobs of configuration. Struts is pretty
feature-light and has some serious architectural issues
(see Stripes vs. Struts  for details). Others, like
WebWork 2 and Spring-MVC are much better, but still
require a lot of configuration, and seem to require
you to learn a whole new language just to get started.


%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep 
%setup -q 
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath jstl) examples/web/WEB-INF/lib/jstl.jar
ln -sf $(build-classpath log4j) examples/web/WEB-INF/lib/log4j-1.2.15.jar
ln -sf $(build-classpath javamail_1_4_api) examples/web/WEB-INF/lib/mail.jar
ln -sf $(build-classpath taglibs-standard) examples/web/WEB-INF/lib/standard.jar
ln -sf $(build-classpath el_1_0_api) stripes/lib/build/el-api.jar
ln -sf $(build-classpath jsp_2_1_api) stripes/lib/build/jsp-api.jar
ln -sf $(build-classpath javamail_1_4_api) stripes/lib/build/mail.jar
ln -sf $(build-classpath servlet_2_5_api) stripes/lib/build/servlet-api.jar
ln -sf $(build-classpath tlddoc) stripes/lib/build/tlddoc.jar
ln -sf $(build-classpath commons-logging) stripes/lib/deploy/commons-logging.jar
ln -sf $(build-classpath maven2/empty-dep) stripes/lib/deploy/cos.jar
ln -sf $(build-classpath commons-fileupload) stripes/lib/test/commons-fileupload-1.2.1.jar
ln -sf $(build-classpath commons-io) stripes/lib/test/commons-io-1.4.jar
ln -sf $(build-classpath log4j) stripes/lib/test/log4j-1.2.15.jar
ln -sf $(build-classpath spring2) stripes/lib/test/spring.jar
ln -sf $(build-classpath testng) tests/lib/testng-5.5-jdk15.jar
# cos-multipart is not free
rm stripes/src/net/sourceforge/stripes/controller/multipart/CosMultipartWrapper.java

%build
ant dist

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -m 644 stripes/dist/stripes.jar \
           %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
ln -s ${jar} ${jar/-%{version}/}; done)

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr stripes/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_1jpp6
- fixed build with new testng and xbean

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_1jpp6
- new version

