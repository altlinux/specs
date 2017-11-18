BuildRequires: javapackages-local
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2007, JPackage Project
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

Name:           dtdparser
Version:        1.21
Release:        alt3_18jpp8
Summary:        A Java DTD Parser

# The code has no license attribution.
# There is a LICENSE.INFO file, but it does not specify versions.
# The only versioning is in the ASL_LICENSE file, which has been edited by the upstream.
License:        LGPLv2+ or ASL 1.1
URL:            http://wutka.com/%{name}.html
BuildArch:      noarch

Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tgz
Source1:        http://repo1.maven.org/maven2/com/wutka/%{name}/%{version}/%{name}-%{version}.pom

# Without removing these comments, build fails
Patch0:         %{name}-unmappable-chars-in-comments.patch

BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  jpackage-utils

Requires:       jpackage-utils
Source44: import.info

%description
DTD parsers for Java seem to be pretty scarce. That's probably because
DTD isn't valid XML. At some point, if/when XML Schema becomes widely
accepted, no one will need DTD parsers anymore. Until then, you can
use this library to parse a DTD.

%package javadoc
Group: Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
find -name \*.jar -delete -o -name \*.class -delete

echo com.wutka.dtd > doc/package-list

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%patch0

%build
ant build createdoc

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{name}120.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -d -m 0755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc CHANGES LICENSE README ASL_LICENSE


%files javadoc
%doc %{_javadocdir}/*
%doc LICENSE ASL_LICENSE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt3_18jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt2_18jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt2_17jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt2_16jpp8
- java 8 mass update

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt2_8jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt1_8jpp6
- new jpp relase

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt1_7jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt1_5jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt1_4jpp5
- converted from JPackage by jppimport script

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.21-alt1_3jpp1.7
- converted from JPackage by jppimport script

