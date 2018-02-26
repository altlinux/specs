BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

#def_with maven
%bcond_with maven
%bcond_without repolib

%define short_name      scout

%define real_version    0.7rc2

%define repodir %{_javadir}/repository.jboss.com/apache-scout/%{real_version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

Name:           ws-scout0
Version:        0.7
Release:        alt2_0.rc2.6jpp6
Epoch:          0
Summary:        Apache Scout Implementation of JSR 93 (JAXR)
License:        ASL 2.0
Group:          Development/Java
URL:            http://ws.apache.org/scout/
# svn export https://svn.apache.org/repos/asf/webservices/scout/tags/v0.7rc2/ ws-scout-0.7rc2 
# tar cjf ws-scout-0.7rc2.tar.bz2 ws-scout-0.7rc2
Source0:        ws-scout-%{real_version}.tar.bz2
Source2:        pom-maven2jpp-newdepmap.xsl
Source3:        pom-maven2jpp-mapdeps.xsl
Source4:        ws-scout-1.0-jpp-depmap.xml
Source6:        ws-scout-component-info.xml
Source8:        ws-scout0-build.xml
Source9:        ws-scout0-maven-build.xml
Source10:       ws-scout0-modules-scout-build.xml
Source11:       ws-scout0-modules-scout-maven-build.xml
Source12:       ws-scout0-0.7rc2.pom
Patch0:         ws-scout-1.0-jaxr-api-project_xml.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
%if %with maven
Requires:       axis >= 0:1.2
Requires:       jakarta-commons-discovery
Requires:       jakarta-commons-logging
Requires:       jdom
%endif
Requires:       jaf
Requires:       juddi
BuildRequires:  jpackage-utils
BuildRequires:  junit
%if %with maven
BuildRequires:  maven1 >= 1.0.2
BuildRequires:  maven1-plugins-base >= 1.0.2
BuildRequires:  maven1-plugin-multiproject >= 1.0.2
BuildRequires:  maven1-plugin-license >= 1.0.2
BuildRequires:  maven1-plugin-test >= 1.0.2
BuildRequires:  maven1-plugin-xdoc >= 1.0.2
BuildRequires:  axis >= 0:1.2
BuildRequires:  jakarta-commons-discovery
BuildRequires:  jakarta-commons-logging
BuildRequires:  jdom
BuildRequires:  saxon-scripts
%else
BuildRequires:  ant
%endif
BuildRequires:  jaf
BuildRequires:  juddi
BuildRequires:  ws-scout
BuildArch:      noarch
Source44: import.info

%description
Apache Scout is an implementation of the 
JSR 93 (JAXR). 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

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
%setup -q -n ws-scout-%{real_version}

# Already clean
#find . -name "*.jar" | xargs -t rm

cp -a %{SOURCE8} build.xml
cp -a %{SOURCE9} maven-build.xml
cp -a %{SOURCE10} modules/scout/build.xml
cp -a %{SOURCE11} modules/scout/maven-build.xml

# These tests need a running juddi server instance
rm modules/scout/src/test/org/apache/ws/scout/registry/publish/PublishConceptTest.java
rm modules/scout/src/test/org/apache/ws/scout/registry/query/JAXRQueryTest.java

# for checkstyle
cp -p LICENSE.TXT modules/jaxr-api/LICENSE.txt

# Remove log4j.properties file. It is not needed by scout directly, and may 
# cause conflicts/problems with other applications.
rm -f modules/scout/src/conf/log4j.properties

%patch0 -p0

perl -pi -e 's/\r$//g' LICENSE.TXT

%build
%if %with maven
export DEPCAT=$(pwd)/ws-scout-1.0-depcat.new.xml
/bin/echo '<?xml version="1.0" standalone="yes"?>' > $DEPCAT
/bin/echo '<depset>' >> $DEPCAT
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    %{_bindir}/saxon project.xml %{SOURCE1} >> $DEPCAT
    popd
done
/bin/echo >> $DEPCAT
/bin/echo '</depset>' >> $DEPCAT
%{_bindir}/saxon $DEPCAT %{SOURCE2} > ws-scout-1.0-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname $p)
    cp project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done
for p in $(find . -name project.properties); do
    /bin/echo >> $p
    /bin/echo maven.repo.remote=file:/usr/share/maven1/repository >> $p
    /bin/echo maven.home.local=$(pwd)/.maven >> $p
done

export MAVEN_HOME_LOCAL=$(pwd)/.maven
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository
pushd modules/jaxr-api
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository javadoc:generate
popd
pushd modules/scout
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -Dmaven.repo.remote=file:/usr/share/maven1/repository javadoc:generate
popd
%else
export CLASSPATH=$(build-classpath jaf juddi junit ws-scout/jaxr-api log4j)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dmaven.mode.offline=true package javadoc
%endif

%install

%{__mkdir_p} %{buildroot}%{_javadir}/%{name}
%if %with maven
%{__cp} -p modules/jaxr-api/target/jaxr-api-1.0-SNAPSHOT.jar \
                %{buildroot}%{_javadir}/%{name}/jaxr-api-%{version}.jar
%{__cp} -p modules/scout/target/scout-1.0-SNAPSHOT.jar \
                %{buildroot}%{_javadir}/%{name}/%{name}-%{version}.jar
%else
%{__cp} -p modules/scout/target/scout-%{real_version}.jar \
                %{buildroot}%{_javadir}/%{name}/%{name}-%{version}.jar
%endif
# create unprefixed and unversioned symlinks
(cd %{buildroot}%{_javadir}/%{name}
%{__ln_s} %{name}-%{version}.jar %{short_name}-%{version}.jar
for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done
)

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%if %with maven
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxr-api
%{__cp} -pr modules/jaxr-api/target/docs/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/jaxr-api
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}/scout
%{__cp} -pr modules/scout/target/docs/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/scout
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%else
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}/scout
%{__cp} -pr modules/scout/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/scout
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%endif

# poms
%add_to_maven_depmap scout scout %{version} JPP/%{name} %{name}
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE12} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE6} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{real_version}-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}/%{name}-%{version}.jar %{buildroot}%{repodirlib}/%{short_name}.jar
%endif

%files
%doc LICENSE.TXT
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/scout-%{version}.jar
%{_javadir}/%{name}/scout.jar
%{_javadir}/%{name}/%{name}-%{version}.jar
%{_javadir}/%{name}/%{name}.jar
%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt2_0.rc2.6jpp6
- fixed build with moved maven1

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_0.rc2.6jpp6
- new jpp relase

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_0.rc2.5jpp6
- new jpp release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_0.rc2.4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_0.rc2.1jpp5
- converted from JPackage by jppimport script

