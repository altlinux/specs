Name: lombok-maven-plugin
Version: 1.18.20.0
Release: alt1

Summary: Maven Plugin for Project Lombok
License: MIT
Group: Development/Java
Url: https://awhitford.github.io/lombok.maven
Vcs: https://github.com/awhitford/lombok.maven
BuildArch: noarch

Source0: https://github.com/awhitford/lombok.maven/archive/lombok-maven-%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default

BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.projectlombok:lombok)

%description
This is the maven plugin for Project Lombok.

%javadoc_package

%prep
%setup -n lombok-maven-%version

%pom_remove_plugin :dependency-check-maven
%pom_remove_plugin :tidy-maven-plugin
%pom_disable_module test-maven-lombok

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Wed Oct 14 2026 Anton Meleshnikov <alton@altlinux.org> 1.18.20.0-alt1
- Initial build for Sisyphus.
