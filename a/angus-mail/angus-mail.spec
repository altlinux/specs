Name:           angus-mail
Version:        2.0.5
Release:        alt1.1

Summary:        Angus Mail
License:        EPL-2.0
Group:          Development/Java
URL:            https://eclipse-ee4j.github.io/angus-mail/
VCS:            https://github.com/eclipse-ee4j/angus-mail

Source0:        %name-%version.tar

Patch0:         0001-Remove-GraalVM-native-image-dependency.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.angus:angus-activation)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(jakarta.mail:jakarta.mail-api)
BuildRequires:  mvn(jakarta.servlet.jsp:jakarta.servlet.jsp-api)

BuildArch:      noarch

%description
This project provides the implementation of Jakarta Mail Specification 2.1+
providing a platform-independent and protocol-independent framework to build
mail and messaging applications.

%prep
%setup
%autopatch -p1

%pom_remove_parent

%pom_remove_dep -r :graal-sdk

# Jakarta.mail can't imoprt
%pom_disable_module jakarta.mail providers

%pom_disable_module webapp demos
%pom_disable_module logging demos
%pom_disable_module doc

%pom_change_dep org.eclipse.angus:jakarta.mail jakarta.mail:jakarta.mail-api dsn

%pom_change_dep -r org.eclipse.angus:jakarta.mail jakarta.mail:jakarta.mail-api demos/

# Remove test with org.eclipse.angus.mail import
rm demos/servlet/src/test/java/example/app/ModulesTest.java
rm demos/taglib/src/test/java/demo/ModulesTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.0.5-alt1.1
- Cosmetic fixes.

* Wed Feb 25 2026 Evgeniy Serov <scala@altlinux.org> 2.0.5-alt1
- Initial build for Sisyphus.
