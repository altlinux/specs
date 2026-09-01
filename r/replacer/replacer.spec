%define _unpackaged_files_terminate_build 1

Name: replacer
Version: 1.6
Release: alt3

Summary: Replacer Maven Mojo
License: MIT
Group: Development/Java
Url: https://code.google.com/archive/p/maven-replacer-plugin
Vcs: https://github.com/beiliubei/maven-replacer-plugin
Source0: %name-%version.tar

Patch0: 0001-Port-to-commons-lang3.patch
Patch1: 0002-Port-to-maven-plugin-annotations.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: jpackage-default

BuildRequires: sonatype-oss-parent
BuildRequires: maven-plugin-plugin
BuildREquires: xerces-j2

BuildArch: noarch

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-compiler-plugin

%pom_change_dep :commons-lang org.apache.commons:commons-lang3
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations::provided

%mvn_file :%name %name
%mvn_alias :%name com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md LICENSE

%changelog
* Fri Aug 28 2026 Evgeniy Serov <scala@altlinux.org> 1.6-alt3
- Moved commons-lang3 source changes to a patch.
- Ported to modern Maven plugin annotations.

* Mon Dec 08 2025 Ivan Khanas <xeno@altlinux.org> 1.6-alt2
- Return to the Sisyphus repository.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.6-alt1_20jpp11
- update

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.6-alt1_17jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.6-alt1_13jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_11jpp8
- update

* Tue Jul 16 2019 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_9jpp8
- build with new mockito

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2jpp8
- new version

