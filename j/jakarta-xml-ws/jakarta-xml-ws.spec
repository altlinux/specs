Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/git
%global srcname jax-ws-api

Name:           jakarta-xml-ws
Version:        4.0.0
Release:        alt1
Summary:        Jakarta XML Web Services API
License:        BSD-3-Clause

URL:            https://github.com/jakartaee/jax-ws-api
Source0:        https://github.com/jakartaee/jax-ws-api/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(jakarta.xml.soap:jakarta.xml.soap-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Source44: import.info


%description
Jakarta XML Web Services defines a means for implementing XML-Based Web
Services based on Jakarta SOAP with Attachments and Jakarta Web Services
Metadata.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}

cd api
# remove unnecessary dependency on parent POM
  %pom_remove_parent
# remove unnecessary maven plugin
  %pom_remove_plugin :glassfish-copyright-maven-plugin
  %pom_remove_plugin :buildnumber-maven-plugin
cd -


%build
cd api
  %mvn_build
cd -


%install
cd api
  %mvn_install
cd -


%files -f api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md

%files javadoc -f api/.mfiles-javadoc


%changelog
* Fri Apr 17 2026 Anton Meleshnikov <alton@altlinux.org> 4.0.0-alt1
- new version

* Mon Apr 17 2023 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_1jpp11
- update

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_1jpp11
- new version

