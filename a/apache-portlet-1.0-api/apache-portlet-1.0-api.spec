BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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

%define gcj_support 0

# If you don't want to build with maven, and use straight ant instead,
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

%define base_name portlet-1.0-api


Name:           apache-portlet-1.0-api
Version:        1.0
Release:        alt2_8jpp6
Epoch:          0
Summary:        Portlet API 1.0 from Jetspeed2
License:        ASL 2.0
Group:          Development/Java
URL:            http://portals.apache.org/jetspeed-2/
Source0:        apache-portlet-1.0-api.tar.gz
# svn export http://svn.apache.org/repos/asf/portals/jetspeed-2/tags/JETSPEED-RELEASE-2.0/portlet-api/
Source1:        apache-portlet-1.0-api-pom.xml
Source2:        apache-portlet-1.0-api-LICENSE.TXT
Source3:        apache-portlet-1.0-api-build.xml
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
%if %{with_maven}
BuildRequires:  maven2 >= 2.0.8
BuildRequires:  maven2-plugin-compiler
BuildRequires:  maven2-plugin-install
BuildRequires:  maven2-plugin-jar
BuildRequires:  maven2-plugin-javadoc
BuildRequires:  maven-release
BuildRequires:  maven2-plugin-resources
BuildRequires:  maven-surefire-plugin
%endif
Requires(post):  alternatives
Requires(preun): alternatives
Requires(post):  jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

Provides:       portlet-1.0-api = %{epoch}:%{version}
Provides:       portlet = %{epoch}:%{version}
Provides:       portlet_api = %{epoch}:%{version}
Provides:       portlet_1_0_api = %{epoch}:%{version}

%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif
Source44: import.info

%description
Java Standard Portlet API accoring to JSR-168, from Jetspeed-2 

%package javadoc
Summary:        Javadoc %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} LICENSE.TXT
cp -p %{SOURCE3} build.xml

%build
%if %{with_maven}
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -Dmaven.test.skip=true \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        install javadoc:javadoc
%else
export CLASSPATH
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc
%endif

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 0644 target/portlet-api-1.0.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}-%{version}.jar %{base_name}-%{version}.jar)
%add_to_maven_depmap javax.portlet portlet-api 1.0 JPP %{base_name}
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} $(echo $jar | sed -e 's+-%{version}\.jar+.jar+'); done)

#poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{base_name}.pom

touch $RPM_BUILD_ROOT%{_javadir}/portlet.jar
touch $RPM_BUILD_ROOT%{_javadir}/portlet_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/portlet_1_0_api.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/portlet_apache-portlet-1.0-api<<EOF
%{_javadir}/portlet.jar	%{_javadir}/portlet-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/portlet_api_apache-portlet-1.0-api<<EOF
%{_javadir}/portlet_api.jar	%{_javadir}/portlet-1.0-api.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/portlet_1_0_api_apache-portlet-1.0-api<<EOF
%{_javadir}/portlet_1_0_api.jar	%{_javadir}/portlet-1.0-api.jar	10000
EOF

%files
%_altdir/portlet_1_0_api_apache-portlet-1.0-api
%_altdir/portlet_api_apache-portlet-1.0-api
%_altdir/portlet_apache-portlet-1.0-api
%doc LICENSE.TXT
%{_javadir}/%{name}*.jar
%{_javadir}/%{base_name}*.jar
%exclude %{_javadir}/portlet.jar
%exclude %{_javadir}/portlet_api.jar
%exclude %{_javadir}/portlet_1_0_api.jar

%{_datadir}/maven2/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_8jpp6
- new jpp relase

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_7jpp5
- fixed repocop warnings

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp1.7
- build with maven2

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp1.7
- converted from JPackage by jppimport script

