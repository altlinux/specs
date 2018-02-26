BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
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

%define wsmdver  2.0

Name:           sun-ws-metadata-2.0-api
Version:        1.0.MR1
Release:        alt3_3jpp6
Epoch:          0
Summary:        Web Services Metadata 2.0 MR API
License:        CDDL
Group:          Development/Java
URL:            https://jsr250.dev.java.net/
Source0:        http://download.java.net/maven/1/javax.jws/java-sources/jsr181-api-1.0-MR1-sources.jar
Source1:        http://download.java.net/maven/1/javax.jws/poms/jsr181-api-1.0-MR1.pom
Source2:        CDDLv1.0.html
Source3:        sun-ws-metadata-2.0-api-build.properties
Source4:        sun-ws-metadata-2.0-api-build.xml
Provides:       ws_metadata_api = 0:%{wsmdver}
Provides:       ws_metadata_2_0_api = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires(post): alternatives
Requires(preun): alternatives
Requires:       jpackage-utils
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  jpackage-utils >= 0:1.7.3
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
Web Services Metadata for the Java Platform 2.0 Maintenance Release
according to JSR-181.
This is JSR-181 MR1 in fact, which changed its version from 1.0 to 2.0.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
# FIXME: (dwalluck): needs symlink
Provides:       ws-metadata-javadoc = 0:%{wsmdver}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c 
mkdir -p src/java
mv javax src/java
cp -p %{SOURCE2} .
cp -p %{SOURCE3} build.properties
cp -p %{SOURCE4} build.xml

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 release

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 jws.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.jws jsr181-api %{version} JPP %{name}

(cd %{buildroot}%{_javadir} 
ln -s %{name}-%{version}.jar ws_metadata_2_0_api.jar
ln -s %{name}-%{version}.jar ws_metadata_api.jar
ln -s %{name}-%{version}.jar %{name}.jar)

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ws_metadata_2_0_api_sun-ws-metadata-2.0-api<<EOF
%{_javadir}/ws_metadata_2_0_api.jar	%{_javadir}/%{name}.jar	20000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/ws_metadata_api_sun-ws-metadata-2.0-api<<EOF
%{_javadir}/ws_metadata_api.jar	%{_javadir}/%{name}.jar	20000
EOF

%files
%_altdir/ws_metadata_api_sun-ws-metadata-2.0-api
%_altdir/ws_metadata_2_0_api_sun-ws-metadata-2.0-api
%doc CDDLv1.0.html
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%exclude %{_javadir}/ws_metadata_2_0_api.jar
%exclude %{_javadir}/ws_metadata_api.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif


%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.MR1-alt3_3jpp6
- new jpp relase

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.MR1-alt3_2jpp5
- fixes for java6 support

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.MR1-alt2_2jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.MR1-alt1_2jpp5
- fixed repocop warnings

* Fri Jan 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.MR1-alt1_1jpp5.0
- first build

