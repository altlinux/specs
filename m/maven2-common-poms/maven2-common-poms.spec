Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2006, JPackage Project
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

%define parent maven2
%define subname common-poms

Name:              %{parent}-%{subname}
Version:           1.0
Release:           alt4_12jpp6
Epoch:             0
Summary:           Common poms for maven2
License:           Apache Software License, BSD
Group:             Development/Java
URL:               http://jpackage.org/

# No source location for these. They are ascii files generated from maven
# repositories, and are not in cvs/svn.
Source0:           %{name}-%{version}.tar


BuildArch:         noarch
BuildRequires: jpackage-utils >= 0:1.7.2
Requires: jpackage-utils >= 0:1.7.2

%description
This package is a collection of poms required by various maven2-dependent 
packages.

%prep
%setup  

pushd maven2-common-poms
# rename logkit to avalon-logkit and update its version to 2.2.1
sed -i "s|logkit|avalon-logkit|g" JPP.excalibur-logkit.pom
sed -i "s|1.0.1|2.2.1|" JPP.excalibur-logkit.pom

# remove xom dependency
sed -i '227,231d' JPP-jaxen.pom
popd

cp -n \
5.0/maven2-common-poms/JPP-commons.pom \
5.0/maven2-common-poms/JPP-commons-net.pom \
maven2-common-poms

%build

%install

# Map
install -dm 755 $RPM_BUILD_ROOT%{_mavendepmapdir}
cp %{name}-jpp-depmap.xml $RPM_BUILD_ROOT%{_mavendepmapdir}/maven2-versionless-depmap.xml

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven2
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms
install -pm 644 maven2-common-poms/*.pom $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/maven2
ln -s %{_datadir}/maven2/default_poms $RPM_BUILD_ROOT%{_javadir}/maven2

%files
%doc maven2-common-poms-docs/*
%{_mavendepmapdir}/maven2-versionless-depmap.xml
%{_javadir}/maven2
%{_datadir}/maven2

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_12jpp6
- replaced plexus-maven-plugin in JPP.plexus-components.pom
- dropped JPP-oro.pom

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_12jpp6
- added maven3 fedora poms

* Sun Sep 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_12jpp6
- fixed maven-embedder depmap

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_12jpp6
- new version

* Mon Apr 06 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_6jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

