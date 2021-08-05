Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          reflections
Version:       0.9.12
Release:       alt1_7jpp11
Summary:       Java run-time meta-data analysis
License:       WTFPL
URL:           https://github.com/ronmamo/reflections
Source0:       https://github.com/ronmamo/reflections/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.dom4j:dom4j)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.jsr-305:ri)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

BuildArch:     noarch
Source44: import.info

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

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find -name "*.class" -print -delete
find -name "*.jar" -print -delete

# Unwanted
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin
# Use system maven default conf
%pom_remove_plugin :maven-javadoc-plugin

# Force servlet 3.1 apis
%pom_change_dep :servlet-api :javax.servlet-api:3.1.0

# Cannot find symbol package javax.annotation
%pom_add_dep org.jsr-305:ri

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference COPYING.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING.txt

%changelog
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

