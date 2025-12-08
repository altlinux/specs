%define _unpackaged_files_terminate_build 1

Name: replacer
Version: 1.6
Release: alt2

Summary: Replacer Maven Mojo
License: MIT
Group: Development/Java
Url: https://code.google.com/archive/p/maven-replacer-plugin
Vcs: https://github.com/beiliubei/maven-replacer-plugin
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: jpackage-default
BuildRequires: apache-commons-io
BuildRequires: ant-lib
BuildRequires: apache-commons-lang3
BuildRequires: maven-lib
BuildRequires: maven-plugin-plugin
BuildRequires: xerces-j2
BuildRequires: maven-plugin-annotations

BuildArch: noarch
Source44: import.info

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
This package contains javadoc for %name.

%prep
%setup

%pom_change_dep org.apache.maven:maven-plugin-api:3.0.3 org.apache.maven:maven-plugin-api:3.0.3:provided
%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations:3.9.0:compile

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

# remove hard-coded compiler settings
%pom_remove_plugin :maven-compiler-plugin

# trivial port to commons-lang3
%pom_change_dep :commons-lang org.apache.commons:commons-lang3:3.8.1

for i in $(find -name "*.java"); do
    sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" $i;
done

%mvn_file :%name %name
%mvn_alias :%name com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
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

