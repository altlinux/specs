Name:           google-gson
Version:        2.14.0
Release:        alt1

Summary:        Java lib for conversion of Java objects into JSON representation
License:        Apache-2.0
Group:          Development/Java
URL:            https://google.github.io/gson/
VCS:            https://github.com/google/gson

Source:         %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(com.google.errorprone:error_prone_core)
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

#Requires for tests
#BuildRequires:  mvn(com.google.guava:guava-testlib)
#BuildRequires:  mvn(com.google.truth:truth)

BuildArch:      noarch

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%javadoc_package

%prep
%setup

%pom_xpath_remove pom:extensions

%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin :maven-artifact-plugin

%pom_remove_plugin :proguard-maven-plugin gson

%pom_remove_plugin :templating-maven-plugin gson
sed 's/${project.version}/%version/' gson/src/main/java-templates/com/google/gson/internal/GsonBuildConfig.java >gson/src/main/java/com/google/gson/internal/GsonBuildConfig.java

%pom_remove_dep -r :error_prone_annotations
%java_remove_annotations gson extras -s \
  -p com[.]google[.]errorprone[.]annotations[.] \

%pom_disable_module test-jpms
%pom_disable_module test-graal-native-image
%pom_disable_module test-shrinker

#depends on com.google.caliper
%pom_disable_module metrics

%pom_disable_module proto

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%changelog
* Fri Jun 26 2026 Anton Meleshnikov <alton@altlinux.org> 2.14.0-alt1
- Updated to 2.14.0.

* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 2.13.2-alt1.1
- Cosmetic fixes.

* Mon Jan 12 2026 Evgeniy Serov <scala@altlinux.org> 2.13.2-alt1
- Updated to 2.13.2.

* Sat Jan 03 2026 Evgeniy Serov <scala@altlinux.org> 2.12.1-alt1
- Updated to 2.12.1.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 2.9.1-alt1_1jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.9.0-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.8.6-alt1_7jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 2.8.6-alt1_3jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_3jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_2jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_1jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3jpp7
- new version

