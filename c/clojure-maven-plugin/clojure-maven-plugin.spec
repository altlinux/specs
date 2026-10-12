Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global upstream    talios
%global groupId     com.theoryinpractise
%global artifactId  clojure-maven-plugin

Name:           %{artifactId}
Version:        1.9.3
Release:        alt1
Summary:        Clojure plugin for Maven

License:        EPL-1.0
URL:            https://github.com/%{upstream}/%{name}
VCS:            https://github.com/talios/clojure-maven-plugin

# wget --content-disposition %%{url}/tarball/%%{version}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
This plugin has been designed to make working with clojure as easy as
possible, when working in a mixed language, enterprise project.

%prep
%setup -q -n %{artifactId}-%{artifactId}-%{version}

# release plugin is not required for RPM builds
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :ossindex-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin

%build
# test1.clj does not get discovered if LANG=C
# also, using 'package' instead of 'install' to avoid
# running integration tests - they do installation tests
# for a lot of packages*versions we do not currently have
export LANG=en_US.utf8
# Do not run tests cause we miss dependencies fest-assert
# and maven-surefire-provider-junit5
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference epl-v10.html 
%doc README.markdown

%changelog
* Wed Oct 07 2026 Anton Meleshnikov <alton@altlinux.org> 1.9.3-alt1
- new version
- added vcs tag

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.8.4-alt1_3jpp11
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.10-alt1_2jpp7
- new version
