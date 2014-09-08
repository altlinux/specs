BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.apache.felix.utils

Name:             felix-utils
Version:          1.2.0
Release:          alt1_3jpp7
Summary:          Utility classes for OSGi
License:          ASL 2.0
Group:            Development/Java
URL:              http://felix.apache.org
Source0:          http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    jpackage-utils
BuildRequires:    felix-osgi-compendium
BuildRequires:    felix-osgi-core
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    mockito
Source44: import.info


%description
Utility classes for OSGi

%package javadoc
Group:            Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

# Remove compiler plugin so default target of 1.5 is used
%pom_remove_plugin :maven-compiler-plugin
# Remove rat plugin that is not in Fedora
%pom_remove_plugin org.codehaus.mojo:rat-maven-plugin

%mvn_file :%{bundle} "felix/%{bundle}"

%build
# one of the tests fails in mock (local build is ok)
%mvn_build -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp7
- new release

