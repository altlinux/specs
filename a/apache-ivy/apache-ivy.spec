BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:           apache-ivy
Version:        2.2.0
Release:        alt1_1jpp6
Epoch:          0
Summary:        Agile dependency manager
License:        ASL 2.0
URL:            http://ant.apache.org/ivy/
Group:          Development/Java
Source0:        http://www.apache.org/dist/ant/ivy/2.2.0/apache-ivy-2.2.0-src.tar.gz
Source1:        http://repo1.maven.org/maven2/org/apache/ivy/ivy/2.2.0/ivy-2.2.0.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       bouncycastle
Requires:       oro
Requires:       jakarta-commons-codec
Requires:       jakarta-commons-httpclient
Requires:       jakarta-commons-lang
Requires:       jakarta-commons-logging
Requires:       jakarta-commons-vfs
Requires:       jpackage-utils
Requires:       jsch
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  ant-nodeps
BuildRequires:  ant-trax
BuildRequires:  bouncycastle
BuildRequires:  emma
BuildRequires:  jakarta-commons-codec
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  jakarta-commons-lang
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-vfs
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  jsch
BuildRequires:  oro
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildArch:      noarch
Source44: import.info
AutoReqProv: yes,noosgi

%description
Ivy is a free java based dependency manager, with powerful features such 
as transitive dependencies, ant integration, maven repository compatibility,
continuous integration, html reports and many more.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%{__mv} CHANGES.txt CHANGES.txt.orig
%{_bindir}/iconv -f iso88591 -t utf8 CHANGES.txt.orig > CHANGES.txt
%{__rm} CHANGES.txt.orig

%{__perl} -pi -e 's/\r$//g' CHANGES.txt LICENSE NOTICE README RELEASE_NOTES

%{__mkdir_p} lib
pushd lib
%{__ln_s} $(%{_bindir}/build-classpath ant-launcher) ant-launcher.jar
%{__ln_s} $(%{_bindir}/build-classpath ant/ant-nodeps) ant-nodeps.jar
%{__ln_s} $(%{_bindir}/build-classpath ant-testutil) ant-testutil.jar
%{__ln_s} $(%{_bindir}/build-classpath ant/ant-trax) ant-trax.jar
%{__ln_s} $(%{_bindir}/build-classpath ant) ant.jar
%{__ln_s} $(%{_bindir}/build-classpath bcpg) bcpg.jar
%{__ln_s} $(%{_bindir}/build-classpath bcprov) bcprov.jar
%{__ln_s} $(%{_bindir}/build-classpath commons-codec) commons-codec.jar
%{__ln_s} $(%{_bindir}/build-classpath commons-httpclient) commons-httpclient.jar
%{__ln_s} $(%{_bindir}/build-classpath commons-lang) commons-lang.jar
%{__ln_s} $(%{_bindir}/build-classpath commons-logging) commons-logging.jar
%{__ln_s} $(%{_bindir}/build-classpath commons-vfs) commons-vfs.jar
%{__ln_s} $(%{_bindir}/build-classpath emma) emma.jar
%{__ln_s} $(%{_bindir}/build-classpath emma_ant) emma_ant.jar
%{__ln_s} $(%{_bindir}/build-classpath jsch) jsch.jar
%{__ln_s} $(%{_bindir}/build-classpath junit) junit.jar
%{__ln_s} $(%{_bindir}/build-classpath oro) oro.jar
%{__ln_s} $(%{_bindir}/build-classpath xerces-j2) xercesImpl.jar
%{__ln_s} $(%{_bindir}/build-classpath xml-commons-jaxp-1.3-apis) xmlParserAPIs.jar
popd

%build
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/{junit,nodeps}`
export CLASSPATH=$(%{_bindir}/build-classpath commons-httpclient commons-vfs oro jsch)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first -Dtarget.ivy.version=%{version} /offline jar javadoc

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}

%{__cp} -p build/artifact/jars/ivy.jar %{buildroot}%{_javadir}/ivy-%{version}.jar
%{__ln_s} ivy-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)
# XXX: conflicts with ivy
%{__rm} %{buildroot}%{_javadir}/ivy.jar

%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.ivy ivy %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/doc/reports/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}

%files
%doc LICENSE CHANGES.txt NOTICE README RELEASE_NOTES 
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/ivy-%{version}.jar
%if 0
%{_javadir}/ivy.jar
%endif
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Wed Sep 07 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.2.0-alt1_1jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.0-alt1_2jpp6
- new version

