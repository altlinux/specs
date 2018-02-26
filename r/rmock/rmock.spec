Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: avalon-logkit
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%define plugin_version  1.0
%define skin_version    1.0

Name:           rmock
Summary:        RMOCK - A Java Test-Double Framework
Url:            http://rmock.sourceforge.net/
Version:        2.0.0
Release:        alt6_2jpp5
Epoch:          0
License:        Apache Software License 2.0
Group:          Development/Java
Source0:        rmock-2.0.0.tar.gz
# Steps to reproduce
# mkdir rmock-2.0.0; cd rmock-2.0.0
# cvs -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock login
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 com.agical.rdoc
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 com.agical.rmock
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 documentation
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 lib
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 rmock-ext-aspectj
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 rmock-ext-gui
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 rmock-framework
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 rmock-maven-plugin
#cvs -z3 -d:pserver:anonymous@rmock.cvs.sourceforge.net:/cvsroot/rmock export -r RMOCK_2_0_0 rmock-skin
# cd ..; tar cf rmock-2.0.0.tar rmock-2.0.0; gzip rmock-2.0.0.tar


Source1:        rmock-2.0.0-settings.xml
Source2:        rmock-2.0.0-jpp-depmap.xml
Patch0:         rmock-com.agical.rmock-pom.patch
Patch1:         rmock-com.agical.rdoc-pom.patch
Patch33:	rmock-com.agical.rdoc-pom-alt-javacc5.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-site
BuildRequires: maven-surefire-plugin
BuildRequires: mojo-maven2-plugin-javacc
BuildRequires: ant
BuildRequires: ant-trax
BuildRequires: fop


BuildRequires: cglib
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-commons-collections
BuildRequires: junit
BuildRequires: velocity

Requires: maven2
Requires: cglib
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-collections
Requires: junit
Requires: velocity


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
RMock is a Java mock object framework to use with jUnit. 
RMock has support for a setup-modify-run-verify workflow 
when writing jUnit tests. It integrates better with IDE 
refactoring support and allows designing classes and 
interfaces in a true test-first fashion. 


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
chmod -R go=u-w *
for f in $(find . -name "*.jar"); do
  mv $f $f.no
done
cp %{SOURCE1} settings.xml

%patch0 -b .sav0
%patch1 -b .sav1
%patch33 -b .sav1

%build
export LANG=en_US.ISO8859-1

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL

mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
ln -sf $(pwd)/rmock-maven-plugin/pom.xml \
  $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/com.agical.rmock-rmock-maven-plugin.pom

mkdir -p $MAVEN_REPO_LOCAL/com.agical.rmock
ln -sf $(pwd)/rmock-maven-plugin/target/rmock-maven-plugin-1.0.jar \
  $MAVEN_REPO_LOCAL/com.agical.rmock/rmock-maven-plugin.jar

# 208 hacks
mkdir -p $MAVEN_REPO_LOCAL/com/agical/rmock/rmock-maven-plugin/2.0.8/
ln -sf $(pwd)/rmock-maven-plugin/pom.xml \
  $MAVEN_REPO_LOCAL/com/agical/rmock/rmock-maven-plugin/2.0.8/rmock-maven-plugin-2.0.8.pom
ln -sf $(pwd)/rmock-maven-plugin/target/rmock-maven-plugin-1.0.jar \
  $MAVEN_REPO_LOCAL/com/agical/rmock/rmock-maven-plugin/2.0.8/rmock-maven-plugin-2.0.8.jar
#end 208 hacks

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export SETTINGS=$(pwd)/settings.xml
cd rmock-framework
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $SETTINGS \
        -Dmaven.test.failure.ignore=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/plugins

%add_to_maven_depmap com.agical.rmock parent %{version} JPP/%{name} parent
install -m 644 rmock-framework/parent_pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-parent.pom

install -m 644 com.agical.rdoc/target/tddoc-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/tddoc-%{version}.jar
%add_to_maven_depmap com.agical.rmock tddoc %{version} JPP/%{name} tddoc
install -m 644 com.agical.rdoc/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-tddoc.pom

install -m 644 com.agical.rmock/target/%{name}-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
%add_to_maven_depmap com.agical.rmock %{name} %{version} JPP/%{name} %{name}
install -m 644 com.agical.rmock/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom

install -m 644 documentation/target/documentation-%{version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/documentation-%{version}.jar
%add_to_maven_depmap com.agical.rmock documentation %{version} JPP/%{name} documentation
install -m 644 documentation/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-documentation.pom

install -m 644 rmock-maven-plugin/target/%{name}-maven-plugin-%{plugin_version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-maven-plugin-%{plugin_version}.jar
%add_to_maven_depmap com.agical.rmock %{name}-maven-plugin %{plugin_version} JPP/%{name} %{name}-maven-plugin
install -m 644 rmock-maven-plugin/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-maven-plugin.pom


install -m 644 rmock-skin/target/%{name}-skin-%{skin_version}.jar \
   $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-skin-%{skin_version}.jar
%add_to_maven_depmap com.agical.rmock %{name}-skin %{skin_version} JPP/%{name} %{name}-maven-plugin
install -m 644 rmock-skin/pom.xml \
   $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-skin.pom


(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{plugin_version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{plugin_version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{skin_version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{skin_version}||g"`; done)
pushd ${RPM_BUILD_ROOT}%{_datadir}/maven2/plugins
    ln -sf %{_javadir}/%{name}/%{name}-maven-plugin.jar
popd

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
for m in com.agical.rdoc com.agical.rmock documentation rmock-maven-plugin; do 
    mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${m}
    cp -pr ${m}/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/${m}
done
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}
%{_datadir}/maven2/plugins/*maven-plugin.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt6_2jpp5
- fixed build with java 7

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt5_2jpp5
- fixed build with new javacc5

* Wed Sep 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt4_2jpp5
- fixed build with new maven 2.0.8

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt3_2jpp5
- fixes for java6 support

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt2_2jpp5
- fixed build with maven 2.0.7

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp5
- converted from JPackage by jppimport script

