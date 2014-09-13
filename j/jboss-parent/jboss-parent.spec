Epoch: 0
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:                 jboss-parent
Version:              11
Release:              alt1_1jpp7
Summary:              JBoss Parent POM
License:              Public Domain
URL:                  http://www.jboss.org/
Source0:              https://github.com/jboss/jboss-parent-pom/archive/86bff326310a192ef657d893fa8e96ebd33e1ae4.tar.gz
BuildArch:            noarch

BuildRequires:        maven-local
BuildRequires:        maven-install-plugin
BuildRequires:        maven-javadoc-plugin
BuildRequires:        maven-release-plugin
BuildRequires:        maven-resources-plugin
BuildRequires:        maven-enforcer-plugin
Source44: import.info

%description
The Project Object Model files for JBoss packages.

%prep
%setup -n jboss-parent-pom-86bff326310a192ef657d893fa8e96ebd33e1ae4

%pom_remove_plugin ":maven-clover2-plugin"
%pom_remove_plugin ":findbugs-maven-plugin"
%pom_remove_plugin ":sonar-maven-plugin"
%pom_remove_plugin ":javancss-maven-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:11-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:6-alt2_10jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:6-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:6-alt1_8jpp7
- new version

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_0.CR1.1jpp6
- jpp 6.0 release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_4jpp5
- new version

