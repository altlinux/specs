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

# Use rpmbuild --without gcj to disable gcj bits
%define with_gcj %{?_with_gcj:1}%{!?_with_gcj:0}

Name:           visad
Version:        2.0
Release:        alt3_0.20020925.1jpp6
Summary:        Visualization and analysis of numerical data

Group:          Development/Java
License:        LGPL
URL:            http://www.ssec.wisc.edu/~billh/visad.html
Source0:        http://sourceforge.net/projects/visad/files/VisAD%%20Source%%20files/2.0%%20_%%202002%%20Sep%%2025/visad_src-2.0-20020925.jar
Source1:        %%{name}-%%{version}.pom

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant
BuildRequires: java3d
Requires: java3d

%if %{with_gcj}
BuildRequires: java-gcj-compat-devel >= 1.0.31
Requires(post): java-gcj-compat >= 1.0.31
Requires(postun): java-gcj-compat >= 1.0.31
%else
BuildArch:      noarch
%endif
Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0


%description
VisAD is a Java component library for interactive and 
collaborative visualization and analysis of numerical data. 


%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q -c -T
mkdir -p build/classes
mkdir src
cd src
unzip -qq %{SOURCE0}


%build
export CLASSPATH=$(build-classpath \
java3d/j3dcore \
java3d/j3dutils \
java3d/vecmath \
)
javac -J-Xmx256m -J-Xms256m -source 1.4 -d build/classes $(find src -name "*.java")
pushd build/classes
jar cf ../visad.jar * 
popd
javadoc -J-Xmx256m -J-Xms256m -source 1.4 -d  build/api $(find src -name "*.java")

%install
install -d $RPM_BUILD_ROOT%{_javadir} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
install -m 644 build/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -pr build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap net.java.dev.swing-layout %{name} %{version} JPP %{name}

%if %{with_gcj}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/%{name}*.jar
%if %{with_gcj}
%{_libdir}/gcj/%{name}
%endif
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_0.20020925.1jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Wed Oct 12 2011 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_0.20020925.1jpp6
- added -J-Xmx -J-Xms to fix 586 build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_0.20020925.1jpp6
- new version

