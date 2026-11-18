Group: Development/Java
BuildRequires(pre): rpm-macros-java
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
Version:        3.5.1
Release:        alt1
Summary:        Maven Plugin Testing
License:        Apache-2.0
URL:            http://maven.apache.org/plugin-testing/
BuildArch:      noarch

Source0:        %name-%version.tar

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-resolver-provider)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-testing)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.mockito:mockito-junit-jupiter)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
%endif

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

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.2 maven-plugin-testing-harness

%build
%mvn_build -s -- -Dmaven.compiler.release=8 -Dmaven.source.skip=true

%install
%mvn_install
rm -f %buildroot%_javadocdir/%name/args

%files -f .mfiles-%{name}
%doc maven-plugin-testing-harness/target/classes/META-INF/LICENSE
%doc maven-plugin-testing-harness/target/classes/META-INF/NOTICE
%files harness -f .mfiles-%{name}-harness
%files javadoc -f .mfiles-javadoc
%doc maven-plugin-testing-harness/target/classes/META-INF/LICENSE
%doc maven-plugin-testing-harness/target/classes/META-INF/NOTICE

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 3.5.1-alt1
- New version.

* Tue Apr 22 2025 Anton Meleshnikov <alton@altlinux.org> 3.3.0-alt2
- fixed FTBFS (with update to maven 3.8.1)

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

