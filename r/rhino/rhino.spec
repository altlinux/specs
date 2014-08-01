Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define scm_version 1_7R4

Name:           rhino
# R3 doesn't mean a prerelease, but behind R there is a version of this implementation
# of Javascript version 1.7 (which is independent from this particular implementation,
# e.g., there is C++ implementation in Spidermonkey)
Version:        1.7R4
Release:        alt1_2jpp7
Summary:        JavaScript for Java
License:        MPLv2.0 

Source0:        https://github.com/mozilla/rhino/archive/Rhino%{scm_version}_RELEASE.zip
Source1:        http://repo1.maven.org/maven2/org/mozilla/rhino/%{version}/rhino-%{version}.pom
Source2:        %{name}.script

Patch0:         %{name}-build.patch
# Add OSGi metadata from Eclipse Orbit project
# Rip out of MANIFEST.MF included in this JAR:
# http://www.eclipse.org/downloads/download.php?r=1&file=/tools/orbit/downloads/drops/R20110523182458/repository/plugins/org.mozilla.javascript_1.7.2.v201005080400.jar
Patch1:         %{name}-addOrbitManifest.patch
Patch2:         %{name}-1.7R3-crosslink.patch

URL:            http://www.mozilla.org/rhino/
Group:          Development/Java

BuildRequires:  ant
Requires:       jpackage-utils
Requires:       jline

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
Summary:        Examples for %{name}
Group:          Development/Java

%description    demo
Examples for %{name}.

%package        manual

Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
Documentation for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildRequires:  java-javadoc
Requires:       java-javadoc
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-Rhino%{scm_version}_RELEASE
%patch0 -p1 -b .build
%patch1 -p1 -b .fixManifest
%patch2 -p1 -b .crosslink

# Fix build
sed -i -e '/.*<get.*src=.*>$/d' build.xml testsrc/build.xml \
       toolsrc/org/mozilla/javascript/tools/debugger/build.xml xmlimplsrc/build.xml

# Fix manifest
sed -i -e '/^Class-Path:.*$/d' src/manifest

# Add jpp release info to version
sed -i -e 's|^implementation.version: Rhino .* release .* \${implementation.date}|implementation.version: Rhino %{version} release %{release} \${implementation.date}|' build.properties

%build
ant deepclean jar copy-all javadoc -Dno-xmlbeans=1

pushd examples

export CLASSPATH=../build/%{name}%{scm_version}/js.jar:$(build-classpath xmlbeans/xbean 2>/dev/null)
%{javac} *.java
%{jar} cvf ../build/%{name}%{scm_version}/%{name}-examples.jar *.class
popd

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -a build/%{name}%{scm_version}/js.jar %{buildroot}%{_javadir}
ln -s js.jar %{buildroot}%{_javadir}/%{name}.jar
cp -a build/%{name}%{scm_version}/%{name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a build/%{name}%{scm_version}/javadoc/* %{buildroot}%{_javadocdir}/%{name}

## script
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}

# examples
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a examples/* %{buildroot}%{_datadir}/%{name}
find %{buildroot}%{_datadir}/%{name} -name '*.build' -delete

# POM and depmap
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "rhino:js"

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/%{name}.conf

%files
%attr(0755,root,root) %{_bindir}/*
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%config(noreplace,missingok) /etc/%{name}.conf

%files demo
%{_datadir}/%{name}

%files manual
%if 0
%doc build/%{name}%{scm_version}/docs/*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
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

