Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: maven-local unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           maven-shared-utils
Version:        3.3.4
Release:        alt1_2jpp11
Summary:        Maven shared utility classes
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-shared-utils
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# XXX temporary for maven upgrade
Patch1:         0001-Restore-compatibility-with-current-maven.patch
Patch2:         0002-Avoid-setting-POSIX-attributes-for-symbolic-links.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  %{?module_prefix}mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
%endif
Source44: import.info

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%{?javadoc_package}

%prep
%setup -q

find -name '*.java' -exec sed -i 's/\r//' {} +

%patch1 -p1
%patch2 -p1

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

%pom_remove_dep org.apache.commons:commons-text
rm src/test/java/org/apache/maven/shared/utils/CaseTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 3.3.4-alt1_2jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_0.5jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_0.3jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_0.1jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_5jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_4jpp8
- new jpp release

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_3jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.2jpp
- rebuild to add provides

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

