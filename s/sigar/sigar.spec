%set_verify_elf_method relaxed
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

%define name sigar

Name:           %{name}
Group:          Monitoring
Summary:        System Information Gatherer And Reporter
Version:        1.6.4
Release:        alt2_1jpp6
License:        GPL
URL:            http://support.hyperic.com/display/SIGAR/Home
Source0:        http://download.github.com/hyperic-sigar-sigar-1.6.4-0-g4b67f57.tar.gz
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.7
BuildRequires: cpptasks
BuildRequires: gcc
Requires: jpackage-utils >= 0:1.7.5
Source44: import.info

%description
The Sigar API provides a portable interface for gathering system information
such as:

    * System memory, swap, cpu, load average, uptime, logins
    * Per-process memory, cpu, credential info, state, arguments,
      environment, open files
    * File system detection and metrics
    * Network interface detection, configuration info and metrics
    * TCP and UDP connection tables
    * Network route table


%prep
%setup -q -n hyperic-sigar-d156ef4

%build
pushd bindings/java
    ant
popd


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 bindings/java/sigar-bin/lib/sigar.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}
install -m 644 bindings/java/sigar-bin/lib/*.so $RPM_BUILD_ROOT%{_libdir}

%files
%{_javadir}/*
%{_libdir}/lib*so*

%changelog
* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt2_1jpp6
- fixed build

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_1jpp6
- new version

