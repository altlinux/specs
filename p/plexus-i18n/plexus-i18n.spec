Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
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

%define parent plexus
%define subname i18n

Name:           plexus-i18n
Version:        1.0
Release:        alt3_0.b10.2.2jpp7
Summary:        Plexus I18N Component
License:        ASL 2.0
Group:          Development/Java
URL:           http://plexus.codehaus.org/plexus-components/plexus-i18n
Source0:        plexus-i18n-1.0-beta-10-src.tar.bz2
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-i18n-1.0-beta-10/
# tar cjf plexus-i18n-1.0-beta-10-src.tar.bz2 plexus-i18n-1.0-beta-10/

Patch0:         %{name}-migration-to-component-metadata.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant >= 0:1.6
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia-sitetools
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  classworlds >= 0:1.1
BuildRequires:  plexus-container-default
BuildRequires:  plexus-utils
Requires:  classworlds >= 0:1.1
Requires:  plexus-container-default
Requires:  plexus-utils
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for 
writing applications. At the core is the container, which can be 
embedded or for a full scale application server. There are many 
reusable components for hibernate, form processing, jndi, i18n, 
velocity, etc. Plexus also includes an application server which 
is like a J2EE application server, without all the baggage.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n plexus-i18n-1.0-beta-10
%patch0 -p1

%build
mvn-rpmbuild -e -Dmaven.test.skip=true \
	install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-%{version}-beta-10.jar \
     %{buildroot}/%{_javadir}/%{parent}/%{subname}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}.pom
%add_maven_depmap JPP.%{name}.pom %{parent}/%{subname}.jar

# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/%{parent}/%{subname}.jar
%{_mavenpomdir}/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.2.2jpp7
- fc version

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b10.1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp5
- new jpackage release

* Sun Nov 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.b6.5jpp1.7
- build with maven2

* Tue Oct 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.b6.5jpp1.7
- bootstrap build for maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.5jpp1.7
- updated to new jpackage release

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.b6.4jpp1.7
- converted from JPackage by jppimport script

