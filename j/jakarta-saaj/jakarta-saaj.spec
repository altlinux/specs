Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/git
%global srcname saaj-api

Name:           jakarta-saaj
Version:        3.0.2
Release:        alt1
Summary:        SOAP with Attachments API for Java
License:        BSD-3-Clause
URL:            https://github.com/jakartaee/saaj-api
BuildArch:      noarch

Source0:        https://github.com/jakartaee/saaj-api/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
Source44: import.info

%description
Jakarta SOAP with Attachments defines an API enabling developers to
produce and consume messages conforming to the SOAP 1.1, SOAP 1.2, and
SOAP Attachments Feature.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch
%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{srcname}-%{version}

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent
# remove unnecessary maven plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin
# add compatibility alias for old maven artifact coordinates
%mvn_alias jakarta.xml.soap:jakarta.xml.soap-api javax.xml.soap:saaj-api
# add compatibility symlink for old classpath
%mvn_file : %{name}/jakarta.xml.soap-api geronimo-saaj
popd

%build
pushd api
# - skip tests because metro-saaj is not packaged for fedora yet:
#   https://github.com/eclipse-ee4j/metro-saaj
%mvn_build -f
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md
%files javadoc -f api/.mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md

%changelog
* Fri Apr 17 2026 Anton Meleshnikov <alton@altlinux.org> 3.0.2-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.4.2-alt1_8jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.4.2-alt1_2jpp11
- new version

