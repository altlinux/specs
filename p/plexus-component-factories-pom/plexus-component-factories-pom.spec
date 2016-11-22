# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global artifactId plexus-component-factories

Name:		plexus-component-factories-pom
Version:	1.0
Release:	alt1_0.11.alpha11jpp8
Summary:	Plexus Component Factories POM
BuildArch:	noarch
Group:		Development/Other
License:	ASL 2.0
URL:		https://github.com/codehaus-plexus/plexus-component-factories
Source0:	http://repo1.maven.org/maven2/org/codehaus/plexus/%{artifactId}/%{version}-alpha-11/%{artifactId}-%{version}-alpha-11.pom
Source1:	http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:	maven-local
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
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.11.alpha11jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.10.alpha11jpp8
- new version

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.6.alpha11jpp7
- new version

