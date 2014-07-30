# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
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

%global parent plexus
%global subname interactivity

Name:           plexus-interactivity
Version:        1.0
Release:        alt4_0.10.alpha6jpp7
Epoch:          0
Summary:        Plexus Interactivity Handler Component
License:        MIT
Group:          Development/Java
URL:            http://plexus.codehaus.org/
# svn export \
#   http://svn.codehaus.org/plexus/plexus-components/tags/plexus-interactivity-1.0-alpha-6/
# tar caf plexus-interactivity-1.0-alpha-6-src.tar.xz \
#   plexus-interactivity-1.0-alpha-6
Source0:        plexus-interactivity-1.0-alpha-6-src.tar.xz
Patch1:         plexus-interactivity-dependencies.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant >= 0:1.6
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  jline
BuildRequires:  plexus-utils
BuildRequires:  plexus-component-api

Requires:  plexus-component-api
Requires:  plexus-utils
Requires:  jline
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
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n plexus-interactivity-1.0-alpha-6
%patch1 -p1

%build
mvn-rpmbuild -e \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/plexus
install -pm 644 \
  plexus-interactivity-api/target/%{name}-api-%{version}-alpha-6.jar \
  $RPM_BUILD_ROOT%{_javadir}/plexus/interactivity-api.jar
install -pm 644 \
  plexus-interactivity-jline/target/%{name}-jline-%{version}-alpha-6.jar \
  $RPM_BUILD_ROOT%{_javadir}/plexus/interactivity-jline.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 \
pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom
install -pm 644 \
plexus-interactivity-api/pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-interactivity-api.pom
install -pm 644 \
plexus-interactivity-jline/pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-interactivity-jline.pom

%add_maven_depmap JPP.%{parent}-%{subname}.pom
%add_maven_depmap JPP.%{parent}-interactivity-api.pom  plexus/interactivity-api.jar
%add_maven_depmap JPP.%{parent}-interactivity-jline.pom  plexus/interactivity-jline.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/*


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.10.alpha6jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.7.alpha6jpp7
- fc update

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a6.1jpp6
- new version

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a5.6jpp5
- fixed build

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.6jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a5.5jpp1.7
- build with maven2

* Wed Jun 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.5jpp1.7
- updated to new jpackage release

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a5.4jpp1.7
- converted from JPackage by jppimport script

* Sun Dec 04 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1.alpha5
- Rebuild for ALTLinux Sisyphus
- spec cleanup

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0-0.a5.1jpp
- First JPackage build

