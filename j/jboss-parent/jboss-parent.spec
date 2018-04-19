Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jboss-parent
Version:        20
Release:        alt1_4jpp8
Summary:        JBoss Parent POM
License:        CC0
URL:            http://www.jboss.org/
BuildArch:      noarch

Source0:        https://github.com/jboss/jboss-parent-pom/archive/%{name}-%{version}.tar.gz
Source1:        http://repository.jboss.org/licenses/cc0-1.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
Source44: import.info

%description
The Project Object Model files for JBoss packages.

%prep
%setup -q -n %{name}-pom-%{name}-%{version}

# NOT available plugins
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :javancss-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :sonar-maven-plugin

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :buildnumber-maven-plugin

cp -p %SOURCE1 LICENSE
sed -i 's/\r//' LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_2jpp8
- new jpp release

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

