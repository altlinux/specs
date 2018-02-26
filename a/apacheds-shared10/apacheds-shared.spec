BuildRequires: maven2-plugin-site
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
%define oldname apacheds-shared
Conflicts: apacheds-shared
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


Summary:        Shared APIs of Apache Directory Project
Name:           apacheds-shared10
Version:        0.9.5.5
Release:        alt5_2jpp5
Epoch:		0
Group:          Development/Java
License:        Apache 2.0 License
URL:            http://directory.apache.org/subprojects/shared/
Source0:        %{oldname}-%{version}.tar.gz
# svn export http://svn.apache.org/repos/asf/directory/shared/tags/0.9.5.5/ apacheds-shared-0.9.5.5

Source1:        directory-pom-1.0.4.xml
Source2:        %{oldname}-jpp-depmap.xml
Source3:        %{oldname}-settings.xml

Patch0:		apacheds-shared-pom_xml.patch

Patch1:		apacheds-shared-ldap-pom_xml.patch

#Vendor: %{?_vendorinfo:%{_vendorinfo}}%{!?_vendorinfo:%{_vendor}}
#Distribution: %{?_distribution:%{_distribution}}%{!?_distribution:%{_vendor}}

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: maven2 >= 0:2.0.7
BuildRequires: maven2-plugin-antrun
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-project-info-reports
BuildRequires: maven2-plugin-resources
BuildRequires: maven-jxr
BuildRequires: maven-release
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-report-plugin
BuildRequires: mojo-maven2-plugin-antlr

BuildRequires: junit

BuildRequires: antlr
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-lang
BuildRequires: slf4j
BuildRequires: nlog4j
BuildRequires: mina10

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
Requires: mina10
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

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{oldname}
Provides:	%{oldname}-asn1-codec-javadoc
Obsoletes:	%{oldname}-asn1-javadoc < %{epoch}-%{version}
Provides:	%{oldname}-asn1-javadoc
Obsoletes:	%{oldname}-ldap-javadoc < %{epoch}-%{version}
Provides:	%{oldname}-ldap-javadoc
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{oldname}-%{version}
%patch0 -b .sav0
%patch1 -b .sav1

%build
export LANG=en_US.ISO8859-1
cp %{SOURCE3} maven2-settings.xml

sed -i -e "s|<url>__JPP_URL_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__JAVADIR_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENREPO_DIR_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" maven2-settings.xml
sed -i -e "s|<url>__MAVENDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/maven2/plugins</url>|g" maven2-settings.xml
sed -i -e "s|<url>__ECLIPSEDIR_PLUGIN_PLACEHOLDER__</url>|<url>file:///usr/share/eclipse/plugins</url>|g" maven2-settings.xml


mkdir -p m2_repo/repository/JPP/maven2/default_poms
cp %{SOURCE1} m2_repo/repository/JPP/maven2/default_poms/org.apache.directory-build.pom
install -m 644 -D %{SOURCE1} m2_repo/repository/org/apache/directory/build/1.0.5/build-1.0.5.pom

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

export M2SETTINGS=$(pwd)/maven2-settings.xml
export MAVEN_REPO_LOCAL=`pwd`/m2_repo/repository

mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e \
        -s ${M2SETTINGS} \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file=%{SOURCE2} \
	-Dmaven.test.skip=true \
	-Dmaven.test.skip.exec=true \
	install javadoc:javadoc


%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 asn1-codec/target/shared-asn1-codec-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}-asn1-codec-%{version}.jar
install -m 644 asn1-codec/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{oldname}-asn1-codec.pom
%add_to_maven_depmap org.apache.directory.shared shared-asn1-codec %{version} JPP %{oldname}-asn1-codec

install -m 644 asn1/target/shared-asn1-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}-asn1-%{version}.jar
install -m 644 asn1/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{oldname}-asn1.pom
%add_to_maven_depmap org.apache.directory.shared shared-asn1 %{version} JPP %{oldname}-asn1

install -m 644 ldap/target/shared-ldap-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{oldname}-ldap-%{version}.jar
install -m 644 ldap/pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{oldname}-ldap.pom
%add_to_maven_depmap org.apache.directory.shared shared-ldap %{version} JPP %{oldname}-ldap

install -m 644 pom.xml $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{oldname}-build.pom
%add_to_maven_depmap org.apache.directory.shared build %{version} JPP %{oldname}-build

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}/asn1-codec
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}/asn1
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}/ldap
cp -pr asn1-codec/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}/asn1-codec
cp -pr asn1/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}/asn1
cp -pr ldap/target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{oldname}-%{version}/ldap
ln -sf %{oldname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{oldname} #ghost

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{oldname}
ln -s %{oldname}-%{version} %{_javadocdir}/%{oldname}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{oldname}
fi

%files asn1-codec
%doc asn1-codec/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{oldname}-asn1-codec-%{version}.jar
%{_javadir}/%{oldname}-asn1-codec.jar
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{oldname}
%{_libdir}/gcj/%{oldname}/%{oldname}-asn1-codec-%{version}.jar.*
%endif

%files asn1
%doc asn1/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{oldname}-asn1-%{version}.jar
%{_javadir}/%{oldname}-asn1.jar
%if %{gcj_support}
%{_libdir}/gcj/%{oldname}/%{oldname}-asn1-%{version}.jar.*
%endif

%files ldap
%doc ldap/src/main/resources/META-INF/LICENSE.txt
%{_javadir}/%{oldname}-ldap*.jar
%if %{gcj_support}
%{_libdir}/gcj/%{oldname}/%{oldname}-ldap-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{oldname}-%{version}
%ghost %{_javadocdir}/%{oldname}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt5_2jpp5
- fixed build with java 7

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt4_2jpp5
- fixed build with slf4j

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt3_2jpp5
- fixed build

* Sat Sep 25 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt2_2jpp5
- fixed build with new maven 2.0.8

* Sat Sep 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt1_2jpp5
- compat build

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.12-alt1_2jpp6
- new version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt2_2jpp5
- explicit selection of java5 compiler

* Sat Oct 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.5-alt1_2jpp5
- converted from JPackage by jppimport script

* Thu Jan 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5.3-alt1_2jpp1.7
- converted from JPackage by jppimport script

