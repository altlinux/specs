%define _unpackaged_files_terminate_build 1

Name: jboss-parent
Version: 55
Release: alt1

Summary: JBoss Parent POM
License: Apache-2.0
Group: Development/Java
URL: https://www.jboss.org/
VCS: https://github.com/jboss/jboss-parent-pom.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel

%description
Common Maven parent POM for JBoss projects.

%prep
%setup
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 55-alt1
- New version.

* Wed Mar 25 2026 Evgeniy Serov <scala@altlinux.org> 52-alt1
- Updated to 52.

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:20-alt1_14jpp11
- java11 build

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:20-alt1_5jpp8
- fc29 update

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

