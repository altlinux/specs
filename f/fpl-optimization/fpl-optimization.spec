Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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

Name:           fpl-optimization
Version:        2005.8.8
Release:        alt1_1jpp6
Summary:        Nonlinear Optimization Java Package

Group:          Development/Java
License:        Public Domain
URL:            http://www1.fpl.fs.fed.us/optimization.html

Source0:        ftp://www1.fpl.fs.fed.us/pub/optim/src.tar.Z

BuildRequires: ant >= 1.6.5
BuildRequires: jpackage-utils >= 0:5.0.0

Requires: jpackage-utils >= 0:5.0.0

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
Currently (as of 8/8/05) this package contains Java 
translations of the 1-dimensional minimization routine, 
fmin, the multi-dimensional minimization routine Uncmin, 
the MINPACK nonlinear least squares routines (lmder1, 
lmder, lmdif1, and lmdif), and the SLATEC 1-dimensional 
zero-finding routine, dfzero. Eventually, the package will 
also contain Java translations of some of the MINPACK 
nonlinear equation solvers. 

%package javadoc 
Summary:        Javadocs for %{name} 
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description javadoc 
%{summary}. 

%prep
%setup -c -q 
mkdir -p src/optimization
mv *.java src/optimization
rm *.class
mkdir classes
mkdir apidocs

%build
javac -d classes src/optimization/*java
pushd classes
jar cf ../%{name}.jar *
popd
javadoc -d apidocs -sourcepath src corejava linear_algebra optimization

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# javadoc 
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__cp -a apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%files
%doc copyright disclaimer README
%{_javadir}/*.jar

%files javadoc 
%{_javadocdir}/%{name}-%{version} 
%{_javadocdir}/%{name} 

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 2005.8.8-alt1_1jpp6
- new version

