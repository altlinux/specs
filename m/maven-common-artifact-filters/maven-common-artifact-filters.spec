Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          maven-common-artifact-filters
Version:       1.4
Release:       alt5_16jpp8
Summary:       Maven Common Artifact Filters
License:       ASL 2.0
Url:           http://maven.apache.org/shared/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: easymock3

BuildRequires: maven-shared
BuildRequires: maven-resources-plugin
BuildRequires: plexus-containers-container-default
BuildRequires: maven-test-tools
BuildRequires: maven-plugin-testing-harness


Provides:      maven-shared-common-artifact-filters = %{version}-%{release}
Obsoletes:     maven-shared-common-artifact-filters < %{version}-%{release}
Source44: import.info

%description
A collection of ready-made filters to control inclusion/exclusion of artifacts
during dependency resolution.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

# Maven 2 -> Maven 3
%pom_remove_dep :maven-project
%pom_add_dep org.apache.maven:maven-core
%pom_add_dep org.apache.maven:maven-compat
%pom_xpath_set "pom:dependency[pom:groupId[text()='org.apache.maven']]/pom:version" 3.0.4

# Workaround for rhbz#911365
%pom_add_dep aopalliance:aopalliance::test
%pom_add_dep cglib:cglib::test

# Migrate from easymock 1 to easymock 3
%pom_remove_dep easymock:
%pom_add_dep org.easymock:easymock:3.2:test

%build
# NoSuchMethodError: org.easymock.internal.ObjectMethodsFilter.<init>(Ljava/lang/reflect/InvocationHandler;)V
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt5_16jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_11jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt3_3jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_3jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp7
- new version

