Name:           slf4j-mock
Version:        2.4.0
Release:        alt1.1

Summary:        Library to easy mock request on sl4j-api
License:        Apache-2.0
Group:          Development/Java
URL:            https://www.simplify4u.org/slf4j-mock/
VCS:            https://github.com/s4u/slf4j-mock

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.mockito:mockito-core)
# TODO: switch to mvn() prov, after fixing mockito bug
BuildRequires:  osgi(org.mockito.junit-jupiter)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-simple::sources:)

BuildArch:      noarch

%description
Yet another way to testing logging in application which use SLF4J.

%javadoc_package

%prep
%setup

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.simplify4u</groupId>"

%pom_remove_plugin :pgpverify-maven-plugin

# We don't have slf4j2
%pom_disable_module slf4j2-mock
%pom_disable_module slf4j-mock-coverage-report

%mvn_package :%name-parent __noinstall

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md LICENSE.txt

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.4.0-alt1.1
- Cosmetic fixes.

* Wed Feb 18 2026 Evgeniy Serov <scala@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus.
