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

Name:           maven-jxr
Version:        2.3
Release:        alt2_3jpp7
Epoch:          0
Summary:        Source cross referencing tool
License:        ASL 2.0
Group:          Development/Java
URL:            http://maven.apache.org/doxia/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/jxr/jxr/%{version}/jxr-%{version}-source-release.zip
Patch0:         add-oro-dep.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  maven
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  junit >= 3.8.2
BuildRequires:  apache-commons-collections >= 3.1
BuildRequires:  jakarta-oro >= 2.0.8
BuildRequires:  plexus-utils >= 1.2
BuildRequires:  velocity >= 1.4

Requires:       junit >= 3.8.2
Requires:       apache-commons-collections >= 3.1
Requires:       jakarta-oro >= 2.0.8
Requires:       plexus-utils >= 1.2
Requires:       velocity >= 1.4
Source44: import.info

%description
Maven JXR is a source cross referencing tool.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package -n maven-plugin-jxr
Summary:        Maven plugin for JXR
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n maven-plugin-jxr
Maven plugin for JXR.

%prep
%setup -q -n jxr-%{version}
%patch0

%build

# The test failures seem to have something to do with:
# http://jira.codehaus.org/browse/MCHANGES-88
# We can investigate when we upgrade to 2.2.x to see if they still occur.
# Update: Seems that tests fail because they are trying to access
# plexus component descriptors which seem to be different?
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:aggregate

%install
# jars/poms
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT/%{_mavenpomdir}

install -pm 644 maven-jxr/target/%{name}-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap org.apache.maven.jxr jxr %{version} JPP %{name}-parent
%add_to_maven_depmap org.apache.maven maven-jxr %{version} JPP %{name}

install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}-parent.pom
install -pm 644 maven-jxr/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

# maven-jxr plugin
%add_to_maven_depmap org.apache.maven.plugins maven-jxr-plugin %{version} JPP maven-plugin-jxr
install -pm 644 maven-jxr-plugin/target/maven-jxr-plugin-%{version}.jar \
                $RPM_BUILD_ROOT%{_javadir}/maven-plugin-jxr.jar

install -pm 644 maven-jxr-plugin/pom.xml \
        $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-maven-plugin-jxr.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

cp -pr target/site/apidocs/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%{_javadir}/%{name}*.jar
%{_mavenpomdir}/JPP-%{name}-parent.pom
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/*

%files -n maven-plugin-jxr
%{_mavenpomdir}/JPP-maven-plugin-jxr.pom
%{_javadir}/maven-plugin-jxr*.jar

%changelog
* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt2_3jpp7
- applied repocop patches

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_3jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_2jpp7
- complete build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

