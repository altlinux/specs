# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global short_name plexus-components

Name:           %{short_name}-pom
Version:        1.3.1
Release:        alt1_6jpp8
Summary:        Plexus Components POM
BuildArch:      noarch
Group:          Development/Other
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-components
Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  plexus-pom
Source44: import.info

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_6jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_5jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_2jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_2jpp7
- update

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

