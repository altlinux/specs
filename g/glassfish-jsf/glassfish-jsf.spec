Patch33: glassfish-jsf-1.2.12-alt-java7.patch
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/sun-jsf/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define version_maj  1
%define version_min  2
%define version_rev  12
%define version_tag %{version_maj}.%{version_min}_%{version_rev}
%define version_full %{version_tag}

Name:           glassfish-jsf
Version:        %{version_maj}.%{version_min}_%{version_rev}
Release:        alt4_1jpp6
Epoch:          0
Summary:        GlassFish JSF
License:        CDDL
Group:          Development/Java
URL:            https://javaserverfaces.dev.java.net/
# cvs -Q -z3 -d :pserver:guest@cvs.dev.java.net:/cvs export -r JSF_1_2_12_B01 -d glassfish-jsf-1.2.12 javaserverfaces-sources && tar cjf glassfish-jsf-1.2.12.tar.bz2 glassfish-jsf-1.2.12
Source0:        glassfish-jsf-1.2.12.tar.bz2
Source1:        glassfish-jsf-component-info.xml
Source2:        glassfish-jsf-1.2.12-dependencies.tar.bz2
Patch0:         glassfish-jsf-xslt.patch
Patch1:         glassfish-jsf-create-domain-no-failonerror.patch
BuildRequires: annotation_1_0_api
BuildRequires: ant
BuildRequires: ant-trax
BuildRequires: apache-portlet-1.0-api
BuildRequires: el_1_0_api
BuildRequires: glassfish-jstl
BuildRequires: groovy15
BuildRequires: htmlunit
BuildRequires: jakarta-cactus
BuildRequires: jakarta-taglibs-standard
BuildRequires: jpackage-utils
BuildRequires: jsp_2_1_api
BuildRequires: junit >= 0:3.8.1
BuildRequires: portlet_1_0_api
BuildRequires: servlet_2_5_api
BuildRequires: tlddoc >= 0:1.3
BuildRequires: unzip
BuildArch:      noarch
Source44: import.info

%description
The JSF 1.2 implementation. NB: We've omitted the classes
Jetty6InjectionProvider and GlassFishInjectionProvider from the
package com.sun.faces.vendor.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n glassfish-jsf-%{version_maj}.%{version_min}.%{version_rev}
%setup -q -n glassfish-jsf-%{version_maj}.%{version_min}.%{version_rev} -T -D -a 2
%if 0
%{_bindir}/find -name "*.jar" -o -name "*.class" | %{_bindir}/xargs -t %{__rm}
%endif

pushd dependencies
for i in *.zip; do
    %{__unzip} -qq $i
done
popd

%{__cp} -p build.properties.glassfish build.properties

cat >> build.properties << EOF
junit.jar=$(build-classpath junit)
htmlunit.home=%{_javadir}
cactus.home=%{_javadir}
tlddoc.jar=$(build-classpath tlddoc)
maven.repository.importer.jar=$(pwd)/dependencies/jars/maven-repository-importer-1.2.jar
servlet.jar=$(build-classpath servlet_2_5_api)
jsp.jar=$(build-classpath jsp_2_1_api)
jstl.jar=$(build-classpath jstl)
# This is jsr250-api
annotation.jar=$(build-classpath annotation_1_0_api)
portlet.jar=$(build-classpath portlet_1_0_api)
groovy.jar=$(build-classpath groovy15-all)
sun-commons-collections.jar=$(pwd)/dependencies/jars/com-sun-commons-collections-2.1.jar
sun-commons-digester.jar=$(pwd)/dependencies/jars/com-sun-commons-digester-1.5.jar
sun-commons-beanutils.jar=$(pwd)/dependencies/jars/com-sun-commons-beanutils-1.6.1.jar
sun-commons-logging.jar=$(pwd)/dependencies/jars/com-sun-commons-logging-1.0.4.jar
##tomcat6.home=%{_javadir}/tomcat6
##jetty.home=%{_javadir}/jetty6
glassfish.installer.jar=glassfish-installer-v2ur1-b09d-
jsf.build.home=$(pwd)
#facelet.jar=$(build-classpath jsf-facelets)
EOF

dependency_base_dir=$(pwd)/dependencies
glassfish_installer_jar=glassfish-installer-v2ur1-b09d-
fl_os=linux

#rm dependencies/glassfish-installer-v2ur1-b09d-linux.jar

pushd ${dependency_base_dir}
echo > ${dependency_base_dir}/install.bat
echo a > input
%{java} -Xmx256m -jar ${dependency_base_dir}/${glassfish_installer_jar}${fl_os}.jar -console < ./input
chmod 700 ${dependency_base_dir}/install.bat
${dependency_base_dir}/install.bat || :
rm ${dependency_base_dir}/install.bat
rm ${dependency_base_dir}/input
popd
%patch0 -p0 -b .xslt
%patch1 -p0 -b .create-domain-no-failonerror
%patch33
pushd ${dependency_base_dir}/glassfish
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f ${dependency_base_dir}/glassfish/setup.xml setup
popd
echo > ${dependency_base_dir}/glassfish/password.txt << EOF
AS_ADMIN_PASSWORD=adminadmin
EOF

%build
export CLASSPATH=$(build-classpath el_1_0_api)
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/trax`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first

%install

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 0644 jsf-api/build/lib/jsf-api.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-api-%{version_full}.jar
install -p -m 0644 jsf-ri/build/lib/jsf-impl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-impl-%{version_full}.jar

pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-api-%{version_full}.jar  %{name}-api.jar
ln -s %{name}-impl-%{version_full}.jar %{name}-impl.jar
ln -s %{name}-api-%{version_full}.jar  jsf-api.jar
ln -s %{name}-impl-%{version_full}.jar jsf-impl.jar
popd

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i s/@VERSION@/%{version_full}-brew/g $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/jsf-api.jar $RPM_BUILD_ROOT%{repodirlib}/jsf-api.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/jsf-impl.jar $RPM_BUILD_ROOT%{repodirlib}/jsf-impl.jar
%endif

%if %with repolib
%define compatrepodir %{_javadir}/repository.jboss.com/glassfish/jsf/%{version_full}-brew
install -d -m 755 $RPM_BUILD_ROOT%{compatrepodir}/
ln -s ../../../sun-jsf/%{version_full}-brew/lib $RPM_BUILD_ROOT%{compatrepodir}/lib
ln -s ../../../sun-jsf/%{version_full}-brew/src $RPM_BUILD_ROOT%{compatrepodir}/src
cp $RPM_BUILD_ROOT%{repodir}/component-info.xml $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
sed -i s,sun-jsf,glassfish/jsf, $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
%endif

%files
%{_javadir}/jsf-api.jar
%{_javadir}/%{name}-api.jar
%{_javadir}/%{name}-api-%{version_full}.jar
%{_javadir}/jsf-impl.jar
%{_javadir}/%{name}-impl.jar
%{_javadir}/%{name}-impl-%{version_full}.jar

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2_12-alt4_1jpp6
- fixed build with java 7

* Sun Jul 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2_12-alt3_1jpp6
- fixed build

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2_12-alt2_1jpp6
- jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2_12-alt1_1jpp6
- new jpackage release

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2_09-alt1_1jpp5
- new version

