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


Name:           org.osgi.enterprise
Version:        4.2.0
Release:        alt1_2jpp6
Epoch:          0
Summary:        OSGi Enterprise library
License:        Apache Software License 2.0
Url:            http://www.osgi.org
Source0:        http://repo1.maven.org/maven2/org/osgi/org.osgi.enterprise/4.2.0/org.osgi.enterprise-4.2.0-sources.jar
Source1:        http://repo1.maven.org/maven2/org/osgi/org.osgi.enterprise/4.2.0/org.osgi.enterprise-4.2.0.pom
Group:          Development/Java
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  org.osgi.core = 0:4.2.0
BuildRequires:  jpa_3_0_api
BuildRequires:  servlet_2_5_api
BuildArch:      noarch
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:  org.osgi.core = 0:4.2.0
Requires:  jpa_3_0_api
Requires:  servlet_2_5_api
Source44: import.info

%description
OSGi enterprise library.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
mkdir src
mv org src

%build
export JAVA_HOME=%{java_home}
export PATH=%{java_home}/bin:$PATH
export CLASSPATH=$(build-classpath org.osgi.core jpa_3_0_api servlet_2_5_api)
cd src
%javac -source 5 `find . -name \*.java`
%javadoc -source 5 -d ../apidocs `find . -name \*.java`

%install

# jar
export JAVA_HOME=%{java_home}
%__mkdir_p %{buildroot}%{_datadir}/maven2/poms
%__cp -a %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.osgi %{name} %{version} JPP %{name}

cd src
%__mkdir_p %{buildroot}%{_javadir}
%jar cvmf /dev/null %{name}.jar -C . org/
%__cp -a %{name}.jar \
%{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a ../apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && %__ln_s %{name}-%{version} %{name})


%files
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/*

%changelog
* Thu Feb 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.0-alt1_2jpp6
- new version

