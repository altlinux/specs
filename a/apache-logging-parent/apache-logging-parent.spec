Name:           apache-logging-parent
Version:        12.1.1
Release:        alt1

Summary:        Parent project internally used in Maven-based projects of the Apache Logging Services
License:        Apache-2.0
Group:          Development/Java
URL:            https://logging.apache.org/logging-parent
VCS:            https://github.com/apache/logging-parent

Source0:        %name-%version.tar

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch:      noarch

%description
%summary.

%prep
%setup

%pom_remove_plugin :flatten-maven-plugin
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :apache-rat-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.adoc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 21 2026 Evgeniy Serov <scala@altlinux.org> 12.1.1-alt1
- Updated to 12.1.1.
- Returned to Sisyphus.

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2-alt1_1jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1-alt1_5jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1-alt1_4jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1-alt1_3jpp8
- java update

* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1-alt1_2jpp8
- new version

