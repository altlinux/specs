BuildRequires: concurrent
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


Name:           colt
Version:        1.2.0
Release:        alt1_5jpp6
Epoch:          0
Summary:        Open-source libraries for high-performance scientific and technical computing
License:        X11-like
Source0:        http://dsd.lbl.gov/~hoschek/colt-download/releases/colt-1.2.0.tar.gz
Source1:        %{name}-%{version}.build.xml
URL:            http://dsd.lbl.gov/~hoschek/colt/
Group:          Development/Java
BuildArch:      noarch
Requires:       concurrent >= 0:1.3.4 corejava-format
BuildRequires:  concurrent >= 0:1.3.4 corejava-format
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7
BuildRequires:  /bin/bash
Source44: import.info

%description
Colt provides a set of open-source libraries for high-performance scientific
and technical computing in Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package -n colt-hep
Summary:        Compact, extensible, modular and performant histogramming functionality
License:        LGPL (but usage related to military applications is expressly forbidden)
Group:          Development/Java
Requires:       colt >= 0:1.2.0

%description -n colt-hep
Compact, extensible, modular and performant histogramming functionality,
from the COLT distribution.

%package -n colt-hep-javadoc
Summary:        Javadoc for colt-hep
Group:          Development/Documentation

%description -n colt-hep-javadoc
Javadoc for colt-hep.

%prep
%setup -c -q
mv colt/* .
cp %{SOURCE1} build.xml

%build
export CLASSPATH=%(build-classpath corejava-format concurrent)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  -Dconcurrent.apiurl=%{_javadocdir}/concurrent \
  -Dcorejava-format.apiurl=%{_javadocdir}/corejava-format \
  jars javadoc

%install
rm -fr $RPM_BUILD_ROOT

# COLT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs-colt/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# HEP
install -m 644 colt-hep-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
ln -s colt-hep-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/colt-hep.jar
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/colt-hep-%{version}
cp -pr docs-colt-hep/* $RPM_BUILD_ROOT%{_javadocdir}/colt-hep-%{version}
ln -s colt-hep-%{version} $RPM_BUILD_ROOT%{_javadocdir}/colt-hep # ghost symlink

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files -n colt-hep
%{_javadir}/colt-hep-%{version}.jar
%{_javadir}/colt-hep.jar

%files -n colt-hep-javadoc
%doc %{_javadocdir}/colt-hep-%{version}
%ghost %doc %{_javadocdir}/colt-hep

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_5jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_4jpp5
- new jpackage release

* Wed Oct 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

