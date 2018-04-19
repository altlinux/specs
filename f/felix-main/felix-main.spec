# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bundle org.apache.felix.main

Name:    felix-main
Version: 5.4.0
Release: alt1_5jpp8
Summary: Apache Felix Main
Group:   Development/Other
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch: noarch

BuildRequires: java-devel >= 1.6.0
BuildRequires: jpackage-utils
BuildRequires: felix-bundlerepository
BuildRequires: felix-gogo-command
BuildRequires: felix-gogo-runtime
BuildRequires: felix-gogo-shell
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: felix-parent
BuildRequires: felix-framework >= 4.2.0
BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: mockito

Requires: felix-bundlerepository
Requires: felix-gogo-command
Requires: felix-gogo-runtime
Requires: felix-gogo-shell
Requires: felix-osgi-compendium
Requires: felix-osgi-core
Requires: felix-framework >= 4.2.0
Source44: import.info
Obsoletes: felix < 2

%description
Apache Felix Main Classes.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} "felix/%{bundle}"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_3jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_4jpp7
- new release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_1jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt3_8jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt3_6jpp6
- fixed build with maven3

* Sun Jan 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt2_6jpp6
- obsolete felix1

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_6jpp6
- new jpp release

