Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
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

Name:           maven-plugin-testing
Version:        3.3.0
Release:        alt1_21jpp11
Summary:        Maven Plugin Testing
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-testing/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugin-testing/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Port-to-plexus-utils-3.0.21.patch
Patch1:         0002-Port-to-current-maven-artifact.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif
Source44: import.info

%description
The Maven Plugin Testing contains the necessary modules
to be able to test Maven Plugins.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package harness
Group: Development/Java
Summary: Maven Plugin Testing Mechanism

%description harness
The Maven Plugin Testing Harness provides mechanisms to manage tests on Mojo.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin maven-plugin-testing-harness

%pom_disable_module maven-plugin-testing-tools
%pom_disable_module maven-test-tools

%mvn_alias : org.apache.maven.shared:

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles-%{name}
%doc LICENSE NOTICE
%files harness -f .mfiles-%{name}-harness
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_21jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_16jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_14jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_12jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_9jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_7jpp8
- new fc release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_6jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_7jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt3_4.alpha1jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4.alpha1jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_4.alpha1jpp7
- new fc release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_3.alpha1jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

