Name:           jaxb-api
Version:        4.0.2
Release:        alt1.1

Summary:        Jakarta XML Binding API
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://github.com/jakartaee/jaxb-api
VCS:            https://github.com/jakartaee/jaxb-api

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch:      noarch

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%prep
%setup

%pom_remove_parent

%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin

sed -i '/<compilerArgs>/,/<\/compilerArgs>/d' api/pom.xml

%mvn_file :jakarta.xml.bind-api glassfish-jaxb-api/jakarta.xml.bind-api jaxb-api

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 4.0.2-alt1.1
- Cosmetic fixes.

* Mon Jan 19 2026 Evgeniy Serov <scala@altlinux.org> 4.0.2-alt1
- Updated to 4.0.2.
- Removed import.info.

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_3jpp11
- new version
