BuildRequires: maven-plugin-descriptor
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

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define base_name   torque

Name:           db-torque
Version:        3.3
Release:        alt4_3jpp5
Epoch:          0
Summary:        Torque persistence layer

Group:          Development/Java
License:        Apache Software License
URL:            http://db.apache.org/torque/
Source0:        torque-3.3-src.tar.gz
#svn export http://svn.apache.org/repos/asf/db/torque/runtime/tags/TORQUE_3_3/ torque-runtime-3.3
#svn export http://svn.apache.org/repos/asf/db/torque/generator/tags/TORQUE_3_3/ torque-generator-3.3
#svn export http://svn.apache.org/repos/asf/db/torque/templates/tags/TORQUE_3_3/ torque-templates-3.3
#svn export http://svn.apache.org/repos/asf/db/torque/maven-plugin/tags/TORQUE_3_3/ torque-maven-plugin-3.3
#svn export http://svn.apache.org/repos/asf/db/torque/maven2-plugin/tags/TORQUE_3_3/ torque-maven2-plugin-3.3
#svn export http://svn.apache.org/repos/asf/db/torque/site/tags/TORQUE_3_3/ torque-site-3.3
#svn export http://svn.apache.org/repos/asf/db/torque/common/tags/TORQUE_3_3/ torque-common-3.3
#svn export http://svn.apache.org/repos/asf/db/torque/village/tags/TORQUE_3_3/ torque-village-3.3
##svn export  http://svn.apache.org/repos/asf/db/torque/test/tags/TORQUE_3_3/ torque-test-3.3

Source1:        db-torque-3.3-jpp-depmap.xml
Source2:        db-torque-3.3-settings.xml
Source3:        torque-nav-inc.xml
Source4:        db-torque-maven1-jpp-depmap.xml
Source5:        pom-maven2jpp-depcat.xsl
Source6:        pom-maven2jpp-newdepmap.xsl
Source7:        pom-maven2jpp-mapdeps.xsl
Source8:        project-nav-inc.xml


Patch0:         db-torque-common-pom.patch
Patch1:         db-torque-3.3-runtime-pom.patch
Patch2:         db-torque-3.3-generator-project_xml.patch

%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: junit
%if %{with_maven}
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugins-base
BuildRequires: maven1-plugin-changelog
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: checkstyle4
BuildRequires: checkstyle4-optional
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-jcoverage
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-linkcheck
BuildRequires: maven1-plugin-pmd
BuildRequires: maven1-plugin-scm
BuildRequires: maven1-plugin-site
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: sf-findbugs-maven-plugin

#
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-gpg
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-surefire-plugin
%endif
BuildRequires: excalibur-avalon-framework-api
BuildRequires: excalibur-avalon-framework-impl
BuildRequires: excalibur-avalon-logkit
BuildRequires: fulcrum-testcontainer
BuildRequires: fulcrum-yaafi
BuildRequires: gnu.getopt
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-configuration >= 0:1.2
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-pool
BuildRequires: jakarta-jcs
BuildRequires: jamonapi
BuildRequires: log4j
BuildRequires: mysql-connector-java
BuildRequires: saxon
BuildRequires: saxon-scripts
BuildRequires: texen
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

Requires: excalibur-avalon-framework-api
Requires: excalibur-avalon-framework-impl
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-configuration >= 0:1.2
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-commons-pool
Requires: jakarta-jcs
Requires: jamonapi
Requires: jdbc-stdext >= 0:2.0
Requires: jndi >= 0:1.2.1
Requires: log4j
Requires: texen
Requires: xerces-j2
Requires: xml-commons-apis
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Torque is a persistence layer. Torque includes a 
generator to generate all the database resources 
required by your application and includes a 
runtime environment to run the generated classes. 

%package        runtime-javadoc
Summary:        Javadoc for %{name}-runtime
Group:          Development/Documentation

%description    runtime-javadoc
%{summary}.

%package        runtime-manual
Summary:        Docs for %{name}-runtime
Group:          Development/Documentation

%description    runtime-manual
%{summary}.

%package        gen
Summary:        Generator for %{name}
Group:          Development/Java

%description    gen
%{summary}.

%package        gen-javadoc
Summary:        Javadoc for %{name}-gen
Group:          Development/Documentation

%description    gen-javadoc
%{summary}.

%package        gen-manual
Summary:        Docs for %{name}-gen
Group:          Development/Documentation

%description    gen-manual
%{summary}.

%package        gen-templates
Summary:        Templates for %{name}
Group:          Development/Java

%description    gen-templates
%{summary}.

%package        gen-templates-manual
Summary:        Docs for %{name}-gen-templates
Group:          Development/Documentation

%description    gen-templates-manual
%{summary}.

%package        village
Summary:        Village for %{name}
Group:          Development/Java
Provides:       village = %{epoch}:%{version}-%{release}
Obsoletes:      village < 0:3.3

%description    village
%{summary}.

%package        village-javadoc
Summary:        Javadoc for %{name}-village
Group:          Development/Documentation
Provides:       village-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      village-javadoc < 0:3.3

%description    village-javadoc
%{summary}.

%package        village-manual
Summary:        Docs for %{name}-village
Group:          Development/Documentation
Provides:       village-manual = %{epoch}:%{version}-%{release}
Obsoletes:      village-manual < 0:3.3

%description    village-manual
%{summary}.

%package        maven-plugin
Summary:        Maven plugin for %{name}
Group:          Development/Java
Requires: %{name}-gen = %{epoch}:%{version}

%description    maven-plugin
%{summary}.

%package        maven-plugin-manual
Summary:        Docs for %{name}-maven-plugin
Group:          Development/Documentation

%description    maven-plugin-manual
%{summary}.

%package        maven2-plugin
Summary:        Maven2 plugin for %{name}
Group:          Development/Java
Requires: %{name}-gen = %{epoch}:%{version}

%description    maven2-plugin
%{summary}.

%package        maven2-plugin-javadoc
Summary:        Javadoc for %{name}-maven2-plugin
Group:          Development/Documentation

%description    maven2-plugin-javadoc
%{summary}.

%package        maven2-plugin-manual
Summary:        Docs for %{name}-maven2-plugin
Group:          Development/Documentation

%description    maven2-plugin-manual
%{summary}.

%prep
%setup -q -c -n %{base_name}-%{version}-src
cp %{SOURCE3} .
cp %{SOURCE8} .
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2

for p in $(find . -name project.xml | grep common); do
    sed -i -e '/simian/d' -e 's/3\.3\.1-SNAPSHOT/3.3/' $p
done

if [ ! -f %{SOURCE4} ]; then
export DEPCAT=$(pwd)/%{name}-%{version}-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE5} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE6} > %{name}-%{version}-depmap.new.xml
fi
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE7} map=%{SOURCE4}
    popd
done


%build
export LANG=C
#mkdir external_repo
#ln -s %{_javadir} external_repo/JPP

#export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository

pushd torque-common-3.3
sed -i -e 's,<module>../,<module>,' pom.xml
ln -s ../torque-[g-v]*-3.3 .

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dgpg.skip=true \
        -Dmaven.test.failure.ignore=true \
        install 
#	javadoc:javadoc 

popd

export MAVEN_HOME_LOCAL=$(pwd)/.maven
mkdir -p $MAVEN_HOME_LOCAL/repository/JPP/jars/
ln -sf $(build-classpath jdbc-stdext) $MAVEN_HOME_LOCAL/repository/JPP/jars/jdbc.jar
ln -sf $(build-classpath jndi) $MAVEN_HOME_LOCAL/repository/JPP/jars/jndi.jar
mkdir -p $MAVEN_HOME_LOCAL/repository/JPP/jars/batik
ln -sf $(build-classpath xmlgraphics-batik/dom) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/dom.jar
ln -sf $(build-classpath xmlgraphics-batik/awt-util) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/awt-util.jar
ln -sf $(build-classpath xmlgraphics-batik/bridge) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/bridge.jar
ln -sf $(build-classpath xmlgraphics-batik/css) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/css.jar
ln -sf $(build-classpath xmlgraphics-batik/ext) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/ext.jar
ln -sf $(build-classpath xmlgraphics-batik/extension) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/extension.jar
ln -sf $(build-classpath xmlgraphics-batik/gui-util) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/gui-util.jar
ln -sf $(build-classpath xmlgraphics-batik/gvt) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/gvt.jar
ln -sf $(build-classpath xmlgraphics-batik/parser) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/parser.jar
ln -sf $(build-classpath xmlgraphics-batik/rasterizer) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/rasterizer.jar
ln -sf $(build-classpath xmlgraphics-batik/script) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/script.jar
ln -sf $(build-classpath xmlgraphics-batik/svg-dom) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/svg-dom.jar
ln -sf $(build-classpath xmlgraphics-batik/svggen) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/svggen.jar
ln -sf $(build-classpath xmlgraphics-batik/swing) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/swing.jar
ln -sf $(build-classpath xmlgraphics-batik/transcoder) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/transcoder.jar
ln -sf $(build-classpath xmlgraphics-batik/util) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/util.jar
ln -sf $(build-classpath xmlgraphics-batik/xml) $MAVEN_HOME_LOCAL/repository/JPP/jars/batik/xml.jar


pushd torque-site-%{version}
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    xdoc:transform
popd
pushd torque-village-%{version}
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    jar:install xdoc:transform
popd
pushd torque-runtime-%{version}
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    xdoc:transform
popd
pushd torque-templates-%{version}
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    jar:install xdoc:transform
popd
pushd torque-generator-%{version}
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    jar:install xdoc:transform
popd
pushd torque-maven2-plugin-%{version}
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    xdoc:transform
popd

pushd torque-maven-plugin-%{version}
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    jar:install javadoc:generate xdoc:transform
popd


%install
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 torque-runtime-%{version}/target/torque-runtime-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}-runtime-%{version}.jar
install -m 644 torque-generator-%{version}/target/torque-generator-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}-generator-%{version}.jar
install -m 644 torque-templates-%{version}/target/torque-templates-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}-templates-%{version}.jar
install -m 644 torque-village-%{version}/target/village-%{version}.jar \
                  $RPM_BUILD_ROOT%{_javadir}/%{name}-village-%{version}.jar

ln -s %{name}-runtime-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-runtime.jar
ln -s %{name}-runtime-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-generator-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-generator.jar
ln -s %{name}-generator.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-gen.jar
ln -s %{name}-templates-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-templates.jar
ln -s %{name}-templates.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-gen-templates.jar
ln -s %{name}-village-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-village.jar
ln -s %{name}-village.jar $RPM_BUILD_ROOT%{_javadir}/village.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 torque-common-3.3/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-common.pom
%add_to_maven_depmap org.apache.torque torque %{version} JPP %{name}-common
install -m 644 torque-generator-3.3/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-generator.pom
%add_to_maven_depmap org.apache.torque torque-generator %{version} JPP %{name}-generator
install -m 644 torque-maven2-plugin-3.3/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-maven2-plugin.pom
%add_to_maven_depmap org.apache.torque torque-maven-plugin %{version} JPP %{name}-maven2-plugin
install -m 644 torque-runtime-3.3/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-runtime.pom
%add_to_maven_depmap org.apache.torque torque-runtime %{version} JPP %{name}-runtime
install -m 644 torque-templates-3.3/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-templates.pom
%add_to_maven_depmap org.apache.torque torque-templates %{version} JPP %{name}-templates
install -m 644 torque-village-3.3/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-village.pom
%add_to_maven_depmap org.apache.torque village %{version} JPP village

install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
install -m 644 torque-maven2-plugin-%{version}/target/torque-maven-plugin-%{version}.jar \
               $RPM_BUILD_ROOT%{_javadir}/torque-maven2-plugin-%{version}.jar
ln -s torque-maven2-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/torque-maven2-plugin.jar
ln -s %{_javadir}/torque-maven2-plugin.jar $RPM_BUILD_ROOT%{_datadir}/maven2/plugins/torque-maven-plugin.jar

install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/maven1/plugins
install -d -m 755 ${RPM_BUILD_ROOT}%{_javadir}/maven1-plugins
install -m 644 torque-maven-plugin-%{version}/target/maven-torque-plugin-%{version}.jar \
               $RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-torque-plugin-%{version}.jar
ln -s maven-torque-plugin-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/maven1/plugins/maven-torque-plugin.jar
ln -s %{_datadir}/maven1/plugins/maven-torque-plugin.jar $RPM_BUILD_ROOT%{_javadir}/maven1-plugins/maven-torque-plugin.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf
cp -pr torque-runtime-3.3/src/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/conf

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-generator-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-maven2-plugin-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-runtime-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-village-%{version}
%if %{with_maven}
#cp -pr torque-generator-%{version}/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-generator-%{version}
#cp -pr torque-maven2-plugin-%{version}/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-maven2-plugin-%{version}
#cp -pr torque-runtime-%{version}/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-runtime-%{version}
#cp -pr torque-village-%{version}/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-village-%{version}
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-generator-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-generator # ghost symlink
ln -s %{name}-maven2-plugin-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-maven2-plugin # ghost symlink
ln -s %{name}-runtime-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-runtime # ghost symlink
ln -s %{name}-village-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-village # ghost symlink


# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp torque-common-%{version}/LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-generator-%{version}/generator
cp -pr torque-generator-3.3/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-generator-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-maven2-plugin-%{version}
cp -pr torque-maven2-plugin-3.3/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-maven2-plugin-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-maven-plugin-%{version}
cp -pr torque-maven-plugin-3.3/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-maven-plugin-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-runtime-%{version}
cp -pr torque-runtime-3.3/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-runtime-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
cp -pr torque-site-3.3/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/site
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-templates-%{version}
cp -pr torque-templates-3.3/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-templates-%{version}
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-village-%{version}
cp -pr torque-village-3.3/target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-village-%{version}


%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%doc %{_docdir}/%{name}-%{version}/*.txt
%doc %{_docdir}/%{name}-%{version}/site
%{_javadir}/%{name}-runtime-%{version}.jar
%{_javadir}/%{name}-runtime.jar
%{_javadir}/%{name}.jar
%{_datadir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-runtime-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files runtime-javadoc
%doc %{_javadocdir}/%{name}-runtime-%{version}
%doc %{_javadocdir}/%{name}-runtime

%files runtime-manual
%doc %{_docdir}/%{name}-runtime-%{version}

%files gen
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}-generator-%{version}.jar
%{_javadir}/%{name}-generator.jar
%{_javadir}/%{name}-gen.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-generator-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files gen-javadoc
%doc %{_javadocdir}/%{name}-generator-%{version}
%doc %{_javadocdir}/%{name}-generator

%files gen-manual
%doc %{_docdir}/%{name}-generator-%{version}

%files gen-templates
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}-templates-%{version}.jar
%{_javadir}/%{name}-templates.jar
%{_javadir}/%{name}-gen-templates.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files gen-templates-manual
%doc %{_docdir}/%{name}-templates-%{version}

%files village
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}-village-%{version}.jar
%{_javadir}/%{name}-village.jar
%{_javadir}/village.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-village-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files village-javadoc
%doc %{_javadocdir}/%{name}-village-%{version}
%doc %{_javadocdir}/%{name}-village

%files village-manual
%doc %{_docdir}/%{name}-village-%{version}

%files maven-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_datadir}/maven1/plugins/maven-torque-plugin-%{version}.jar
%{_datadir}/maven1/plugins/maven-torque-plugin.jar
%{_javadir}/maven1-plugins/maven-torque-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files maven-plugin-manual
%doc %{_docdir}/%{name}-maven-plugin-%{version}

%files maven2-plugin
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/torque-maven2-plugin-%{version}.jar
%{_javadir}/torque-maven2-plugin.jar
%{_datadir}/maven2/plugins/torque-maven-plugin.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%files maven2-plugin-javadoc
%doc %{_javadocdir}/%{name}-maven2-plugin-%{version}
%doc %{_javadocdir}/%{name}-maven2-plugin

%files maven2-plugin-manual
%doc %{_docdir}/%{name}-maven2-plugin-%{version}

%changelog
* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt4_3jpp5
- java5 target build

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_3jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt2_3jpp5
- use maven1

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_3jpp5
- new jpp release

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_2jpp5
- new version

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_7jpp5
- fixed build w/java5

* Fri Aug 10 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_7jpp1.7
- converted from JPackage by jppimport script

