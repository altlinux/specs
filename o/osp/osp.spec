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

Name:           osp
Version:        1.2
Release:        alt2_1jpp6
Summary:        Open Source Physics Core Library

Group:          Development/Java
License:        GPL v2
URL:            http://www.compadre.org/osp/

Source0:        http://www.opensourcephysics.org/download/1.2/osp_core.zip
Source1:        osp-core-build.xml


BuildRequires: ant >= 0:1.7.1
BuildRequires: jpackage-utils >= 0:5.0.0

Requires: jpackage-utils >= 0:5.0.0

Requires(post): jpackage-utils >= 0:5.0.0
Requires(postun): jpackage-utils >= 0:5.0.0

BuildArch:      noarch

%description
Open Source Physics core library.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils >= 0:5.0.0
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
mkdir build
cp %{SOURCE1} build/build.xml

%build
export LANG=en_US.ISO8859-1
cd build
%ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jarfile docs


%install
%__rm -rf %{buildroot}

# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 build/build/jar/osp.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar

(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}
%__cp -a build/docs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_1jpp6
- fixed build with java 7

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1jpp6
- new version

