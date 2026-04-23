Name:           jaxb-svg11
Version:        11.4.0
Release:        alt1

Summary:        JAXB classes for SVG 1.1, generated using XJC
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/plutext/JAXB-classes-for-SVG
VCS:            https://github.com/plutext/JAXB-classes-for-SVG

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)

BuildArch:      noarch

%description
JAXB content model for SVG, generated using XJC.

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
* Wed Apr 22 2026 Evgeniy Serov <scala@altlinux.org> 11.4.0-alt1
- Initial build for Sisyphus.
