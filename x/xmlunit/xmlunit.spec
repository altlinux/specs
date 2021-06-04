Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
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

Name:           xmlunit
Summary:        Provides classes to do asserts on xml
Epoch:          0
Version:        2.7.0
Release:        alt1_6jpp11
# xmlunit2 is licensed under ASL 2.0, xmlunit-legacy is still BSD-licensed
License:        ASL 2.0 and BSD

URL:            https://www.xmlunit.org/
Source0:        https://github.com/xmlunit/xmlunit/releases/download/v%{version}/%{name}-%{version}-src.tar.gz

Patch0:         0001-Disable-tests-requiring-network-access.patch
Patch1:         xmlunit-2.7.0-ValueAssertTest-fix.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.mockito:mockito-core)
Source44: import.info

%description
XMLUnit provides you with the tools to verify the XML you emit is the one you
want to create. It provides helpers to validate against an XML Schema, assert
the values of XPath queries or compare XML documents against expected outcomes.


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}


%package        assertj
Group: Development/Java
Summary:        Assertj for %{name}

%description    assertj
This package provides %{summary}.


%package        core
Group: Development/Java
Summary:        Core package for %{name}

%description    core
This package provides %{summary}.


%package        legacy
Group: Development/Java
Summary:        Legacy package for %{name}

%description    legacy
This package provides %{summary}.


%package        matchers
Group: Development/Java
Summary:        Matchers for %{name}

%description    matchers
This package provides %{summary}.


%package        placeholders
Group: Development/Java
Summary:        Placeholders for %{name}

%description    placeholders
This package provides %{summary}.


%prep
%setup -q -n %{name}-%{version}-src

%patch0 -p1
%patch1 -p1

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

# Add deps to EE APIs removed in Java 11
%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api . xmlunit-core
%pom_change_dep com.sun.xml.bind:jaxb-core com.sun.xml.bind:jaxb-impl . xmlunit-core
%pom_add_dep com.sun.istack:istack-commons-runtime::test xmlunit-core

%mvn_alias "org.xmlunit:xmlunit-legacy" "xmlunit:xmlunit"


%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install


%files -f .mfiles-xmlunit-parent
%doc README.md CONTRIBUTING.md RELEASE_NOTES.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%files assertj -f .mfiles-xmlunit-assertj
%files core -f .mfiles-xmlunit-core
%files legacy -f .mfiles-xmlunit-legacy
%files matchers -f .mfiles-xmlunit-matchers
%files placeholders -f .mfiles-xmlunit-placeholders


%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 0:2.7.0-alt1_6jpp11
- fixed build

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.7.0-alt1_4jpp11
- new version

* Sun May 09 2021 Igor Vlasenko <viy@altlinux.ru> 0:2.6.3-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_9jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_6jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_1jpp7
- bugfixes

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_6jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_6jpp7
- new version

* Mon Aug 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_4jpp6
- fixed build

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp6
- build with ant17

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_6jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_6jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp1.7
- updated to new jpackage release

* Wed May 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_4jpp1.7
- converted from JPackage by jppimport script

* Thu Mar 23 2006 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt2
- Fix build with j2se-1.5

* Sat Apr 30 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Rebuilt for ALTLinux Sisyphus
- spec cleanup

* Thu Aug 26 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0-3jpp
- Build with ant-1.6.2

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-2jpp
- Fix license and improved description
- Thanks to Ralph Apel who produced a spec - merged version info

* Wed Dec 17 2003 Paul Nasrat <pauln at truemesh.com> - 0:1.0-1jpp
- Initial Version
