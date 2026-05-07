Name:           lorem-java
Version:        2.1
Release:        alt1

Summary:        An extremely useful Lorem Ipsum generator
License:        MIT
Group:          Development/Java
URL:            https://github.com/mdeanda/lorem
VCS:            https://github.com/mdeanda/lorem

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:      noarch

%description
An extremely useful Lorem Ipsum generator for Java!

%javadoc_package

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc license.txt README.md

%changelog
* Mon Apr 27 2026 Evgeniy Serov <scala@altlinux.org> 2.1-alt1
- Initial build for Sisyphus.
