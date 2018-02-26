Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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


Name:           jdemo
Version:        1.6.0
Release:	alt2_1jpp6
Epoch:          0
Summary:        Java to Html converter
Group:          Development/Java
License:        CPL1.0
URL:            http://www.jdemo.de
Source0:        jdemo-1.6.0.tgz
# cvs -d:pserver:anonymous@jdemo.cvs.sourceforge.net:/cvsroot/jdemo login
# cvs -z3 -d:pserver:anonymous@jdemo.cvs.sourceforge.net:/cvsroot/jdemo export -r jdemo_release_2008-02-27_version_1-6-0 JDemo
# cvs -z3 -d:pserver:anonymous@jdemo.cvs.sourceforge.net:/cvsroot/jdemo export -r jdemo_release_2008-02-27_version_1-6-0 JDemo_swingrunner
# cvs -z3 -d:pserver:anonymous@jdemo.cvs.sourceforge.net:/cvsroot/jdemo export -r jdemo_release_2008-02-27_version_1-6-0 JDemo_thirdparty 
# cvs -z3 -d:pserver:anonymous@jdemo.cvs.sourceforge.net:/cvsroot/jdemo export -r jdemo_release_2008-02-27_version_1-6-0 JDemo_imageprocessing
# cvs -z3 -d:pserver:anonymous@jdemo.cvs.sourceforge.net:/cvsroot/jdemo export -r jdemo_release_2008-02-27_version_1-6-0 JDemo_examples
# tar czf ../SOURCES/jdemo-1.6.0.tgz JDemo/ JDemo_build/ JDemo_swingrunner/ JDemo_thirdparty/ JDemo_imageprocessing JDemo_examples
Patch0:         jdemo-build.patch


BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7
BuildRequires: ant-junit
BuildRequires: junit4
BuildRequires: eclipse-swt
BuildRequires: proguard

BuildArch:      noarch
Source44: import.info

%description
JDemo is the Java demonstration framework. Its concept is
similar to the one of JUnit.
As supplement to test driven software development, JDemo
provides a new approach of demo driven development: When
developing software, you write short code snippets (demo
cases) that use your new API. The demo then demonstrates
both: how to use the API and what happens when you execute
the code. So you can for example interactively test the
usability of GUI components.
JDemo has a lot of convenience classes and methods that
make implementing those demos very easy. The demos can then
be launched from a Swing application called Demo Runner.
Demos can also be used for automatically taking screenshots
for documentation purposes.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep 
%setup -q -c
%patch0 -b .sav0
for j in $(find JDemo_thirdparty -name "*.jar"); do
    mv $j $j.no
done
ln -s $(build-classpath ant) JDemo_thirdparty/ant.jar
#JDemo_thirdparty/junit-4.4-src.jar
#JDemo_thirdparty/drop-in/java2html.jar
PKG=
if [ -d /usr/lib/eclipse/ ]; then
PKG=$(find /usr/lib/eclipse/ -name "org.eclipse.swt.gtk.linux*.jar" | grep -v source)
fi
if [ -z $PKG ]; then
if [ -d /usr/lib64/eclipse/ ]; then
PKG=$(find /usr/lib64/eclipse/ -name "org.eclipse.swt.gtk.linux*.jar" | grep -v source)
fi
fi
if [ -z $PKG ]; then
if [ -d /usr/share/eclipse/ ]; then
PKG=$(find /usr/share/eclipse/ -name "org.eclipse.swt.gtk.linux*.jar" | grep -v source)
fi
fi
ln -s ${PKG} JDemo_thirdparty/swt.jar
ln -s $(build-classpath proguard/proguard) JDemo_thirdparty/proguard.jar
ln -s $(build-classpath junit4) JDemo_thirdparty/junit.jar

%build
cd JDemo_build
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
	-Drt.jar.jdk.path=%{java_home}/jre/lib/rt.jar \
	-Djavac.jdk.path=%{java_home}/bin/javac \
	-Djava.jdk.path=%{java_home}/bin/java

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -m 644 JDemo_build/dist/%{name}.jar \
           %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -m 644 JDemo_build/dist/%{name}_core.jar \
           %{buildroot}%{_javadir}/%{name}_core-%{version}.jar
install -m 644 JDemo_build/dist/%{name}_runner.jar \
           %{buildroot}%{_javadir}/%{name}_runner-%{version}.jar
install -m 644 JDemo_build/dist/%{name}_runner_pre.jar \
           %{buildroot}%{_javadir}/%{name}_runner_pre-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
ln -s ${jar} ${jar/-%{version}/}; done)

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr JDemo_build/tmp/doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}*.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt2_1jpp6
- built with java 6

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt1_1jpp6
- new version

