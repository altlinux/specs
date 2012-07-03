Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:           doctypechanger
Version:        1.1
Release:	alt1_2jpp6
Epoch:          0
Summary:        Modifies DOCTYPE declaration from a byte stream as it is fed into an XML parser
Group:          Development/Java
License:        ASL 1.1
URL:            http://doctypechanger.sourceforge.net/
Source0:        http://download.sourceforge.net/project/doctypechanger/doctypechanger/1.1/DoctypeChanger-1.1-src.tar.gz
Source1:        http://repository.jboss.org/maven2/net/socialchange/doctype/doctype-changer/1.1/doctype-changer-1.1.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant
BuildRequires: jpackage-utils
Provides:       DoctypeChanger = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description
DoctypeChanger is a Java class that lets you add, modify or remove a DOCTYPE
declaration from a byte stream as it is fed into an XML parser. 

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for DoctypeChanger
Provides:       DoctypeChanger-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
Javadoc for DoctypeChanger.

%prep
%setup -q -n DoctypeChanger-%{version}-src
%{__perl} -pi -e 's/^Class-Path:.*\n$//g' src/etc/Manifest.mf
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%{ant} -Dbuild.sysclasspath=only -Dno.ctags=true jar javadocs docs

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p build/DoctypeChanger.jar %{buildroot}/%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}/%{_javadir}/DoctypeChanger-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.socialchange.doctype doctype-changer %{version} JPP %{name}

# javadocs
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/DoctypeChanger-%{version}
%{__ln_s} DoctypeChanger-%{version} %{buildroot}%{_javadocdir}/DoctypeChanger

%files
%doc PROJECT.txt src/etc/licenses/LICENSE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/DoctypeChanger-%{version}.jar
%{_javadir}/DoctypeChanger.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/DoctypeChanger-%{version}
%{_javadocdir}/DoctypeChanger

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp6
- new version

