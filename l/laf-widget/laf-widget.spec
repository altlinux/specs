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

Name:           laf-widget
Version:        4.3
Release:        alt1_1jpp6
Summary:        Support for common "feel" widgets in look-and-feel libraries

Group:          Development/Java
License:        BSD and zlib
URL:            https://laf-widget.dev.java.net/
Source0:        https://laf-widget.dev.java.net/files/documents/5097/135952/laf-widget-all.zip
Patch0:         laf-widget-build.patch

BuildArch:      noarch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant >= 0:1.7.1
BuildRequires: asm2

Requires: jpackage-utils >= 0:5.0.0
Requires: asm2

%description
The goal of this project is to provide support for and base
set of additional behaviour and widgets in look-and-feels. 

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c %{name}-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

ln -s %{_javadir}/asm2-all.jar lib/asm-all-2.2.2.jar

%build
%{ant} -Djdk.home=%{_jvmdir}/java all javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

install -m644 drop/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp -pr api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cd $RPM_BUILD_ROOT%{_javadocdir}
ln -s %{name}-%{version} %{name}

%files
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1_1jpp6
- new version

