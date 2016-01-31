Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-skins
Version:        10
Release:        alt1_2jpp8
Summary:        Maven Skins
License:        ASL 2.0
URL:            http://maven.apache.org/skins/
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/skins/maven-skins/%{version}/maven-skins-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
Source44: import.info

%description
Skins for the maven site generator. 

%prep
%setup -q 
%pom_remove_plugin :maven-scm-publish-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 10-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 5-alt2_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 5-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 5-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 5-alt1_6jpp7
- new version

