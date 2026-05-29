Name:           jakarta-server-pages
Version:        3.0.0
Release:        alt2

Summary:        Jakarta Server Pages (JSP)
License:        (EPL-2.0 or GPLv2 with exceptions) and Apache-2.0
Group:          Development/Java
URL:            https://projects.eclipse.org/projects/ee4j.jsp
VCS:            https://github.com/eclipse-ee4j/jsp-api

Source0:        %name-%version.tar

Patch0:         jakarta-server-pages-el6-getFeatureDescriptors.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-17-compat

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(jakarta.el:jakarta.el-api)

BuildArch:      noarch

%description
Jakarta Server Pages provides a container-independent implementation of
the JSP API.

%package        api
Group:          Development/Java
Summary:        Jakarta Server Pages (JSP) API

%description    api
Jakarta Server Pages provides a container-independent implementation of
the JSP API. This package contains the API only.

%prep
%setup
%autopatch -p1

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
* Fri May 29 2026 Evgeniy Serov <scala@altlinux.org> 3.0.0-alt2
- Fixed FTBFS: fixed build with new el-api.

* Wed Feb 25 2026 Evgeniy Serov <scala@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 2.3.6-alt1_9jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.6-alt1_3jpp11
- new version

