Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-mapping
Version:        3.0.0
Release:        alt1_8jpp8
Summary:        Apache Maven Mapping
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
Source44: import.info

%description
Maven shared component that implements file name mapping.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_8jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_4jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_3jpp8
- new version

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_2jpp8
- new version

