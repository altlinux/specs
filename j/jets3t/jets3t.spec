BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2011, JPackage Project
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

%define gcj_support 0


Name:           jets3t
Version:        0.8.1
Release:        alt2_1jpp6
Epoch:          0
Summary:        Amazon S3 toolkit
Group:          Development/Java
License:        Apache Software License 2.0
URL:            https://bitbucket.org/jmurty/jets3t/wiki/Home
Source0:        jets3t-0.8.1.tgz
# hg clone -r 0.8.1 https://bitbucket.org/jmurty/jets3t
# tar czf jets3t-0.8.1.tgz jets3t/
Source1:        http://www.jets3t.org/maven2/net/java/dev/jets3t/jets3t/0.8.1/jets3t-0.8.1.pom
Patch0:         jets3t-bbbl-replace.patch
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-httpclient
BuildRequires:  apache-commons-logging
BuildRequires:  bouncycastle
BuildRequires:  jaf_1_1_api
BuildRequires:  javamail_1_4_api
BuildRequires:  java-xmlbuilder
BuildRequires:  jug
BuildRequires:  junit4
BuildRequires:  servlet_2_5_api
Requires:  apache-commons-codec
Requires:  apache-commons-httpclient
Requires:  apache-commons-logging
Requires:  bouncycastle
Requires:  jaf_1_1_api
Requires:  javamail_1_4_api
Requires:  java-xmlbuilder
Requires:  jug
Requires:  servlet_2_5_api
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%endif
Source44: import.info

%description
JetS3t is a free, open-source Java toolkit and application 
suite for Amazon Simple Storage Service (Amazon S3), Amazon 
CloudFront content delivery network, and Google Storage for 
Developers.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}
for j in $(find . -name "*.jar"); do 
    mv $j $j.no
done
%patch0 -b .sav0
ln -sf $(build-classpath bcprov) libs/bouncycastle/bcprov-jdk14-138.jar
ln -sf $(build-classpath commons-codec) libs/commons-codec/commons-codec-1.3.jar
ln -sf $(build-classpath commons-httpclient) libs/commons-httpclient/commons-httpclient-3.1.jar
ln -sf $(build-classpath commons-logging) libs/commons-logging/commons-logging-1.1.1.jar
ln -sf $(build-classpath jaf_1_1_api) libs/jaf/activation.jar
ln -sf $(build-classpath javamail_1_4_api) libs/javamail/mail.jar
ln -sf $(build-classpath java-xmlbuilder) libs/java-xmlbuilder/java-xmlbuilder-0.4.jar
ln -sf $(build-classpath junit4) libs/junit/junit.jar
ln -sf $(build-classpath log4j) libs/logging-log4j/log4j-1.2.15.jar
ln -sf $(build-classpath jug-asl) libs/safehaus_jug/jug-asl-2.0.0.jar
ln -sf $(build-classpath servlet_2_5_api) libs/servlet/servlet-api.jar

%build
export LANG=en_US.ISO8859-1
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist api-docs

%install

install -d 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 dist/%{name}-%{version}/jars/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%add_to_maven_depmap net.java.dev.jets3t %{name} %{version} JPP/%{name} %{name}

#
install -d 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/api-docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt2_1jpp6
- fixed build with java 7

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt1_1jpp6
- new version

