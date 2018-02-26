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

Summary:		Java 3D
URL:			https://java3d.dev.java.net/
Name:			java3d
License:		GPL
Group:			Development/Java
Version:		1.5.2
Release:		alt2_1jpp6

BuildArch:      noarch

# cvs -d :pserver:guest@cvs.dev.java.net:/cvs login
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r rel-1_5_2-fcs vecmath-test
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r rel-1_5_2-fcs vecmath
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r rel-1_5_2-fcs j3d-optional-utils
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r rel-1_5_2-fcs j3d-examples
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r rel-1_5_2-fcs j3d-core-utils
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r rel-1_5_2-fcs j3d-core
# tar czf ../SOURCES/java3d-1.5.2.tgz j3d-core j3d-core-utils j3d-examples j3d-optional-utils  vecmath vecmath-test
Source0:		java3d-%{version}.tgz

BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: jpackage-utils >= 0:5.0.0


%description
The Java 3D API provides a set of object-oriented interfaces that
support a simple, high-level programming model you can use to
build, render, and control the behavior of 3D objects and visual
environments. With the Java 3D API, you can incorporate high quality,
scalable, platform-independent 3D graphics into applications andvecmath
applets based on Java technology.

%package javadoc
Summary:	Javadoc for java3d
Group:		Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c -n %{name}

%build
pushd vecmath
	%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dant.javadoc.maxmemory=512m jar-opt
popd

pushd j3d-core
	# to avoid Out of heap memory on "small" machines ...
	export ANT_OPTS=-Xmx256m
	%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dant.javadoc.maxmemory=512m \
		-Dbuild.type=stable \
		jar-opt docs-public
popd

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true

%__install -dm 755 %{buildroot}%{_javadir}/%{name}
%__install -dm 755 %{buildroot}%{_libdir}
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}

# jars
%__install -m 644 vecmath/build/opt/lib/ext/vecmath.jar \
		%{buildroot}%{_javadir}/%{name}
%__install -m 644 j3d-core/build/default/opt/lib/ext/*.jar \
		%{buildroot}%{_javadir}/%{name}

## libs
#%__install -m 644 j3d-core/build/default/opt/native/*.so \
#		%{buildroot}%{_libdir}

# javadoc
%__cp -a j3d-core/build/*/javadocs/docs-public/* \
		%{buildroot}%{_javadocdir}/%{name}-%{version}

ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink


%files
%doc j3d-core/*.txt
%doc j3d-core/*.html
%doc j3d-core/docs
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
#%{_libdir}/lib*.so

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt2_1jpp6
- built with java 6 due to com.sun.image.codec.jpeg

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1jpp6
- new version

