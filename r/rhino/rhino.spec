Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: perl(Getopt/Mixed.pm)
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define scm_version 1_7_7_1

Name:           rhino
Version:        1.7.7.1
Release:        alt1_1jpp8
Summary:        JavaScript for Java
License:        MPLv2.0

Source0:        https://github.com/mozilla/rhino/archive/Rhino%{scm_version}_RELEASE.tar.gz
Source1:        http://repo1.maven.org/maven2/org/mozilla/rhino/%{version}/rhino-%{version}.pom
Source2:        %{name}.script

Patch0:         %{name}-build.patch
# Add OSGi metadata from Eclipse Orbit project
Patch1:         %{name}-addOrbitManifest.patch

URL:            http://www.mozilla.org/rhino/

BuildRequires:  ant
BuildRequires:  java-devel >= 1.6.0.0
BuildRequires:  sonatype-oss-parent
BuildRequires:  javapackages-local
Requires:       jline
Obsoletes:      %{name}-javadoc < %{version}-%{release}
Obsoletes:      %{name}-manual < %{version}-%{release}

# Disable xmlbeans until we can get it into Fedora
#Requires:       xmlbeans
#BuildRequires:  xmlbeans
BuildArch:      noarch
Source44: import.info

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%package        demo
Group: Development/Java
Summary:        Examples for %{name}

%description    demo
Examples for %{name}.

%prep
%setup -q -n %{name}-Rhino%{scm_version}_RELEASE
%patch0 -p1 -b .build
%patch1 -b .fixManifest

# Fix manifest
sed -i -e '/^Class-Path:.*$/d' src/manifest

# Add jpp release info to version
sed -i -e 's|^implementation.version: Rhino .* release .* \${implementation.date}|implementation.version: Rhino %{version} release %{release} \${implementation.date}|' build.properties

%mvn_alias : rhino:js
%mvn_file : js %{name}

%build
ant deepclean jar copy-all -Dno-xmlbeans=1
%mvn_artifact %{SOURCE1} build/%{name}%{version}/js.jar

pushd examples

export CLASSPATH=../build/%{name}%{version}/js.jar:$(build-classpath xmlbeans/xbean 2>/dev/null)
%{javac} *.java
%{jar} cf ../build/%{name}%{version}/%{name}-examples.jar *.class
popd

%install
%mvn_install

# man page
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

## script
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}

# examples
cp -a build/%{name}%{version}/%{name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a examples/* %{buildroot}%{_datadir}/%{name}
find %{buildroot}%{_datadir}/%{name} -name '*.build' -delete

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files -f .mfiles
%attr(0755,root,root) %{_bindir}/*
%{_javadir}/*
%{_mandir}/man1/%{name}.1*
%config(noreplace,missingok) /etc/%{name}.conf

%files demo
%{_datadir}/%{name}

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7.7.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7.7-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7.7-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7R4-alt1_6jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7R4-alt1_2jpp7
- new version

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7R3-alt1_9jpp7
- update

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7R3-alt1_6jpp7
- R3

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_1.r2.8jpp6
- updated OSGi manifest

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1.r2.8jpp6
- added repolib

* Sun Feb 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1.r2.6jpp5
- rev. 2.6

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1.r2.3jpp5
- converted from JPackage by jppimport script

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_0.r2.2jpp1.7
- converted from JPackage by jppimport script

