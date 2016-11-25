Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-parent
Version:        27
Release:        alt1_2jpp8
Summary:        Apache Maven parent POM
License:        ASL 2.0
URL:            http://maven.apache.org
Source0:        http://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-parent
Source44: import.info

%description
Apache Maven parent POM file used by other Maven projects.

%prep
%setup -q
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :apache-rat-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 27-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 20-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_3jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_2jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

