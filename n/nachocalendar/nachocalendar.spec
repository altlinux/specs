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

Name:           nachocalendar
Version:        0.23
Release:        alt1_4jpp6
Summary:        Provides a flexible Calendar component to the Java Platform
Group:          Development/Java
License:        LGPLv2+
URL:            http://nachocalendar.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires: jpackage-utils >= 5.0.0
BuildRequires: ant
Requires: jpackage-utils >= 5.0.0

%description
Provide a flexible Calendar component to the Java Platform.
Currently is under early development but can be used safely. It comes with
conventient factory classes, providing a fast and easy way to start using
them.


%package javadoc
Summary:           Javadocs for nachocalendar
Group:             Development/Java
Requires: %name = %{version}-%{release}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
NachoCalendar development documentation.


%prep
%setup -q # -n %{name}-%{version}

rm -rf doc lib/*


%build
ant clean jar javadoc

%install

# jar
install -d $RPM_BUILD_ROOT%{_javadir}/
install -m644 lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc LICENSE.txt CHANGELOG.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*


%changelog
* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_4jpp6
- new version

