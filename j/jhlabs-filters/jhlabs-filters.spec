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

Name:           jhlabs-filters
Version:        2.0
Release:        alt1_1jpp6
Summary:        Java Image Filters

Group:          Development/Java
License:        Apache License 2.0
URL:            http://www.jhlabs.com/ip/index.html
Source0:        http://www.jhlabs.com/ip/filters/Filters.zip
Patch0:         jhlabs-filters-build.patch
BuildArch:      noarch

BuildRequires: jpackage-utils >= 0:5.0.0
BuildRequires: ant

Requires: jpackage-utils >= 0:5.0.0

%description
A large collection of Java2D image filters, including blur,
emboss, lighting effects and texturing. 

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Java
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c %{name}-%{version}
%patch0 -b .orig

%build
%{ant} jar javadoc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir} \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

install -m 644 dist/Filters.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp -pr api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp6
- new version

