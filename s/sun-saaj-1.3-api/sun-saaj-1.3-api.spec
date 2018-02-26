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

%define saajver  1.3

Name:           sun-saaj-1.3-api
Version:        1.3
Release:        alt1_4jpp6
Epoch:          0
Summary:        SAAJ API 1.3
License:        CDDL
Url:            https://jax-ws-sources.dev.java.net/
Source0:        http://download.java.net/maven/1/javax.xml.soap/java-sources/saaj-api-1.3-sources.jar

Source1:        http://download.java.net/maven/1/javax.xml.soap/poms/saaj-api-1.3.pom
Source2:        CDDLv1.0.html
Source3:        sun-saaj-1.3-api-manifest.mf
Source4:        sun-saaj-1.3-api-build.properties
Source5:        sun-saaj-1.3-api-build.xml


Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: jaf_1_1_api
BuildRequires: geronimo-qname-1.1-api
Requires: jaf_1_1_api
Requires: geronimo-qname-1.1-api
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Provides:       saaj_api = 0:%{saajver}
Provides:       saaj_1_3_api = 0:%{version}-%{release}
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
The SOAP with Attachments API for Java (SAAJ) 1.3
according to JSR-67 MR3

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       saaj-javadoc = 0:%{saajver}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c 
mkdir -p src/java
mv javax src/java
cp %{SOURCE3} saaj.mf
cp %{SOURCE4} build.properties
cp %{SOURCE5} build.xml

%build
if [ -z "$JAVA_HOME" ]; then export JAVA_HOME=/usr/lib/jvm/java; fi
export CLASSPATH=$(build-classpath jaf_1_1_api qname_1_1_api)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=only release

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 saaj.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.xml.soap saaj-api %{saajver} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} 
touch saaj_1_3_api.jar
touch saaj_api.jar
ln -sf %{name}-%{version}.jar %{name}.jar)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -pm 644 %{SOURCE2} \
           $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/CDDLv1.0.html

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/saaj_1_3_api_sun-saaj-1.3-api<<EOF
%{_javadir}/saaj_1_3_api.jar	%{_javadir}/%{name}.jar	10300
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/saaj_api_sun-saaj-1.3-api<<EOF
%{_javadir}/saaj_api.jar	%{_javadir}/%{name}.jar	10300
EOF

%files
%_altdir/saaj_api_sun-saaj-1.3-api
%_altdir/saaj_1_3_api_sun-saaj-1.3-api
%{_docdir}/%{name}-%{version}/CDDLv1.0.html
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
%exclude %{_javadir}/saaj_1_3_api.jar
%exclude %{_javadir}/saaj_api.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp6
- jpp 6 release

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_3jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_2jpp5
- fixed repocop warnings

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_2jpp1.7
- updated to new jpackage release

* Sat Dec 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

