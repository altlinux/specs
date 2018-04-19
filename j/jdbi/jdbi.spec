Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jdbi
Version:       2.63.1
Release:       alt1_5jpp8
Summary:       A SQL convenience library for Java
License:       ASL 2.0
URL:           http://jdbi.org/
Source0:       https://github.com/brianm/jdbi/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(cglib:cglib)
BuildRequires: mvn(com.fasterxml:classmate)
BuildRequires: mvn(com.google.code.findbugs:annotations)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.antlr:antlr-runtime)
BuildRequires: mvn(org.antlr:stringtemplate)
BuildRequires: mvn(org.antlr:antlr3-maven-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-jdbc)
BuildRequires: mvn(org.springframework:spring-tx)

%if 0
# test deps
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.h2database:h2)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-jexl)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.springframework:spring-mock)
BuildRequires: mvn(postgresql:postgresql)
%endif

BuildArch:     noarch
Source44: import.info

%description
jDBI is designed to provide convenient tabular data access in
Java. It uses the Java collections framework for query
results, provides a convenient means of externalizing SQL
statements, and provides named parameter support for any database
being used.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -type f -delete

# https://github.com/basepom/basepom org.basepom:basepom-standard-oss:11
%pom_remove_parent

# disable embedded antlr3-runtime, cglib, and classmate copy
%pom_remove_plugin :maven-shade-plugin

%pom_xpath_remove "pom:profiles"

%pom_change_dep log4j: ::1.2.17

# org.springframework spring 2.0.1
%pom_change_dep org.springframework:spring org.springframework:spring-beans
%pom_add_dep org.springframework:spring-core:'${dep.spring.version}'
%pom_add_dep org.springframework:spring-jdbc:'${dep.spring.version}'
%pom_add_dep org.springframework:spring-tx:'${dep.spring.version}'

%pom_xpath_remove "pom:dependency[pom:scope = 'test']"

%mvn_file : %{name}

%build

# unavailable test deps
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES_PLANNED_FOR_3_0 CONTRIBUTORS README.md RELEASE_NOTES
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.63.1-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.63.1-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.63.1-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.63.1-alt1_2jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 2.59-alt1_2jpp8
- new version

