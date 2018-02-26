BuildRequires: /proc
BuildRequires: jpackage-compat
%define oldname slf4j
BuildRequires: excalibur excalibur-avalon-framework
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

%define repodir %{_javadir}/repository.jboss.com/org/slf4j/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define gcj_support 0


Name:           slf4j15
Version:        1.5.8
Release:        alt3_1jpp6
Epoch:          0
Summary:        Simple Logging Facade for Java
Group:          Development/Java
License:        MIT
URL:            http://www.slf4j.org/
Source0:        http://www.slf4j.org/dist/slf4j-1.5.8.tar.gz
Source1:        %{oldname}-settings.xml
Source2:        %{oldname}-jpp-depmap.xml
Source3:        slf4j-component-info.xml
Patch0:         %{oldname}-pom_xml.patch
Patch1:         slf4j-1.5.8-skip-integration-tests.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit >= 0:1.6.5
BuildRequires: javassist >= 0:3.4
BuildRequires: junit >= 0:3.8.2
BuildRequires: maven2 >= 2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: excalibur-avalon-framework
BuildRequires: log4j
BuildRequires: jakarta-commons-logging
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL). 

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter.. 

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

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
%setup -q -n %{oldname}-%{version}
%patch0 -p0
%patch1 -p1
find . -name "*.jar" | xargs rm
cp -p %{SOURCE1} settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL/org.slf4j
ln -sf $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org.slf4j/slf4j-api.jar
ln -sf $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org.slf4j/slf4j-simple.jar
ln -sf $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org.slf4j/slf4j-log4j12.jar
ln -sf $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org.slf4j/slf4j-nop.jar
mkdir -p $MAVEN_REPO_LOCAL/org/slf4j/slf4j-api/%version/
cp $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org/slf4j/slf4j-api/%version/slf4j-api-%version.jar
cp $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org/slf4j/slf4j-api/%version/slf4j-simple-%version.jar
cp $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org/slf4j/slf4j-api/%version/slf4j-log4j12-%version.jar
cp $(build-classpath maven2/empty-dep) $MAVEN_REPO_LOCAL/org/slf4j/slf4j-api/%version/slf4j-nop-%version.jar

%{_bindir}/find -name "*.css" -o -name "*.js" -o -name "*.txt" | %{_bindir}/xargs -t %{__perl} -pi -e 's/\r$//g'

%build
export LANG=en_US.ISO8859-1
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5 \
        -e \
        -s $(pwd)/settings.xml \
        -Dmaven2.jpp.mode=true \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}

#install -m 644 jcl104-over-slf4j/target/jcl104-over-slf4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jcl104-over-slf4j-%{version}.jar
ln -sf jcl-over-slf4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jcl104-over-slf4j-%{version}.jar
install -m 644 jcl-over-slf4j/target/jcl-over-slf4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jcl-over-slf4j-%{version}.jar
install -m 644 jul-to-slf4j/target/jul-to-slf4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jul-to-slf4j-%{version}.jar
install -m 644 log4j-over-slf4j/target/log4j-over-slf4j-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/log4j-over-slf4j-%{version}.jar
install -m 644 slf4j-api/target/%{oldname}-api-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/api-%{version}.jar
install -m 644 slf4j-api/target/%{oldname}-api-%{version}-tests.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/api-tests-%{version}.jar
install -m 644 slf4j-ext/target/%{oldname}-ext-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/ext-%{version}.jar
install -m 644 slf4j-jcl/target/%{oldname}-jcl-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jcl-%{version}.jar
install -m 644 slf4j-jdk14/target/%{oldname}-jdk14-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/jdk14-%{version}.jar
install -m 644 slf4j-log4j12/target/%{oldname}-log4j12-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/log4j12-%{version}.jar
install -m 644 slf4j-migrator/target/%{oldname}-migrator-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/migrator-%{version}.jar
install -m 644 slf4j-nop/target/%{oldname}-nop-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/nop-%{version}.jar
install -m 644 slf4j-simple/target/%{oldname}-simple-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/simple-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap org.slf4j jcl104-over-slf4j %{version} JPP/%{name} jcl104-over-slf4j
%add_to_maven_depmap org.slf4j jcl-over-slf4j %{version} JPP/%{name} jcl-over-slf4j
%add_to_maven_depmap org.slf4j jul-to-slf4j %{version} JPP/%{name} jul-to-slf4j
%add_to_maven_depmap org.slf4j log4j-over-slf4j %{version} JPP/%{name} log4j-over-slf4j
%add_to_maven_depmap org.slf4j %{oldname}-parent %{version} JPP/%{name} parent
%add_to_maven_depmap org.slf4j %{oldname}-api %{version} JPP/%{name} api
%add_to_maven_depmap org.slf4j %{oldname}-ext %{version} JPP/%{name} ext
%add_to_maven_depmap org.slf4j %{oldname}-jcl %{version} JPP/%{name} jcl
%add_to_maven_depmap org.slf4j %{oldname}-jdk14 %{version} JPP/%{name} jdk14
%add_to_maven_depmap org.slf4j %{oldname}-log4j12 %{version} JPP/%{name} log4j12
%add_to_maven_depmap org.slf4j %{oldname}-migrator %{version} JPP/%{name} migrator
%add_to_maven_depmap org.slf4j %{oldname}-nop %{version} JPP/%{name} nop
%add_to_maven_depmap org.slf4j %{oldname}-simple %{version} JPP/%{name} simple

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-parent.pom
install -pm 644 jcl104-over-slf4j/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jcl104-over-slf4j.pom
install -pm 644 jcl-over-slf4j/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jcl-over-slf4j.pom
install -pm 644 jul-to-slf4j/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jul-to-slf4j.pom
install -pm 644 log4j-over-slf4j/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-log4j-over-slf4j.pom
install -pm 644 slf4j-api/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-api.pom
install -pm 644 slf4j-ext/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ext.pom
install -pm 644 slf4j-jcl/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jcl.pom
install -pm 644 slf4j-jdk14/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-jdk14.pom
install -pm 644 slf4j-log4j12/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-log4j12.pom
install -pm 644 slf4j-migrator/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-migrator.pom
install -pm 644 slf4j-nop/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-nop.pom
install -pm 644 slf4j-simple/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-simple.pom

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/api*/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf target/site/api*

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
install -m 644 LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%if %with repolib
%{__install} -d -m 755 %{buildroot}%{repodir}
%{__install} -d -m 755 %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{oldname}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 755 %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH1} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}/api-%{version}.jar %{buildroot}%{repodirlib}/slf4j-api.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/*-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}/site
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt3_1jpp6
- fixed build with java 7

* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt2_1jpp6
- fixed release

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_alt1_16jpp6
- compat version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_4jpp6
- new version (full build)

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp6
- new version (bootstrap)

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_1jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_2jpp1.7
- updated to new jpackage release

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp1.7
- added dependency on new excalibur

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

