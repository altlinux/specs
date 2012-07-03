%define _without_demo 1
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 1.2.3
%define name xdoclet
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with demo
%bcond_with demo
#def_with gcj_support
%bcond_with gcj_support
%bcond_without maven
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/xdoclet/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define mversion 1.2
%define xjavadoc_version 1.1


# FIXME: JPP 1.7 lacks webwork and xwork, needed for the demo

Name:           xdoclet
Version:        1.2.3
Release:        alt4_13jpp6
Epoch:          0
Summary:        Attribute Orientated Programming Framework
# BSD-style, see <http://xdoclet.sourceforge.net/xdoclet/licenses/xdoclet-license.html>
License:        BSD
Group:          Development/Java
URL:            http://xdoclet.sourceforge.net/
Source0:        %{name}-src-%{version}.tgz
Source1:        %{name}-modules-objectweb-4.6.tgz
Source2:        %{name}-component-info.xml
Source3:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet/1.2.3/xdoclet-1.2.3.pom
Source4:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-apache-module/1.2.3/xdoclet-apache-module-1.2.3.pom
Source5:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-bea-module/1.2.3/xdoclet-bea-module-1.2.3.pom
Source6:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-borland-module/1.2.3/xdoclet-borland-module-1.2.3.pom
Source7:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-caucho-module/1.2.3/xdoclet-caucho-module-1.2.3.pom
Source8:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-de-locale/1.2.3/xdoclet-de-locale-1.2.3.pom
Source9:        http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-ejb-module/1.2.3/xdoclet-ejb-module-1.2.3.pom
Source10:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-exolab-module/1.2.3/xdoclet-exolab-module-1.2.3.pom
Source11:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-fr_FR-locale/1.2.3/xdoclet-fr_FR-locale-1.2.3.pom
Source12:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-hibernate-module/1.2.3/xdoclet-hibernate-module-1.2.3.pom
Source13:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-hp-module/1.2.3/xdoclet-hp-module-1.2.3.pom
Source14:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-ibm-module/1.2.3/xdoclet-ibm-module-1.2.3.pom
Source15:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-java-module/1.2.3/xdoclet-java-module-1.2.3.pom
Source16:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-jboss-module/1.2.3/xdoclet-jboss-module-1.2.3.pom
Source17:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-jdo-module/1.2.3/xdoclet-jdo-module-1.2.3.pom
Source18:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-jmx-module/1.2.3/xdoclet-jmx-module-1.2.3.pom
Source19:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-jsf-module/1.2.3/xdoclet-jsf-module-1.2.3.pom
Source20:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-libelis-module/1.2.3/xdoclet-libelis-module-1.2.3.pom
Source21:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-macromedia-module/1.2.3/xdoclet-macromedia-module-1.2.3.pom
Source22:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-mockobjects-module/1.2.3/xdoclet-mockobjects-module-1.2.3.pom
Source23:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-mvcsoft-module/1.2.3/xdoclet-mvcsoft-module-1.2.3.pom
Source24:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-mx4j-module/1.2.3/xdoclet-mx4j-module-1.2.3.pom
Source25:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-objectweb-module/1.2.3/xdoclet-objectweb-module-1.2.3.pom
Source26:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-openejb-module/1.2.3/xdoclet-openejb-module-1.2.3.pom
Source27:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-oracle-module/1.2.3/xdoclet-oracle-module-1.2.3.pom
Source28:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-orion-module/1.2.3/xdoclet-orion-module-1.2.3.pom
Source29:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-portlet-module/1.2.3/xdoclet-portlet-module-1.2.3.pom
Source30:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-pramati-module/1.2.3/xdoclet-pramati-module-1.2.3.pom
Source31:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-pt_BR-locale/1.2.3/xdoclet-pt_BR-locale-1.2.3.pom
Source32:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-solarmetric-module/1.2.3/xdoclet-solarmetric-module-1.2.3.pom
Source33:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-spring-module/1.2.3/xdoclet-spring-module-1.2.3.pom
Source34:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-sun-module/1.2.3/xdoclet-sun-module-1.2.3.pom
Source35:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-sybase-module/1.2.3/xdoclet-sybase-module-1.2.3.pom
Source36:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-tjdo-module/1.2.3/xdoclet-tjdo-module-1.2.3.pom
Source37:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-web-module/1.2.3/xdoclet-web-module-1.2.3.pom
Source38:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-webwork-module/1.2.3/xdoclet-webwork-module-1.2.3.pom
Source39:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-wsee-module/1.2.3/xdoclet-wsee-module-1.2.3.pom
Source40:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/xdoclet-xdoclet-module/1.2.3/xdoclet-xdoclet-module-1.2.3.pom
Source41:       http://mirrors.ibiblio.org/pub/mirrors/maven2/xdoclet/maven-xdoclet-plugin/1.2/maven-xdoclet-plugin-1.2.pom
Patch0:         xdoclet-build_xml.patch
Patch1:         xdoclet-XDocletModulesEjbMessages.patch
Patch2:         xdoclet-ant.not-required.patch
Patch3:         xdoclet-WebLogicSubTask.patch
Patch4:         xdoclet-project_xml.patch
Patch5:         xdoclet-AbstractProgramElementTagsHandler.patch
Patch6:         xdoclet-build_docs_xml.patch
Patch7:         xdoclet-maven-plugin-project.patch
Patch8:         xdoclet-maven-plugin-template.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       bsf
Requires:       jakarta-commons-collections
Requires:       jakarta-commons-logging
Requires:       log4j
Requires:       mockobjects >= 0:0.09-17
Requires:       velocity
Requires:       xalan-j2 >= 0:2.7.0
Requires:       xml-commons-jaxp-1.3-apis
Requires:       xjavadoc >= 0:%{xjavadoc_version}
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-nodeps >= 0:1.5
BuildRequires:  ant-trax
%if %with maven
BuildRequires:  maven1 >= 0:1.1
%endif
BuildRequires:  junit
BuildRequires:  javacc
BuildRequires:  jrefactory
BuildRequires:  bsf
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-lang
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-net
BuildRequires:  log4j
BuildRequires:  mockobjects >= 0:0.09-17
BuildRequires:  struts
BuildRequires:  velocity
BuildRequires:  xalan-j2 >= 0:2.7.0
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xjavadoc = 0:1.1
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
This package contains the XDoclet Attribute Orientated Programming Framework

%if %with demo
%package demo
Summary:        XDoclet Sample Projects
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       geronimo-ejb-2.1-api
Requires:       myfaces
Requires:       geronimo-jms-1.1-api
Requires:       webwork
Requires:       xwork
Requires:       mx4j
Requires:       struts
Requires:       servletapi4
BuildRequires:  servletapi4
BuildRequires:  struts
BuildRequires:  velocity
BuildRequires:  webwork >= 0:2.1
BuildRequires:  xwork
BuildRequires:  geronimo-ejb-2.1-api
BuildRequires:  myfaces
BuildRequires:  geronimo-jms-1.1-api
BuildRequires:  mx4j

%description demo
This package contains sample XDoclet projects.
%endif

%if %with maven
%package maven-plugin
Summary:        XDoclet Maven Plugin
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       maven1 >= 0:1.1

%description maven-plugin
%{summary}.
%endif

%package javadoc
Summary:        XDoclet Javadoc
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains XDoclet javadoc

%package manual
Summary:        XDoclet Sample Manuals and Documentation
Group:          Development/Documentation
BuildArch: noarch

%description manual
This package contains XDoclet documentation.

%if %with repolib
%package repolib
Summary:         Artifacts to be uploaded to a repository library
Group:           Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
find -type f -name "*.jar" | xargs -t %{__rm}

# Replace JOnAS specific tasks with code blessed by ObjectWeb
# FIXME: (dwalluck) use %%setup here
pushd modules
mv objectweb objectweb.orig
tar xzf %{SOURCE1}
popd

XJAVADOC_VERSION=%{xjavadoc_version}
for j in jrefactory javacc junit bsf commons-collections commons-logging log4j velocity xalan-j2 xjavadoc-${XJAVADOC_VERSION} xml-commons-jaxp-1.3-apis mockobjects-core; do
        ln -s $(build-classpath $j) lib
done

%if %with demo
for j in servletapi4 struts velocity webwork-migration xwork geronimo-ejb-2.1-api myfaces/myfaces-jsf-api geronimo-jms-1.1-api; do
        ln -s $(build-classpath $j) samples/lib
done
for j in mx4j/mx4j-jmx mx4j/mx4j-tools; do
        i=$(build-classpath $j)
        ln -s $(build-classpath $j) samples/lib
done
%endif

%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5
%patch6 -p0 -b .sav6
%patch7 -p0 -b .sav7
%patch8 -p0 -b .sav8

%build
export CLASSPATH=$(%{_bindir}/build-classpath xalan-j2-serializer)
export MAVEN_HOME=%{_datadir}/maven
export MAVEN_LOCAL_HOME=$(pwd)/.maven
XJAVADOC_VERSION=%{xjavadoc_version}
%if %with maven
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dxjavadoc.version=${XJAVADOC_VERSION} core modules maven docs l10n
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Dxjavadoc.version=${XJAVADOC_VERSION} core modules docs l10n
%endif
%if %with demo
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 samples
%endif

%install

mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 644 target/lib/xdoclet*-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
%if %with maven
install -p -m 644 target/lib/maven-xdoclet-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/
%endif
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -s ${jar} `/bin/echo ${jar} | sed "s|-%{version}||g"`; done)

%if %with demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr samples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
%endif

%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet.pom
%{__cp} -p %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-apache-module.pom
%{__cp} -p %{SOURCE5} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-bea-module.pom
%{__cp} -p %{SOURCE6} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-borland-module.pom
%{__cp} -p %{SOURCE7} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-caucho-module.pom
%{__cp} -p %{SOURCE8} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-de-locale.pom
%{__cp} -p %{SOURCE9} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-ejb-module.pom
%{__cp} -p %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-exolab-module.pom
%{__cp} -p %{SOURCE11} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-fr_FR-locale.pom
%{__cp} -p %{SOURCE12} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-hibernate-module.pom
%{__cp} -p %{SOURCE13} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-hp-module.pom
%{__cp} -p %{SOURCE14} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-ibm-module.pom
%{__cp} -p %{SOURCE15} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-java-module.pom
%{__cp} -p %{SOURCE16} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jboss-module.pom
%{__cp} -p %{SOURCE17} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jdo-module.pom
%{__cp} -p %{SOURCE18} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jmx-module.pom
%{__cp} -p %{SOURCE19} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jsf-module.pom
%{__cp} -p %{SOURCE20} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-libelis-module.pom
%{__cp} -p %{SOURCE21} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-macromedia-module.pom
%{__cp} -p %{SOURCE22} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-mockobjects-module.pom
%{__cp} -p %{SOURCE23} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-mvcsoft-module.pom
%{__cp} -p %{SOURCE24} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-mx4j-module.pom
%{__cp} -p %{SOURCE25} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-objectweb-module.pom
%{__cp} -p %{SOURCE26} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-openejb-module.pom
%{__cp} -p %{SOURCE27} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-oracle-module.pom
%{__cp} -p %{SOURCE28} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-orion-module.pom
%{__cp} -p %{SOURCE29} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-portlet-module.pom
%{__cp} -p %{SOURCE30} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-pramati-module.pom
%{__cp} -p %{SOURCE31} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-pt_BR-locale.pom
%{__cp} -p %{SOURCE32} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-solarmetric-module.pom
%{__cp} -p %{SOURCE33} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-spring-module.pom
%{__cp} -p %{SOURCE34} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-sun-module.pom
%{__cp} -p %{SOURCE35} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-sybase-module.pom
%{__cp} -p %{SOURCE36} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-tjdo-module.pom
%{__cp} -p %{SOURCE37} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-web-module.pom
%{__cp} -p %{SOURCE38} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-webwork-module.pom
%{__cp} -p %{SOURCE39} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-wsee-module.pom
%{__cp} -p %{SOURCE40} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-xdoclet-module.pom
%{__cp} -p %{SOURCE41} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-maven-xdoclet-plugin.pom
%add_to_maven_depmap xdoclet xdoclet %{version} JPP/%{name} xdoclet
%add_to_maven_depmap xdoclet xdoclet-apache-module %{version} JPP/%{name} xdoclet-apache-module
%add_to_maven_depmap xdoclet xdoclet-bea-module %{version} JPP/%{name} xdoclet-bea-module
%add_to_maven_depmap xdoclet xdoclet-borland-module %{version} JPP/%{name} xdoclet-borland-module
%add_to_maven_depmap xdoclet xdoclet-caucho-module %{version} JPP/%{name} xdoclet-caucho-module
%add_to_maven_depmap xdoclet xdoclet-de-locale %{version} JPP/%{name} xdoclet-de-locale
%add_to_maven_depmap xdoclet xdoclet-ejb-module %{version} JPP/%{name} xdoclet-ejb-module
%add_to_maven_depmap xdoclet xdoclet-exolab-module %{version} JPP/%{name} xdoclet-exolab-module
%add_to_maven_depmap xdoclet xdoclet-fr_FR-locale %{version} JPP/%{name} xdoclet-fr_FR-locale
%add_to_maven_depmap xdoclet xdoclet-hibernate-module %{version} JPP/%{name} xdoclet-hibernate-module
%add_to_maven_depmap xdoclet xdoclet-hp-module %{version} JPP/%{name} xdoclet-hp-module
%add_to_maven_depmap xdoclet xdoclet-ibm-module %{version} JPP/%{name} xdoclet-ibm-module
%add_to_maven_depmap xdoclet xdoclet-java-module %{version} JPP/%{name} xdoclet-java-module
%add_to_maven_depmap xdoclet xdoclet-jboss-module %{version} JPP/%{name} xdoclet-jboss-module
%add_to_maven_depmap xdoclet xdoclet-jdo-module %{version} JPP/%{name} xdoclet-jdo-module
%add_to_maven_depmap xdoclet xdoclet-jmx-module %{version} JPP/%{name} xdoclet-jmx-module
%add_to_maven_depmap xdoclet xdoclet-jsf-module %{version} JPP/%{name} xdoclet-jsf-module
%add_to_maven_depmap xdoclet xdoclet-libelis-module %{version} JPP/%{name} xdoclet-libelis-module
%add_to_maven_depmap xdoclet xdoclet-macromedia-module %{version} JPP/%{name} xdoclet-macromedia-module
%add_to_maven_depmap xdoclet xdoclet-mockobjects-module %{version} JPP/%{name} xdoclet-mockobjects-module
%add_to_maven_depmap xdoclet xdoclet-mvcsoft-module %{version} JPP/%{name} xdoclet-mvcsoft-module
%add_to_maven_depmap xdoclet xdoclet-mx4j-module %{version} JPP/%{name} xdoclet-mx4j-module
%add_to_maven_depmap xdoclet xdoclet-objectweb-module %{version} JPP/%{name} xdoclet-objectweb-module
%add_to_maven_depmap xdoclet xdoclet-openejb-module %{version} JPP/%{name} xdoclet-openejb-module
%add_to_maven_depmap xdoclet xdoclet-oracle-module %{version} JPP/%{name} xdoclet-oracle-module
%add_to_maven_depmap xdoclet xdoclet-orion-module %{version} JPP/%{name} xdoclet-orion-module
%add_to_maven_depmap xdoclet xdoclet-portlet-module %{version} JPP/%{name} xdoclet-portlet-module
%add_to_maven_depmap xdoclet xdoclet-pramati-module %{version} JPP/%{name} xdoclet-pramati-module
%add_to_maven_depmap xdoclet xdoclet-pt_BR-locale %{version} JPP/%{name} xdoclet-pt_BR-locale
%add_to_maven_depmap xdoclet xdoclet-solarmetric-module %{version} JPP/%{name} xdoclet-solarmetric-module
%add_to_maven_depmap xdoclet xdoclet-spring-module %{version} JPP/%{name} xdoclet-spring-module
%add_to_maven_depmap xdoclet xdoclet-sun-module %{version} JPP/%{name} xdoclet-sun-module
%add_to_maven_depmap xdoclet xdoclet-sybase-module %{version} JPP/%{name} xdoclet-sybase-module
%add_to_maven_depmap xdoclet xdoclet-tjdo-module %{version} JPP/%{name} xdoclet-tjdo-module
%add_to_maven_depmap xdoclet xdoclet-web-module %{version} JPP/%{name} xdoclet-web-module
%add_to_maven_depmap xdoclet xdoclet-webwork-module %{version} JPP/%{name} xdoclet-webwork-module
%add_to_maven_depmap xdoclet xdoclet-wsee-module %{version} JPP/%{name} xdoclet-wsee-module
%add_to_maven_depmap xdoclet xdoclet-xdoclet-module %{version} JPP/%{name} xdoclet-xdoclet-module
%add_to_maven_depmap xdoclet maven-xdoclet-plugin %{mversion} JPP/%{name} maven-xdoclet-plugin

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/api
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH5} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH6} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH7} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 0644 %{PATCH8} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-jmx-module.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-web-module.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-java-module.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-portlet-module.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-jboss-module.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p %{_javadir}/xjavadoc.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-hibernate-module.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-ejb-module.jar $RPM_BUILD_ROOT%{repodirlib}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/xdoclet-xdoclet-module.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm --exclude %{_datadir}/%{name}-%{version}/target/classes
%endif

%files
%doc LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/xdoclet-%{version}.jar
%{_javadir}/%{name}/xdoclet.jar
%{_javadir}/%{name}/xdoclet-apache-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-apache-module.jar
%{_javadir}/%{name}/xdoclet-bea-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-bea-module.jar
%{_javadir}/%{name}/xdoclet-borland-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-borland-module.jar
%{_javadir}/%{name}/xdoclet-caucho-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-caucho-module.jar
%{_javadir}/%{name}/xdoclet-de-locale-%{version}.jar
%{_javadir}/%{name}/xdoclet-de-locale.jar
%{_javadir}/%{name}/xdoclet-ejb-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-ejb-module.jar
%{_javadir}/%{name}/xdoclet-exolab-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-exolab-module.jar
%{_javadir}/%{name}/xdoclet-fr_FR-locale-%{version}.jar
%{_javadir}/%{name}/xdoclet-fr_FR-locale.jar
%{_javadir}/%{name}/xdoclet-hibernate-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-hibernate-module.jar
%{_javadir}/%{name}/xdoclet-hp-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-hp-module.jar
%{_javadir}/%{name}/xdoclet-ibm-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-ibm-module.jar
%{_javadir}/%{name}/xdoclet-java-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-java-module.jar
%{_javadir}/%{name}/xdoclet-jboss-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-jboss-module.jar
%{_javadir}/%{name}/xdoclet-jdo-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-jdo-module.jar
%{_javadir}/%{name}/xdoclet-jmx-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-jmx-module.jar
%{_javadir}/%{name}/xdoclet-jsf-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-jsf-module.jar
%{_javadir}/%{name}/xdoclet-libelis-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-libelis-module.jar
%{_javadir}/%{name}/xdoclet-macromedia-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-macromedia-module.jar
%{_javadir}/%{name}/xdoclet-mockobjects-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-mockobjects-module.jar
%{_javadir}/%{name}/xdoclet-mvcsoft-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-mvcsoft-module.jar
%{_javadir}/%{name}/xdoclet-mx4j-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-mx4j-module.jar
%{_javadir}/%{name}/xdoclet-objectweb-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-objectweb-module.jar
%{_javadir}/%{name}/xdoclet-openejb-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-openejb-module.jar
%{_javadir}/%{name}/xdoclet-oracle-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-oracle-module.jar
%{_javadir}/%{name}/xdoclet-orion-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-orion-module.jar
%{_javadir}/%{name}/xdoclet-portlet-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-portlet-module.jar
%{_javadir}/%{name}/xdoclet-pramati-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-pramati-module.jar
%{_javadir}/%{name}/xdoclet-pt_BR-locale-%{version}.jar
%{_javadir}/%{name}/xdoclet-pt_BR-locale.jar
%{_javadir}/%{name}/xdoclet-solarmetric-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-solarmetric-module.jar
%{_javadir}/%{name}/xdoclet-spring-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-spring-module.jar
%{_javadir}/%{name}/xdoclet-sun-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-sun-module.jar
%{_javadir}/%{name}/xdoclet-sybase-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-sybase-module.jar
%{_javadir}/%{name}/xdoclet-tjdo-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-tjdo-module.jar
%{_javadir}/%{name}/xdoclet-web-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-web-module.jar
%{_javadir}/%{name}/xdoclet-webwork-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-webwork-module.jar
%{_javadir}/%{name}/xdoclet-wsee-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-wsee-module.jar
%{_javadir}/%{name}/xdoclet-xdoclet-module-%{version}.jar
%{_javadir}/%{name}/xdoclet-xdoclet-module.jar
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-apache-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-bea-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-borland-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-caucho-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-de-locale.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-ejb-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-exolab-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-fr_FR-locale.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-hibernate-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-hp-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-ibm-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-java-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jboss-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jdo-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jmx-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-jsf-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-libelis-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-macromedia-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-mockobjects-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-mvcsoft-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-mx4j-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-objectweb-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-openejb-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-oracle-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-orion-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-portlet-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-pramati-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-pt_BR-locale.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-solarmetric-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-spring-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-sun-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-sybase-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-tjdo-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-web-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-webwork-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-wsee-module.pom
%{_datadir}/maven2/poms/JPP.%{name}-xdoclet-xdoclet-module.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/xdoclet-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-apache-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-bea-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-borland-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-caucho-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-ejb-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-exolab-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-hibernate-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-hp-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-ibm-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-java-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-jboss-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-jdo-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-jmx-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-jsf-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-libelis-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-macromedia-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-mockobjects-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-mvcsoft-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-mx4j-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-objectweb-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-openejb-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-oracle-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-orion-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-portlet-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-pramati-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-solarmetric-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-spring-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-sun-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-sybase-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-tjdo-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-web-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-webwork-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-wsee-module-%{version}.jar.*
%{_libdir}/gcj/%{name}/xdoclet-xdoclet-module-%{version}.jar.*
%endif

%if %with maven
%files maven-plugin
%{_javadir}/%{name}/maven-xdoclet-plugin-%{version}.jar
%{_javadir}/%{name}/maven-xdoclet-plugin.jar
%{_datadir}/maven2/poms/JPP.%{name}-maven-xdoclet-plugin.pom
%endif

%if %with demo
%files demo
%{_datadir}/%{name}-%{version}
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt4_13jpp6
- new jpp relase

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt4_12jpp5
- maven1 dependency translaton

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt3_12jpp5
- fixed repocop warnings

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt3_9jpp1.7
- rebuilt with maven1

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt2_9jpp1.7
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt1_9jpp1.7
- converted from JPackage by jppimport script

