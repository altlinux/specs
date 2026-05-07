Name:           jaxb-xslfo
Version:        11.4.0
Release:        alt1

Summary:        JAXB classes for XSL FO, generated from Apache FOP's XSD
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/plutext/JAXB-classes-for-XSL-FO
VCS:            https://github.com/plutext/JAXB-classes-for-XSL-FO

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)

BuildArch:      noarch

%description
JAXB content model for XSL FO, generated using XJC.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt

%changelog
* Tue Apr 28 2026 Evgeniy Serov <scala@altlinux.org> 11.4.0-alt1
- Initial build for Sisyphus.
