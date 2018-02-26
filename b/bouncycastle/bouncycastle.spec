BuildRequires(pre): java-1.4.2-devel java-1.5.0-devel java-1.6.0-devel
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

#def_with jdk6
%bcond_with jdk6
%bcond_without signed

%global archivever 146


Name:           bouncycastle
Version:        1.46
Release:        alt2_3jpp6
Epoch:          0
Summary:        Bouncy Castle Crypto Package for Java
Group:          Development/Java
License:        BSD
URL:            http://www.bouncycastle.org/java.html
Source0:        http://downloads.bouncycastle.org/java/crypto-%{archivever}.tar.gz
Source1:        http://downloads.bouncycastle.org/java/bcprov-jdk15-%{archivever}.jar
Source2:        http://downloads.bouncycastle.org/java/bcprov-jdk16-%{archivever}.jar
Obsoletes:      bouncycastle-jdk1.4 < %{epoch}:%{version}-%{release}
Obsoletes:      bouncycastle-jdk1.5 < %{epoch}:%{version}-%{release}
Obsoletes:      bouncycastle-jdk1.6 < %{epoch}:%{version}-%{release}
Obsoletes:      bouncycastle-extras < %{epoch}:%{version}-%{release}
Provides:       bouncycastle-extras = %{epoch}:%{version}-%{release}
# BEGIN PROVIDER
Obsoletes:      %{name}-provider < %{epoch}:%{version}-%{release}
Provides:       %{name}-provider = %{epoch}:%{version}-%{release}
%if %with jdk6
Provides:       jce = 0:1.6.0.0
%else
Provides:       jce = 0:1.5.0.0
%endif
Requires:       jaf_1_0_2_api
Requires:       javamail_1_4_api
Requires:       jpackage-utils
# END PROVIDER
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  jaf_1_0_2_api
BuildRequires:  javamail_1_4_api
BuildRequires:  junit
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info
Provides: bouncycastle-mail = %version
Provides: bouncycastle-tsp = %version

%description
The Bouncy Castle Crypto APIs for Java consist of the following:

    * A lightweight cryptography API for Java.

    * A provider for the Java Cryptography Extension and the Java Cryptography
      Architecture.

    * A clean room implementation of the JCE 1.2.1.

    * A library for reading and writing encoded ASN.1 objects.

    * A light weight client-side TLS API.

    * Generators for Version 1 and Version 3 X.509 certificates, Version 2
      CRLs, and PKCS12 files.

    * Generators for Version 2 X.509 attribute certificates.

    * Generators/Processors for S/MIME and CMS (PKCS7/RFC 3852).

    * Generators/Processors for OCSP (RFC 2560).

    * Generators/Processors for TSP (RFC 3161).

    * Generators/Processors for OpenPGP (RFC 2440).
%if %without jdk6
    * A signed jar version suitable for JDK 1.5 and the Sun JCE.
%else
    * A signed jar version suitable for JDK 1.6 and the Sun JCE.
%endif
The lightweight API works with everything from the J2ME to the JDK 1.6.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Obsoletes:      bouncycastle-javadoc-jdk1.4 < %{epoch}:%{version}-%{release}
Obsoletes:      bouncycastle-javadoc-jdk1.5 < %{epoch}:%{version}-%{release}
Obsoletes:      bouncycastle-javadoc-jdk1.6 < %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n crypto-%{archivever}
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
export CLASSPATH=$(%{_bindir}/build-classpath jaf javamail_1_4_api junit)
export OPT_JAR_LIST="`%{__cat} %{_sysconfdir}/ant.d/junit`"
export LC_ALL=en_US.UTF-8
%if %with jdk6
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f jdk16.xml -Dbuild.sysclasspath=first -Drelease.suffix=%{version} build-provider build build-test
%else
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f jdk15.xml -Dbuild.sysclasspath=first -Drelease.suffix=%{version} build-provider build build-test
%endif

%install

%{__mkdir_p} %{buildroot}%{_javadir}

%if %with jdk6
pushd build/artifacts/jdk1.6/jars
for jar16 in {bcmail,bcpg,bcprov,bctest,bctsp}-jdk16-%{version}.jar; do
   jar16d=`/bin/echo ${jar16} | %{__sed} s/-jdk16//g`
   %{__install} -p -m 644 ${jar16} %{buildroot}%{_javadir}/${jar16d}
done
popd
%else
pushd build/artifacts/jdk1.5/jars
for jar15 in {bcmail,bcpg,bcprov,bctest,bctsp}-jdk15-%{version}.jar; do
   jar15d=`/bin/echo ${jar15} | %{__sed} s/-jdk15//g`
   %{__install} -p -m 644 ${jar15} %{buildroot}%{_javadir}/${jar15d}
done
popd
%endif

%if %with signed
%if %without jdk6
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{_javadir}/bcprov-%{version}.jar
%else
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{_javadir}/bcprov-%{version}.jar
%endif
%endif

pushd %{buildroot}%{_javadir}
  for jar in *-%{version}.jar; do
    %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} s/-%{version}//g`
  done
popd

%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with jdk6
pushd build/artifacts/jdk1.6
  ver=16
  for javadoc in bcmail bcpg bcprov bctsp; do
    %{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}/${javadoc}
    %{__cp} -pr ${javadoc}-jdk${ver}-%{version}/docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/${javadoc}
  done
popd
%else
pushd build/artifacts/jdk1.5
  ver=15
  for javadoc in bcmail bcpg bcprov bctsp; do
    %{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}/${javadoc}
    %{__cp} -pr ${javadoc}-jdk${ver}-%{version}/docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}/${javadoc}
  done
popd
%endif

%files
%doc *.html
# BEGIN PROVIDER
%{_javadir}/bcmail-%{version}.jar
%{_javadir}/bcpg-%{version}.jar
%{_javadir}/bctest-%{version}.jar
%{_javadir}/bctest.jar
%{_javadir}/bctsp-%{version}.jar
%{_javadir}/bcmail.jar
%{_javadir}/bcpg.jar
%{_javadir}/bctsp.jar
%{_javadir}/bcprov-%{version}.jar
%{_javadir}/bcprov.jar
# END PROVIDER

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt2_3jpp6
- fixed provides

* Tue Sep 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.46-alt1_3jpp6
- new jpp release

* Sat May 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.43-alt1_1jpp6
- new version

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.37-alt1_5jpp1.7
- converted from JPackage by jppimport script

