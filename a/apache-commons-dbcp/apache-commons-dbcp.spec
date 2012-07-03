BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define base_name       dbcp
%define short_name      commons-%{base_name}

Name:           apache-commons-dbcp
Version:        1.3.0
Release:        alt2_0.r830852.4jpp6
Epoch:          0
Summary:        Apache Commons DataBase Pooling Package
License:        Apache Software License 
Group:          Development/Java
Url:            http://commons.apache.org/dbcp
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# svn export -r 830852 http://svn.apache.org/repos/asf/commons/proper/dbcp/trunk commons-dbcp-1.3.0-src
Source1:        %{name}-settings.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-component-info.xml
Source6:        dbcp-tomcat5-build.xml
Patch0:         apache-commons-dbcp-pom.patch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7
BuildRequires: apache-commons-pool
BuildRequires: jakarta-commons-logging
BuildRequires: junit >= 3.8.1
BuildRequires: geronimo-genesis
BuildRequires: geronimo-j2ee-connector-1.5-api
BuildRequires: geronimo-txmanager
BuildRequires: howl-logger
BuildRequires: apache-commons-pool-tomcat5
BuildRequires: apache-commons-collections-tomcat5
BuildRequires: tomcat5-common-lib
BuildRequires: jta_1_1_api
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
Requires(post): alternatives >= 0:0.4
Requires(preun): alternatives >= 0:0.4
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0
Requires: apache-commons-collections
Requires: apache-commons-pool
%if ! %{gcj_support}
BuildArch:      noarch
%endif
Provides:   hibernate_jdbc_cache = %{epoch}:%{version}-%{release}
Provides:   jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:  jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Provides:   %{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:  %{short_name} < %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info
Obsoletes: jakarta-%{short_name} < 1:%{version}-%{release}
Conflicts: jakarta-%{short_name} < 1:%{version}-%{release}

%description
Many Jakarta projects support interaction with a relational 
database. Creating a new connection for each user can be time 
consuming (often requiring multiple seconds of clock time), 
in order to perform a database transaction that might take 
milliseconds. Opening a connection per user can be unfeasible 
in a publicly-hosted Internet application where the number of 
simultaneous users can be very large. Accordingly, developers 
often wish to share a "pool" of open connections between all 
of the application's current users. The number of users actually 
performing a request at any given time is usually a very small 
percentage of the total number of active users, and during 
request processing is the only time that a database connection 
is required. The application itself logs into the DBMS, and 
handles any user account issues internally.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java
Provides:   jakarta-%{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:  jakarta-%{short_name}-repolib < %{epoch}:%{version}-%{release}
Provides:   %{short_name}-repolib = %{epoch}:%{version}-%{release}
Obsoletes:  %{short_name}-repolib < %{epoch}:%{version}-%{release}

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:   jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:  jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
Provides:   %{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:  %{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package tomcat5
Summary:        DBCP dependency for Tomcat5
Group:          Development/Java
Provides:   jakarta-%{short_name}-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:  jakarta-%{short_name}-tomcat5 < %{epoch}:%{version}-%{release}
Provides:   %{short_name}-tomcat5 = %{epoch}:%{version}-%{release}
Obsoletes:  %{short_name}-tomcat5 < %{epoch}:%{version}-%{release}

%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description tomcat5
DBCP dependency for Tomcat5

%if %with maven
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
Provides:   jakarta-%{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:  jakarta-%{short_name}-manual < %{epoch}:%{version}-%{release}
Provides:   %{short_name}-manual = %{epoch}:%{version}-%{release}
Obsoletes:  %{short_name}-manual < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description manual
%{summary}.
%endif

%prep
%setup -q -n %{short_name}-%{version}-src
%{__sed} -i 's/\r//' LICENSE.txt
%{__sed} -i 's/\r//' NOTICE.txt
%{__sed} -i 's/\r//' README.txt
cp %{SOURCE6} .
%{__perl} -pi \
    -e 's/\r$//g;' \
  PROPOSAL.html LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%patch0 -b .sav0
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
export CLASSPATH=$(build-classpath jta_1_1_api jdbc-stdext xerces-j2)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
        -Dbuild.sysclasspath=first \
        -Dbackport-util-concurrent.jar=$(build-classpath backport-util-concurrent) \
        -Dcommons-collections.jar=$(build-classpath commons-collections) \
        -Dcommons-logging.jar=$(build-classpath commons-logging) \
        -Dcommons-pool.jar=$(build-classpath commons-pool) \
        -Dejb-spec.jar=$(build-classpath ejb_3_0_api) \
        -Djunit.jar=$(build-classpath junit) \
        -Djta-impl.jar=$(build-classpath geronimo-transaction) \
        -Djta-spec.jar=$(build-classpath jta_1_1_api) \
        -Dnaming-common.jar=$(build-classpath tomcat5/naming-resources) \
        -Dnaming-java.jar=$(build-classpath tomcat5/naming-factory) \
        -Dxerces.jar=$(build-classpath xerces-j2) \
        -Dxml-apis.jar=$(build-classpath xml-commons-apis) \
        -Djava.io.tmpdir=. \
        dist
# test
%endif

export CLASSPATH=$(build-classpath jta_1_1_api jdbc-stdext xerces-j2 commons-collections-tomcat5 commons-pool-tomcat5)        
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5     -f dbcp-tomcat5-build.xml

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
%if %with maven
install -m 644 target/%{short_name}-%{version}-SNAPSHOT.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%else
install -m 644 dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%endif
#tomcat5 jars 
install -m 644 dbcp-tomcat5/%{short_name}-tomcat5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tomcat5-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|apache-|jakarta-|g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in apache-*-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%if %with maven
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf target/site/apidocs
%else
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{short_name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/jakarta-%{short_name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt NOTICE.txt README.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%if %with maven
# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/site $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%endif

# hibernate_jdbc_cache ghost symlink
touch $RPM_BUILD_ROOT%{_javadir}/hibernate_jdbc_cache.jar

# Install pom file
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -p pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-apache-commons-dbcp.pom
%add_to_maven_depmap commons-dbcp commons-dbcp %{version} JPP apache-commons-dbcp

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}%{repodirsrc}/
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}%{repodirsrc}/
%{__install} -p -m 0644 %{SOURCE2} %{buildroot}%{repodirsrc}/
%{__install} -p -m 0644 %{SOURCE3} %{buildroot}%{repodirsrc}/
%{__cp} -p %{buildroot}%{_javadir}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/hibernate_jdbc_cache_apache-commons-dbcp<<EOF
%{_javadir}/hibernate_jdbc_cache.jar	%{_javadir}/%{name}.jar	60
EOF

%files
%_altdir/hibernate_jdbc_cache_apache-commons-dbcp
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{short_name}.jar
%{_javadir}/%{short_name}-%{version}.jar
%{_javadir}/jakarta-%{short_name}.jar
%{_javadir}/jakarta-%{short_name}-%{version}.jar
%exclude %{_javadir}/hibernate_jdbc_cache.jar
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/*.txt
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files tomcat5
%{_javadir}/*-tomcat5*.jar
%doc LICENSE.txt NOTICE.txt

%if %{gcj_support}
%{_libdir}/gcj/%{name}/*-tomcat5*
%endif

%files javadoc
%doc %{_javadocdir}/*

%if %with maven
%files manual
%doc %{_docdir}/%{name}-%{version}/site
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_0.r830852.4jpp6
- build w/java6

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_0.r830852.4jpp6
- new version

