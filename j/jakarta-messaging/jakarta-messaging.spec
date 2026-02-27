Name:           jakarta-messaging
Version: 	3.1.0
Release:        alt1

Summary:        Jakarta Messaging
License:        EPL-2.0
Group:          Development/Java
URL:            https://projects.eclipse.org/projects/ee4j.messaging
VCS:            https://github.com/jakartaee/messaging
BuildArch:      noarch

Source:         %name-%version.tar

BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.eclipse.ee4j:project:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
This repository contain the API definition source code for the
Jakarta Messaging API. This is used to generate the official Javadocs.

%javadoc_package

%prep
%setup

%pom_remove_plugin :spec-version-maven-plugin api
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :maven-javadoc-plugin api

%pom_disable_module spec

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Sun Feb 22 2026 Evgeniy Serov <scala@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus.
