# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global artifactId plexus-component-factories

Name:		plexus-component-factories-pom
Version:	1.0
Release:	alt1_0.15.alpha11jpp8
Summary:	Plexus Component Factories POM
BuildArch:	noarch
Group:		Development/Other
License:	ASL 2.0
URL:		https://github.com/codehaus-plexus/plexus-component-factories
Source0:	http://repo1.maven.org/maven2/org/codehaus/plexus/%{artifactId}/%{version}-alpha-11/%{artifactId}-%{version}-alpha-11.pom
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
Source44: import.info


%description
This package provides Plexus Component Factories parent POM used by different
Plexus packages.

%prep
%setup -cT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_xpath_remove pom:modules

%build
%mvn_alias : plexus:
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.15.alpha11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.14.alpha11jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.13.alpha11jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.12.alpha11jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.11.alpha11jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.10.alpha11jpp8
- new version

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.6.alpha11jpp7
- new version

