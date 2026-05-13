Name:           mojo-executor
Version:        2.4.1
Release:        alt1

Summary:        Execute other plugins within a maven plugin
License:        Apache-2.0
Group:          Development/Java
URL:            http://mojo-executor.github.io/mojo-executor/
VCS:            https://github.com/mojo-executor/mojo-executor

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)

BuildArch:      noarch

%description
The Mojo Executor provides a way to to execute other Mojos (plugins)
within a Maven plugin, allowing you to easily create Maven plugins that
are composed of other plugins.

%javadoc_package

%package        maven-plugin
Group:          Development/Java
Summary:        Maven plugin for mojo-executor

%description    maven-plugin
%summary.

%prep
%setup

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :jacoco-maven-plugin

%mvn_package :%name-parent __noinstall

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-mojo-executor
%doc LICENSE.txt README.md

%files maven-plugin -f .mfiles-mojo-executor-maven-plugin

%changelog
* Tue May 12 2026 Evgeniy Serov <scala@altlinux.org> 2.4.1-alt1
- Updated to 2.4.1.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.4.0-alt1_1jpp11
- new version

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt1_1jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_8jpp11
- update

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_5jpp11
- fixed build

* Thu Nov 12 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_4jpp8
- new version

