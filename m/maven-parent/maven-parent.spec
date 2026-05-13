Name:           maven-parent
Version:        48
Release:        alt1

Summary:        Apache Maven Project Parent POMs
License:        Apache-2.0
Group:          Development/Java
URL:            https://maven.apache.org/pom/maven/
VCS:            https://github.com/apache/maven-parent

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)

BuildArch:      noarch

%description
This POM is the common parent of all of the Maven components in the Apache Maven
project. Most of its contents are pinning down version numbers of plugins. It
does provide minimal dependencyManagement for plexus-component and plugin-tools
annotations.

%prep
%setup

%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-scm-publish-plugin
%pom_remove_plugin -r :spotless-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Fri May 08 2026 Evgeniy Serov <scala@altlinux.org> 48-alt1
- New version 48.

* Mon May 05 2025 Anton Meleshnikov <alton@altlinux.org> 39-alt1
- New version 39.

* Wed Apr 30 2025 Anton Meleshnikov <alton@altlinux.org> 35-alt1
- New version 35.

* Sat May 21 2022 Igor Vlasenko <viy@altlinux.org> 34-alt1_8jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 34-alt1_5jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 33-alt1_3jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 27-alt1_7jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 27-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 27-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 27-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 20-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_3jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_2jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

