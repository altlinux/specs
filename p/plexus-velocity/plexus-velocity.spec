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

%define parent plexus
%define subname velocity

Name:           plexus-velocity
Version:        1.1.8
Release:        alt1_9jpp7
Epoch:          0
Summary:        Plexus Velocity Component
License:        ASL 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-velocity-1.1.8/
# tar czf plexus-velocity-1.1.8-src.tar.gz plexus-velocity-1.1.8/
Source0:        plexus-velocity-%{version}-src.tar.gz

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  ant >= 0:1.6
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia-sitetools
BuildRequires:  ant-contrib
BuildRequires:  classworlds >= 0:1.1
BuildRequires:  apache-commons-collections
BuildRequires:  plexus-container-default
BuildRequires:  plexus-utils
BuildRequires:  velocity
Requires:  classworlds >= 0:1.1
Requires:  apache-commons-collections
Requires:  plexus-container-default
Requires:  plexus-utils
Requires:  velocity
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
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n plexus-velocity-%{version}
for j in $(find . -name "*.jar"); do
        mv $j $j.no
done

%build
    # Use normal pom for now
    rm -f release-pom.xml
    mvn-rpmbuild \
        -e \
        install javadoc:aggregate

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar \
   %{buildroot}/%{_javadir}/%{parent}/%{subname}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP.%{name}.pom
%add_maven_depmap JPP.%{name}.pom %{parent}/%{subname}.jar

# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}

%files
%{_javadir}/%{parent}/*
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*

%files javadoc
%doc %{_javadocdir}/*

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.8-alt1_9jpp7
- fc version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt3_1jpp5
- explicit selection of java5 compiler

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt2_1jpp5
- fixed build with maven 2.0.7

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.7-alt1_1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_3jpp1.7
- build with maven2

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

