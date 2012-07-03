Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
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

Name:           jline
Version:        1.0
Release:        alt2_1jpp7
Summary:        Java library for reading and editing user input in console applications
License:        BSD
URL:            http://jline.sourceforge.net/
Group:          Development/Java
Source0:        http://download.sourceforge.net/sourceforge/jline/jline-%{version}.zip
Source1:        CatalogManager.properties
Patch1:         %{name}-0.9.94-crosslink.patch

Requires:      bash
# for /bin/stty
Requires:      coreutils
Requires:      jpackage-utils

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: java-javadoc

BuildArch:     noarch
Source44: import.info

%description
JLine is a java library for reading and editing user input in console
applications. It features tab-completion, command history, password
masking, configurable key-bindings, and pass-through handlers to use to
chain to other console applications.

%package        demo
Summary:        Demos for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       java-javadoc
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch1 -p1

# Make sure upstream hasn't sneaked in any jars we don't know about
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Remove pre-built Windows-only binary artifacts
rm src/src/main/resources/jline/jline*.dll

# Use locally installed DTDs
mkdir build
cp -p %{SOURCE1} build/

%build
# Use locally installed DTDs
export CLASSPATH=%{_builddir}/%{name}-%{version}/build

cd src/

mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -pD -T -m 644 src/target/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr src/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# demo
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr examples %{buildroot}%{_datadir}/%{name}

# pom
install -pD -T -m 644 src/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*
%doc LICENSE.txt src/src/main/resources/jline/keybindings.properties

%files demo
%{_datadir}/%{name}

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/*

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.9.94-alt1_1jpp5
- new version

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt2_1jpp5
- fixed build w/java5

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt2_1jpp1.7
- build with maven

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9.1-alt1_1jpp1.7
- updated to new jpackage release

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.9.9-alt2_2jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2
- fixed build using elinks-utf8-hack

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 0.9.1-alt1
- Rebuild for ALTLinux Sisyphus
- spec cleanup

* Mon Apr 25 2005 Fernando Nasser <fnasser@redhat.com> - 0:0.9.1-1jpp
- Upgrade to 0.9.1
- Disable attempt to include external jars

* Mon Apr 25 2005 Fernando Nasser <fnasser@redhat.com> - 0:0.8.1-3jpp
- Changes to use locally installed DTDs
- Do not try and access sun site for linking javadoc

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:0.8.1-2jpp
- Rebuild with ant-1.6.2

* Mon Jan 26 2004 David Walluck <david@anti-microsoft.org> 0:0.8.1-1jpp
- release
