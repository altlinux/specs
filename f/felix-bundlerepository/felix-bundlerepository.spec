Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
%global site_name org.apache.felix.bundlerepository
%global grp_name  felix

Name:           felix-bundlerepository
Version:        1.6.6
Release:        alt4_19jpp8
Summary:        Bundle repository service
License:        ASL 2.0 and MIT
URL:            http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html

Source0:        http://www.fightrice.com/mirrors/apache/felix/org.apache.felix.bundlerepository-%{version}-source-release.tar.gz
Patch1:         0001-Unbundle-libraries.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.shell)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.felix:org.osgi.service.obr)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.osgi:org.osgi.compendium)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(xpp3:xpp3)
%{?fedora:BuildRequires: mvn(org.easymock:easymock)}
Source44: import.info


%description
Bundle repository service

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{site_name}-%{version}
%patch1 -p1

# Parent POM pulls in unneeded dependencies (mockito)
%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>org.apache.felix</groupId>"
%pom_add_dep junit:junit::test
%if 0%{?fedora}
  # easymock is test dependency
  %pom_xpath_inject "pom:dependency[pom:artifactId[text()='easymock']]" "<scope>test</scope>"
%else
  %pom_remove_dep org.easymock:easymock
%endif

%if !0%{?fedora}
  # These tests won't work without easymock3
  rm -f src/test/java/org/apache/felix/bundlerepository/impl/RepositoryAdminTest.java
  rm -f src/test/java/org/apache/felix/bundlerepository/impl/RepositoryImplTest.java
  rm -f src/test/java/org/apache/felix/bundlerepository/impl/StaxParserTest.java
  rm -f src/test/java/org/apache/felix/bundlerepository/impl/ResolverImplTest.java
%endif

# Add xpp3 dependency (upstream bundles this)
%pom_add_dep "xpp3:xpp3:1.1.3.4.O" pom.xml "<optional>true</optional>"

# Make felix utils mandatory dep
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='org.apache.felix.utils']]/pom:optional"

# For compatibility reasons
%mvn_file : felix/%{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE LICENSE.kxml2 NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE LICENSE.kxml2 NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_19jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_18jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1_7jpp7
- new release

