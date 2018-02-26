BuildRequires: glassfish-jaxb
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-core
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

%define svnrev 6029

Name:           opends
Version:        1.0.0
Release:	alt3_5jpp6
Epoch:          0
Summary:        OpenDS directory service
Group:          Development/Java
License:        CDDL
URL:            http://www.opends.org/
# svn -q export --username guest https://opends.dev.java.net/svn/opends/tags/build15 opends-1.0.0
Source0:        opends-1.0.0.tar.gz
Source1:        http://repository.jboss.com/maven2/sun-opends/OpenDS/1.0.0/OpenDS-1.0.0.pom
Patch0:         opends-svnkit-CheckPrecommit.patch
Patch1:         opends-svnkit-CoverageDiff.patch
Patch2:         opends-svnkit-GetSubversionRevision.patch
Patch3:         opends-build.patch
Patch4:         opends-xslt.patch
Patch5:         opends-no-svnrev.patch
BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant17 >= 0:1.6.5
BuildRequires: ant17-antlr
BuildRequires: ant17-apache-bcel
BuildRequires: ant17-apache-bsf
BuildRequires: ant17-apache-log4j
BuildRequires: ant17-apache-oro
BuildRequires: ant17-apache-regexp
BuildRequires: ant17-apache-resolver
BuildRequires: ant17-commons-logging
BuildRequires: ant17-commons-net
BuildRequires: ant-contrib
BuildRequires: ant17-javamail
BuildRequires: ant17-jdepend
BuildRequires: ant17-jmf
BuildRequires: ant17-jsch
BuildRequires: ant17-junit
BuildRequires: ant17-nodeps
BuildRequires: ant17-swing
BuildRequires: ant17-trax
BuildRequires: emma
BuildRequires: svnkit
BuildRequires: aspectj
BuildRequires: ganymed-ssh2
BuildRequires: berkeleydb-je32
BuildRequires: jaf_1_1_api
BuildRequires: javamail_1_4_api
BuildRequires: jaxb_2_1_api
BuildRequires: relaxngDatatype
BuildRequires: saaj_1_3_api
BuildRequires: servlet_2_5_api
BuildRequires: stax_1_0_api
BuildRequires: glassfish-jaxb
BuildRequires: xerces-j2
BuildRequires: xml-commons-jaxp-1.3-apis
Requires: aspectj
Requires: ganymed-ssh2
Requires: berkeleydb-je32
Requires: jaf_1_1_api
Requires: javamail_1_4_api
Requires: jaxb_2_1_api
Requires: relaxngDatatype
Requires: saaj_1_3_api
Requires: servlet_2_5_api
Requires: stax_1_0_api
Requires: glassfish-jaxb
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
OpenDS is an open source community project building a free 
and comprehensive next generation directory service. OpenDS 
is designed to address large deployments, to provide high 
performance, to be highly extensible, and to be easy to 
deploy, manage and monitor. The OpenDS directory service 
will ultimately include not just the Directory Server, but 
also other essential directory-related services like 
directory proxy, virtual directory, namespace distribution 
and data synchronization. Initial development of OpenDS was 
done by Sun Microsystems, but is now available under the 
open source Common Development and Distribution License 
(CDDL).

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q 
find . -name "*.jar" | xargs -t rm
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
#BUILD/opends-1.0.0/ext/svnkit/ganymed.jar.no
ln -sf $(build-classpath ganymed-ssh2) ext/svnkit/ganymed.jar
#BUILD/opends-1.0.0/ext/svnkit/svnkit-javahl.jar.no
ln -sf $(build-classpath svnkit-javahl) ext/svnkit/
#BUILD/opends-1.0.0/ext/svnkit/svnkit.jar.no
ln -sf $(build-classpath svnkit) ext/svnkit/
#BUILD/opends-1.0.0/ext/svnkit/svnkit-cli.jar.no
ln -sf $(build-classpath svnkit-cli) ext/svnkit/
#BUILD/opends-1.0.0/ext/emma/lib/emma_ant.jar.no
ln -sf $(build-classpath emma_ant) ext/emma/lib
#BUILD/opends-1.0.0/ext/emma/lib/emma.jar.no
ln -sf $(build-classpath emma) ext/emma/lib
#BUILD/opends-1.0.0/lib/je.jar.no
ln -sf $(build-classpath je32) lib/je.jar
#BUILD/opends-1.0.0/lib/mail.jar.no
ln -sf $(build-classpath javamail_1_4_api) lib/mail.jar
#BUILD/opends-1.0.0/lib/aspectjrt.jar.no
ln -sf $(build-classpath aspectjrt) lib/aspectjrt.jar
#BUILD/opends-1.0.0/lib/activation.jar.no
ln -sf $(build-classpath jaf_1_1_api) lib/activation.jar
#BUILD/opends-1.0.0/resource/dsml/lib/jaxb-impl.jar.no
ln -sf $(build-classpath glassfish-jaxb/jaxb-impl) resource/dsml/lib/jaxb-impl.jar
#BUILD/opends-1.0.0/resource/dsml/lib/jaxb-xjc.jar.no
ln -sf $(build-classpath glassfish-jaxb/jaxb-xjc) resource/dsml/lib/jaxb-xjc.jar
#BUILD/opends-1.0.0/resource/dsml/lib/jaxb1-impl.jar.no
ln -sf $(build-classpath glassfish-jaxb/jaxb1-impl) resource/dsml/lib/jaxb1-impl.jar
#BUILD/opends-1.0.0/resource/dsml/lib/jaxb-api.jar.no
ln -sf $(build-classpath jaxb_2_1_api) resource/dsml/lib/jaxb-api.jar
ln -sf $(build-classpath relaxngDatatype) resource/dsml/lib/
ln -sf $(build-classpath jaf_1_1_api) resource/dsml/lib/
ln -sf $(build-classpath saaj_1_3_api) resource/dsml/lib/
ln -sf $(build-classpath servlet_2_5_api) resource/dsml/lib/
ln -sf $(build-classpath stax_1_0_api) resource/dsml/lib/
#BUILD/opends-1.0.0/ext/ant/lib/ant-antlr.jar.no
ln -sf $(build-classpath ant/ant-antlr) ext/ant/lib/ant-antlr.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-apache-bcel.jar.no
ln -sf $(build-classpath ant/ant-apache-bcel) ext/ant/lib/ant-apache-bcel.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-apache-bsf.jar.no
ln -sf $(build-classpath ant/ant-apache-bsf) ext/ant/lib/ant-apache-bsf.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-apache-log4j.jar.no
ln -sf $(build-classpath ant/ant-apache-log4j) ext/ant/lib/ant-apache-log4j.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-apache-oro.jar.no
ln -sf $(build-classpath ant/ant-apache-oro) ext/ant/lib/ant-apache-oro.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-apache-regexp.jar.no
ln -sf $(build-classpath ant/ant-apache-regexp) ext/ant/lib/ant-apache-regexp.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-apache-resolver.jar.no
ln -sf $(build-classpath ant/ant-apache-resolver) ext/ant/lib/ant-apache-resolver.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-commons-logging.jar.no
ln -sf $(build-classpath ant/ant-commons-logging) ext/ant/lib/ant-commons-logging.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-commons-net.jar.no
ln -sf $(build-classpath ant/ant-commons-net) ext/ant/lib/ant-commons-net.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-contrib-1.0b3.jar.no
ln -sf $(build-classpath ant-contrib) ext/ant/lib/ant-contrib.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-icontract.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant-jai.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant.jar.no
ln -sf $(build-classpath ant) ext/ant/lib/ant.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-javamail.jar.no
ln -sf $(build-classpath ant/ant-javamail) ext/ant/lib/ant-javamail.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-jdepend.jar.no
ln -sf $(build-classpath ant/ant-jdepend) ext/ant/lib/ant-jdepend.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-jmf.jar.no
ln -sf $(build-classpath ant/ant-jmf) ext/ant/lib/ant-jmf.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-jsch.jar.no
ln -sf $(build-classpath ant/ant-jsch) ext/ant/lib/ant-jsch.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-junit.jar.no
ln -sf $(build-classpath ant/ant-junit) ext/ant/lib/ant-junit.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-launcher.jar.no
ln -sf $(build-classpath ant-launcher) ext/ant/lib/ant-launcher.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-netrexx.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant-nodeps.jar.no
ln -sf $(build-classpath ant/ant-nodeps) ext/ant/lib/ant-nodeps.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-starteam.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant-stylebook.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant-swing.jar.no
ln -sf $(build-classpath ant/ant-swing) ext/ant/lib/ant-swing.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-trax.jar.no
ln -sf $(build-classpath ant/ant-trax) ext/ant/lib/ant-trax.jar
#BUILD/opends-1.0.0/ext/ant/lib/ant-vaj.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant-weblogic.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant-xalan1.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/ant-xslp.jar.no
#BUILD/opends-1.0.0/ext/ant/lib/xercesImpl.jar.no
ln -sf $(build-classpath xerces-j2) ext/ant/lib/xercesImpl.jar
#BUILD/opends-1.0.0/ext/ant/lib/xml-apis.jar.no
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) ext/ant/lib/xml-apis.jar

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{nodeps,trax}`
export CLASSPATH=
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dant.home=%{_usr} -DREVISION_NUMBER=%{svnrev} -DMEM=1g package javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -p -m 644 build/package/OpenDS-%{version}/lib/OpenDS.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar | sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap sun-opends OpenDS %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt3_5jpp6
- built with java 6

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt2_5jpp6
- build with ant17

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_5jpp6
- new version

