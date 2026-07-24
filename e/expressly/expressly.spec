Name: expressly
Version: 6.0.0
Release: alt1

Summary: Expressly, a Jakarta Expression Language implementation
License: EPL-2.0, GPL-2.0
Group: Development/Java
Url: https://projects.eclipse.org/projects/ee4j.expressly
Vcs: https://github.com/eclipse-ee4j/expressly
BuildArch: noarch

Source0: https://github.com/eclipse-ee4j/expressly/archive/%version-RELEASE/%name-%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires: mvn(org.eclipse.ee4j:project:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(jakarta.el:jakarta.el-api)

%description
Eclipse Expressly implements Jakarta Expression Language,
an expression language for Java applications.
This project contains the Eclipse implementation.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md NOTICE.md
%doc --no-dereference LICENSE.md

%changelog
* Fri Jul 24 2026 Anton Meleshnikov <alton@altlinux.org> 6.0.0-alt1
- Initial build for Sisyphus.
