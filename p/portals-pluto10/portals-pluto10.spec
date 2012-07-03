Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define bname    pluto

Name:           portals-%{bname}10
Version:        1.0.1
Release:        alt5_2jpp5
Epoch:          0
Summary:        Portlet 1.0 Reference Implementation
License:        Apache Software License 2.0
Url:            http://portals.apache.org/pluto/
Group:          Development/Java
Source0:        portals-pluto-1.0.1.tar.gz
# svn export http://svn.apache.org/repos/asf/portals/pluto/tags/release-1.0.1/ portals-pluto-1.0.1

Source1:        pom-maven2jpp-depcat.xsl
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        pluto-1.0.1-jpp-depmap.xml
Source5:        http://repo1.maven.org/maven2/portlet-api/portlet-api/1.0/portlet-api-1.0.pom
Source6:        http://repo1.maven.org/maven2/org/apache/pluto/pluto/1.0.1/pluto-1.0.1.pom
Source7:        http://repo1.maven.org/maven2/org/apache/pluto/pluto-deploy/1.0.1/pluto-deploy-1.0.1.pom
Source8:        http://repo1.maven.org/maven2/org/apache/pluto/pluto-portal/1.0.1/pluto-portal-1.0.1.pom
Source9:        http://repo1.maven.org/maven2/org/apache/pluto/pluto-descriptors/1.0.1/pluto-descriptors-1.0.1.pom
Source10:       portals-pluto-1.0.1-deploy-build.xml
Source11:       portals-pluto-1.0.1-testsuite-build.xml
Patch0:         pluto-1.0.1-project_xml.patch
Patch1:         pluto-1.0.1-container-project_xml.patch
Patch2:         pluto-1.0.1-portal-project_xml.patch
Patch3:         pluto-1.0.1-api-project_xml.patch
Patch4:         pluto-1.0.1-descriptors-project_xml.patch
Patch5:         pluto-1.0.1-deploy-project_xml.patch
Patch6:         pluto-1.0.1-container-build.patch
Patch7:         pluto-1.0.1-descriptors-build.patch
Patch8:         pluto-1.0.1-portal-build.patch

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: junit
%if %{with_maven}
BuildRequires: maven1 >= 0:1.1
BuildRequires: maven1-plugin-changelog
BuildRequires: maven1-plugin-changes
BuildRequires: maven1-plugin-checkstyle
BuildRequires: maven1-plugin-developer-activity
BuildRequires: maven1-plugin-faq
BuildRequires: maven1-plugin-file-activity
BuildRequires: maven1-plugin-javadoc
BuildRequires: maven1-plugin-jdepend
BuildRequires: maven1-plugin-junit-report
BuildRequires: maven1-plugin-jxr
BuildRequires: maven1-plugin-license
BuildRequires: maven1-plugin-multiproject
BuildRequires: maven1-plugin-tasklist
BuildRequires: maven1-plugin-test
BuildRequires: maven1-plugin-xdoc
BuildRequires: saxon
BuildRequires: saxon-scripts
%endif
BuildRequires: castor0
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-taglibs-standard
BuildRequires: servletapi4
BuildRequires: xerces-j2

Requires: %{name}-portlet-1.0-api = %{epoch}:%{version}-%{release}
Requires: castor0
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-digester
Requires: jakarta-commons-fileupload
Requires: jakarta-commons-logging
Requires: jakarta-taglibs-standard
Requires: servletapi4
Requires: xerces-j2

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
Pluto is the Reference Implementation of the Java Portlet 
Specfication. The current version of this specification 
is JSR 168. 
Portlets are designed to run in the context of a portal. 
They are written to the Portlet API which are similar to 
the Servlet API.
A portlet container provides a runtime environment for 
portlets implemented according to the Portlet API. In 
this environment portlets can be instantiated, used and 
finally destroyed. The portlet container is not a 
stand-alone container like the servlet container; instead 
it is implemented as a thin layer on top of the servlet 
container and reuses the functionality provided by the 
servlet container. 
Pluto serves as portlet container that implements the 
Portlet API and offers developers a working example 
platform from which they can test their portlets. 


%package portlet-1.0-api
Summary:        Portlet 1.0 API from %{name}
Group:          Development/Java
Provides:       portlet_1_0_api
Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description portlet-1.0-api
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%if %{with_maven}
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n portals-%{bname}-%{version}
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8

mv deploy/build.xml deploy/deploy-build.xml
cp %{SOURCE10} deploy/build.xml
cp %{SOURCE11} testsuite/build.xml

%build
%if %{with_maven}
cp container/maven.xml descriptors
export DEPCAT=$(pwd)/pluto-1.0.1-depcat.new.xml
echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    /usr/bin/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
echo >> $DEPCAT
echo '</depset>' >> $DEPCAT
/usr/bin/saxon $DEPCAT %{SOURCE2} > pluto-1.0.1-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    /usr/bin/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven

maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
    -Dmaven.repo.remote=file:///usr/share/maven1/repository \
    -Dmaven.home.local=$MAVEN_HOME_LOCAL \
    -Dgoal=jar:install,javadoc,test:test \
    multiproject:goal xdoc:transform
%else
#Our processing order:
#Portlet API (JSR-168)
#Pluto Portlet Container
#Pluto Descriptor Libraries
#Pluto Portlet Deployment
#Pluto Portal Driver
#Pluto Portlet Test Suite
export CLASSPATH=
pushd api
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
servletapi4 \
)
CLASSPATH=$CLASSPATH:$(pwd)/api/target/portlet-api-1.0.jar
pushd container
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
castor0 \
servletapi4 \
xerces-j2 \
)
pushd descriptors
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
xerces-j2 \
)
CLASSPATH=$CLASSPATH:$(pwd)/descriptors/target/pluto-descriptors-1.0.1.jar
pushd deploy
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
castor0 \
commons-fileupload \
servletapi4 \
xerces-j2 \
)
CLASSPATH=$CLASSPATH:$(pwd)/api/target/portlet-api-1.0.jar
CLASSPATH=$CLASSPATH:$(pwd)/container/target/pluto-1.0.1.jar
CLASSPATH=$CLASSPATH:$(pwd)/descriptors/target/pluto-descriptors-1.0.1.jar
pushd portal
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
export CLASSPATH=$(build-classpath \
commons-digester \
servletapi4 \
xerces-j2 \
)
CLASSPATH=$CLASSPATH:$(pwd)/api/target/portlet-api-1.0.jar
pushd testsuite
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
popd
%endif

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 api/target/portlet-api-1.0.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}-portlet-1.0-api-%{version}.jar
%add_to_maven_depmap javax.portlet portlet-api 1.0 JPP portlet_1_0_api
%add_to_maven_depmap portlet-api portlet-api 1.0 JPP %{name}-portlet-1.0-api
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP-%{name}-portlet-1.0-api.pom

install -m 644 container/target/%{bname}-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/%{bname}-%{version}.jar
%add_to_maven_depmap org.apache.pluto %{bname} %{version} JPP/%{name} %{bname}
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-%{bname}.pom

install -m 644 deploy/target/%{bname}-deploy-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/%{bname}-deploy-%{version}.jar
%add_to_maven_depmap org.apache.pluto %{bname}-deploy %{version} JPP/%{name} %{bname}-deploy
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-%{bname}-deploy.pom

install -m 644 portal/target/%{bname}-portal-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/%{bname}-portal-%{version}.jar
%add_to_maven_depmap org.apache.pluto %{bname}-portal %{version} JPP/%{name} %{bname}-portal
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-%{bname}-portal.pom

install -m 644 descriptors/target/%{bname}-descriptors-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/%{bname}-descriptors-%{version}.jar
%add_to_maven_depmap org.apache.pluto %{bname}-descriptors %{version} JPP/%{name} %{bname}-descriptors
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT/%{_datadir}/maven2/poms/JPP.%{name}-%{bname}-descriptors.pom

install -m 644 testsuite/target/testsuite-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/%{name}/testsuite-%{version}.jar

# create unversioned symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/deploy
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/descriptors
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/portal
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/testsuite
%if %{with_maven}
cp -pr api/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr container/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
cp -pr deploy/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/deploy
cp -pr descriptors/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/descriptors
cp -pr portal/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/portal
cp -pr testsuite/target/docs/apidocs/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/testsuite
%else
cp -pr api/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/api
cp -pr container/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/container
cp -pr deploy/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/deploy
cp -pr descriptors/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/descriptors
cp -pr portal/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/portal
cp -pr testsuite/dist/docs/api/* \
    $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/testsuite
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.TXT $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.portlet-api $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %{with_maven}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/portlet_1_0_api_%{name}-portlet-1.0-api<<EOF
%{_javadir}/portlet_1_0_api.jar	%{_javadir}/%{name}-portlet-1.0-api.jar	10000
EOF

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files 
%doc %{_docdir}/%{name}-%{version}/LICENSE.TXT
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{bname}-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{bname}-deploy-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{bname}-portal-%{version}.jar.*
%{_libdir}/gcj/%{name}/%{bname}-descriptors-%{version}.jar.*
%{_libdir}/gcj/%{name}/testsuite-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files portlet-1.0-api
%_altdir/portlet_1_0_api_%{name}-portlet-1.0-api
%doc %{_docdir}/%{name}-%{version}/LICENSE.portlet-api
%{_javadir}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{bname}-portlet-1.0-api-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if %{with_maven}
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt5_2jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt4_2jpp5
- use maven1

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_2jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_2jpp5
- fixed repocop warnings

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_2jpp5
- converted from JPackage by jppimport script

