%define _unpackaged_files_terminate_build 1

Name: jakarta-ws-rs
Version: 4.0.0
Release: alt1

Summary: Jakarta RESTful Web Services
License: EPL-2.0
Group: Development/Java
Url: https://github.com/jakartaee/rest
Vcs: https://github.com/jakartaee/rest.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: ee4j-parent
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: mockito-core
BuildRequires: maven-assembly-plugin
BuildRequires: maven-enforcer-plugin

%description
Jakarta RESTful Web Services provides a specification document, TCK and
foundational API to develop web services following the Representational State
Transfer (REST) architectural pattern.

%package spec
Summary: Jakarta RESTful Web Services specification POM
Group: Development/Java

%description spec
Jakarta RESTful Web Services specification artifact and parent metadata used
for Maven builds.

%package parent
Summary: Jakarta RESTful Web Services parent POM
Group: Development/Java

%description parent
Parent POM for Jakarta RESTful Web Services Maven artifacts.

%{?javadoc_package}

%prep
%setup
%pom_disable_module examples
%pom_disable_module jaxrs-tck

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :asciidoctor-maven-plugin jaxrs-spec/pom.xml

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jakarta.ws.rs-api

%files spec -f .mfiles-jakarta.ws.rs-spec

%files parent -f .mfiles-all

%changelog
* Wed Mar 18 2026 Ivan Khanas <xeno@altlinux.org> 4.0.0-alt1
- New version.

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.1.6-alt1_8jpp11
- new version
