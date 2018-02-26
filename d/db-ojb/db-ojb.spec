Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: xdoclet
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
# Copyright (c) 2000-2009, JPackage Project
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

# If you want to build with the xdoclet-ojb-module
# give rpmbuild option '--with xdoclet'
# You will then need to set and export an environment
# variable 'XDOCLETSRC' pointing to 
# /some/where/BUILD/xdoclet-x.y.z

%define with_xdoclet %{?_with_xdoclet:1}%{!?_with_xdoclet:0}
%define without_xdoclet %{!?_with_xdoclet:1}%{?_with_xdoclet:0}

%define base_name ojb

Name:           db-ojb
Version:        1.0.4
Release:        alt2_4jpp5
Epoch:          0
Summary:        ObJectRelationalBridge

Group:          Development/Java
License:        Apache Software License
URL:            http://db.apache.org/ojb/
Source0:        ojb-1.0.4-src.tar.gz
# FIXME: build forrest package iot build these documents:
Source1:        ojb-1.0.4-doc.tar.gz
Source2:        db-ojb-torque-database_3_1.dtd
Source3:        http://repo1.maven.org/maven2/ojb/db-ojb/1.0.4/db-ojb-1.0.4.pom

Patch0:         db-ojb-1.0.4-build_xml.patch
Patch1:         db-ojb-1.0.4-Torque33-TorqueDBHandling.patch
Patch2:         db-ojb-1.0.4-ojbcore-schema.patch
Patch3:         db-ojb-1.0.4-ojbtest-schema.patch


%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-swing
BuildRequires: ant-trax
BuildRequires: apache-jdo-1.1-api
BuildRequires: apache-jdo-1.1-impl
BuildRequires: junit
BuildRequires: antlr
BuildRequires: concurrent
BuildRequires: db-ddlutils
BuildRequires: excalibur-avalon-logkit
BuildRequires: geronimo-j2ee-1.4-apis
BuildRequires: geronimo-servlet-2.4-api
BuildRequires: hsqldb
BuildRequires: jakarta-commons-betwixt0
BuildRequires: jakarta-jcs
BuildRequires: xalan-j2
BuildRequires: xdoclet
BuildRequires: xjavadoc

BuildRequires: asm
BuildRequires: cglib
BuildRequires: db-torque-gen >= 0:3.3
BuildRequires: db-torque-gen-templates >= 0:3.3
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-configuration
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-pool
BuildRequires: jakarta-commons-transaction
BuildRequires: regexp
BuildRequires: log4j
BuildRequires: p6spy
BuildRequires: texen
BuildRequires: velocity
BuildRequires: village
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis

Requires: asm
Requires: cglib
Requires: db-torque-gen >= 0:3.3
Requires: db-torque-gen-templates >= 0:3.3
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-configuration
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-digester
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-commons-pool
Requires: jakarta-commons-transaction
Requires: regexp
Requires: log4j
Requires: p6spy
Requires: texen
Requires: velocity
Requires: village
#Requires:  jaxp_parser_impl
#Requires:  xml-commons-jaxp-1.3-apis
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3

%description
ObJectRelationalBridge (OJB) is an Object/Relational 
mapping tool that allows transparent persistence for 
Java Objects against relational databases. 

%if %{with_xdoclet}
%package        xdoclet-module
Summary:        XDoclet module for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}
Requires: xdoclet

%description    xdoclet-module
%{summary}.
%endif

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildRequires: jakarta-commons-beanutils-javadoc
BuildRequires: jakarta-commons-collections-javadoc
BuildRequires: jakarta-commons-dbcp-javadoc
BuildRequires: jakarta-commons-lang-javadoc
BuildRequires: jakarta-commons-logging-javadoc
BuildRequires: jakarta-commons-pool-javadoc
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.

%package        demo
Summary:        Samples for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}

%description    demo
%{summary}.

%prep
%setup -q -n %{base_name}-%{version}-src
gzip -dc %{SOURCE1} | tar xf -
#find . -name "*.jar" -exec rm {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
cp %{SOURCE2} database_3_1.dtd
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3

%build
export ANT_OPTS="$ANT_OPTS -Xms512m -Xmx2048m -Xss1m"
pushd lib
ln -sf $(build-classpath ant) .
ln -sf $(build-classpath ant/ant-junit) .
ln -sf $(build-classpath ant/ant-swing) .
ln -sf $(build-classpath ant/ant-trax) .
ln -sf $(build-classpath ant-launcher) .
ln -sf $(build-classpath antlr) .
ln -sf $(build-classpath asm/asm) .
ln -sf $(build-classpath cglib) .
ln -sf $(build-classpath commons-beanutils) .
ln -sf $(build-classpath commons-betwixt0) .
ln -sf $(build-classpath commons-collections) .
ln -sf $(build-classpath commons-dbcp) .
ln -sf $(build-classpath commons-digester) .
ln -sf $(build-classpath commons-lang) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath commons-pool) .
ln -sf $(build-classpath commons-transaction) .
ln -sf $(build-classpath concurrent) .
ln -sf $(build-classpath db-ddlutils) .
ln -sf $(build-classpath excalibur/avalon-logkit) .
ln -sf $(build-classpath geronimo-j2ee-1.4-apis) .
ln -sf $(build-classpath geronimo-servlet-2.4-api) .
ln -sf $(build-classpath hsqldb) .
ln -sf $(build-classpath jcs) .
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath log4j) .
ln -sf $(build-classpath p6spy) .
ln -sf $(build-classpath regexp) .
ln -sf $(build-classpath texen) .
ln -sf $(build-classpath db-torque-gen) .
ln -sf $(build-classpath db-torque-gen-templates) .
ln -sf $(build-classpath velocity) .
ln -sf $(build-classpath village) .
ln -sf $(build-classpath xalan-j2) .
ln -sf $(build-classpath xdoclet/xdoclet) .
ln -sf $(build-classpath xdoclet/xdoclet-ejb-module) .
ln -sf $(build-classpath xdoclet/xdoclet-jboss-module) .
ln -sf $(build-classpath xdoclet/xdoclet-jmx-module) .
ln -sf $(build-classpath xdoclet/xdoclet-objectweb-module) .
ln -sf $(build-classpath xdoclet/xdoclet-web-module) .
ln -sf $(build-classpath xjavadoc) .
ln -sf $(build-classpath xerces-j2) .
ln -sf $(build-classpath xml-commons-apis) .
#
ln -sf $(build-classpath apache-jdo-1.1-api) .
ln -sf $(build-classpath apache-jdo-1.1-impl) .
popd

ant \
    oql \
    jdoql \
    jar \
    javadoc \
    junit \
    junit-report \
    ejb-examples \
    lockservlet-war \
    sample-jars \
    rar \
    war
%if %{with_xdoclet}
ant -Dxdoclet.src.dir=${XDOCLETSRC} -f build-xdoclet-module.xml rebuild
%endif
#   ojb-quickstart \
#   with-jdori \

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -Dpm 644 dist/%{name}-%{version}.jar \
     $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
install -pm 644 dist/%{name}-%{version}-junit.jar \
     $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit-%{version}.jar
install -pm 644 dist/%{name}-%{version}-tools.jar \
     $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-tools-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap ojb %{name} %{version} JPP/%{name} %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr profile $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -pm 644 dist/%{base_name}-lockserver.war \
           $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -pm 644 dist/%{base_name}-jca.rar \
           $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%if %{with_xdoclet}
# xdoclet module
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/xdoclet
install -pm 644 lib/xdoclet-ojb-module*.jar $RPM_BUILD_ROOT%{_javadir}/xdoclet
pushd $RPM_BUILD_ROOT%{_javadir}/xdoclet
    for j in xdoclet-ojb-module*.jar; do
        ln -sf $j xdoclet-ojb-module.jar
    done
popd
%endif

#javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf doc/api

#manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p release-notes.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# demo
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/ejb
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/ejb/src
cp -pr src/ejb/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/ejb/src
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/ejb/lib
install -pm 644 dist/%{name}-%{version}-client.jar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/ejb/lib
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
install -pm 644 dist/tutorial*-src.jar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
install -pm 644 dist/misc-samples-src.jar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/samples
install -pm 644 dist/ojb-servlet.war \
      $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# remove cruft we REALLY don't need
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/bin
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/db-ojb-blank*.jar

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm \
--exclude %{_datadir}/%{name}-%{version}/ojb-lockserver.war \
--exclude %{_datadir}/%{name}-%{version}/ojb-servlet.war \
--exclude %{_datadir}/%{name}-%{version}/ojb-jca.rar \
--exclude %{_datadir}/%{name}-%{version}/ejb/lib/db-ojb-1.0.4-client.jar
%endif

%files
%doc %{_docdir}/%{name}-%{version}/LICENSE
%doc %{_docdir}/%{name}-%{version}/release-notes.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-%{version}.jar
%{_javadir}/%{name}/%{name}.jar
%{_javadir}/%{name}/%{name}-junit-%{version}.jar
%{_javadir}/%{name}/%{name}-junit.jar
%{_javadir}/%{name}/%{name}-tools-%{version}.jar
%{_javadir}/%{name}/%{name}-tools.jar
%{_datadir}/%{name}-%{version}/profile
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{name}-%{version}-client.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if %{with_xdoclet}
%files xdoclet-module
%{_javadir}/xdoclet/*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/xdoclet*-%{version}.jar.*
%endif
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}-%{version}

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt2_4jpp5
- selected java5 compiler explicitly

* Fri Dec 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_4jpp5
- new release

* Sat Feb 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_3jpp5
- fixed build after maven 2.0.7

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.4-alt1_3jpp1.7
- converted from JPackage by jppimport script

