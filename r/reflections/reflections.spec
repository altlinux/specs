%define _unpackaged_files_terminate_build 1

Group: Development/Java
BuildRequires: rpm-build-java
BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          reflections
Version:       0.10.2
Release:       alt1
Summary:       Java run-time meta-data analysis
License:       WTFPL AND Apache-2.0
URL:           https://github.com/ronmamo/reflections
VCS:           https://github.com/ronmamo/reflections.git
BuildArch:     noarch

Source0:       %name-%version.tar
Patch0:        %name-system.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(org.jboss:jboss-vfs)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.dom4j:dom4j)
BuildRequires:  mvn(org.javassist:javassist)

%description
A Java run-time meta-data analysis, in the spirit of Scannotations

Reflections scans your class-path, indexes the meta-data, allows you
to query it on run-time and may save and collect that information
for many modules within your project.

Using Reflections you can query your meta-data such as:
* get all sub types of some type
* get all types/methods/fields annotated with some annotation,
  w/o annotation parameters matching
* get all resources matching matching a regular expression

%{?javadoc_package}

%prep
%setup -q
%autopatch -p1


find -type f '(' -name '*.jar' -o -name '*.class' ')' -not -path './src/test/*' -print -delete

# The upstream release tag retains the next-development POM version.
%pom_xpath_set pom:version %version
%pom_change_dep javax.servlet:servlet-api javax.servlet:javax.servlet-api

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-reflections
%doc README.md
%doc --no-dereference COPYING.txt LICENSE-2.0.txt

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 0.10.2-alt1
- New version.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.9.12-alt1_10jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0.9.12-alt1_7jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0.9.12-alt1_4jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0.9.12-alt1_1jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_8jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_4jpp8
- new version

