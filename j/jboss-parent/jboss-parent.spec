Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jboss-parent
Version:        11
Release:        alt3_7jpp8
Summary:        JBoss Parent POM
License:        Public Domain
URL:            http://www.jboss.org/
BuildArch:      noarch

Source0:        https://github.com/jboss/jboss-parent-pom/archive/86bff326310a192ef657d893fa8e96ebd33e1ae4.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Source44: import.info

%description
The Project Object Model files for JBoss packages.

%prep
%setup -n jboss-parent-pom-86bff326310a192ef657d893fa8e96ebd33e1ae4

%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :sonar-maven-plugin
%pom_remove_plugin :javancss-maven-plugin

%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:11-alt3_7jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:11-alt3_6jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:11-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

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

