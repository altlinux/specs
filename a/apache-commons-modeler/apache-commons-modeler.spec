BuildRequires: /proc
BuildRequires: jpackage-compat
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

%bcond_without maven
#def_with gcj_support
%bcond_with gcj_support
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-%{base_name}/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirres %{repodir}/resources
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define base_name modeler
%define short_name commons-%{base_name}

Name:           apache-commons-modeler
Epoch:          0
Version:        2.1
Release:        alt2_0.r832084.4jpp6
Summary:        Apache Commons Modeler
Group:          Development/Java
License:        ASL 2.0
Url:            http://commons.apache.org/modeler/
Source0:        %{short_name}-%{version}-src.tar.gz
# svn export -r 832084 http://svn.apache.org/repos/asf/commons/proper/modeler/trunk commons-modeler-2.1-src
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml


%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
%if %with maven
BuildRequires: apache-commons-parent >= 0:12
BuildRequires: maven2 >= 0:2.0.8
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-idea
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-resources
%endif
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-collections
BuildRequires: apache-commons-digester
BuildRequires: jakarta-commons-logging
BuildRequires: junit
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: apache-commons-beanutils
Requires: apache-commons-collections
Requires: apache-commons-digester
Requires: jakarta-commons-logging
%if ! %{gcj_support}
BuildArch: noarch
%endif
Provides: %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes: %{short_name} < %{epoch}:%{version}-%{release}
Provides: jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes: jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info

%description
The Modeler project shall create and maintain a set of Java
classes to provide the facilities described in the preceeding section, plus
unit tests and small examples of using these facilities to instrument
Java classes with Model MBean support.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:       jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Provides: %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes: %{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides: jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes: jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
# remove all binary files
find . \( -name "*.jar" -o -name "*.class" -o -name "*.zip" \) \
    | xargs %{__rm} -f
# fix eol encodings
%{__sed} -i 's/\r//' xdocs/downloads.xml
%{__sed} -i 's/\r//' xdocs/cvs-usage.xml
%{__sed} -i 's/\r//' xdocs/issue-tracking.xml
%{__sed} -i 's/\r//' LICENSE.txt
%{__sed} -i 's/\r//' xdocs/navigation.xml
%{__sed} -i 's/\r//' xdocs/style/project.css
%{__sed} -i 's/\r//' xdocs/index.xml
%{__sed} -i 's/\r//' xdocs/building.xml
%{__sed} -i 's/\r//' NOTICE.txt
%{__sed} -i 's/\r//' RELEASE-NOTES.txt
%if %with maven
cp -p %{SOURCE1} settings.xml
sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/.m2/repository</url>|g" settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" settings.xml

mkdir external_repo
ln -s %{_javadir} external_repo/JPP
%endif

%build
%if %with maven
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p ${MAVEN_REPO_LOCAL}
export MAVEN_OPTS="-Dmaven2.jpp.mode=true -Dmaven2.jpp.depmap.file=%{SOURCE2} -Dmaven.repo.local=${MAVEN_REPO_LOCAL}"
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc
%else

export CLASSPATH=$(build-classpath xml-commons-apis jaxp_parser_impl jaxp_transform_impl jmxri junit commons-beanutils commons-collections commons-digester commons-logging)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 dist

%endif

%install

# jars
%{__install} -d -m 755 %{buildroot}%{_javadir}

%if %with maven
%{__install} -m 644 target/%{short_name}-%{version}-SNAPSHOT.jar \
    %{buildroot}%{_javadir}/%{name}-%{version}.jar
%else
%{__install} -m 644 dist/%{short_name}.jar \
    %{buildroot}%{_javadir}/%{name}-%{version}.jar
%endif
(
    cd %{buildroot}%{_javadir}
    for jar in *-%{version}*; do
        %{__ln_s} ${jar} `echo $jar | %{__sed} "s|apache-|jakarta-|g"`
    done
)
(
    cd %{buildroot}%{_javadir}
    for jar in *-%{version}*; do
        %{__ln_s} ${jar} `echo $jar | %{__sed} "s|apache-||g"`
    done
)
(
    cd %{buildroot}%{_javadir}
    for jar in *-%{version}*; do
        %{__ln_s} ${jar} `echo $jar | %__sed "s|-%{version}||g"`
    done
)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap commons-modeler commons-modeler %{version} JPP %{name}

# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %with maven
%{__cp} -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%else
%{__cp} -a dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%endif
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{short_name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{short_name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jakarta-%{short_name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/jakarta-%{short_name}-%{version}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
#%{__install} -p -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
    %{_bindir}/aot-compile-rpm
%endif

%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]; then
    %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt xdocs
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/*

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_0.r832084.4jpp6
- set target 5

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_0.r832084.4jpp6
- new version

