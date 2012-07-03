Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: xsltproc
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
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


Name:           sisc
Version:        1.16.6
Release:        alt2_1jpp5
Epoch:          0
Summary:        Second Interpreter of Scheme Code

Group:          Development/Java
License:        GPL, MPL 1.1
URL:            http://sisc-scheme.org/
Source0:        http://prdownloads.sourceforge.net/sisc/sisc-1.16.6.jar


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: docbook-style-xsl
BuildRequires: libxslt


Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
SISC is an extensible Java based interpreter of the 
algorithmic language Scheme. SISC uses modern interpretation
techniques, and handily outperforms all existing Java 
interpreters (often by more than an order of magnitude).

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.


%prep
%setup -q -c
for j in $(find modules/lib -name "*.jar"); do
    mv $j $j.no
done

%build
cd %{name}
ant -Ddoc.style=%{_datadir}/sgml/docbook/xsl-stylesheets/html/chunk.xsl

%install
cd %{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 sisc.shp $RPM_BUILD_ROOT%{_datadir}/%{name}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 %{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{name}-heap.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-heap-%{version}.jar
install -m 644 %{name}-lib.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-lib-%{version}.jar
install -m 644 %{name}-opt.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-opt-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/generated/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%doc sisc/LICENSE.txt
%{_datadir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Thu Aug 06 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.16.6-alt2_1jpp5
- fixed build

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.16.6-alt1_1jpp5
- new version

