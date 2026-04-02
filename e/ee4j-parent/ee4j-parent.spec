Name:           ee4j-parent
Version:        2.0.0
Release:        alt1.1

Summary:        Eclipse EE4J Top-level Project and community related issues
License:        EPL-2.0
Group:          Development/Java
URL:            https://projects.eclipse.org/projects/ee4j
VCS:            https://github.com/eclipse-ee4j/ee4j

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildArch:      noarch

%description
Eclipse Enterprise for Java (EE4J) is an open source initiative to create
standard APIs, implementations of those APIs, and technology compatibility
kits for Java runtimes that enable development, deployment, and management
of server-side and cloud-native applications. EE4J is based on the Java
Platform, Enterprise Edition (Java EE) standards, and uses Java EE 8 as the
baseline for creating new standards.

%prep
%setup -n %name-%version/parent

%pom_remove_plugin :cyclonedx-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ../LICENSE.txt ../*.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.0.0-alt1.1
- Cosmetic fixes.

* Sun Feb 22 2026 Evgeniy Serov <scala@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus.
