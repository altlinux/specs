%define _unpackaged_files_terminate_build 1

Name: money-api
Version: 1.1
Release: alt1

Summary: JavaMoney API
License: Apache-2.0
Group: Development/Java
Url: https://javamoney.github.io
Vcs: https://github.com/JavaMoney/jsr354-api.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: bnd-maven-plugin
BuildRequires: logback
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: slf4j
BuildRequires: mockito-core
BuildRequires: testng
BuildRequires: maven-surefire-plugin

%description
JSR 354 API for representing and processing money and currencies.

%prep
%setup
%autopatch -p1

%pom_remove_plugin  :maven-site-plugin
%pom_remove_plugin  :maven-javadoc-plugin
%pom_remove_plugin  :maven-source-plugin
%pom_remove_plugin  :maven-enforcer-plugin
%pom_remove_plugin  :maven-war-plugin
%pom_remove_plugin  :maven-assembly-plugin
%pom_remove_plugin  :maven-deploy-plugin
%pom_remove_plugin  :maven-install-plugin
%pom_remove_plugin  :maven-dependency-plugin
%pom_remove_plugin  :versions-maven-plugin
%pom_remove_plugin  :jacoco-maven-plugin
%pom_remove_plugin  :asciidoctor-maven-plugin
%pom_remove_plugin  :license-maven-plugin
%pom_remove_plugin  :lifecycle-mapping

%pom_change_dep org.mockito:mockito-all org.mockito:mockito-core
%pom_change_dep org.hamcrest:hamcrest-library org.hamcrest:hamcrest

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt README.md

%changelog
* Wed Mar 25 2026 Ivan Khanas <xeno@altlinux.org> 1.1-alt1
- Initial build for ALT.
