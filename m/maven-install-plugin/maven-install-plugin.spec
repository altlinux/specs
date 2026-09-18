Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-install-plugin
Version:        3.2.0
Release:        alt1
Summary:        Maven Install Plugin

License:        Apache-2.0
URL:            https://maven.apache.org/plugins/maven-install-plugin
Source0:        https://github.com/apache/maven-install-plugin/archive/%name-%version.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Copies the project artifacts to the user's local repository.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup
# maven-core has scope "provided" in Plugin Testing Harness, so we
# need to provide it or tests will fail to compile.  This works for
# upstream because upstream uses a different version of Plugin Testing
# Harness in which scope of maven-core dependency is "compile".
%pom_add_dep org.apache.maven:maven-core::test

%pom_add_dep org.apache.maven:maven-compat

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Sep 17 2026 Anton Meleshnikov <alton@altlinux.org> 3.2.0-alt1
- new version

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 2.5.2-alt1_11jpp11
- java11 build

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_11jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_9jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_4jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_1jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_6jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_6jpp7
- new fc release

* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

