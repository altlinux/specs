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


Name:           logback
Version:        0.9.27
Release:	alt1_1jpp6
Epoch:          0
Summary:        Logback
License:        LGPLv2+
Group:          Development/Java
URL:            http://logback.qos.ch
# git clone git://github.com/ceki/logback && cd logback && git checkout v_0.9.27 && rm -rf .git && cd .. && mv logback logback-0.9.27 && tar cjf logback-0.9.27.tar.bz2 logback-0.9.27
Source0:        logback-0.9.27.tar.bz2
Source1:        logback-jpp-depmap.xml
Source2:        logback-settings.xml
Patch0:         logback-classic-pom.patch
Patch1:         logback-no-jetty7.patch
Patch2:         logback-access-RequestLogImpl.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       jpackage-utils
Requires:       glassfish-javamail
Requires:       janino
Requires:       jms_1_1_api
Requires:       slf4j >= 0:1.6.1
BuildRequires:  felix-main >= 0:2.0.2
BuildRequires:  fest >= 0:1.0.2
BuildRequires:  fest-assert >= 0:1.2
BuildRequires:  geronimo-genesis
BuildRequires:  gmaven
BuildRequires:  gmaven-runtime-1.6
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven2 >= 0:2.0.7
BuildRequires:  maven2-plugin-antrun
BuildRequires:  maven2-plugin-assembly
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-eclipse
BuildRequires:  maven2-plugin-idea
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven2-plugin-source
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-release
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  h2database >= 0:1.2.132
BuildRequires:  mysql-connector-java >= 0:5.1.9
BuildRequires:  postgresql-jdbc >= 0:8.4.701
BuildRequires:  junit4
BuildRequires:  dom4j
BuildRequires:  easymock2
BuildRequires:  gmaven
BuildRequires:  greenmail
BuildRequires:  hsqldb
BuildRequires:  subethasmtp2
BuildRequires:  glassfish-javamail
BuildRequires:  janino
BuildRequires:  jetty6-core
BuildRequires:  jms_1_1_api
BuildRequires:  servlet_2_5_api
BuildRequires:  slf4j >= 0:1.6.1
BuildRequires:  tomcat6-lib
BuildArch:      noarch
Source44: import.info

%description
Logback.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2

%{__rm} -rv logback-access/src/main/java/ch/qos/logback/access/jetty/v7/

%build
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
export M2SETTINGS=%{SOURCE2}
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.test.failure.ignore=true \
        -Dmaven.test.skip=false \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
        -Dorg.slf4j:slf4j-api:jar=%{_javadir}/slf4j/slf4j-api.jar \
        -Dslf4jJAR=%{_javadir}/slf4j/slf4j-api.jar \
        deploy javadoc:aggregate

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -p -m 644 %{name}-core/target/%{name}-core-%{version}.jar %{buildroot}%{_javadir}/%{name}/core-%{version}.jar
install -p -m 644 %{name}-core/target/%{name}-core-%{version}-tests.jar %{buildroot}%{_javadir}/%{name}/core-tests-%{version}.jar
%add_to_maven_depmap ch.qos.logback %{name}-core %{version} JPP/%{name} core
install -p -m 644 %{name}-classic/target/%{name}-classic-%{version}.jar %{buildroot}%{_javadir}/%{name}/classic-%{version}.jar
install -p -m 644 %{name}-classic/target/%{name}-classic-%{version}-tests.jar %{buildroot}%{_javadir}/%{name}/classic-tests-%{version}.jar
%add_to_maven_depmap ch.qos.logback %{name}-classic %{version} JPP/%{name} classic
install -p -m 644 %{name}-access/target/%{name}-access-%{version}.jar %{buildroot}%{_javadir}/%{name}/access-%{version}.jar
install -p -m 644 %{name}-access/target/%{name}-access-%{version}-tests.jar %{buildroot}%{_javadir}/%{name}/access-tests-%{version}.jar
%add_to_maven_depmap ch.qos.logback %{name}-access %{version} JPP/%{name} access
install -p -m 644 %{name}-examples/target/%{name}-examples-%{version}.jar %{buildroot}%{_javadir}/%{name}/examples-%{version}.jar
%add_to_maven_depmap ch.qos.logback %{name}-examples %{version} JPP/%{name} examples
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
%add_to_maven_depmap ch.qos.logback %{name}-parent %{version} JPP/%{name} parent
install -p -m 644 %{name}-core/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-core.pom
install -p -m 644 %{name}-classic/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-classic.pom
install -p -m 644 %{name}-access/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-access.pom
install -p -m 644 %{name}-examples/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-examples.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -rf target/site/apidocs/* \
                  %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}*/%{name}
%exclude %dir %{_javadocdir}/%{name}
%{_javadir}/%{name}/access-%{version}.jar
%{_javadir}*/%{name}/access.jar
%{_javadir}*/%{name}/classic-%{version}.jar
%{_javadir}*/%{name}/classic.jar
%{_javadir}*/%{name}/core-%{version}.jar
%{_javadir}*/%{name}/core.jar
%{_javadir}*/%{name}/examples-%{version}.jar
%{_javadir}*/%{name}/examples.jar
%{_javadir}*/%{name}/access-tests-%{version}.jar
%{_javadir}*/%{name}/access-tests.jar
%{_javadir}*/%{name}/classic-tests-%{version}.jar
%{_javadir}*/%{name}/classic-tests.jar
%{_javadir}*/%{name}/core-tests-%{version}.jar
%{_javadir}*/%{name}/core-tests.jar
%{_datadir}/maven2/poms/JPP.%{name}-access.pom
%{_datadir}/maven2/poms/JPP.%{name}-classic.pom
%{_datadir}/maven2/poms/JPP.%{name}-core.pom
%{_datadir}/maven2/poms/JPP.%{name}-examples.pom
%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.27-alt1_1jpp6
- new version

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt2_2jpp6
- build with compat slf4j15

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.14-alt1_2jpp6
- new version

