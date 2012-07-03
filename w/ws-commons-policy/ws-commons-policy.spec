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

#def_with maven
%bcond_with maven
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/wscommons-policy/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define short_name policy

Name:           ws-commons-policy
Version:        1.0
Release:        alt4_10jpp6
Epoch:          0
Summary:        Web Services Commons - WS-Policy implementation
License:        ASL 2.0
Url:            http://ws.apache.org/commons/policy/
Group:          Development/Java
# svn export -r '{2006-01-19}' https://svn.apache.org/repos/asf/webservices/commons/trunk/policy ws-commons-policy
Source0:        http://www.mirrorservice.org/sites/ftp.apache.org/ws/commons/policy/1_0/policy-1.0-src.zip
Source1:        %{name}-pom-maven2jpp-depcat.xsl
Source2:        %{name}-pom-maven2jpp-newdepmap.xsl
Source3:        %{name}-pom-maven2jpp-mapdeps.xsl
Source4:        %{name}-jpp-depmap.xml
Source5:        ws-commons-policy-component-info.xml
Source6:        ws-commons-policy-MANIFEST.MF
Source7:        ws-commons-policy.pom
Patch0:         %{name}-properties.patch
Patch1:         %{name}-om.patch
# FIXME: (dwalluck): Package has an incorrect and unversioned Provides on ws-common-policy
Obsoletes:      neethi <= 1.0.1-1jpp
Obsoletes:      ws-commons-neethi <= 2.0.1-2jpp
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jakarta-commons-logging >= 0:1.0.4
Requires: stax_1_0_api
Requires: wsdl4j >= 0:1.5.1
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: junit
%if %with maven
BuildRequires: maven >= 0:1.0.2
BuildRequires: maven-plugins-base >= 0:1.0.2
BuildRequires: maven-plugin-license >= 0:1.0.2
BuildRequires: maven-plugin-test >= 0:1.0.2
%endif
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: saxon-scripts
BuildRequires: stax_1_0_api
BuildRequires: wsdl4j >= 0:1.5.1
BuildRequires: ws-commons-axiom
BuildArch:      noarch
Source44: import.info

%description
WS-Policy implementation, part of Web Services Commons.

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
%setup -q -n policy-%{version}-src
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1

%{__sed} -i -e 's#<name>WS-Policy Implementation</name>##' project.xml

# FIXME: (dwalluck): This class requires axis2
%{__mv} src/org/apache/ws/policy/util/OMPolicyReader.java{,.bak}

%if %with maven
%{__mkdir_p} $(pwd)/.maven/repository/JPP/jars

export DEPCAT=$(pwd)/%{name}-depcat.new.xml
/bin/echo '<?xml version="1.0" standalone="yes"?>' > ${DEPCAT}
/bin/echo '<depset>' >> ${DEPCAT}
for p in $(%{_bindir}/find -name project.xml); do
    pushd $(dirname ${p})
    %{_bindir}/saxon project.xml %{SOURCE1} >> ${DEPCAT}
    popd
done
/bin/echo >> ${DEPCAT}
/bin/echo '</depset>' >> ${DEPCAT}
%{_bindir}/saxon ${DEPCAT} %{SOURCE2} > %{name}-depmap.new.xml
for p in $(find . -name project.xml); do
    pushd $(dirname ${p})
    %{__cp} -p project.xml project.xml.orig
    %{_bindir}/saxon -o project.xml project.xml.orig %{SOURCE3} map=%{SOURCE4}
    popd
done
for p in $(find . -name project.properties); do
    /bin/echo >> ${p}
    /bin/echo maven.repo.remote=file:/usr/share/maven/repository >> ${p}
    /bin/echo maven.home.local=$(pwd)/.maven >> ${p}
done
%endif

%build
%if %with maven
export MAVEN_HOME_LOCAL=$(pwd)/.maven
# FIXME: The test compilation is not finding JUnit,
# although it is found fine in JPackage.
maven -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dmaven.test.skip=true -X \
        -Dmaven.repo.remote=file://%{_datadir}/maven/repository \
                jar:jar

# FIXME: (dwalluck) javadocs are missing
%else
export CLASSPATH=$(%{_bindir}/build-classpath commons-logging stax_1_0_api)
pushd src
%{javac}  -target 1.5 -source 1.5 `find . -name '*.java'`
%{__mkdir_p} ../target
%{jar} cfm ../target/policy-1.0.jar %{SOURCE6} `%{_bindir}/find -name '*.class'`
popd
%endif

%install

# jar
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p target/policy-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && %{__ln_s} %{name}-%{version}.jar %{name}.jar)

# poms
%{__mkdir_p} %{buildroot}/%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE7} %{buildroot}/%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap ws-commons-policy ws-commons-policy %{version} JPP %{name}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE5} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH1} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/ws-commons-policy.jar %{buildroot}%{repodirlib}/policy.jar
%endif

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_10jpp6
- fixed build with moved maven1

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_10jpp6
- target 5 build

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_10jpp6
- new jpp release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_7jpp5
- rebuild with default profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_7jpp5
- converted from JPackage by jppimport script

* Sat Jan 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to sutisfy circular dependencies

