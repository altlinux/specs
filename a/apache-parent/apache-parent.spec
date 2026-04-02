Name:           apache-parent
Version:        37
Release:        alt1.1

Summary:        Apache Software Foundation Parent POM
License:        Apache-2.0
Group:          Development/Java
URL:            http://apache.org/
VCS:            https://github.com/apache/maven-apache-parent

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)

Requires:       mvn(org.apache:apache-jar-resource-bundle)

BuildArch:      noarch

%description
This package contains the parent pom file for apache projects.

%prep
%setup

sed -i 's/org\.apache\.apache\.resources:/org.apache:/g' pom.xml

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-site-plugin docs
%pom_remove_plugin :maven-scm-publish-plugin docs

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE *.md

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 37-alt1.1
- Cosmetic fixes.

* Thu Feb 19 2026 Evgeniy Serov <scala@altlinux.org> 37-alt1
- Updated to 37.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 26-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 23-alt1_6jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 23-alt1_3jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 19-alt1_4jpp8
- new version

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 19-alt1_2jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 18-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 18-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 18-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_10jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_7jpp7
- rebuild with new apache-resource-bundles

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 10-alt1_7jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_5jpp7
- new release

