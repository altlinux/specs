%define _unpackaged_files_terminate_build 1

Name: httpcomponents-project
Version: 15
Release: alt1

Summary: Common Maven POM for Apache HttpComponents
License: Apache-2.0
Group: Development/Java
URL: https://hc.apache.org/
VCS: https://github.com/apache/httpcomponents-parent.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Common Maven parent POM for Apache HttpComponents projects.

%prep
%setup
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-site-plugin
%mvn_alias :httpcomponents-parent :project
%mvn_package :*::sources: __noinstall

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 15-alt1
- New version.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 12-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 12-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 11-alt1_2jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 9-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 9-alt1_3jpp8
- fc29 update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 9-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 7-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 7-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 7-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 7-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 6-alt2_4jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 6-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 6-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 6-alt1_1jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_4jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

