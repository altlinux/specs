Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

Name:           kxml
Version:        2.3.0
Release:        alt3_15jpp8
Summary:        Small XML pull parser
License:        MIT
URL:            http://kxml.sourceforge.net/
# ./create-tarball %%{version}
Source0:        %{name}-%{version}-clean.tar.gz
Source1:        http://repo1.maven.org/maven2/net/sf/kxml/kxml2/%{version}/kxml2-%{version}.pom
Source2:        http://repo1.maven.org/maven2/net/sf/kxml/kxml2-min/%{version}/kxml2-min-%{version}.pom
Source3:        %{name}-%{version}-OSGI-MANIFEST.MF

Patch0:         0001-Unbundle-xpp3-classes.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  xpp3 >= 0:1.1.3.1
Requires:       xpp3 >= 0:1.1.3.1

BuildArch:      noarch
Source44: import.info
Provides: kxml2 = %version-%release
Conflicts: kxml2 < %version-%release
Obsoletes: kxml2 < %version-%release

%description
kXML is a small XML pull parser, specially designed for constrained
environments such as Applets, Personal Java or MIDP devices.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%build
export OPT_JAR_LIST=xpp3
ant

jar ufm dist/%{name}2-%{version}.jar %{SOURCE3}

%mvn_artifact %{SOURCE1} dist/%{name}2-%{version}.jar
%mvn_artifact %{SOURCE2} dist/%{name}2-min-%{version}.jar

# Compat symlinks
%mvn_file :kxml2 kxml/kxml2 kxml
%mvn_file :kxml2-min kxml/kxml2-min kxml-min

%install
%mvn_install -J www/kxml2/javadoc
# jpp compat - just in case
ln -s kxml.jar %buildroot%_javadir/kxml2.jar

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt3_15jpp8
- new fc release

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt3_14jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt3_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt3_11jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt3_8jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_12jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt3_12jpp7
- added jpp compatible symlink

