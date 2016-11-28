# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# Copyright (c) 2000-2009, JPackage Project
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

Name:           slf4j
Version:        1.7.18
Release:        alt1_1jpp8
Epoch:          0
Summary:        Simple Logging Facade for Java
Group:          Development/Other
# the log4j-over-slf4j and jcl-over-slf4j submodules are ASL 2.0, rest is MIT
License:        MIT and ASL 2.0
URL:            http://www.slf4j.org/
Source0:        http://www.slf4j.org/dist/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  java-devel >= 1.5.0
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-junit >= 0:1.6.5
BuildRequires:  javassist >= 0:3.4
BuildRequires:  junit >= 0:3.8.2
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-plugin-build-helper
BuildRequires:  log4j
BuildRequires:  apache-commons-logging
BuildRequires:  cal10n
BuildRequires:  perl
Source44: import.info

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL).

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%package manual
Group: Development/Java
Summary:        Manual for %{name}
BuildArch: noarch

%description manual
This package provides documentation for %{name}.

%package jdk14
Group: Development/Java
Summary:        SLF4J JDK14 Binding

%description jdk14
SLF4J JDK14 Binding.

%package log4j12
Group: Development/Java
Summary:        SLF4J LOG4J-12 Binding

%description log4j12
SLF4J LOG4J-12 Binding.

%package jcl
Group: Development/Java
Summary:        SLF4J JCL Binding

%description jcl
SLF4J JCL Binding.

%package ext
Group: Development/Java
Summary:        SLF4J Extensions Module

%description ext
Extensions to the SLF4J API.

%package -n jcl-over-slf4j
Group: Development/Java
Summary:        JCL 1.1.1 implemented over SLF4J

%description -n jcl-over-slf4j
JCL 1.1.1 implemented over SLF4J.

%package -n log4j-over-slf4j
Group: Development/Java
Summary:        Log4j implemented over SLF4J

%description -n log4j-over-slf4j
Log4j implemented over SLF4J.

%package -n jul-to-slf4j
Group: Development/Java
Summary:        JUL to SLF4J bridge

%description -n jul-to-slf4j
JUL to SLF4J bridge.

%prep
%setup -q
find . -name "*.jar" | xargs rm
cp -p %{SOURCE1} APACHE-LICENSE

%pom_disable_module integration
%pom_disable_module osgi-over-slf4j
%pom_disable_module slf4j-android
%pom_disable_module slf4j-migrator
%pom_remove_plugin :maven-source-plugin

# Because of a non-ASCII comment in slf4j-api/src/main/java/org/slf4j/helpers/MessageFormatter.java
%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>ISO-8859-1</project.build.sourceEncoding>"

# Fix javadoc links
%pom_xpath_remove "pom:links"
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='maven-javadoc-plugin']]/pom:configuration" "
    <detectJavaApiLink>false</detectJavaApiLink>
    <isOffline>false</isOffline>
    <links><link>/usr/share/javadoc/java</link></links>"

# dos2unix
%{_bindir}/find -name "*.css" -o -name "*.js" -o -name "*.txt" | \
    %{_bindir}/xargs -t %{__perl} -pi -e 's/\r$//g'

# Remove wagon-ssh build extension
%pom_xpath_remove pom:extensions

# The general pattern is that the API package exports API classes and does
# not require impl classes. slf4j was breaking that causing "A cycle was
# detected when generating the classpath slf4j.api, slf4j.nop, slf4j.api."
# The API bundle requires impl package, so to avoid cyclic dependencies
# during build time, it is necessary to mark the imported package as an
# optional one.
# Reported upstream: http://bugzilla.slf4j.org/show_bug.cgi?id=283
sed -i "/Import-Package/s/.$/;resolution:=optional&/" slf4j-api/src/main/resources/META-INF/MANIFEST.MF

%mvn_package :%{name}-parent __noinstall
%mvn_package :%{name}-site __noinstall
%mvn_package :%{name}-api
%mvn_package :%{name}-simple
%mvn_package :%{name}-nop

%build
%mvn_build -f -s

%install
# Compat symlinks
%mvn_file ':%{name}-{*}' %{name}/%{name}-@1 %{name}/@1

%mvn_install

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-manual
rm -rf target/site/{.htaccess,apidocs}
cp -pr target/site/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-manual

%files -f .mfiles
%doc LICENSE.txt APACHE-LICENSE
%dir %{_javadir}/%{name}

%files jdk14 -f .mfiles-%{name}-jdk14
%files log4j12 -f .mfiles-%{name}-log4j12
%files jcl -f .mfiles-%{name}-jcl
%files ext -f .mfiles-%{name}-ext
%files -n jcl-over-slf4j -f .mfiles-jcl-over-slf4j
%files -n log4j-over-slf4j -f .mfiles-log4j-over-slf4j
%files -n jul-to-slf4j -f .mfiles-jul-to-slf4j

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt APACHE-LICENSE

%files manual
%doc LICENSE.txt APACHE-LICENSE
%{_defaultdocdir}/%{name}-manual

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.18-alt1_1jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.14-alt1_1jpp8
- added osgi provides

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.12-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt1_3jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1_1jpp7
- update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt4_4jpp7
- more symlinks

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt3_4jpp7
- added compat symlinks

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt2_4jpp7
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_4jpp7
- update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_1jpp7
- new version

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.6-alt1_2jpp7
- new version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_5jpp7
- fc version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp7
- fc version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp6
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_4jpp6
- new version (full build)

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp6
- new version (bootstrap)

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_1jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_2jpp1.7
- updated to new jpackage release

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp1.7
- added dependency on new excalibur

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

