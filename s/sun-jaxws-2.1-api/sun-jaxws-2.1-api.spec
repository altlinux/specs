Requires: sun-ws-metadata-2.0-api sun-annotation-1.0-api
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define jaxwsver 2.1

Name:           sun-jaxws-2.1-api
Version:        2.1
Release:        alt4_3jpp6
Epoch:          0
Summary:        Java API for XML Web Services API
License:        CDDL
Group:          Development/Java
URL:            https://jax-ws-sources.dev.java.net/
Source0:        http://download.java.net/maven/1/javax.xml.ws/java-sources/jaxws-api-2.1-sources.jar
Source1:        http://download.java.net/maven/1/javax.xml.ws/poms/jaxws-api-2.1.pom
Source2:        CDDLv1.0.html
Source3:        sun-jaxws-2.1-api-manifest.mf
Source4:        sun-jaxws-2.1-api-build.properties
Source5:        sun-jaxws-2.1-api-build.xml
Provides:       jaxws_api = %{epoch}:%{jaxwsver}
Provides:       jaxws_2_1_api = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires(post): alternatives
Requires(preun): alternatives
Requires:       annotation_1_0_api
Requires:       jpackage-utils
Requires:       jaxb_2_1_api
Requires:       jpackage-utils
Requires:       saaj_1_3_api
Requires:       stax_1_0_api
Requires:       ws_metadata_2_0_api
BuildRequires:  annotation_1_0_api
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  jaxb_2_1_api
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  saaj_1_3_api
BuildRequires:  stax_1_0_api
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
The Java API for XML-Based Web Services (JAX-WS) 2.1 
according to JSR-224 MR2.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
# FIXME: (dwalluck): this needs an alternative to %%{_javadocdir}/jaxws_2_1_api then
Provides:       jaxws-javadoc = 0:%{jaxwsver}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c 
mkdir -p src/java
mv javax src/java
cp -p %{SOURCE2} CDDLv1.0.html
cp -p %{SOURCE3} jaxws.mf
cp -p %{SOURCE4} build.properties
cp -p %{SOURCE5} build.xml

%build
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath jaxb_2_1_api saaj_1_3_api stax_1_0_api)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only release

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 jaxws.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.xml.ws jaxws-api %{jaxwsver} JPP %{name}

(cd %{buildroot}%{_javadir} 
/bin/touch jaxws_2_1_api.jar
/bin/touch jaxws_api.jar
ln -s %{name}-%{version}.jar %{name}.jar)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxws_2_1_api_sun-jaxws-2.1-api<<EOF
%{_javadir}/jaxws_2_1_api.jar	%{_javadir}/%{name}.jar	20100
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaxws_api_sun-jaxws-2.1-api<<EOF
%{_javadir}/jaxws_api.jar	%{_javadir}/%{name}.jar	20100
EOF

%files
%_altdir/jaxws_api_sun-jaxws-2.1-api
%_altdir/jaxws_2_1_api_sun-jaxws-2.1-api
%doc CDDLv1.0.html
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%exclude %{_javadir}/jaxws_2_1_api.jar
%exclude %{_javadir}/jaxws_api.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif


%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_3jpp6
- new release

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_2jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_2jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_2jpp5
- alternatives 0.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_2jpp5
- converted from JPackage by jppimport script

* Fri Jan 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp5.0
- first build

