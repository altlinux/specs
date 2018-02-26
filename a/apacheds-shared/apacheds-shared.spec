Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define gcj_support 0


Summary:        Shared APIs of Apache Directory Project
Name:           apacheds-shared
Version:        0.9.12
Release:        alt5_2jpp6
Epoch:          0
Group:          Development/Java
License:        Apache 2.0 License
URL:            http://directory.apache.org/subprojects/shared/
Source0:        %{name}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/directory/shared/tags/0.9.12/ apacheds-shared-0.9.12


Source1:        directory-project-12.tar.gz
# svn export http://svn.apache.org/repos/asf/directory/project/tags/12/ directory-project-12

Source2:        %{name}-jpp-depmap.xml
Source3:        %{name}-settings.xml
Source4:        apache-jar-resource-bundle-1.3.jar

Patch0:         directory-project-12-pom.patch
Patch1:         apacheds-shared-pom.patch
Patch2:         apacheds-shared-convert-pom.patch
Patch3:         apacheds-shared-ldap-pom.patch
Patch4:         apacheds-shared-bouncycastle-reduced-pom.patch
Patch5:		apacheds-shared-0.9.12-alt-use-maven2-plugin-shade.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-remote-resources
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-stage
BuildRequires: maven-jxr
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: mojo-maven2-plugin-antlr
BuildRequires: mojo-maven2-plugin-rat
BuildRequires: maven2-plugin-shade
BuildRequires: mojo-maven2-support
BuildRequires: geronimo-genesis

BuildRequires: junit
BuildRequires: bouncycastle

BuildRequires: antlr
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-lang
BuildRequires: slf4j
BuildRequires: nlog4j
BuildRequires: mina11

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif


%description
This package contains the shared APIs of the
Apache Directory Project.

%package asn1-codec
Group:          Development/Java
Summary:        Apache shared ASN.1 Codec
Requires: mina11
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description asn1-codec
The ASN.1 subproject attempts to isolate the ASN.1 libraries and tools
for encoding ASN.1 in BER/DER/CER/PER encodings. The LDAP and X.500
aspects of the directory project impose the need for ASN.1 and BER
codecs.  Kerberos requires DER.  Rather than implement highly
specific and britle code for these needs we decided to separate out
the APIs and implementations used for dealing with ASN.1 codecs for any
ASN.1 defined protocol.

%package asn1
Group:          Development/Java
Summary:        Apache shared ASN.1 Tools
Requires: %{name}-asn1-codec = %{epoch}:%{version}-%{release}
Requires: slf4j
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description asn1
The ASN.1 subproject attempts to isolate the ASN.1 libraries and tools
for encoding ASN.1 in BER/DER/CER/PER encodings. The LDAP and X.500
aspects of the directory project impose the need for ASN.1 and BER
codecs.  Kerberos requires DER.  Rather than implement highly
specific and britle code for these needs we decided to separate out
the APIs and implementations used for dealing with ASN.1 codecs for any
ASN.1 defined protocol.

%package ldap
Group:          Development/Java
Summary:        Shared LDAP APIs of Apache Directory Project
Requires: %{name}-asn1-codec = %{epoch}:%{version}-%{release}
Requires: %{name}-asn1 = %{epoch}:%{version}-%{release}
Requires: antlr
Requires: jakarta-commons-collections
Requires: slf4j
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description ldap
%{summary}.

%package bouncycastle-reduced
Group:          Development/Java
Summary:        Reduced Bouncycastle from Apache Directory Project
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description bouncycastle-reduced
Repackages the BouncyCastle jar including only those files we require
rather than everything which includes patented algorithms like IDEA.

%package converter
Group:          Development/Java
Summary:        Shared converters from Apache Directory Project
Requires: %{name}-ldap = %{epoch}:%{version}-%{release}
%if %{gcj_support}
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description converter
%{summary}.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
Provides:       %{name}-asn1-codec-javadoc
Obsoletes:      %{name}-asn1-javadoc < %{epoch}-%{version}
Provides:       %{name}-asn1-javadoc
Obsoletes:      %{name}-ldap-javadoc < %{epoch}-%{version}
Provides:       %{name}-ldap-javadoc
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
gzip -dc %{SOURCE1} | tar xf -

%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -p1

%build
export LANG=en_US.ISO8859-1
cp %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository


#mkdir -p m2_repo/repository/JPP/maven2/default_poms
#cp %{SOURCE1} m2_repo/repository/JPP/maven2/default_poms/org.apache.directory-build.pom
mkdir -p $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/
cp directory-project-12/pom.xml \
   $MAVEN_REPO_LOCAL/JPP/maven2/default_poms/org.apache.directory.project-project.pom
mkdir -p $MAVEN_REPO_LOCAL/org/apache/directory/project/project/12/
cp directory-project-12/pom.xml \
$MAVEN_REPO_LOCAL/org/apache/directory/project/project/12/project-12.pom
mkdir -p $MAVEN_REPO_LOCAL/org.apache/
mkdir -p $MAVEN_REPO_LOCAL/org/apache/apache-jar-resource-bundle/1.4/
cp %{SOURCE4} $MAVEN_REPO_LOCAL/org.apache/apache-jar-resource-bundle.jar
cp %{SOURCE4} $MAVEN_REPO_LOCAL/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.jar


mkdir external_repo
ln -s %{_javadir} external_repo/JPP

pushd ldap-constants
mvn-jpp -e \
        -s ${M2SETTINGS} \
	-Dmaven.test.skip=true \
	-Dmaven.test.skip.exec=true \
	-Dmaven.compile.target=1.5 \
	-Dmaven.javadoc.source=1.5 \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
        install
popd

mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
	-Dmaven.test.skip=true \
	-Dmaven.test.skip.exec=true \
	-Dmaven.compile.target=1.5 \
	-Dmaven.javadoc.source=1.5 \
        install

mvn-jpp -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
	-Dmaven.test.skip=true \
	-Dmaven.test.skip.exec=true \
	-Dmaven.compile.target=1.5 \
	-Dmaven.javadoc.source=1.5 \
        javadoc:javadoc

mkdir tmp
pushd tmp
jar xf ../bouncycastle-reduced/target/shared-bouncycastle-reduced-%{version}.jar
rm -rf META-INF
# alt; remove embedded junit
rm -rf junit org/junit org/hamcrest
# end alt
jar cf ../bouncycastle-reduced/target/shared-bouncycastle-reduced-%{version}.jar *
popd

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 asn1-codec/target/shared-asn1-codec-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-asn1-codec-%{version}.jar
install -m 644 asn1-codec/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-asn1-codec.pom
%add_to_maven_depmap org.apache.directory.shared shared-asn1-codec %{version} JPP %{name}-asn1-codec

install -m 644 asn1/target/shared-asn1-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-asn1-%{version}.jar
install -m 644 asn1/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-asn1.pom
%add_to_maven_depmap org.apache.directory.shared shared-asn1 %{version} JPP %{name}-asn1

install -m 644 ldap/target/shared-ldap-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ldap-%{version}.jar
install -m 644 ldap/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ldap.pom
%add_to_maven_depmap org.apache.directory.shared shared-ldap %{version} JPP %{name}-ldap

install -m 644 ldap-constants/target/shared-ldap-constants-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ldap-constants-%{version}.jar
install -m 644 ldap-constants/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ldap-constants.pom
%add_to_maven_depmap org.apache.directory.shared shared-ldap-constants %{version} JPP %{name}-ldap-constants

install -m 644 ldap-jndi/target/shared-ldap-jndi-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-ldap-jndi-%{version}.jar
install -m 644 ldap-jndi/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-ldap-jndi.pom
%add_to_maven_depmap org.apache.directory.shared shared-ldap-jndi %{version} JPP %{name}-ldap-jndi

install -m 644 convert/target/shared-converter-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-converter-%{version}.jar
install -m 644 convert/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-converter.pom
%add_to_maven_depmap org.apache.directory.shared shared-converter %{version} JPP %{name}-converter

install -m 644 bouncycastle-reduced/target/shared-bouncycastle-reduced-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-bouncycastle-reduced-%{version}.jar
install -m 644 bouncycastle-reduced/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bouncycastle-reduced.pom
%add_to_maven_depmap org.apache.directory.shared shared-bouncycastle-reduced %{version} JPP %{name}-bouncycastle-reduced

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-build.pom
%add_to_maven_depmap org.apache.directory.shared build %{version} JPP %{name}-build

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
#cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/
ln -sf %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} #ghost

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files asn1-codec
%doc directory-project-12/LICENSE.txt
%{_javadir}/%{name}-asn1-codec-%{version}.jar
%{_javadir}/%{name}-asn1-codec.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-asn1-codec-%{version}.jar.*
%endif

%files asn1
%doc directory-project-12/LICENSE.txt
%{_javadir}/%{name}-asn1-%{version}.jar
%{_javadir}/%{name}-asn1.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-asn1-%{version}.jar.*
%endif

%files ldap
%doc directory-project-12/LICENSE.txt
%{_javadir}/%{name}-ldap*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-ldap-%{version}.jar.*
%endif

%files bouncycastle-reduced
%doc directory-project-12/LICENSE.txt
%{_javadir}/%{name}-bouncycastle*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-bouncycastle-reduced-%{version}.jar.*
%endif

%files converter
%doc directory-project-12/LICENSE.txt
%{_javadir}/%{name}-converter*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{name}/%{name}-converter-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt5_2jpp6
- fixed build with java 7

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt4_2jpp6
- use maven2-plugin-shade

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt3_2jpp6
- fixed build

* Fri Oct 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt2_2jpp6
- removed junit embedded in bouncycastle

* Sat Sep 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt1_2jpp6.1
- fixed build with maven 2.0.8

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt1_2jpp6
- new version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt2_2jpp5
- explicit selection of java5 compiler

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt1_2jpp5
- converted from JPackage by jppimport script

* Thu Jan 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.3-alt1_2jpp1.7
- converted from JPackage by jppimport script

