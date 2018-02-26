BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define version 0.9
%define name juddi
# Copyright (c) 2000-2011, JPackage Project
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

%bcond_without jboss
%bcond_without repolib

%define version_full %{version}RC4

%define repodir %{_javadir}/repository.jboss.com/juddi/%{version_full}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


# To make the tarball:
#  export CVSROOT=:pserver:anoncvs@cvs.apache.org:/home/cvspublic
#  cvs login (password: anoncvs)
#  cvs export -r juddi-0_9rc4 ws-juddi
#  find ws-juddi -name '*.jar' | xargs rm

%define basedir %{_var}/lib/%{name}
%define appdir %{basedir}/webapps
%define sqldir %{basedir}/sql
%define apphomedir %{_datadir}/%{name}

Name:           juddi
Version:        0.9
Release:        alt2_0.rc4.8jpp6
Epoch:          0
Summary:        Open source Java implementation UDDI specification
License:        ASL 2.0
Group:          Development/Java
URL:            http://ws.apache.org/juddi/
Source0:        juddi-0.9rc4.tar.bz2
Source1:        http://repository.jboss.com/maven2/juddi/juddi/0.9RC4/juddi-0.9RC4.pom
Source2:        juddi-component-info.xml
Patch0:         juddi-jdk5-enum.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jakarta-commons-logging
Requires:       jpackage-utils
Requires:       servlet_2_5_api
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  axis
BuildRequires:  jakarta-commons-logging
%if %with jboss
BuildRequires:  jboss-security-spi
%endif
BuildRequires:  jpackage-utils
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  servlet_2_5_api
BuildArch:      noarch
Source44: import.info

%description
jUDDI (pronounced "Judy") is an open source Java implementation 
of the Universal Description, Discovery, and Integration (UDDI) 
specification for Web Services.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if 0
%package webapp
Summary:        Webapp for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-discovery
Requires:       log4j
Requires:       wsdl4j

%description webapp
Webapp for %{name}.
%endif

%package sql-init-statements
Group:          Development/Java
Summary:        SQL statements for database creation/configuration
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description sql-init-statements
SQL statements for creation/configuration of a database 
for storing web services metadata for %{name}.

%package apps
Group:          Development/Java
Summary:        EAR file for jUDDI
#Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:       axis
Requires:       jakarta-commons-logging
Requires:       tomcat5-servlet-2.4-api

%description apps
The Enterprise Archive (ear) file for %{name}.

%package webapps
Group:          Development/Java
Summary:        WAR file for jUDDI
#Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:       axis
Requires:       jakarta-commons-logging
Requires:       tomcat5-servlet-2.4-api

%description webapps
The Web Archive (war) file for %{name}.

%prep
%setup -q -n ws-juddi
%patch0 -p1 -b .sav0
%{_bindir}/build-jar-repository -p -s lib \
    axis/axis \
    axis/jaxrpc \
    axis/saaj \
    jakarta-commons-logging \
%if %with jboss
    jboss-security-spi/jboss-security-spi-bare \
%endif
    log4j \
    servlet_2_5_api

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 ear javadoc test

%install

# *ars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
cp -p build/juddi.ear $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi-%{version}.ear
ln -s juddi-%{version}.ear $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi.ear

cp -p build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi-%{version}.jar
ln -s juddi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi.jar

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-juddi.pom
%add_to_maven_depmap juddi juddi %{version_full} JPP/%{name} juddi

cp -p build/juddi.war $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi-%{version}.war
ln -s juddi-%{version}.war $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi.war

install -d -m 755 $RPM_BUILD_ROOT%{appdir}
install -d -m 755 $RPM_BUILD_ROOT%{sqldir}

%if 0
# webapps
cp -pr build/webapp/* $RPM_BUILD_ROOT%{appdir}
%endif

# sql
cp -pr sql/* $RPM_BUILD_ROOT%{sqldir}

# /usr/share/juddi
install -d -m 755 $RPM_BUILD_ROOT/%{apphomedir}
pushd $RPM_BUILD_ROOT%{apphomedir}
        [ -d webapps ] || ln -fs %{appdir} webapps
        [ -d sql ] || ln -fs %{sqldir} sql
popd

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/apiDocs/ $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version_full}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi.jar $RPM_BUILD_ROOT%{repodirlib}/juddi.jar
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}/juddi.war $RPM_BUILD_ROOT%{repodirlib}/juddi.war
cp -p %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-juddi.pom $RPM_BUILD_ROOT%{repodirlib}/juddi.pom
%endif

%if 0
%post webapp
pushd %{appdir}/%{name}/WEB-INF >& /dev/null
        %{_bindir}/build-jar-repository lib \
                axis/axis.jar \
                jakarta-commons-discovery.jar \
                jakarta-commons-logging.jar \
                log4j.jar \
                wsdl4j.jar
popd >& /dev/null

%preun webapp
rm -f %{appdir}/%{name}/WEB-INF/lib/*.jar
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/juddi-%{version}.jar
%{_javadir}/%{name}/juddi.jar
%{_datadir}/maven2/poms/JPP.%{name}-juddi.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if 0
%files webapp
%{appdir}
%dir %{apphomedir}/webapps
%dir %{apphomedir}
%dir %{basedir}
%endif

%files sql-init-statements
%{sqldir}
%dir %{apphomedir}/sql
%dir %{apphomedir}
%dir %{basedir}

%files apps
%{_javadir}/%{name}/juddi-%{version}.ear
%{_javadir}/%{name}/juddi.ear

%files webapps
%dir %{apphomedir}/webapps
%{_javadir}/%{name}/juddi-%{version}.war
%{_javadir}/%{name}/juddi.war
%exclude /usr/share/juddi/webapps

%if %with repolib
%files repolib
%dir %{_javadir}
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_0.rc4.8jpp6
- new jpp relase

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_0.rc4.7jpp6
- added pom

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_0.rc4.4jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_0.rc4.3jpp5
- converted from JPackage by jppimport script

* Sat Feb 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt2_0.rc4.2jpp1.7
- packaged /var/lib/juddi/webapps (thanks to Alexey Torbin)

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt1_0.rc4.2jpp1.7
- converted from JPackage by jppimport script

