Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

%define staxver  1.0

Name:           sun-stax-1.0-api
Version:        1.0.2
Release:        alt1_1jpp5
Epoch:          0
Summary:        Streaming API for XML (StAX) 1.0 API
License:        CDDL
Url:            http://stax.codehaus.org/
Source0:        http://download.java.net/maven/1/javax.xml.stream/java-sources/stax-api-1.0-2-sources.jar

Source1:        http://download.java.net/maven/1/javax.xml.stream/poms/stax-api-1.0-2.pom
Source2:        CDDLv1.0.html
Source3:        sun-stax-1.0-api-build.properties
Source4:        sun-stax-1.0-api-build.xml

Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: geronimo-qname-1.1-api
Requires: geronimo-qname-1.1-api
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Provides:       stax_api = 0:%{staxver}
Provides:       stax_1_0_api = 0:%{version}-%{release}

%description
The Streaming API for XML (StAX) 1.0 API
according to JSR-173

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       stax-javadoc = 0:%{staxver}

%description javadoc
%{summary}.

%prep
%setup -q -c 
mv src osrc
mkdir src
mv osrc src/java
cp %{SOURCE3} build.properties
cp %{SOURCE4} build.xml

%build
if [ -z "$JAVA_HOME" ]; then export JAVA_HOME=/usr/lib/jvm/java; fi
export CLASSPATH=$(build-classpath qname_1_1_api)
ant -Dbuild.sysclasspath=only release

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 stax.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.xml.stream stax-api 1.0-2 JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} 
ln -s %{name}-%{version}.jar stax_1_0_api.jar
ln -s %{name}-%{version}.jar stax_api.jar
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
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/stax_1_0_api_%{name}<<EOF
%{_javadir}/stax_1_0_api.jar	%{_javadir}/%{name}.jar	10000
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/stax_api_%{name}<<EOF
%{_javadir}/stax_api.jar	%{_javadir}/%{name}.jar	10000
EOF

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi


%files
%_altdir/stax_api_%{name}
%_altdir/stax_1_0_api_%{name}
%{_docdir}/%{name}-%{version}/CDDLv1.0.html
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
%exclude %{_javadir}/stax_1_0_api.jar
%exclude %{_javadir}/stax_api.jar
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_1jpp5
- fixed repocop warnings

* Sat Dec 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

