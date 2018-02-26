BuildRequires: maven-scm maven2-default-skin
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%bcond_without maven


Name:           xmlrpc
Version:        3.1.3
Release:        alt4_4jpp6
Epoch:          0
Summary:        Java XML-RPC implementation
License:        ASL 2.0
Group:          Development/Java
URL:            http://ws.apache.org/xmlrpc/
Source0:        http://www.apache.org/dist/ws/xmlrpc/sources/apache-xmlrpc-3.1.3-src.tar.gz
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-build.xml
Source4:        %{name}-client-build.xml
Source5:        %{name}-common-build.xml
Source6:        %{name}-server-build.xml
Source7:        %{name}-tests-build.xml
Patch0:         xmlrpc-pom_xml.patch
Patch1:         xmlrpc-tests-pom_xml.patch
Patch2:         xmlrpc-site_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jakarta-commons-codec
Requires: jakarta-commons-httpclient
Requires: jakarta-commons-logging
Requires: servlet_2_5_api
Requires: ws-commons-util
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: junit
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-httpclient
BuildRequires: jakarta-commons-logging
BuildRequires: servlet_2_5_api
BuildRequires: ws-commons-util
%if %with maven
BuildRequires: maven2
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-changes
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-eclipse
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: velocity15
BuildRequires: maven2-plugin-site
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
BuildRequires: maven2-default-skin
BuildRequires: maven-release
BuildRequires: apache-commons-parent
BuildRequires: apache-rat
BuildRequires: fonts-ttf-liberation
BuildRequires: xmlrpc
%endif
Buildarch:      noarch
Source44: import.info

%description
Apache XML-RPC is a Java implementation of XML-RPC, a popular protocol
that uses XML over HTTP to implement remote procedure calls.
Apache XML-RPC was previously known as Helma XML-RPC. If you have code
using the Helma library, all you should have to do is change the import
statements in your code from helma.xmlrpc.* to org.apache.xmlrpc.*.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n apache-%{name}-%{version}-src

cp -p %{SOURCE1} settings.xml
cp -p %{SOURCE3} build.xml
cp -p %{SOURCE4} client/build.xml
cp -p %{SOURCE5} common/build.xml
cp -p %{SOURCE6} server/build.xml

perl -pi -e 's/\r$//g' LICENSE.txt

%build
%if %with maven
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=`pwd`/.m2/repository \
        -Dmaven.test.failure.ignore=true \
        install javadoc:aggregate site:site

%else
pushd common
export CLASSPATH=`%{_bindir}/build-classpath junit ws-commons-java5 ws-commons-util jaxme/jaxmeapi`
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only jar javadoc
popd

pushd client
export CLASSPATH=$(build-classpath junit ws-commons-java5 ws-commons-util commons-httpclient)
CLASSPATH=$CLASSPATH:../common/target/%{name}-common-%{version}.jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only jar javadoc
popd

pushd server
export CLASSPATH=$(build-classpath junit commons-logging ws-commons-java5 ws-commons-util servlet_2_4_api)
CLASSPATH=$CLASSPATH:../common/target/%{name}-common-%{version}.jar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only jar javadoc
popd

%endif
mkdir -p temp
pushd temp
%{jar} xf ../server/target/%{name}-server-%{version}.jar
%{jar} xf ../client/target/%{name}-client-%{version}.jar
%{jar} xf ../common/target/%{name}-common-%{version}.jar
%{__sed} -i -e "s|-common||g" META-INF/MANIFEST.MF
%{jar} cmf META-INF/MANIFEST.MF ../%{name}-%{version}.jar *
popd

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 xmlrpc-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlrpc-%{version}.jar
install -m 644 common/target/xmlrpc-common-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlrpc-common-%{version}.jar
install -m 644 client/target/xmlrpc-client-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlrpc-client-%{version}.jar
install -m 644 server/target/xmlrpc-server-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlrpc-server-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap org.apache.xmlrpc xmlrpc %{version} JPP/%{name} xmlrpc
%add_to_maven_depmap org.apache.xmlrpc xmlrpc-client %{version} JPP/%{name} xmlrpc-client
%add_to_maven_depmap org.apache.xmlrpc xmlrpc-common %{version} JPP/%{name} xmlrpc-common
%add_to_maven_depmap org.apache.xmlrpc xmlrpc-server %{version} JPP/%{name} xmlrpc-server

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
install -m 644 client/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-client.pom
install -m 644 common/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-common.pom
install -m 644 server/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-server.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
for m in common client server; do
    install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$m
    cp -pr $m/target/site/apidocs/* \
                      $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$m
done
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/apidocs
%endif

%files
%doc LICENSE.txt
%dir %{_javadir}*/%{name}
%exclude %dir %{_javadocdir}/%{name}
%{_javadir}*/%{name}/xmlrpc-%{version}.jar
%{_javadir}*/%{name}/xmlrpc-client-%{version}.jar
%{_javadir}*/%{name}/xmlrpc-client.jar
%{_javadir}*/%{name}/xmlrpc-common-%{version}.jar
%{_javadir}*/%{name}/xmlrpc-common.jar
%{_javadir}*/%{name}/xmlrpc-server-%{version}.jar
%{_javadir}*/%{name}/xmlrpc-server.jar
%{_javadir}*/%{name}/xmlrpc.jar
%{_datadir}/maven2/poms/JPP.%{name}-xmlrpc.pom
%{_datadir}/maven2/poms/JPP.%{name}-xmlrpc-client.pom
%{_datadir}/maven2/poms/JPP.%{name}-xmlrpc-common.pom
%{_datadir}/maven2/poms/JPP.%{name}-xmlrpc-server.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with maven
%files manual
%{_docdir}/%{name}-%{version}
%endif

%changelog
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

