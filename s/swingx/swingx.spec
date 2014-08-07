BuildRequires: maven-compiler-plugin maven-surefire-plugin maven-jar-plugin maven-install-plugin maven-javadoc-plugin jmock maven-doxia-sitetools
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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

Name:           swingx
Version:        1.6.5
Release:        alt5_0jpp6
Summary:        Extensions to the Swing GUI toolkit

Group:          Development/Java
License:        LGPL
URL:            https://swingx.java.net/

Source0:        swingx-project-%version.zip

Source2:        %{name}-jpp-depmap.xml


BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-provider-junit4
#BuildRequires: mojo-maven2-plugin-emma
BuildRequires: jhlabs-filters
BuildRequires: junit4
BuildRequires: metainf-services
BuildRequires: mockito

Requires: jhlabs-filters

BuildArch:      noarch

%description
Contains extensions to the Swing GUI toolkit, including new
and enhanced components that provide functionality commonly
required by rich client applications. Highlights include:
* Sorting, filtering, highlighting for tables, trees, and lists
* Find/search
* Auto-completion
* Login/authentication framework
* TreeTable component
* Collapsible panel component
* Date picker component
* Tip-of-the-Day component
Many of these features will eventually be incorporated into
the Swing toolkit, although API compatibility will not be
guaranteed. The SwingX project focuses exclusively on the
raw components themselves.

%package javadoc 
Summary:        Javadocs for %{name} 
Group:          Development/Java
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
 
%description javadoc 
%{summary}. 

%prep
%setup -q -n swingx-project-%version


%build
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
	-Djava.awt.headless=true \
	-Daggregate=true \
	-Dallow.test.failure.ignore=true -Dmaven.test.failure.ignore=true \
	-Dmaven.local.depmap.file=%{SOURCE2} \
        install javadoc:javadoc


%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -m 644 %{name}-*/target/%{name}-*-%{version}.jar %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
%__ln_s ${jar} ${jar/-%{version}/}; done)

# poms
%__mkdir_p %{buildroot}%{_mavenpomdir}
%__install -m 644 pom.xml \
               $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc 
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version} 
%__cp -a target/site/apidocs/* \
               %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%files
%{_javadir}/*.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc 
%{_javadocdir}/%{name}-%{version} 
%{_javadocdir}/%{name} 

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt5_0jpp6
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt4_0jpp6
- depmap cleanup

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt3_0jpp6
- migration to mvn-rpmbuild

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.5-alt2_0jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Feb 28 2013 Paul Wolneykien <manowar@altlinux.ru> 1.6.5-alt1_0jpp6
- Install all target JARs.
- Add "metainf-services" and "mockito" to the set of build requisites.
- Remove the unused POM patch
- Fresh up to v1.6.5.

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt4_1jpp6
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_1jpp6
- build without emma-plugin

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1jpp6
- new version

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_7jpp6
- new version

