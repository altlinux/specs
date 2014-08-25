Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

Summary:        Maven Shared Components
URL:            http://maven.apache.org/shared/
Name:           maven-shared
Version:        19
Release:        alt1_3jpp7
License:        ASL 2.0
Group:          Development/Java

Source0:        https://github.com/apache/%{name}/archive/%{name}-components-%{version}.tar.gz

BuildRequires:  maven-local

BuildArch:      noarch

# Obsoleting retired subpackages. The packages with hardcoded versions and
# releases had their versions manually set in maven-shared-15 to something else
# than {version}. To make the change effective, the release below is one
# greater than the last release of maven-shared-15 in rawhide.
Obsoletes:      maven-shared-ant < 1.0-32
Obsoletes:      maven-shared-model-converter < 2.3-32
Obsoletes:      maven-shared-runtime < 1.0-32
Obsoletes:      maven-shared-monitor < 1.0-32
Obsoletes:      maven-shared-javadoc < %{version}-%{release}
Source44: import.info

%description
Maven Shared Components

%prep
%setup -q -n %{name}-%{name}-components-%{version}
chmod -R go=u-w *

# Maven-scm-publish-plugin is not in Fedora
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:19-alt1_3jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:15-alt10_28jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_28jpp7
- update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_24jpp7
- new fc release

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_23jpp7
- dropped versioned requires

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt8_23jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

