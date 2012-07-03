Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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

%define specversion 1.0b

Name:           glassfish-persistence
Version:        2.0.41
Release:        alt4_1jpp5
Epoch:          0
Summary:        Glassfish JPA (Toplink Essentials)
License:        CDDL
Url:            http://www.oracle.com/technology/products/ias/toplink/jpa/index.html
Source0:        http://download.java.net/javaee5/promoted/source/glassfish-persistence-v2-b41-src.zip
Source1:        glassfish-bootstrap.tar.gz
Patch0:         glassfish-entity-persistence-build.patch
Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps
BuildRequires: jta_1_1_api

Requires: jta_1_1_api

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

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
Glassfish Persistence Implementation.

%package %{specversion}-api
Summary:        Persistence %{specversion} API from %{name}
Group:          Development/Java
Provides:       jpa_1_0B_api

%description %{specversion}-api
%{summary}.

%package impl
Summary:        JPA Implementation from %{name}
Group:          Development/Java
Requires: %{name}-%{specversion}-api = %{epoch}:%{version}-%{release}
Provides:       toplink-essentials = %{epoch}:%{version}-%{release}

%description impl
%{summary}.

%package %{specversion}-api-javadoc
Summary:        Javadoc for %{name} %{specversion} API
Group:          Development/Documentation

%description %{specversion}-api-javadoc
%{summary}.

%package impl-javadoc
Summary:        Javadoc for %{name} Implementation
Group:          Development/Documentation

%description impl-javadoc
%{summary}.

%prep
%setup -q -c -n %{name}
gzip -dc %{SOURCE1} | tar xf -
mv glassfish-bootstrap glassfish/bootstrap
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
sed -i -e 's/@VERSION@/%{specversion}/' glassfish/persistence-api/persistence-api.pom
sed -i -e 's/@VERSION@/%{version}/' glassfish/entity-persistence/toplink-essentials.pom
sed -i -e 's/@VERSION@/%{version}/' glassfish/entity-persistence/toplink-essentials-agent.pom

%patch0 -b .sav0


%build
pushd glassfish/persistence-api
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Drelease.version=%{specversion} all javadoc
popd
export CLASSPATH=$(pwd)/publish/glassfish/lib/javaee.jar
pushd glassfish/entity-persistence
ant -Djavaee.jar=$(build-classpath jta_1_1_api) all docs
popd

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/glassfish
install -m 644 publish/glassfish/lib/javaee.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{specversion}-api-%{version}.jar
install -m 644 publish/glassfish/lib/toplink-essentials.jar $RPM_BUILD_ROOT%{_javadir}/glassfish/toplink-essentials-%{version}.jar
install -m 644 publish/glassfish/lib/toplink-essentials-agent.jar $RPM_BUILD_ROOT%{_javadir}/glassfish/toplink-essentials-agent-%{version}.jar
%add_to_maven_depmap javax.persistence persistence-api %{specversion} JPP %{name}-%{specversion}-api
%add_to_maven_depmap toplink.essentials toplink-essentials %{version} JPP/glassfish toplink-essentials
%add_to_maven_depmap toplink.essentials toplink-essentials-agent %{version} JPP/glassfish toplink-essentials-agent

(cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

(cd $RPM_BUILD_ROOT%{_javadir}/glassfish
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 glassfish/persistence-api/persistence-api.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-%{specversion}-api.pom
install -m 644 glassfish/entity-persistence/toplink-essentials.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.glassfish-toplink-essentials.pom
install -m 644 glassfish/entity-persistence/toplink-essentials-agent.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.glassfish-toplink-essentials-agent.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{specversion}-api-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-impl-%{version}
cp -pr glassfish/persistence-api/build/classes/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{specversion}-api-%{version}
cp -pr glassfish/entity-persistence/build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-impl-%{version}
ln -s %{name}-%{specversion}-api-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{specversion}-api # ghost symlink
ln -s %{name}-impl-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-impl # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_1_0B_api_%{name}-%{specversion}-api<<EOF
%{_javadir}/jpa_1_0B_api.jar	%{_javadir}/%{name}-%{specversion}-api.jar	10001
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jpa_3_0_api_%{name}-%{specversion}-api<<EOF
%{_javadir}/jpa_3_0_api.jar	%{_javadir}/%{name}-%{specversion}-api.jar	30000
EOF

%post %{specversion}-api-javadoc
rm -f %{_javadocdir}/%{name}-%{specversion}-api
ln -s %{name}-%{specversion}-api-%{version} %{_javadocdir}/%{name}-%{specversion}-api

%postun %{specversion}-api-javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}-%{specversion}-api
fi

%post impl-javadoc
rm -f %{_javadocdir}/%{name}-impl
ln -s %{name}-impl-%{version} %{_javadocdir}/%{name}-impl

%postun impl-javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}-impl
fi

%files %{specversion}-api
%_altdir/jpa_3_0_api_%{name}-%{specversion}-api
%_altdir/jpa_1_0B_api_%{name}-%{specversion}-api
%{_javadir}/%{name}-%{specversion}-api*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-api-%{version}.jar.*
%endif

%files impl
%{_javadir}/glassfish/toplink-essentials*.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-impl-%{version}.jar.*
%endif

%files %{specversion}-api-javadoc
%{_javadocdir}/%{name}-%{specversion}-api-%{version}
%ghost %{_javadocdir}/%{name}-%{specversion}-api

%files impl-javadoc
%{_javadocdir}/%{name}-impl-%{version}
%ghost %{_javadocdir}/%{name}-impl

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.41-alt4_1jpp5
- built with java 6 due to abstract getParentLogger

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.41-alt3_1jpp5
- fixes for java6 support

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.41-alt2_1jpp5
- alternatives 0.4

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.41-alt1_1jpp5
- converted from JPackage by jppimport script

