Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define base_name ddlutils

Name:           db-%{base_name}
Version:        1.0
Release:        alt1_1jpp6
Epoch:          0
Summary:        DDL utilities

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://db.apache.org/ddlutils/
Source0:        ddlutils-1.0.tar.gz
# svn export  http://svn.apache.org/repos/asf/db/ddlutils/tags/1.0/
Source1:        DdlUtils-1.0-dev-doc.zip
# generated with forrest ...
Source2:        db-ddlutils-jpp-depmap.xml
Source3:        db-ddlutils-settings.xml

Patch0:         db-ddlutils-1.0-jdbc.properties.hsqldb.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.3
# build-only
BuildRequires: ant >= 0:1.6.5
BuildRequires: javacc3
BuildRequires: junit
# dbs
BuildRequires: axion
BuildRequires: derby
BuildRequires: hsqldb
BuildRequires: mckoi
BuildRequires: mysql-connector-java
BuildRequires: postgresql-jdbc

%if %{with_maven}
BuildRequires: maven2 >= 2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven-surefire-plugin
%endif
# runtime
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-betwixt0
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-pool
BuildRequires: dom4j
BuildRequires: jaxen
BuildRequires: jakarta-oro
BuildRequires: log4j
BuildRequires: wstx
BuildRequires: stax_1_0_api

Requires: jakarta-commons-beanutils
Requires: jakarta-commons-betwixt0
Requires: jakarta-commons-codec
Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-digester
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-commons-pool
Requires: dom4j
Requires: jaxen
Requires: jakarta-oro
Requires: log4j
Requires: wstx
Requires: stax_1_0_api
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Source44: import.info

%description
DdlUtils is a small, easy-to-use component for working with 
Database Definition (DDL) files. These are XML files that contain 
the definition of a database schema, e.g. tables and columns. 
These files can be fed into DdlUtils via its Ant task or 
programmatically in order to create the corresponding database 
or alter it so that it corresponds to the DDL. Likewise, DdlUtils 
can generate a DDL file for an existing database.
DdlUtils uses the Turbine XML format, which is shared by Torque 
and OJB. This format expresses the database schema in a 
database-independent way by using JDBC datatypes instead of raw 
SQL datatypes which are inherently database specific.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.

%prep
%setup -q -n %{base_name}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0
unzip -qq %{SOURCE1}
rm -rf doc/api
%if %{with_maven}
cp %{SOURCE3} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml
%else
pushd lib
pushd build-only
ln -sf $(build-classpath ant)
ln -sf $(build-classpath junit)
popd
ln -sf $(build-classpath hsqldb)

ln -sf $(build-classpath wstx/wstx-asl)
ln -sf $(build-classpath log4j)
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath commons-dbcp)
ln -sf $(build-classpath jakarta-oro)
ln -sf $(build-classpath commons-beanutils)
ln -sf $(build-classpath dom4j)
ln -sf $(build-classpath jaxen)
ln -sf $(build-classpath commons-pool)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-codec)
ln -sf $(build-classpath commons-lang)
ln -sf $(build-classpath commons-digester)
ln -sf $(build-classpath commons-betwixt0)
ln -sf $(build-classpath stax_1_0_api)
popd
%endif

%build
%if %{with_maven}
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

mvn-jpp \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
	install:install-file -DgroupId=commons-primitives -DartifactId=commons-primitives -Dversion=1.0 -Dpackaging=jar -Dfile=$(build-classpath commons-primitives)

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djdbc.properties.file=$(pwd)/src/test-profiles/mvdb/jdbc.properties.hsqldb \
    -Dtest.profile.directory=src/test-profiles \
    -Dprofile=mvdb \
    jar javadoc junit-hsqldb
# FIXME:  few unit tests failing now with hsqldb
%endif

%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
%if %{with_maven}
install -m 644 target/ddlutils-1.0.jar \
     $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
install -m 644 dist/DdlUtils-%{version}.jar \
     $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap org.apache.ddlutils %{base_name} %{version} JPP %{name}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

#javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %{with_maven}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr target/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

#manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*.jar
%doc LICENSE.txt
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp6
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- new jpackage release

* Tue Jul 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.070308.1jpp1.7
- converted from JPackage by jppimport script

