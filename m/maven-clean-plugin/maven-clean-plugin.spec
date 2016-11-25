Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-clean-plugin
Version:        3.0.0
Release:        alt1_2jpp8
Summary:        Maven Clean Plugin
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-clean-plugin/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
Source44: import.info

%description
The Maven Clean Plugin is a plugin that removes files generated 
at build-time in a project's directory.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.


%prep
%setup -q 

# junit dependency was removed in Plexus 1.6
%pom_add_dep junit:junit::test

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt2_5jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.5-alt2_2jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_2jpp7
- new release

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

