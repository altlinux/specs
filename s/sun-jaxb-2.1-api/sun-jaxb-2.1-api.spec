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

%define gcj_support 0

%define jaxbver  2.1

Name:           sun-jaxb-2.1-api
Version:        2.1
Release:	alt3_5jpp6
Epoch:          0
Summary:        Java API for XML Web Services API
License:        CDDL
Url:            https://jax-ws-sources.dev.java.net/
Source0:        http://download.java.net/maven/1/javax.xml.bind/jars/jaxb-api-2.1-sources.jar

Source1:        http://download.java.net/maven/1/javax.xml.bind/poms/jaxb-api-2.1.pom
Source2:        CDDLv1.0.html
Source3:        sun-jaxb-2.1-api-manifest.mf
Source4:        sun-jaxb-2.1-api-build.properties
Source5:        sun-jaxb-2.1-api-build.xml

Group:          Development/Java
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  jaf_1_1_api
BuildRequires:  stax_1_0_api
Requires:  jaf_1_1_api
Requires:  stax_1_0_api
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:    java-gcj-compat-devel
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Provides:       jaxb_api = 0:%{jaxbver}
Provides:       jaxb_2_1_api = 0:%{version}-%{release}
Source44: import.info

%description
The Java Architecture for XML Binding (JAXB) 2.1 API
according to JSR-222 MR1

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jaxb-javadoc = 0:%{jaxbver}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c 
mkdir -p src/java
mv javax src/java
cp %{SOURCE3} jaxb.mf
cp %{SOURCE4} build.properties
cp %{SOURCE5} build.xml

%build
export CLASSPATH=$(build-classpath jaf_1_1_api stax_1_0_api)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only release

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 jaxb.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.xml.bind jaxb-api %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} && ln -sf %{name}-%{version}.jar %{name}.jar)
touch $RPM_BUILD_ROOT%{_javadir}/jaxb_2_1_api.jar
touch $RPM_BUILD_ROOT%{_javadir}/jaxb_api.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -pm 644 %{SOURCE2} \
           $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/CDDLv1.0.html

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_2_1_api_sun-jaxb-2.1-api<<EOF
%{_javadir}/jaxb_2_1_api.jar	%{_javadir}/%{name}.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxb_api_sun-jaxb-2.1-api<<EOF
%{_javadir}/jaxb_api.jar	%{_javadir}/%{name}.jar	20100
EOF

%files
%_altdir/jaxb_api_sun-jaxb-2.1-api
%_altdir/jaxb_2_1_api_sun-jaxb-2.1-api
%{_docdir}/%{name}-%{version}/CDDLv1.0.html
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
%exclude %{_javadir}/jaxb_2_1_api.jar
%exclude %{_javadir}/jaxb_api.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_5jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_4jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_4jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_4jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Fri Jan 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp5.0
- first build

