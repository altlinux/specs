%define _unpackaged_files_terminate_build 1

Name: jackson-annotations
Version: 2.22
Release: alt1

Summary: Core annotations for Jackson data processor
License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-annotations
Vcs: https://github.com/FasterXML/jackson-annotations.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: jpackage-default
BuildRequires: maven-local

BuildRequires: jackson-parent
BuildRequires: junit5
BuildRequires: maven-plugin-bundle
BuildRequires: moditect-maven-plugin

%description
Core annotations used for value types,
used by Jackson data-binding package.

%javadoc_package

%prep
%setup

%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :gradle-module-metadata-maven-plugin

%mvn_file : %name

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc LICENSE

%changelog
* Mon Aug 10 2026 Evgeniy Serov <scala@altlinux.org> 2.22-alt1
- Updated to 2.22.

* Fri Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 2.19.4-alt2
- Add JPMS support.

* Fri Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 2.19.4-alt1
- New version.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_6jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.11.2-alt1_1jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 2.10.2-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.9.9-alt1_1jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

