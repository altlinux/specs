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

%define base_name el
%define short_name commons-%{base_name}

Name:           apache-commons-el
Version:        1.0.1
Release:        alt5_0.r936225.4jpp6
Epoch:          0
Summary:        Apache Commons Extension Language
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/el/
Source0:        commons-el-%{version}-src.tar.gz
# svn export -r 831152 http://svn.apache.org/repos/asf/commons/proper/el/trunk commons-el-1.0.1-src
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: apache-commons-logging
BuildRequires: jsp_2_0_api
BuildRequires: servlet_2_4_api
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
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires: apache-commons-logging
Requires: jsp_2_0_api
Requires: servlet_2_4_api
Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:       %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name} < %{epoch}:%{version}-%{release}
Source44: _fEl9UplJH
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}

%description
An implementation of standard interfaces and abstract classes for
javax.servlet.jsp.el which is part of the JSP 2.0 specification.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
#BuildRequires:  java-javadoc
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:       %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

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

%prep
%setup -q -n %{short_name}-%{version}-src
cat > build.properties <<EOBP
build.compiler=modern
junit.jar=$(build-classpath junit)
servlet-api.jar=$(build-classpath servlet_2_4_api)
jsp-api.jar=$(build-classpath jsp_2_0_api)
servletapi.build.notrequired=true
jspapi.build.notrequired=true
EOBP
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
%{_bindir}/mvn-jpp \
        -e \
        -s $(pwd)/settings.xml \
        install javadoc:javadoc
%else
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Dservlet-api.jar=$(build-classpath servlet_2_4_api) \
  -Djsp-api.jar=$(build-classpath jsp_2_0_api) \
  -Dcommons-logging.jar=$(build-classpath commons-logging) \
  -Djunit.jar=$(build-classpath junit) \
  jar javadoc

%endif

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
%if %with maven
install -m 644 target/%{short_name}-%{version}-SNAPSHOT.jar \
                 $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
cp -p dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap commons-el commons-el %{version} JPP %{name}
%add_to_maven_depmap org.apache.commons commons-el %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%else
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

%if %with repolib
%{__install} -d -m 0755 %{buildroot}%{repodir}
%{__install} -d -m 0755 %{buildroot}%{repodirlib}
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__install} -d -m 0755 %{buildroot}%{repodirsrc}
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/%{short_name}.pom
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt PROPOSAL.html
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/apache-commons-el-%{version}.jar.*
%endif
%exclude %_javadir/repository.jboss.com

%files javadoc
%{_javadocdir}/*

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Apr 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt5_0.r936225.4jpp6
- added OSGi manifest

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt4_0.r936225.4jpp6
- excluded repolib from main package

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_0.r936225.4jpp6
- add obsoletes

* Wed Dec 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_0.r936225.3jpp6
- really fixed broken symlink

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_0.r936225.3jpp6
- fixed broken symlink

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_0.r936225.3jpp6
- new version

