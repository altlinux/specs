Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Version
%global major 7
%global minor 1
%global patchlevel 1

# Revision
%global revnum 5
# set to 1 for hg snapshots, 0 for release
%global usesnapshot 0

# SNAPSHOT version
%global hgrevhash 63ec7d0ee8d9
%global hgrevdate 20200608

%global tarball_name jmc7-%{hgrevhash}

%if %{usesnapshot}
  %global releasestr %{revnum}.%{hgrevdate}hg%{hgrevhash}
%else
  %global releasestr %{revnum}
%endif

Name:     jmc-core
Version:  %{major}.%{minor}.%{patchlevel}
Release:  alt1_5.1jpp11
Summary:  Core API for JDK Mission Control
# jmc source README.md states: The Mission Control source code is made
# available under the Universal Permissive License (UPL), Version 1.0 or a
# BSD-style license, alternatively. The full open source license text is
# available at license/LICENSE.txt in the JMC project.
License:  UPL or BSD
URL:      http://openjdk.java.net/projects/jmc/

Source0:    https://hg.openjdk.java.net/jmc/jmc7/archive/%{hgrevhash}.tar.gz

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.owasp.encoder:encoder)
Source44: import.info

# maven requires generator will add Require for runtime dependency
#   on mvn(org.owasp.encoder:encoder)

%description
JDK Mission Control is an advanced set of tools that enables efficient and
detailed analysis of the extensive data collected by Flight Recorder. The
tool chain enables developers and administrators to collect and analyze data
from Java applications running locally or deployed in production environments.

%package javadoc
Group: Development/Java
Summary:  Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{tarball_name}/core
cp ../license/* ./
cp ../README.md ./

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_plugin :jacoco-maven-plugin tests
%pom_disable_module coverage

# don't install test packages
%mvn_package org.openjdk.jmc:missioncontrol.core.tests __noinstall
%mvn_package org.openjdk.jmc:flightrecorder.test __noinstall
%mvn_package org.openjdk.jmc:flightrecorder.rules.test __noinstall
%mvn_package org.openjdk.jmc:flightrecorder.rules.jdk.test __noinstall

%build
# some tests require large heap and fail with OOM
# depending on the builder resources
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc --no-dereference THIRDPARTYREADME.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt
%doc --no-dereference THIRDPARTYREADME.txt
%doc README.md

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 7.1.1-alt1_5.1jpp11
- new version

