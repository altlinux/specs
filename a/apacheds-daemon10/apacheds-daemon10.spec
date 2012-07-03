# quick fix instead of installing pom properly
BuildRequires: apacheds-daemon10-bootstrappers maven2
Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define oname apacheds-daemon

Summary:        Reusable Daemon Framework
Name:           apacheds-daemon10
Version:        1.0.2
Release:        alt4_2jpp5
Epoch:          0
Group:          Development/Java
License:        Apache 2.0 License
URL:            http://directory.apache.org/
Source0:        %{name}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/directory/daemon/tags/1.0.2/ apacheds-daemon-1.0.2

Source1:        directory-pom-1.0.4.xml
Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml

#Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:%{_vendor}}
#Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: maven2-plugins => 0:2.0.7
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin
BuildRequires: izpack
BuildRequires: jakarta-commons-daemon
BuildRequires: plexus-utils
BuildRequires: slf4j
BuildRequires: nlog4j
Requires: jakarta-commons-daemon
Requires: plexus-utils
Requires: slf4j
Requires: nlog4j

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%description
Reusable framework for daemon applications based on Commons
Daemon Jsvc and Procrun. A small installation layout pattern
combined with some utility classes allows applications to 
become UNIX daemons or Windows NT services.  Reusable
bootstrappers along with an installer plugin allow for the
rapid creation of standalone daemon applications.

%package bootstrappers
Group:          Development/Java
Summary:        Apache DS Daemon bootstrappers
Requires: slf4j
Obsoletes:      apacheds-daemon-bootstrappers < %{epoch}:%{version}-%{release}
Provides:       apacheds-daemon-bootstrappers = %{epoch}:%{version}-%{release}

%description bootstrappers
Daemon bootstrappers which initialize a classloader with 
jars laid out in an installation footprint.

%package maven2-plugin
Group:          Development/Java
Summary:        Build installers
Requires: %{name}-bootstrappers = %{epoch}:%{version}-%{release}
Requires: maven2 >= 0:2.0.4
Requires: ant >= 0:1.6.5
Requires: izpack
Requires: plexus-utils
Obsoletes:      apacheds-daemon-maven2-plugin < %{epoch}:%{version}-%{release}
Provides:       apacheds-daemon-maven2-plugin = %{epoch}:%{version}-%{release}

%description maven2-plugin
A plugin that builds installers using bootstrappers
and commons-daemon procrun and jsvc.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Obsoletes:      apacheds-daemon-javadoc < %{epoch}:%{version}-%{release}
Provides:       apacheds-daemon-javadoc = %{epoch}:%{version}-%{release}

%description javadoc
%{summary}.

%prep
%setup -q -n %{oname}-%{version}

%build
cp %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

mkdir -p m2_repo/repository/JPP/maven2/default_poms
cp %{SOURCE1} m2_repo/repository/JPP/maven2/default_poms/org.apache.directory-build.pom
cp pom.xml m2_repo/repository/JPP/maven2/default_poms/JPP-apacheds-daemon-build.pom
install -Dm644 %{SOURCE1} m2_repo/repository/org/apache/directory/build/1.0.5/build-1.0.5.pom

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

MVN=/usr/bin/mvn
export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository
export MAVEN_OPTS="-Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.jpp.mode=true -Dmaven.test.failure.ignore=true -Djava.awt.headless=true"

mvn-jpp -e \
        -s ${M2SETTINGS} \
	-Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
	-Dmaven.compile.target=1.5 \
	-Dmaven.javadoc.source=1.5 \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 bootstrappers/target/daemon-bootstrappers-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-bootstrappers-%{version}.jar
install -m 644 plugin/target/daemon-plugin-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-maven2-plugin-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-build.pom
%add_to_maven_depmap org.apache.directory.daemon build %{version} JPP %{name}-build
install -m 644 bootstrappers/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-bootstrappers.pom
%add_to_maven_depmap org.apache.directory.daemon daemon-bootstrappers %{version} JPP %{name}-daemon-bootstrappers
install -m 644 plugin/pom.xml \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-maven2-plugin.pom
%add_to_maven_depmap org.apache.directory.daemon daemon-plugin %{version} JPP %{name}-daemon-maven2-plugin

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/plugins
pushd $RPM_BUILD_ROOT%{_datadir}/maven2/plugins
    ln -sf %{_javadir}/%{name}-maven2-plugin.jar
popd

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/bootstrappers
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/plugin
cp -pr bootstrappers/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/bootstrappers
cp -pr plugin/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/plugin
ln -sf %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} #ghost

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%post bootstrappers
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun bootstrappers
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%post maven2-plugin
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%if %{gcj_support}
%postun maven2-plugin
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files bootstrappers
%doc bootstrappers/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}-bootstrappers*.jar
%{_datadir}/maven2/poms/JPP-%{name}-build.pom
%{_datadir}/maven2/poms/JPP-%{name}-bootstrappers.pom
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-bootstrappers-%{version}.jar.*
%endif

%files maven2-plugin
%doc plugin/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{name}-maven2-plugin*.jar
%{_datadir}/maven2/poms/JPP-%{name}-maven2-plugin.pom
%{_datadir}/maven2/plugins/*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-maven2-plugin-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt4_2jpp5
- fixed build with maven3

* Sat Sep 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_2jpp5
- fixed build with new maven 2.0.8

* Fri Sep 17 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- fixed build

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- converted from JPackage by jppimport script

