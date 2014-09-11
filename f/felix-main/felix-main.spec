BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.apache.felix.main

Name:    felix-main
Version: 4.2.0
Release: alt1_4jpp7
Summary: Apache Felix Main
Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: felix-bundlerepository
BuildRequires: felix-gogo-command
BuildRequires: felix-gogo-runtime
BuildRequires: felix-gogo-shell
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: felix-framework >= 4.2.0
BuildRequires: maven-local
BuildRequires: maven-dependency-plugin
BuildRequires: maven-surefire-provider-junit4
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

