Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           args4j
Version:        2.33
Release:        alt1_19jpp11
Summary:        Java command line arguments parser
License:        MIT
URL:            https://args4j.kohsuke.org
Source0:        https://github.com/kohsuke/%{name}/archive/%{name}-site-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

# Fix build on Java 11/17
Patch0: 0001-Remove-usage-of-internal-sun-class-removed-in-Java-9.patch

# Stopped shipping these unused subpackages in F34
Obsoletes: %{name}-tools < 2.33-13
Obsoletes: %{name}-parent < 2.33-13
Source44: import.info

%description
args4j is a small Java class library that makes it easy
to parse command line options/arguments in your CUI application.
- It makes the command line parsing very easy by using annotations
- You can generate the usage screen very easily
- You can generate HTML/XML that lists all options for your documentation
- Fully supports localization
- It is designed to parse javac like options (as opposed to GNU-style
  where ls -lR is considered to have two options l and R)

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-site-%{version}
%patch0 -p1

# removing bundled stuff
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Not needed for RPM builds
%pom_remove_plugin -r :maven-site-plugin

# we don't need these now
%pom_disable_module args4j-maven-plugin
%pom_disable_module args4j-maven-plugin-example
%pom_disable_module args4j-tools

# Remove reliance on the parent pom
%pom_remove_parent

# Remove hard-coded source/target
%pom_xpath_remove pom:plugin/pom:configuration/pom:target
%pom_xpath_remove pom:plugin/pom:configuration/pom:source

# Don't package the parent pom
%mvn_package :args4j-site __noinstall

# install also compat symlinks
%mvn_file ":{*}" %{name}/@1 @1

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference %{name}/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference %{name}/LICENSE.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.33-alt1_19jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 2.33-alt1_14jpp11
- fc34 update

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 2.33-alt1_12jpp8
- jvm8 update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_8jpp8
- update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_6jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1_2jpp8
- java8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.32-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.25-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_11jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.16-alt1_8jpp7
- new version

