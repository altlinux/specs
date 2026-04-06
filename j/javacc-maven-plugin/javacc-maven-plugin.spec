Name:           javacc-maven-plugin
Version:        3.2.0
Release:        alt1

Summary:        JavaCC Maven Plugin
License:        Apache-2.0
Group:          Development/Java
URL:            https://www.mojohaus.org/javacc-maven-plugin
VCS:            https://github.com/mojohaus/javacc-maven-plugin

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)

BuildArch:      noarch

%description
Maven Plugin for processing JavaCC grammar files.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-invoker-plugin

%pom_remove_dep edu.ucla.cs.compilers:jtb

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md src/main/resources/NOTICE

%changelog
* Fri Mar 20 2026 Evgeniy Serov <scala@altlinux.org> 3.2.0-alt1
- Updated to 3.2.0.

* Thu Sep 04 2025 Anton Meleshnikov <alton@altlinux.org> 0:3.1.1-alt1
- new version
- build without jtb
- disable building the web site

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:2.6-alt5_35jpp11
- java11 build

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_29jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_27jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_26jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_25jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_24jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_23jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_22jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_21jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt5_20jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_15jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_14jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt3_10jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt2_10jpp7
- fixed build

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_10jpp7
- fc update

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_7jpp6
- new version

