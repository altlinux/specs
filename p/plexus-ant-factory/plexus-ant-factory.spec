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

%define parent plexus
%define subname ant-factory

Name:           %{parent}-%{subname}
Version:        1.0
Release:        alt5_0.8.a2.1.2jpp7
Epoch:          0
Summary:        Plexus Ant component factory
# Email from copyright holder confirms license.
License:        ASL 2.0
Group:          Development/Java
URL:            http://plexus.codehaus.org/
Source0:        %{name}-src.tar.bz2
# svn export http://svn.codehaus.org/plexus/tags/plexus-ant-factory-1.0-alpha-2.1/ plexus-ant-factory/
# tar cjf plexus-ant-factory-src.tar.bz2 plexus-ant-factory/
Source1:        %{name}-jpp-depmap.xml
Source2:        plexus-ant-factory_license_and_copyright.txt

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven2-common-poms >= 1.0-2

BuildRequires:  ant
BuildRequires:  classworlds
BuildRequires:  plexus-container-default
BuildRequires:  plexus-utils

Requires:    ant
Requires:    classworlds
Requires:    plexus-container-default
Requires:    plexus-utils
Source44: import.info

%description
Ant component class creator for Plexus.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
cp %{SOURCE2} .


%build
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -e install javadoc:aggregate

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{parent}
install -pm 644 target/%{name}-%{version}*.jar \
      $RPM_BUILD_ROOT%{_javadir}/%{parent}/%{subname}.jar

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
          $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom
%add_maven_depmap JPP.%{parent}-%{subname}.pom %{parent}/%{subname}.jar

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%doc plexus-ant-factory_license_and_copyright.txt
%dir %{_javadir}/plexus
%{_javadir}/%{parent}/%{subname}.jar
%{_mavenpomdir}/JPP.%{parent}-%{subname}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc plexus-ant-factory_license_and_copyright.txt
%doc %{_javadocdir}/*


%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.8.a2.1.2jpp7
- rebuild with maven-local

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.8.a2.1.2jpp7
- fc update

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a2.1.1jpp6
- fixed build with new plexus-containers

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a2.1.1jpp6
- new jpp release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a1.4jpp5
- new jpackage release

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a1.2jpp1.7
- build with maven2

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a1.2jpp1.7
- converted from JPackage by jppimport script

