Name:           angus-activation
Version:        2.0.3
Release:        alt1.1

Summary:        Angus Activation
License:        BSD-3-Clause
Group:          Development/Java
URL:            https://eclipse-ee4j.github.io/angus-activation/
VCS:            https://github.com/eclipse-ee4j/angus-activation

Source0:        %name-%version.tar

Patch0:         0001-Remove-GraalVM-native-image-dependency.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)

BuildArch:      noarch

%description
This project provides the implementation of Jakarta Activation Specification
which lets you take advantage of standard services to: determine the type of
an arbitrary piece of data; encapsulate access to it; discover the operations
available on it; and instantiate the appropriate bean to perform the
operation(s).

%prep
%setup
%autopatch -p1

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-source-plugin activation-registry

%pom_remove_dep :graal-sdk activation-registry

%pom_disable_module docs

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.0.3-alt1.1
- Cosmetic fixes.

* Wed Feb 25 2026 Evgeniy Serov <scala@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus.
