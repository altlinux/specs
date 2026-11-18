%define _unpackaged_files_terminate_build 1

%define compat_version 2.3.3

Name: jaxb-api
Version: 4.0.5
Release: alt2

Summary: Jakarta XML Binding API
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/jakartaee/jaxb-api
VCS: https://github.com/jakartaee/jaxb-api.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-compat-%compat_version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api)
BuildRequires: mvn(jakarta.activation:jakarta.activation-api:1.2.2)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: junit

%description
Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%package -n jaxb-api2
Summary: JAXB API for the javax.xml.bind namespace
Group: Development/Java

%description -n jaxb-api2
The genuine JAXB 2.3.3 API provides the javax.xml.bind namespace for
applications using the Java EE API. It coexists with Jakarta XML Binding 4.

%prep
%setup -a1
%pom_remove_parent
%pom_remove_parent %name-compat-%compat_version
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :glassfish-copyright-maven-plugin \
    %name-compat-%compat_version
%pom_remove_plugin -r :buildnumber-maven-plugin \
    %name-compat-%compat_version
%pom_remove_plugin -r :maven-source-plugin %name-compat-%compat_version

# These tests dynamically create legacy classpath service providers.
%pom_xpath_inject "//pom:configuration[pom:argLine]" \
    '<useModulePath>false</useModulePath>' jaxb-api-test

%mvn_file :jakarta.xml.bind-api \
    glassfish-jaxb-api/jakarta.xml.bind-api jaxb-api
%mvn_package :jakarta.xml.bind-api-test __noinstall

pushd %name-compat-%compat_version
# Keep genuine compatibility coordinates and versioned paths beside API 4.
%pom_xpath_inject "//pom:configuration[pom:argLine]" \
    '<useModulePath>false</useModulePath>' jaxb-api-test
%mvn_compat_version 'jakarta.xml.bind:*' %compat_version
%mvn_file :jakarta.xml.bind-api jaxb-api2/jakarta.xml.bind-api
%mvn_package :jakarta.xml.bind-api jaxb-api2
%mvn_package :jakarta.xml.bind-api-parent jaxb-api2
%mvn_package :jakarta.xml.bind-api-test __noinstall
popd
cp %name-compat-%compat_version/LICENSE.md compat-LICENSE.md
cp %name-compat-%compat_version/NOTICE.md compat-NOTICE.md

%build
%mvn_build -j -- -Ptest
pushd %name-compat-%compat_version
%mvn_build -j
popd

%install
%mvn_install
pushd %name-compat-%compat_version
%mvn_install
popd

%files -f .mfiles
%doc LICENSE.md NOTICE.md compat-LICENSE.md compat-NOTICE.md

%files -n jaxb-api2 -f %name-compat-%compat_version/.mfiles-jaxb-api2

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 4.0.5-alt2
- Add the genuine JAXB 2 API compatibility subpackage.

* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 4.0.5-alt1
- New version.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 4.0.2-alt1.1
- Cosmetic fixes.

* Mon Jan 19 2026 Evgeniy Serov <scala@altlinux.org> 4.0.2-alt1
- Updated to 4.0.2.
- Removed import.info.

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_3jpp11
- new version
