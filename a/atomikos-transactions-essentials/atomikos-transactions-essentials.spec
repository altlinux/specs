BuildRequires: geronimo-jta-1.0.1B-api
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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


Name:           atomikos-transactions-essentials
Version:        3.2.3
Release:        alt3_1jpp5
Epoch:          0
Summary:        Atomikos JTA/XA Kernel

Group:          Development/Java
License:        ASL 2.0
URL:            http://www.atomikos.com/Main/AtomikosCommunity
Source0:        http://www.atomikos-support.com/downloads/transactions-essentials/3.2.3/AtomikosTransactionsEssentials-3.2.3.zip
Source1:        atomikos-util-%{version}.pom
Source2:        transactions-%{version}.pom
Source3:        transactions-api-%{version}.pom
Source4:        transactions-jta-%{version}.pom

Patch0:         atomikos-transactions-essentials-build.patch
Patch1:		atomikos-transactions-essentials-alt-remove14suppot.patch



BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: ant-nodeps
BuildRequires: ant-trax
#BuildRequires: hibernate2
#BuildRequires: hibernate32
BuildRequires: j2ee_connector_1_5_api
BuildRequires: jms_1_1_api
BuildRequires: jta_1_0_1B_api
BuildRequires: junit
BuildRequires: servlet_2_3_api

Requires: j2ee_connector_1_5_api
Requires: jms_1_1_api
Requires: jta_1_0_1B_api
Requires: servlet_2_3_api

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
This is a free, open-source core subset of ExtremeTransactions(TM)
ideal for community purposes; only basic functionality is included.

%package        hibernate2
Summary:        Hibernate2 module for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: hibernate2

%description    hibernate2
%{summary}.

%package        hibernate3
Summary:        Hibernate3 module for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: hibernate3

%description    hibernate3
%{summary}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q -n AtomikosTransactionsEssentials-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav0
%patch1 -b .sav1 -p1

ln -sf $(build-classpath j2ee_connector_1_5_api) lib/jca.jar
#BUILD/AtomikosTransactionsEssentials-3.1.1/lib/jca.jar.no
#BUILD/AtomikosTransactionsEssentials-3.1.1/lib/jmx.jar.no
ln -sf $(build-classpath jms_1_1_api) lib/jms.jar
#BUILD/AtomikosTransactionsEssentials-3.1.1/lib/jms.jar.no
ln -sf $(build-classpath jta_1_0_1B_api) lib/jta.jar
#BUILD/AtomikosTransactionsEssentials-3.1.1/lib/jta.jar.no
mv lib/ojdbc14.jar.no lib/ojdbc14.jar
#BUILD/AtomikosTransactionsEssentials-3.1.1/lib/ojdbc14.jar.no
ln -sf $(build-classpath servlet_2_3_api) lib/servlet-2.3.jar
#BUILD/AtomikosTransactionsEssentials-3.1.1/lib/servlet-2.3.jar.no
#ln -sf $(build-classpath hibernate2) lib
####ln -sf $(build-classpath hibernate3) lib
#ln -sf $(build-classpath hibernate32) lib


# build w/o hibernate 2
rm sources/com/atomikos/icatch/imp/thread/Java14BackportExecutorFactory.java

%build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 


%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/atomikos
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 dist/atomikos-util.jar \
  $RPM_BUILD_ROOT%{_javadir}/atomikos/atomikos-util-%{version}.jar
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.atomikos-atomikos-util.pom
%add_to_maven_depmap com.atomikos atomikos-util %{version} JPP/atomikos atomikos-util

install -m 644 dist/transactions-api.jar \
  $RPM_BUILD_ROOT%{_javadir}/atomikos/transactions-api-%{version}.jar
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.atomikos-transactions-api.pom
%add_to_maven_depmap com.atomikos transactions-api %{version} JPP/atomikos transactions-api

#install -m 644 dist/transactions-hibernate2.jar \
#  $RPM_BUILD_ROOT%{_javadir}/atomikos/transactions-hibernate2-%{version}.jar
#install -m 644 dist/transactions-hibernate3.jar \
#  $RPM_BUILD_ROOT%{_javadir}/atomikos/transactions-hibernate3-%{version}.jar

install -m 644 dist/transactions.jar \
  $RPM_BUILD_ROOT%{_javadir}/atomikos/transactions-%{version}.jar
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.atomikos-transactions.pom
%add_to_maven_depmap com.atomikos transactions %{version} JPP/atomikos transactions

install -m 644 dist/transactions-jta.jar \
  $RPM_BUILD_ROOT%{_javadir}/atomikos/transactions-jta-%{version}.jar
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.atomikos-transactions-jta.pom
%add_to_maven_depmap com.atomikos transactions-jta %{version} JPP/atomikos transactions-jta

install -m 644 dist/transactions-essentials-all.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/atomikos && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%dir %{_javadir}/atomikos
%{_javadir}/atomikos/atomikos-util*.jar
%{_javadir}/atomikos/transactions-api*.jar
%{_javadir}/atomikos/transactions-jta*.jar
%{_javadir}/atomikos/transactions-%{version}.jar
%{_javadir}/atomikos/transactions.jar
%doc license.txt
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

#%files hibernate2
#%{_javadir}/atomikos/transactions-hibernate2*.jar

#%files hibernate3
#%{_javadir}/atomikos/transactions-hibernate3*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Sun Feb 06 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2.3-alt3_1jpp5
- build without hibernate

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.3-alt2_1jpp5
- selected java5 compiler explicitly

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.2.3-alt1_1jpp5
- first build

