Name:           maven-invoker-plugin
Version:        3.9.0
Release:        alt2

Summary:        Apache Maven Invoker Plugin
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/plugins/maven-invoker-plugin/
VCS:            https://github.com/apache/maven-invoker-plugin

Source0:        %name-%version-source-release.zip

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default
BuildRequires:  unzip

BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildREquires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildREquires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildREquires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildREquires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildREquires:  mvn(org.apache.maven.shared:maven-script-interpreter)
buildRequires:  mvn(org.mockito:mockito-core)
# TODO: switch to mvn() prov, after fixing mockito bug
BuildRequires:  osgi(org.mockito.junit-jupiter)

BuildARch:      noarch

%description
The Invoker Plugin is used to run a set of Maven projects. The plugin can
determine whether each project execution is successful, and optionally can
verify the output generated from a given project execution.

This plugin is in particular handy to perform integration tests for other Maven
plugins. The Invoker Plugin can be employed to run a set of test projects that
have been designed to assert certain features of the plugin under test.

%javadoc_package

%prep
%setup

%pom_remove_dep org.apache.groovy:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Sun May 10 2026 Evgeniy Serov <scala@altlinux.org> 3.9.0-alt2
- Cleanup spec and rebuild with new maven-parent.

* Mon Sep 08 2025 Anton Meleshnikov <alton@altlinux.org> 3.9.0-alt1
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 3.2.1-alt1_2jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 3.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_11jpp8
- update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_9jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2jpp8
- new version

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_5jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_1jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_1jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1jpp7
- new release

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

