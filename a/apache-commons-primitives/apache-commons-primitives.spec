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

%define base_name primitives
%define short_name commons-%{base_name}

%define namedversion 1.1-SNAPSHOT

Name:           apache-commons-primitives
Version:        1.1
Release:        alt1_0.r832341.2jpp6
Epoch:          0
Summary:        Apache Commons Primitives Component

License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://commons.apache.org/primitives/
Source0:        commons-primitives-1.1-src.tar.gz
# svn export -r 832341 http://svn.apache.org/repos/asf/commons/proper/primitives/trunk commons-primitives-1.1-src
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
#Patch0:         %{name}-crosslink.patch

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: junit
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
BuildRequires: apache-commons-parent
BuildRequires: apache-commons-collections-testframework

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: apache-commons-parent >= 0:12

Provides:       %{short_name}11 = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}11 < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}11 = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}11 < %{epoch}:%{version}-%{release}
Source44: import.info

%description
Apache Jakarta Commons Primitives provides a collection of types and
utilities optimized for working with Java primitives (boolean, byte,
char, double, float, int, long, short). Generally, the
Commons-Primitives classes are smaller, faster and easier to work with
than their purely Object based alternatives.

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

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       %{short_name}11-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}11-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       jakarta-%{short_name}11-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}11-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
#%patch0 -p0
%{__perl} -pi \
    -e 's/\r$//g;' \
  PROPOSAL.html LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

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

%else
# No unit tests yet, would require commons-collections snapshot.
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dfinal.name=%{name}-%{version} \
  -Dj2se.apidoc=%{_javadocdir}/java \
  jar javadoc
%endif

%install
install -Dm 644 target/commons-primitives-%{version}-SNAPSHOT.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jakarta-%{short_name}.jar

install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

# poms
install -d -m 755  $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap commons-primitives commons-primitives %{namedversion} JPP %{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml

%{__sed} -i 's/project name=""/project name="%{name}"/g' %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
#%{__install} -m 0644 %{PATCH0} %{buildroot}%{repodirsrc}/
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/apache-commons-lang-%{version}.jar.db
%{_libdir}/gcj/%{name}/apache-commons-lang-%{version}.jar.so
%endif

%files javadoc
%doc %{_javadocdir}/*

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r832341.2jpp6
- new version

