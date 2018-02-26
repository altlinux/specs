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

%define gcj_support 0

Name:           directory-naming
Version:        0.8
Release:        alt4_4jpp6
Epoch:          0
Summary:        Directory Naming
License:        Apache Software License 2.0
URL:            http://directory.apache.org
Group:          Development/Java

Source0:        directory-naming-0.8.tar.gz
# svn export -r 124846 http://svn.apache.org/repos/asf/directory/sandbox/dormant-subprojects/naming/ directory-naming-0.8

Source5:        http://repo1.maven.org/maven2/directory-naming/naming-core/0.8/naming-core-0.8.pom
Source6:        http://repo1.maven.org/maven2/directory-naming/naming-config/0.8/naming-config-0.8.pom
Source7:        http://repo1.maven.org/maven2/directory-naming/naming-factory/0.8/naming-factory-0.8.pom
Source8:        http://repo1.maven.org/maven2/directory-naming/naming-java/0.8/naming-java-0.8.pom
Source9:        http://repo1.maven.org/maven2/directory-naming/naming-management/0.8/naming-management-0.8.pom
Source10:       http://repo1.maven.org/maven2/directory-naming/naming-resources/0.8/naming-resources-0.8.pom

Patch0:         directory-naming-0.8-project.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7.1
BuildRequires: hsqldb
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-dbcp
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-pool
BuildRequires: javamail_1_3_1_api
#BuildRequires:  mx4j

Requires: jakarta-commons-collections
Requires: jakarta-commons-dbcp
Requires: jakarta-commons-digester
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-commons-pool
Requires: javamail_1_3_1_api
#Requires:  mx4j
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info

%description
Old directory/naming module.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q 
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

%build
export CLASSPATH=$(build-classpath \
commons-beanutils \
commons-collections \
commons-dbcp \
commons-digester \
commons-lang \
commons-logging \
commons-pool \
hsqldb \
javamail_1_3_1_api \
junit \
)

CLASSPATH=$CLASSPATH:$(pwd)/naming-config/target/classes:$(pwd)/naming-config/target/test-classes
CLASSPATH=$CLASSPATH:$(pwd)/naming-core/target/classes:$(pwd)/naming-core/target/test-classes
CLASSPATH=$CLASSPATH:$(pwd)/naming-factory/target/classes:$(pwd)/naming-factory/target/test-classes
CLASSPATH=$CLASSPATH:$(pwd)/naming-java/target/classes:$(pwd)/naming-java/target/test-classes
CLASSPATH=$CLASSPATH:$(pwd)/naming-management/target/classes:$(pwd)/naming-management/target/test-classes
CLASSPATH=$CLASSPATH:$(pwd)/naming-resources/target/classes:$(pwd)/naming-resources/target/test-classes

#FIXME failed to create task or type setproxy
for f in $(find . -name build.xml); do
    sed -i "s|<setproxy>|<!-- <setproxy> -->|g" $f
    sed -i "s|</setproxy>|<!-- </setproxy> -->|g" $f
done;

export OPT_JAR_LIST="junit ant/ant-junit"

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc
#ant jar javadoc

%install
# jars
%__mkdir_p %{buildroot}%{_javadir}/%{name}
for p in \
         naming-config \
         naming-core \
         naming-factory \
         naming-java \
         naming-management \
         naming-resources \
         ; do
%__install -m 644 $p/target/$p-%{version}.jar %{buildroot}%{_javadir}/%{name}/$p-%{version}.jar
done
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do %__ln_s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
%__mkdir_p %{buildroot}%{_datadir}/maven2/poms
%__install -m 644 %{SOURCE5}  %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-naming-core.pom
%add_to_maven_depmap %{name} naming-core %{version} JPP/%{name} naming-core
%__install -m 644 %{SOURCE6}  %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-naming-config.pom
%add_to_maven_depmap %{name} naming-config %{version} JPP/%{name} naming-config
%__install -m 644 %{SOURCE7}  %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-naming-factory.pom
%add_to_maven_depmap %{name} naming-factory %{version} JPP/%{name} naming-factory
%__install -m 644 %{SOURCE8}  %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-naming-java.pom
%add_to_maven_depmap %{name} naming-java %{version} JPP/%{name} naming-java
%__install -m 644 %{SOURCE9}  %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-naming-management.pom
%add_to_maven_depmap %{name} naming-management %{version} JPP/%{name} naming-management
%__install -m 644 %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-naming-resources.pom
%add_to_maven_depmap %{name} naming-resources %{version} JPP/%{name} naming-resources

# javadocs
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# docs
%__mkdir_p %{buildroot}%{_docdir}/%{name}-%{version}
%__cp LICENSE.txt  %{buildroot}%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_docdir}/%{name}-%{version}/LICENSE.txt 
%{_javadir}/%{name}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Dec 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt4_4jpp6
- fixed build

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt4_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt3_1jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.8-alt1_1jpp5
- converted from JPackage by jppimport script

