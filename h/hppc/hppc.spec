Name:          hppc
Version:       0.8.2
Release:       alt1

Summary:       High Performance Primitive Collections for Java
License:       Apache-2.0
Group:         Development/Java
URL:           https://labs.carrotsearch.com/
VCS:           https://github.com/carrotsearch/hppc

Source0:       %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)

BuildArch:     noarch

%description
Fundamental data structures (maps, sets, lists, stacks, queues) generated for
combinations of object and primitive types to conserve JVM memory and speed
up execution.

%javadoc_package

%prep
%setup

%pom_remove_plugin -r :junit4-maven-plugin
%pom_remove_plugin :forbiddenapis
%pom_remove_plugin :maven-shade-plugin hppc-benchmarks

# missing deps
%pom_disable_module hppc-benchmarks

%build
# tests are disabled cause some dependencies are missing
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.txt
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Apr 06 2026 Evgeniy Serov <scala@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Fri May 27 2022 Igor Vlasenko <viy@altlinux.org> 0.7.1-alt1_8jpp11
- java11 build

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_8jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_7jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_4jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_3jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_3jpp8
- java 8 mass update

