%define _unpackaged_files_terminate_build 1

Name: jackson-core
Version: 2.20.1
Release: alt4

Summary: Core part of Jackson
License: Apache-2.0
Group: Development/Java
Url: https://github.com/FasterXML/jackson-core
Vcs: https://github.com/FasterXML/jackson-core.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-fastdoubleparser-dep-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: jackson-bom
BuildRequires: replacer
BuildRequires: maven-plugin-bundle
BuildRequires: mvn(org.moditect:moditect-maven-plugin)

%description
Core part of Jackson that defines Streaming API as well
as basic shared abstractions.

%prep
%setup
%autopatch -p1

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin "org.jacoco:jacoco-maven-plugin"

# Remove shade plugin to get a jar with JPMS support.
%pom_remove_plugin ":maven-shade-plugin"

%pom_remove_dep ch.randelshofer:fastdoubleparser
%pom_remove_plugin :gradle-module-metadata-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin

%mvn_file : %name

%build
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md release-notes/*
%doc --no-dereference LICENSE

%changelog
* Thu May 28 2026 Ilfat Aminov <aminov@altlinux.org> 2.20.1-alt4
- fix moditect dependency

* Thu Apr 02 2026 Anton Meleshnikov <alton@altlinux.org> 2.20.1-alt3
- FTBFS fix.

* Mon Nov 10 2025 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt2
- Add JPMS support.

* Fri Nov 08 2025 Ivan Khanas <xeno@altlinux.org> 2.20.1-alt1
- New version.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_7jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.11.4-alt1_2jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.11.2-alt1_1jpp11
- new version

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 2.10.2-alt1_2jpp8
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.9.9-alt1_1jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.8-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_3jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.9.4-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.6-alt1_1jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

