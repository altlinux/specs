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

# XXX: don't use maven, as the produced jar doesn't include all files
#def_with maven
%bcond_with maven

%define reltag GA
%define namedversion %{version}.%{reltag}

Name:           jboss-tattletale
Version:        1.0.1
Release:	alt1_2jpp6
Epoch:          0
Summary:        Jar dependency report library
License:        LGPLv2+
Group:          Development/Java
URL:            http://www.jboss.org/
# svn -q export http://anonsvn.jboss.org/repos/tattletale/tags/1_0_1_GA/ jboss-tattletale-1.0.1 && tar cjf jboss-tattletale-1.0.1.tar.bz2 jboss-tattletale-1.0.1
Source0:        jboss-tattletale-1.0.1.tar.bz2
Source1:        jboss-tattletale-jpp-depmap.xml
Source2:        jboss-tattletale-settings.xml
Source3:        jboss-tattletale-script
Source4:        jboss-tattletale-1.0.1.pom
Patch0:         jboss-tattletale-1.0.1-pom-version.patch
Patch1:         jboss-tattletale-1.0.1-fop.patch
Patch2:         jboss-tattletale-1.0.1-no-classpath-in-manifest.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: ant
Requires: javassist
BuildRequires: jpackage-utils >= 0:1.7.3
%if %with maven
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-release
BuildRequires: maven-surefire-maven-plugin
BuildRequires: jboss-parent >= 0:4
BuildRequires: jboss-test >= 0:1.1.0
BuildRequires: junit44 >= 0:4.4
%endif
BuildRequires: ant >= 0:1.7.0
# XXX: for xmlgraphics-fop
BuildRequires: excalibur-avalon-framework
# XXX: pom.xml wants 3.10.0
BuildRequires: javassist >= 0:3.9.0
BuildRequires: saxon
BuildRequires: xmlgraphics-fop
BuildArch:      noarch
Source44: import.info

%description
JBoss Tattletale is a tool that can help you get an overview of the project you
are working on or a product that you depend on.

The tool will provide you with reports that can help you

    * Identify dependencies between JAR files
    * Find missing classes from the classpath
    * Spot if a class is located in multiple JAR files
    * Spot if the same JAR file is located in multiple locations
    * With a list of what each JAR file requires and provides
    * Verify the SerialVersionUID of a class
    * Find similar JAR files that have different version numbers
    * Find JAR files without a version number
    * Locate a class in a JAR file
    * Get the OSGi status of your project
    * Remove black listed API usage

JBoss Tattletale will recursive scan the directory pass as the argument for JAR
files and then build the reports as HTML files.

The main HTML file is: index.html

JBoss Tattletale is licensed under GNU Lesser General Public License (LGPL)
version 2.1 or later.

We hope that JBoss Tattletale will help you in your development tasks !

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%{__cp} -p %{SOURCE4} pom.xml
%{__perl} -pi -e 's/\r$//g' doc/JBossORG-EULA.txt
%patch0 -p0
%patch1 -p0
%patch2 -p0

%{__ln_s} $(build-classpath ant) lib/ant.jar
%{__ln_s} $(build-classpath javassist) lib/javassist.jar
%{__ln_s} $(build-classpath excalibur/avalon-framework) tools/docbook/support/lib/avalon-framework-cvs-20020806.jar
%{__ln_s} $(build-classpath saxon) tools/docbook/support/lib/saxon.jar
%{__ln_s} $(build-classpath xmlgraphics-batik-all) tools/docbook/support/lib/batik.jar
%{__ln_s} $(build-classpath xmlgraphics-fop) tools/docbook/support/lib/fop.jar

%if %with maven
%{__cp} -p %{SOURCE2} maven2-settings.xml

%{__sed} -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
%{__sed} -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

%{__mkdir_p} external_repo
%{__ln_s} %{_javadir} external_repo/JPP
%endif

for i in xmlgraphics-commons commons-io commons-logging xml-commons-jaxp-1.3-apis excalibur/avalon-framework-api excalibur/avalon-framework-impl xerces-j2 xalan-j2 xalan-j2-serializer ; do
%{__ln_s} $(build-classpath $i) tools/docbook/support/lib/`basename $i`.jar
done

%build
%if %with maven
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=$(pwd)/m2_repo/repository
%{_bindir}/mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=${MAVEN_REPO_LOCAL} \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        install javadoc:javadoc
%else
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} dist doc
%endif

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%if %with maven
%{__cp} -p target/jboss-tattletale.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%else
%{__cp} -p dist/jboss-tattletale.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%endif
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.jboss jboss-tattletale %{namedversion} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %with maven
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%else
%{__cp} -pr doc/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%endif
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# scripts
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files
%doc dist/copyright.txt dist/JBossORG-EULA.txt dist/lgpl.html dist/README.txt
%if %without maven
%doc build/en/pdf/JBossTattletale-DevelopersGuide.pdf build/en/pdf/JBossTattletale-UsersGuide.pdf
%endif
%attr(0755,root,root) %{_bindir}/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace,missingok) /etc/%{name}.conf

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_2jpp6
- new version

