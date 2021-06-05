Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.0
%global gittag testng-remote-parent-%{version}

Name:    testng-remote
Version: 1.3.0
Release: alt1_9jpp11
Summary: Modules for running TestNG remotely
# org/testng/remote/strprotocol/AbstractRemoteTestRunnerClient.java is CPL
License: ASL 2.0 and CPL
URL:     https://github.com/testng-team/testng-remote
Source0: https://github.com/testng-team/testng-remote/archive/%{gittag}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.service:auto-service)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.testng:testng) >= 6.12

Requires:  mvn(org.testng:testng) >= 6.12
Source44: import.info

%description
TestNG Remote contains the modules for running TestNG remotely. This is
normally used by IDE to communicate with TestNG run-time, e.g. receive the
Test Result from run-time so that can display them on IDE views.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n testng-remote-%{gittag}

# Avoid bundling gson
%pom_remove_plugin :maven-shade-plugin remote

# Plugin not in Fedora
%pom_remove_plugin :git-commit-id-plugin
%pom_remove_plugin :git-commit-id-plugin remote
sed -i -e 's/${git.branch}/%{gittag}/' -e 's/${git.commit.id}/%{gittag}/' -e 's/${git.build.version}/%{version}/' \
  remote/src/main/resources/revision.properties

# Not needed for RPM builds
%pom_remove_plugin -r :jacoco-maven-plugin

# Disable support for old versions of TestNG that are not in Fedora
%pom_disable_module remote6_10
%pom_disable_module remote6_9_10
%pom_disable_module remote6_9_7
%pom_disable_module remote6_5
%pom_disable_module remote6_0
%pom_remove_dep :testng-remote6_10 dist
%pom_remove_dep :testng-remote6_9_10 dist
%pom_remove_dep :testng-remote6_9_7 dist
%pom_remove_dep :testng-remote6_5 dist
%pom_remove_dep :testng-remote6_0 dist

# Package the shaded artifact (contains all testng-remote modules in a single jar)
%mvn_package ":testng-remote-dist:jar:shaded:"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.3.0-alt1_9jpp11
- new version

