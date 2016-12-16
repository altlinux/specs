Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           forge-parent
Version:        38
Release:        alt1_7jpp8
Summary:        Sonatype Forge Parent Pom
License:        ASL 2.0
URL:            https://docs.sonatype.org/display/FORGE/Index
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/sonatype/forge/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
Source44: import.info

%description
Sonatype Forge is an open-source community dedicated to the creation of the 
next-generation of development tools and technologies.

%prep
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# We don't have nexus-staging-maven-plugin in Fedora
%pom_remove_plugin :nexus-staging-maven-plugin
# We don't use source JARs in Fedora
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 38-alt1_7jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 38-alt1_5jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 38-alt1_4jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 38-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 31-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 31-alt1_1jpp7
- new version

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 5-alt1_8jpp7
- fc update

* Fri Dec 31 2010 Igor Vlasenko <viy@altlinux.ru> 5-alt1_7jpp6
- fixed repolib

