Name:           jakarta-server-pages
Version:        3.0.0
Release:        alt1

Summary:        Jakarta Server Pages (JSP)
License:        (EPL-2.0 or GPLv2 with exceptions) and ASL 2.0
Group:          Development/Java
URL:            https://projects.eclipse.org/projects/ee4j.jsp
VCS:            https://github.com/eclipse-ee4j/jsp-api
BuildArch:      noarch

Source0:        %name-%version.tar

BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Jakarta Server Pages provides a container-independent implementation of
the JSP API.

%package api
Group:          Development/Java
Summary:        Jakarta Server Pages (JSP) API

%description api
Jakarta Server Pages provides a container-independent implementation of
the JSP API. This package contains the API only.

%prep
%setup

%pom_remove_parent -r

%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :asciidoctor-maven-plugin
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%pom_remove_dep :jdtcore impl

%mvn_package jakarta.servlet.jsp:jsp-parent __noinstall
%mvn_package :jakarta.servlet.jsp-api api

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc *.md

%files api -f .mfiles-api
%doc LICENSE.md NOTICE.md

%changelog
* Wed Feb 25 2026 Evgeniy Serov <scala@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 2.3.6-alt1_9jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.6-alt1_3jpp11
- new version

