Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define shortname bytelist

Name:           jruby-bytelist
Version:        0.1
Release:	alt2_3jpp5
Epoch:          0
Summary:        ByteList
License:        GPL/LGPL
URL:            http://jruby.codehaus.org
Group:          Development/Java
Source0:        bytelist-1.0.tar.gz
# svn export http://svn.codehaus.org/jruby/bytelist/tags/1.0/ bytelist-1.0
Source1:        bytelist-0.1.pom
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: junit
Requires: jpackage-utils >= 0:1.7.5
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
BuildArch:      noarch

%description
ByteList.

%prep
%setup -q -n bytelist-1.0

%build
export OPT_JAR_LIST="ant-launcher ant/ant-junit junit"
ant test jar

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{shortname}-%{version}.jar \
          $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do \
ln -sf ${jar} ${jar/-%{version}/}; done)
%add_to_maven_depmap org.jruby.extras bytelist %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}

%changelog
* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt2_3jpp5
- fixes for java6 support

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_3jpp5
- use default jpp profile

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_2jpp5
- converted from JPackage by jppimport script

