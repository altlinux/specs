%define _unpackaged_files_terminate_build 1

Name: jaxb-api
Version: 4.0.5
Release: alt1

Summary: Jakarta XML Binding API
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/jakartaee/jaxb-api
VCS: https://github.com/jakartaee/jaxb-api.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: junit

%description
Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%prep
%setup
%pom_remove_parent
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-source-plugin

# These tests dynamically create legacy classpath service providers.
%pom_xpath_inject "//pom:configuration[pom:argLine]" \
    '<useModulePath>false</useModulePath>' jaxb-api-test

%mvn_file :jakarta.xml.bind-api \
    glassfish-jaxb-api/jakarta.xml.bind-api jaxb-api
%mvn_package :jakarta.xml.bind-api-test __noinstall

%build
%mvn_build -j -- -Ptest

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 4.0.5-alt1
- New version.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 4.0.2-alt1.1
- Cosmetic fixes.

* Mon Jan 19 2026 Evgeniy Serov <scala@altlinux.org> 4.0.2-alt1
- Updated to 4.0.2.
- Removed import.info.

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_3jpp11
- new version
