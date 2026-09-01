Name:           maven-shade-plugin
Version:        3.6.2
Release:        alt1

Summary:        Apache Maven Shade Plugin
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/plugins/maven-shade-plugin
VCS:            https://github.com/apache/maven-shade-plugin

Source0:        %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.vafer:jdependency)
BuildRequires:  mvn(org.xmlunit:xmlunit-legacy)
BuildRequires:  mvn(org.mockito:mockito-core)

BuildArch:      noarch

%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade - i.e. rename - the
packages of some of the dependencies.

%javadoc_package

%prep
%setup

%pom_add_dep org.apache.maven:maven-compat::test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md LICENSE
 
%changelog
* Fri Aug 28 2026 Evgeniy Serov <scala@altlinux.org> 3.6.2-alt1
- Updated to 3.6.2.

* Mon Jun 22 2026 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt3
- Built with openjdk11.

* Tue Dec 09 2025 Anton Meleshnikov <alton@altlinux.org> 3.6.0-alt2
- Fixed FTBFS.

* Sun Aug 24 2025 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus (without javadoc).
